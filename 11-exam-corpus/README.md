# Altlausur Corpus

This folder contains the curated source of the written-exam upgrade.

## Files

- `exam-corpus.json`: 13 distinct exams, 96 main tasks, topic mappings, source confidence, points, hints, theory links, and solution provenance.
- `exam-inventory.csv`: reconciled metadata, completeness, duplication, solution, rubric, and syllabus status for all 13 exams.
- `task-inventory.csv`: all 96 main tasks with source status, scope status, scoring status, and duplicate family.
- `topic-weighting.csv`: raw and family-adjusted frequency, points, recency, source support, and priority score.
- `topic-weighting-method.md`: transparent formula, point-allocation convention, and limitations.
- `script-gap-analysis.md`: evidence review for the five recurring topics not covered by the script.
- `final-study-priorities.md`: priority A/B/C/Ungeklärt with study-depth recommendations.
- `exam-blueprint.md`: compact corpus summary and links to the detailed audits.
- Original non-duplicate PDFs are packaged under `app/exam-pdfs/` for local source links.

## Provenance Rules

- SS 2021 and SS 2025 are labeled `Offizielle Lösung`; only the SS 2021 resit is labeled `Offizielles Bewertungsschema` because its document explicitly contains a detailed `Bewertungsschlüssel`.
- Tasks without such a document receive hints but no invented official solution.
- SS 2018 and Geiges 2003 are manual visual transcriptions from image scans.
- Thorbergsson 2013 is an uncertain recollection protocol.
- Damaged formulas in Marinescu 2008 must be read in the original PDF.
- SS 2025 uses a generated question-only PDF during timed exams; the complete source with embedded solutions is linked only after submission.
- `Ana2 Altklausur.pdf` is a duplicate archive and is audited but not counted as another exam.

## Rebuild

Run the bundled Python runtime with `scripts/build_exam_corpus.py`, then run the data validators and production build.

The generated app data is not the authority for mathematical wording. The original PDFs remain authoritative.
