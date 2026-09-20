from __future__ import annotations


def calculate_quality_score(record: dict) -> float:
    score = 0

    if record.get("name"):
        score += 15

    if record.get("website"):
        score += 20

    if record.get("website_status") == "active":
        score += 20

    if record.get("category"):
        score += 10

    if record.get("city"):
        score += 10

    if record.get("state"):
        score += 5

    if record.get("country"):
        score += 5

    if record.get("page_title"):
        score += 5

    if record.get("description"):
        score += 5

    if record.get("source_url"):
        score += 5

    return float(score)