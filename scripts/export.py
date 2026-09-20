from pathlib import Path

from exporters.csv import jsonl_to_csv


ROOT = Path(__file__).resolve().parent.parent

input_file = ROOT / "data" / "output" / "clean.jsonl"
output_file = ROOT / "data" / "output" / "businesses.csv"

jsonl_to_csv(
    input_file,
    output_file,
)

print(f"CSV created: {output_file}")