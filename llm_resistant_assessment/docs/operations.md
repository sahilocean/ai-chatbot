### Operations and Proctoring Guide

Goal: maximize resistance to chat-only LLM usage while remaining fair and efficient for real candidates.

### Setup

- Maintain a private `secret_salt` stored in a password manager. Rotate periodically.
- For each candidate, generate a fresh bundle with `generator.py` using the same salt but unique `--candidate-id`.
- Distribute only `task_bundle.enc`, `instructions.txt`, and the `tasks/bugfix_project/` folder.

### Proctoring Recommendations

- **Device constraints**: Require local environment with Python and internet limited to docs only. Optionally provide a prebuilt container.
- **Time-box**: 60–90 minutes. The dataset task is straightforward but requires correct implementation; the bugfix is small but nontrivial.
- **Live check-ins**: Ask for a brief, screen-shared walkthrough of their approach and code at the end (5–10 minutes).

### Anti-Cheating Features

- **Salted dataset**: Answers are unique per candidate; cannot be copied.
- **Encrypted bundle**: Requires code to derive the key and decrypt.
- **Deterministic numeric outputs**: Graded by exact match and checksum.
- **Code tests**: Bugfix project graded by automated tests.

### Scoring

- Dataset task: 60 points (all-or-nothing via exact ids and checksum)
- Bugfix tests: 40 points (all-or-nothing via `pytest` pass)
- Passing suggestion: >= 80/100 with both components passed; adjust to hiring bar.

### Tips

- Keep `secret_salt` confidential. If leaked, rotate and regenerate bundles.
- You can regenerate expected answers at any time from the bundle using the grader.

