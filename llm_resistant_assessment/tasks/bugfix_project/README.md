### Bugfix Mini-Project: Resume Ranker

Your task is to fix the implementation in `resume_ranker/rank.py` so that all tests pass. The tests reflect the scoring rules embedded in the encrypted dataset task.

### Scoring Rules (must match dataset task)

- **score** = sum(skill weights) + 0.7 * min(years_experience, 12) + 0.9 * projects + 1.4 * publications + 1.8 * awards + 1.2 * teams_led
- **Unknown skills**: weight = 0.5
- **Rounding**: scores should be rounded to 6 decimals for output comparisons
- **Tie-break**: When scores are equal, sort by lexicographically smaller `resume_id` first

### What to Do

- Run tests: `python -m pytest -q`
- Open `resume_ranker/rank.py` and correct the implementation to satisfy the tests in `tests/test_rank.py`
- Do not change test expectations. Add code, refactor, or fix logic as needed.

### Deliverable

- Submit this directory with your changes so that `pytest` passes in a clean environment.

