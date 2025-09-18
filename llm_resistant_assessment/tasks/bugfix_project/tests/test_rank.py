from resume_ranker.rank import compute_score, top_k


def test_compute_score_matches_spec():
    weights = {"python": 1.5, "sql": 1.2}
    entry = {
        "resume_id": "C0001",
        "skills": ["python", "sql", "unknown"],
        "years_experience": 15,
        "achievements": {"projects": 3, "publications": 1, "awards": 2, "teams_led": 1},
    }
    # Expected: skills=1.5+1.2+0.5=3.2; exp=0.7*min(15,12)=8.4; ach=0.9*3 + 1.4*1 + 1.8*2 + 1.2*1 = 2.7 + 1.4 + 3.6 + 1.2 = 8.9
    # total = 3.2 + 8.4 + 8.9 = 20.5
    assert abs(compute_score(entry, weights) - 20.5) < 1e-9


def test_top_k_sorting_and_tiebreak():
    weights = {"python": 1.0}
    entries = [
        {"resume_id": "C0002", "skills": ["python"], "years_experience": 0, "achievements": {"projects": 0, "publications": 0, "awards": 0, "teams_led": 0}},
        {"resume_id": "C0001", "skills": ["python"], "years_experience": 0, "achievements": {"projects": 0, "publications": 0, "awards": 0, "teams_led": 0}},
    ]
    # Both have same score 1.0 + 0 + 0 = 1.0, expect lexicographically smaller id first
    out = top_k(entries, weights, k=2)
    assert out == ["C0001", "C0002"]

