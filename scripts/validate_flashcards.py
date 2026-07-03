import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "09-flashcards" / "anki-flashcards.csv"
with path.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f, delimiter=";"))
assert rows[0] == ["Front", "Back", "Tags", "Difficulty", "Source"], rows[0]
bad = [i for i, row in enumerate(rows, start=1) if len(row) != 5]
if bad:
    raise SystemExit(f"Bad row lengths at rows: {bad[:20]}")
print(f"Validated {len(rows)-1} flashcards")
