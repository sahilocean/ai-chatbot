#!/usr/bin/env python3
import argparse
import base64
import json
import os
import random
import re
import secrets
import string
from dataclasses import dataclass
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
    # PBKDF2 parameters are public; the salt value is derived from the secret_salt
    kdf_salt = sha256(secret_salt.encode("utf-8")).digest()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=kdf_salt,
        iterations=120_000,
    )
    key = kdf.derive(normalized.encode("utf-8"))
    # Random 16-byte nonce per bundle
    nonce = secrets.token_bytes(16)
    return key, nonce


def aes_ctr_encrypt(key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()


@dataclass
class Resume:
    resume_id: str
    skills: List[str]
    years_experience: int
    achievements: Dict[str, int]


SKILL_POOL = [
    "python", "java", "javascript", "typescript", "go", "rust", "sql", "nosql",
    "aws", "gcp", "azure", "kubernetes", "docker", "linux", "bash",
    "numpy", "pandas", "pytorch", "tensorflow", "sklearn",
    "react", "node", "django", "flask", "fastapi", "spring",
]


def seeded_random(seed_material: str) -> random.Random:
    seed_int = int.from_bytes(sha256(seed_material.encode("utf-8")).digest(), "big")
    return random.Random(seed_int)


def generate_resumes(rng: random.Random, num_resumes: int = 500) -> List[Resume]:
    resumes: List[Resume] = []
    for i in range(num_resumes):
        resume_id = f"C{i:04d}"
        num_skills = rng.randint(5, 12)
        skills = rng.sample(SKILL_POOL, num_skills)
        years_experience = rng.randint(0, 20)
        achievements = {
            "projects": rng.randint(0, 12),
            "publications": rng.randint(0, 6),
            "awards": rng.randint(0, 3),
            "teams_led": rng.randint(0, 5),
        }
        resumes.append(Resume(resume_id, skills, years_experience, achievements))
    return resumes


def generate_scoring_weights(rng: random.Random) -> Dict[str, float]:
    weights: Dict[str, float] = {}
    for skill in SKILL_POOL:
        # Biased towards backend/infra a bit, but random per-candidate
        base = 1.0
        if skill in {"python", "sql", "aws", "kubernetes", "docker", "linux"}:
            base = 1.2
        weights[skill] = round(base + rng.uniform(0.0, 1.0), 3)
    return weights


def compute_score(resume: Resume, weights: Dict[str, float]) -> float:
    skill_score = sum(weights.get(skill, 0.5) for skill in resume.skills)
    exp_bonus = 0.7 * min(resume.years_experience, 12)
    ach = resume.achievements
    achievements_score = 0.9 * ach["projects"] + 1.4 * ach["publications"] + 1.8 * ach["awards"] + 1.2 * ach["teams_led"]
    return round(skill_score + exp_bonus + achievements_score, 6)


def build_dataset_payload(candidate_id: str, secret_salt: str) -> Dict:
    # Seed with combined materials so results are per-candidate+salt unique
    rng = seeded_random(f"{candidate_id}|{secret_salt}")
    resumes = generate_resumes(rng)
    weights = generate_scoring_weights(rng)
    # Include deterministic rubric and instructions inside the encrypted bundle
    payload = {
        "version": 1,
        "candidate_id": candidate_id,
        "scoring_weights": weights,
        "resumes": [
            {
                "resume_id": r.resume_id,
                "skills": r.skills,
                "years_experience": r.years_experience,
                "achievements": r.achievements,
            }
            for r in resumes
        ],
        "task": {
            "objective": "Compute the Strong Resume Score for each resume and return the top 10 resume_ids in descending order of score. Ties should be broken by lexicographically smaller resume_id first.",
            "formula": "score = sum(weights[skill]) + 0.7*min(years_experience,12) + 0.9*projects + 1.4*publications + 1.8*awards + 1.2*teams_led",
            "output_format": {
                "top_10_resume_ids": ["C0000", "C0001", "..."],
                "checksum": "sha256 of newline-joined resume_ids"
            }
        }
    }
    return payload


def write_candidate_bundle(out_dir: str, candidate_id: str, secret_salt: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    safe_id = normalize_candidate_id(candidate_id)
    candidate_dir = os.path.join(out_dir, safe_id)
    os.makedirs(candidate_dir, exist_ok=True)

    payload = build_dataset_payload(candidate_id, secret_salt)
    json_bytes = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

    key, nonce = derive_encryption_key(candidate_id, secret_salt)
    ciphertext = aes_ctr_encrypt(key, nonce, json_bytes)

    # Bundle format: [16-byte nonce][ciphertext]
    bundle_path = os.path.join(candidate_dir, "task_bundle.enc")
    with open(bundle_path, "wb") as f:
        f.write(nonce + ciphertext)

    instructions_path = os.path.join(candidate_dir, "instructions.txt")
    with open(instructions_path, "w", encoding="utf-8") as f:
        f.write(
            """
You received an encrypted dataset (task_bundle.enc). Your task:

1) Derive a 32-byte key using PBKDF2-HMAC-SHA256 with:
   - password: your candidate_id lowercased and trimmed
   - salt: SHA-256 digest of the provided secret_salt (as raw 32 bytes)
   - iterations: 120000
   - length: 32 bytes

2) Decrypt using AES-CTR:
   - nonce: first 16 bytes of task_bundle.enc
   - ciphertext: remaining bytes

3) Parse the decrypted JSON and follow the embedded instructions to compute the
   Strong Resume Scores and produce a file named dataset_task_output.json with:
   {
     "top_10_resume_ids": ["C....", ...],
     "checksum": "sha256 of the newline-joined resume_ids in order"
   }

4) Also open the bugfix project and make tests pass. Submit both:
   - dataset_task_output.json
   - your edited bugfix project directory

Notes:
 - This task requires writing code. Manual decryption or guessing will not work.
 - Determinism matters: use exact math and tie-breaking rules described.
""".strip()
        )

    return candidate_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate LLM-resistant dataset task bundle")
    parser.add_argument("--candidate-id", required=True, help="Unique candidate id (e.g., email)")
    parser.add_argument("--secret-salt", required=True, help="Private salt string held by proctor")
    parser.add_argument("--out-dir", default="./out", help="Directory to write candidate bundle")
    args = parser.parse_args()

    candidate_dir = write_candidate_bundle(args.out_dir, args.candidate_id, args.secret_salt)
    print(f"Wrote candidate bundle to: {candidate_dir}")


if __name__ == "__main__":
    main()

