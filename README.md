# Analysis II Study System

A local German-language study and exam-training system for Analysis II. It combines a structured theory guide, active recall, proof reconstruction, Anki cards, 96 indexed past-exam tasks, family-aware topic weighting, timed exam mode, and local progress tracking.

## Start

Open `app/index.html` directly in a browser. The production bundle can be generated with:

```powershell
npm run build
```

The generated output is written to `dist/analysis2-app/` and is not committed.

## Repository contents

- `00-overview/` through `10-study-plan/`: theory, recall, proofs, exam preparation, and study schedules.
- `11-exam-corpus/`: audited exam/task inventories, duplicate families, topic weighting, and study priorities.
- `app/`: static study application with no server-side component.
- `scripts/`: repeatable generation, migration, audit, and validation helpers.

The navigation entry point for the written material is [`index.md`](index.md).

## Private source PDFs

University scripts, exams, and official solutions are deliberately excluded from this public repository. The curated metadata remains available, but PDF source links work only after the corresponding files have been supplied locally.

To rebuild the exam corpus, place the source files in a local directory and set:

```powershell
$env:ANALYSIS2_EXAM_DIR = "C:\path\to\your\exam-pdfs"
python scripts/build_exam_corpus.py
```

Set `ANALYSIS2_REQUIRE_PDFS=1` when validating a fully populated local PDF package.

## Validation

```powershell
npm test
npm run lint
npm run typecheck
npm run build
python -m unittest scripts.test_app_content scripts.test_exam_corpus
```

The checked-in corpus currently reconciles 13 exams, 96 main tasks, 48 task families, 21 official solution sources, and 7 explicit grading rubrics.

## Reliability

This is an independent study project, not an official university publication. Extraction warnings and unresolved syllabus conflicts are documented in `QUALITY_AUDIT.md`. The original course materials remain authoritative for exact mathematical notation and current examination scope.

