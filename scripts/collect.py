from __future__ import annotations

import json
import sys
from pathlib import Path

from collectors.website import WebsiteCollector


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "data" / "raw" / "records.jsonl"


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/collect.py URL [URL ...]"
        )
        raise SystemExit(1)

    collector = WebsiteCollector()

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    collected = 0

    with OUTPUT.open(
        "w",
        encoding="utf-8",
    ) as file:

        for url in sys.argv[1:]:
            try:
                records = collector.collect(url)

                for record in records:
                    file.write(
                        json.dumps(
                            record,
                            default=str,
                        )
                        + "\n"
                    )

                    collected += 1

                print(f"[OK] {url}")

            except Exception as exc:
                print(
                    f"[ERROR] {url}: {exc}"
                )

    print()
    print(f"Collected: {collected}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()