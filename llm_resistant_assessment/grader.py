#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import sys
from hashlib import sha256
from typing import Dict, List, Tuple

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def normalize_candidate_id(candidate_id: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9]+", "_", candidate_id.strip().lower())
    return safe.strip("_")


def derive_encryption_key(candidate_id: str, secret_salt: str) -> Tuple[bytes, bytes]:
    normalized = candidate_id.strip().lower()
    kdf_salt = sha256(secret_salt.encode("utf-8")).digest()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=kdf_salt,
        iterations=120_000,
    )
    key = kdf.derive(normalized.encode("utf-8"))
    return key, None


def aes_ctr_decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()


def read_bundle_json(bundle_path: str, candidate_id: str, secret_salt: str) -> Dict:
    key, _ = derive_encryption_key(candidate_id, secret_salt)
    with open(bundle_path, "rb") as f:
        blob = f.read()
    if len(blob) < 17:
        raise ValueError("Encrypted bundle too short")
    nonce = blob[:16]
    ciphertext = blob[16:]
    plaintext = aes_ctr_decrypt(key, nonce, ciphertext)
    return json.loads(plaintext.decode("utf-8"))


def compute_score(entry: Dict, weights: Dict[str, float]) -> float:
    skills = entry["skills"]
    years = entry["years_experience"]
    ach = entry["achievements"]
    skill_score = sum(weights.get(s, 0.5) for s in skills)
    exp_bonus = 0.7 * min(years, 12)
    achievements_score = 0.9 * ach["projects"] + 1.4 * ach["publications"] + 1.8 * ach["awards"] + 1.2 * ach["teams_led"]
    return round(skill_score + exp_bonus + achievements_score, 6)


def expected_top_10_ids(payload: Dict) -> List[str]:
    weights = payload["scoring_weights"]
    entries = payload["resumes"]
    scored = []
    for e in entries:
        scored.append((compute_score(e, weights), e["resume_id"]))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [rid for _, rid in scored[:10]]


def checksum(ids: List[str]) -> str:
    s = "\n".join(ids).encode("utf-8")
    return sha256(s).hexdigest()


def grade_dataset_task(bundle_path: str, candidate_id: str, secret_salt: str, submission_dir: str) -> Tuple[bool, Dict]:
    payload = read_bundle_json(bundle_path, candidate_id, secret_salt)
    expected_ids = expected_top_10_ids(payload)
    expected_checksum = checksum(expected_ids)
    output_path = os.path.join(submission_dir, "dataset_task_output.json")
    if not os.path.exists(output_path):
        return False, {"error": f"Missing {output_path}"}
    with open(output_path, "r", encoding="utf-8") as f:
        try:
            submission = json.load(f)
        except Exception as e:
            return False, {"error": f"Invalid JSON: {e}"}

    submitted_ids = submission.get("top_10_resume_ids")
    submitted_checksum = submission.get("checksum")
    if not isinstance(submitted_ids, list) or not all(isinstance(x, str) for x in submitted_ids):
        return False, {"error": "top_10_resume_ids must be a list of strings"}
    if len(submitted_ids) != 10:
        return False, {"error": "top_10_resume_ids must contain exactly 10 ids"}
    if submitted_checksum != checksum(submitted_ids):
        return False, {"error": "checksum mismatch for submitted ids"}

    correct = submitted_ids == expected_ids
    return correct, {
        "expected_ids": expected_ids,
        "expected_checksum": expected_checksum,
        "submitted_ids": submitted_ids,
        "submitted_checksum": submitted_checksum,
    }


def run_pytest(bugfix_dir: str) -> Tuple[bool, str]:
    # Run pytest quietly; capture output
    if not os.path.isdir(bugfix_dir):
        return False, f"Bugfix directory not found: {bugfix_dir}"
    env = os.environ.copy()
    cmd = [sys.executable, "-m", "pytest", "-q"]
    try:
        result = subprocess.run(cmd, cwd=bugfix_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=120)
        success = result.returncode == 0
        return success, result.stdout
    except subprocess.TimeoutExpired:
        return False, "pytest timed out"


def main() -> None:
    parser = argparse.ArgumentParser(description="Grade LLM-resistant assessment submission")
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--secret-salt", required=True)
    parser.add_argument("--submission-dir", required=True, help="Directory containing dataset_task_output.json")
    parser.add_argument("--bugfix-dir", required=True, help="Path to candidate's bugfix project directory")
    parser.add_argument("--bundle-path", default=None, help="Optional path to task_bundle.enc (defaults to out/<id>/task_bundle.enc)")
    args = parser.parse_args()

    safe_id = normalize_candidate_id(args.candidate_id)
    bundle_path = args.bundle_path or os.path.join("out", safe_id, "task_bundle.enc")
    if not os.path.exists(bundle_path):
        print(f"ERROR: Missing bundle at {bundle_path}. Re-run generator with the same candidate and salt.")
        sys.exit(2)

    dataset_ok, dataset_info = grade_dataset_task(bundle_path, args.candidate_id, args.secret_salt, args.submission_dir)
    bugfix_ok, pytest_output = run_pytest(args.bugfix_dir)

    # Simple scoring: 60% dataset, 40% bugfix
    score = (60 if dataset_ok else 0) + (40 if bugfix_ok else 0)

    print("=== Dataset Task ===")
    if dataset_ok:
        print("PASS")
    else:
        print("FAIL")
        if isinstance(dataset_info, dict) and "error" in dataset_info:
            print("Reason:", dataset_info["error"]) 
    # Print a short diff hint if wrong but valid
    if isinstance(dataset_info, dict) and "submitted_ids" in dataset_info:
        print("Expected:", ",".join(dataset_info["expected_ids"]))
        print("Submitted:", ",".join(dataset_info["submitted_ids"]))

    print("\n=== Bugfix Project ===")
    print("PASS" if bugfix_ok else "FAIL")
    print(pytest_output.strip())

    print("\n=== Summary ===")
    print(f"Dataset: {'PASS' if dataset_ok else 'FAIL'} | Bugfix: {'PASS' if bugfix_ok else 'FAIL'} | Score: {score}/100")

    sys.exit(0 if dataset_ok and bugfix_ok else 1)


if __name__ == "__main__":
    main()

