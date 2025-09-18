### Strong Resume Passer Test (LLM-Resistant)

This project provides an LLM-resistant technical assessment designed to evaluate real-world problem solving, data handling, and code quality. It generates a personalized, encrypted dataset task and a small bugfix project with failing tests. An automated grader verifies submissions deterministically.

The goal is to make it impractical to pass by chat-only LLM usage and require actual local computation, code execution, and reasoning under a salted, per-candidate setup.

### Components

- **Dataset Task Generator**: Produces a per-candidate encrypted dataset (`task_bundle.enc`) and an instruction file. Candidates must programmatically derive a key using PBKDF2 and decrypt the dataset, then compute a score for resumes and return the top results.
- **Bugfix Mini-Project**: A small Python package with failing tests that simulate realistic resume parsing logic. Candidates must fix the implementation to pass tests.
- **Automated Grader**: Re-derives the dataset and expected answers and runs the bugfix tests to compute a composite score.
- **Operations Guide**: Practical guidance to run this in a proctored, LLM-resistant way.

### Quick Start

1) Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2) Generate a candidate bundle (run this with your private salt):

```bash
python generator.py \
  --candidate-id "alice@example.com" \
  --secret-salt "REPLACE_WITH_PRIVATE_SALT" \
  --out-dir ./out
```

This creates `./out/alice_example_com/` containing:
- `instructions.txt` (what to give the candidate)
- `task_bundle.enc` (encrypted dataset with embedded scoring rules)

3) Provide to candidate:
- `instructions.txt`
- `task_bundle.enc`
- A copy (or zip) of `tasks/bugfix_project/`

4) Candidate deliverables:
- A JSON file named `dataset_task_output.json` containing the computed top results per the instructions
- An edited bugfix project so that tests pass

5) Grade the submission:

```bash
python grader.py \
  --candidate-id "alice@example.com" \
  --secret-salt "REPLACE_WITH_PRIVATE_SALT" \
  --submission-dir ./submissions/alice_example_com \
  --bugfix-dir ./submissions/alice_example_com/bugfix_project
```

The grader prints a summary with pass/fail and component scores.

### Why This Is LLM-Resistant

- **Salted, per-candidate datasets**: Even if prompts leak, answers are unique per candidate and session.
- **Decryption step**: Requires coding and local execution to unlock data.
- **Deterministic numeric outputs**: Requires correct algorithms and reproducible computation, not generic prose.
- **Code bugfixing**: Requires reading tests, understanding intent, and implementing correct logic.

Combine this with the operations guide in `docs/operations.md` for strong resistance in practice.

