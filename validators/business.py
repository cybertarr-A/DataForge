from __future__ import annotations

from urllib.parse import urlparse


REQUIRED_FIELDS = {
    "name",
    "website",
    "source_url",
    "collected_at",
}


def validate_record(record: dict) -> list[str]:
    errors: list[str] = []

    missing = REQUIRED_FIELDS - record.keys()

    if missing:
        errors.append(
            f"Missing fields: {sorted(missing)}"
        )

    website = record.get("website")

    if website:
        parsed = urlparse(str(website))

        if parsed.scheme not in {"http", "https"}:
            errors.append(
                "Invalid website URL"
            )

    if not record.get("name"):
        errors.append(
            "Business name is empty"
        )

    return errors