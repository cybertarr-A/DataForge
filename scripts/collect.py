from __future__ import annotations

import json
from pathlib import Path

from collectors.website import WebsiteCollector


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "data" / "raw" / "raw.jsonl"


SOURCES = [
    "https://example.com",
]


def main() -> None:
    collector = WebsiteCollector()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT.open("w", encoding="utf-8") as file:
        for source in SOURCES:
            print(f"Collecting: {source}")

            try:
                records = collector.collect(source)

                for record in records:
                    record["website"] = str(record["website"])
                    record["source_url"] = str(record["source_url"])
                    record["collected_at"] = record["collected_at"].isoformat()

                    file.write(
                        json.dumps(record, ensure_ascii=False) + "\n"
                    )

                print(f"  ✓ {len(records)} record(s)")

            except Exception as exc:
                print(f"  ✗ Failed: {exc}")


if __name__ == "__main__":
    main()