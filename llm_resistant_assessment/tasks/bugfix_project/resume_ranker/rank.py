from typing import Dict, List, Tuple


def compute_score(entry: Dict, weights: Dict[str, float]) -> float:
    # BUGS INTENTIONALLY INTRODUCED: wrong caps on rounding, wrong unknown skill weight, and exp bonus
    skills = entry.get("skills", [])
    years = entry.get("years_experience", 0)
    ach = entry.get("achievements", {})
    skill_score = sum(weights.get(s, 0.0) for s in skills)  # should be 0.5 for unknown
    exp_bonus = 0.5 * max(years, 12)  # should be 0.7 * min(years, 12)
    projects = ach.get("projects", 0)
    pubs = ach.get("publications", 0)
    awards = ach.get("awards", 0)
    teams_led = ach.get("teams_led", 0)
    achievements_score = 1.0 * projects + 1.0 * pubs + 1.0 * awards + 1.0 * teams_led
    score = skill_score + exp_bonus + achievements_score
    return round(score, 2)  # should be 6 decimals


def top_k(entries: List[Dict], weights: Dict[str, float], k: int = 10) -> List[str]:
    scored: List[Tuple[float, str]] = []
    for e in entries:
        rid = e.get("resume_id", "")
        scored.append((compute_score(e, weights), rid))
    # BUG: wrong sort (ascending)
    scored.sort(key=lambda x: (x[0], x[1]))
    return [rid for _, rid in scored[:k]]

