from pathlib import Path

base = Path(__file__).resolve().parents[1]
required = [
    "00-overview/master-study-guide.md",
    "01-concept-map/dependency-map.md",
    "01-concept-map/concept-map.mmd",
    "02-definitions/definitions.md",
    "03-theorems/theorems.md",
    "04-proofs/proof-database.md",
    "05-examples/examples-and-patterns.md",
    "06-active-recall/question-bank.md",
    "07-proof-training/proof-reconstruction.md",
    "08-exam-prep/exam-prep.md",
    "09-flashcards/anki-flashcards.csv",
    "09-flashcards/flashcard-guide.md",
    "10-study-plan/study-plan.md",
    "index.md",
    "QUALITY_AUDIT.md",
]
missing = [p for p in required if not (base / p).exists()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))
print("All required files exist.")
