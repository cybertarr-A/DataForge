from __future__ import annotations

import csv
import json
from pathlib import Path


def jsonl_to_csv(
    input_file: Path,
    output_file: Path,
) -> None:
    records = []

    with input_file.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            records.append(json.loads(line))

    if not records:
        return

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fields = list(records[0].keys())

    with output_file.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fields,
        )

        writer.writeheader()
        writer.writerows(records)