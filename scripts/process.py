from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from validators.business import validate_record
from validators.quality import calculate_quality_score


ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "data" / "raw" / "records.jsonl"
OUTPUT = ROOT / "data" / "output" / "businesses.csv"


def load_records() -> list[dict]:
    records = []

    with INPUT.open(
        "r",
        encoding="utf-8",
    ) as file:

        for line in file:
            if not line.strip():
                continue

            records.append(
                json.loads(line)
            )

    return records


def main() -> None:
    records = load_records()

    valid_records = []

    for record in records:
        errors = validate_record(record)

        if errors:
            print(
                f"[INVALID] "
                f"{record.get('website')}: "
                f"{errors}"
            )
            continue

        record["data_quality_score"] = (
            calculate_quality_score(record)
        )

        valid_records.append(record)

    if not valid_records:
        print("No valid records found.")
        return

    df = pd.DataFrame(
        valid_records
    )

    df = df.drop_duplicates(
        subset=["website"]
    )

    df.to_csv(
        OUTPUT,
        index=False,
    )

    print(
        f"Valid records: {len(df)}"
    )

    print(
        f"Output: {OUTPUT}"
    )


if __name__ == "__main__":
    main()