# Quality Audit

## Completed

- Source PDF read locally; the university PDF is not included in the public repository.
- Reconstructed outline sections: 79.
- Numbered study objects extracted: 404.
- Definitions: 120.
- Theorems/Sätze: 177.
- Lemmas: 18.
- Folgerungen/Korollare: 15.
- Examples: 37.
- Active recall questions generated: 760.
- Required files missing: none.

## Verification Questions

1. Did this cover every chapter/section of the PDF? **Yes**, every outline entry from chapters 1-9, Appendix A, notes, exercises, and literature is represented in the overview/dependency system.
2. Did it extract all major definitions? **Yes with OCR caveat**: 120 numbered definitions were extracted.
3. Did it extract all major theorems/lemmas/propositions/corollaries? **Yes for numbered Satz/Lemma/Folgerung/Korollar entries**: 210 detected.
4. Did it include proof training for important proofs? **Yes**, high-yield proof trainers were generated.
5. Did it create active recall questions for every major section? **Yes**, section-level and item-level questions were generated.
6. Did it create Anki cards? **Yes**, see `09-flashcards/anki-flashcards.csv`.
7. Did it create a study plan? **Yes**, see `10-study-plan/study-plan.md`.
8. Did it mark uncertainties? **Yes**, every item has an uncertainty line; 45 entries have extraction warnings.
9. Did it avoid unsupported invented claims? **Mostly yes**: generated explanations are labeled as study explanations; exact statements are sourced from the PDF extraction or marked for verification. Supplementary examples are explicitly marked.
10. Is there an index explaining how to use the system? **Yes**, see `index.md`.

## What May Be Incomplete

- Unnumbered statements, examples, and informal comments may not be separately indexed unless they occur inside a numbered block.
- Some proofs are only available as OCR-normalized script transcriptions and should be manually checked for exact symbols.
- Exercise sections are represented as study prompts and strategy material, not official solutions.
- Mathematical diagrams and figures are not recreated.

## Extraction Limitations

- The PDF text layer contains corrupted symbols for square roots, mapsto arrows, empty set, matrix brackets, and some display math.
- Ligatures were normalized, but not every formula can be safely converted to perfect LaTeX automatically.
- Page ranges for sections beginning on the same physical page are approximate.

## Recommended Manual Checks

- Check every high-yield theorem statement against the PDF before exam memorization.
- Verify formulas in entries with extraction warnings.
- For proof memorization, compare `04-proofs/proof-database.md` with the original PDF proof.
- Add official exercise solutions separately if your course provides them.

## Next Improvements

- Manually polish the LaTeX of the 40-60 highest-yield entries.
- Add solved exercise sheets when available.
- Add screenshots or redraw diagrams for compactness, Bolzano-Weierstrass, and inverse/implicit theorem intuition.

## Strict Post-Generation Audit

- Sampled/check rows recorded: 363.
- Correct: 303.
- Minor issues: 46.
- Serious issues: 10.
- Unverifiable/deficit rows: 4.
- Files modified after audit: `scripts/build_study_system.py`, `source-inventory.json`, `scripts/source-inventory.md`, generated Markdown databases, `09-flashcards/anki-flashcards.csv`, `app/data.js`, `AUDIT_REPORT_STRICT.md`, `QUALITY_AUDIT.md`.
- Serious issues fixed: Appendix A extraction, missing Markdown source inventory, and wrong high-yield overlays for `3.2.3`, `4.2.1`, `4.3.2`, `5.2.4`, `5.3.5`, `6.4.2`, `6.6.5`, `7.2.9`.
- Minor issues fixed: broad section-title fallback labels for unnamed definitions.
- Remaining manual checks: visually verify uncertainty-marked formulas against the PDF and do not treat generic proof-database scaffolds as fully polished proof rewrites.
- Reliability claim: sample results support using the system as a structured study index and active-recall scaffold, not as a fully verified substitute for the PDF.

## App Math Rendering Fix

- Rendering library: MathJax 3 SVG is vendored at `app/vendor/mathjax-tex-svg.js`; the local app no longer needs a CDN for mathematics.
- Delimiters supported: `$...$`, `\(...\)`, `$$...$$`, and `\[...\]`.
- Dynamic views call MathJax after Browse, Abfrage, Karteikarten, Beweise, and detail updates.
- Invalid formulas are validated before rendering, logged with their item ID, and replaced by a readable non-crashing fallback.
- The raw-source toggle remains available in the detail view for manual comparison.

## Complete Study Card Redesign

- Scope: all 403 learning blocks, 757 recall questions, and 34 proof records in the app data.
- Data schema: app data now uses schema version 2 with separate `metadata`, German `summary`, semantic `contentBlocks`, and internal `needsReview` fields.
- Migration: `scripts/migrate_app_data.py` creates the one-time backup `app/data.pre-card-redesign.js`, restores German PDF source text, removes repeated headers/footers, adds remarks, and applies the shared enrichment pipeline.
- Generation: `scripts/app_content.py` centralizes source cleanup, German summaries, metadata parsing, LaTeX normalization/validation, semantic blocks, and the three required regression entries. `scripts/build_study_system.py` now calls this pipeline for future app data.
- Interface: all visible navigation, filters, states, accessibility labels, difficulty badges, buttons, summaries, and detail controls are German. Internal values such as `low`, `medium`, and `high` are mapped centrally and are not displayed.
- Cards: metadata is separate from titles and mathematical content; titles omit meaningless fallback names; content uses paragraph, label, and formula blocks; action buttons use the high-contrast label `Lernen`.
- Responsive layout: shared grids use `minmax(0, 1fr)`, card/form controls may shrink, formulas scroll only within their formula block, and navigation becomes a stable two-column grid at narrow widths.
- Regression cards verified: `6.4.3`, `4.1.4`, and `4.1.6`, including the integral, inverse-function, monotonicity, and root formulas requested.
- Automated verification: 15 JavaScript tests and 10 Python tests pass; syntax/lint, both data validators, and the production build pass. Validated data contains 403 learning blocks, 757 questions, 34 proofs, 13 exams, and 96 exam tasks.
- Visual verification: final headless Edge captures are stored in `qa-screenshots/` for two desktop regression cards and one narrow regression card. The 390px Windows headless capture was discarded because Edge imposed a larger minimum layout viewport and cropped the bitmap; the final narrow capture uses Edge's actual minimum viewport, while CSS tests cover the 320px rule set.
- Remaining manual review: 58 learning blocks, 197 generated questions, and 3 proof records retain `needsReview` because their source extraction contains ambiguous or damaged mathematics. These flags are internal and must be checked against the PDF before exact memorization.
- Reliability claim: the redesigned interface and regression formulas are verified, but the app is not claimed as a mathematically perfect replacement for the PDF while these source-review flags remain.

## Altlausur-Driven Exam Upgrade

- Source inventory: 16 supplied PDFs were hashed and page-counted. The 111-page `Ana2 Altklausur.pdf` bundle is recorded as a duplicate archive rather than a fourteenth exam.
- Curated corpus: 13 distinct exams and 96 main tasks from SS 2003 through SS 2025.
- Official solution coverage: 21 tasks from SS 2021, its resit, and SS 2025 link to supplied course-produced solutions or marking guidance. No official status is assigned to generated hints.
- Scan handling: SS 2018 and Geiges 2003 were visually transcribed from rendered pages. Thorbergsson 2013 remains low confidence because the source itself says it is an uncertain recollection.
- Point validation: all exams with complete point metadata sum to their published totals: 50, 40, 53, 150, 150, and 120 points.
- Theory mapping: stable study IDs are attached only where the current script covers the concept. Tasks on differential equations, curves, multidimensional integration, manifolds, and dynamical systems are marked outside or partly outside the script.
- Exam-prerequisite repair: Definition `7.2.9` was manually checked against PDF page 121 (printed page 119), reduced to the exact definitions of completeness, Banach space, and Hilbert space, and removed from the review queue.
- New app workflows: `Aufgaben` provides filters, staged hints, source links, self-scoring, confidence, and error categories; `Prüfung` provides original and mixed exams, a persistent timer, flags, answer lockout, and rubric review; `Fehleranalyse` provides the 20/50/30 queue, mastery dimensions, and an error log.
- Answer-leak protection: the supplied SS 2025 file embeds solutions below each prompt, so the corpus builder creates a seven-page question-only PDF using verified CropBox boundaries. The complete official file is linked only after submission.
- Persistence: attempts and active exam state stay in local storage under `analysis2-exam-progress-v1`.
- Automated verification: corpus schema, unique IDs, point totals, task/source pages, local PDF assets, solution provenance, source confidence, solution lockout, timer restoration, scoring, mock selection, and queue behavior are tested.
- Remaining limitation: no current exercise sheets were included, so exercise-sheet overlap could not be weighted. The current-script mapping is the strongest available course-specific signal.
- Browser verification: filtering, hints, solution reveal, attempt storage, timer restoration, submission, post-submit solution access, scoring, dashboard updates, and narrow layouts were exercised in the production build with no browser warnings or errors.

## Exam Corpus Scope and Priority Audit

- Reconciled corpus: 13 distinct exams, 96 bundled main tasks, and 48 unique task families. The five exact Sweers 2010 duplicate pairs are family-collapsed for adjusted frequency while remaining visible as source tasks.
- Exam metadata: `exam-inventory.csv` records duration, points, completeness, source confidence, duplicates, solution/rubric availability, and syllabus fit. Unknown metadata remains `unknown`. The SS 2018 lecturer spelling was corrected to Alexander Lytchak; Geiges 2003 is recorded as 100 inferred points from the ten visible task values, not as a published cover-sheet total.
- Task reconciliation: `task-inventory.csv` contains all 96 IDs with valid solution and scope labels. Current-scope counts are 66 `confirmed_current`, 4 `likely_current`, 1 `historically_examined`, 9 `likely_outdated`, and 16 `unresolved`.
- Solution coverage: 21 tasks have an official supplied solution source. Exactly 7 tasks, all from the SS 2021 resit, have an explicit official `Bewertungsschlüssel`; SS 2021 and SS 2025 worked solutions are not mislabeled as rubrics.
- Confirmed script topics: multidimensional differentiability, extrema, metric spaces, compactness, topology, implicit functions, directional derivatives, continuity, Lagrange multipliers, uniform convergence, inverse theorem, completeness, connectedness, one-dimensional integration, series, Banach fixed point, improper integrals, Taylor expansion, sequences, and complex numbers.
- Likely outdated topic groups: curves/arc length, Analysis-I-only review, and planar dynamical systems. This is an evidence classification, not proof of exclusion.
- Unresolved scope: differential equations, manifolds, and multidimensional integration occur in SS 2025 but lack adequate script coverage; the incomplete Thorbergsson convergence recollection is also unresolved. Current exercise sheets or an official scope list are required before promoting or excluding these topics.
- Script gaps: `script-gap-analysis.md` verifies the five requested groups. Differential equations, manifolds, and multidimensional integration require supplementary material if confirmed; curves and dynamical systems currently have only older evidence.
- Weighting: `topic-weighting.csv` reports exam count, raw tasks, unique families, apportioned known points, recent appearances, official-source coverage, script coverage, and source confidence. The formula and equal point-apportionment limitation are documented in `topic-weighting-method.md`. Exercise evidence is explicitly `not_provided` and contributes no fabricated signal.
- Scoring limitations: exact earned points are supported only for tasks with an official rubric. All other app assessments are labeled `Geschätzte Bewertung`, stored separately as self-estimates, and paired with confidence plus one of six partial-credit categories.
- Reliability indicators: every task displays one of the six required German solution statuses. Reconstructed and AI-generated statuses are supported by the mandatory warning but no such solutions currently exist in the corpus.
- Verification: 19 JavaScript tests and 17 Python tests pass. Syntax/lint, both data validators, and the production build pass. The data validator reconciles 13 exams, 96 tasks, 48 families, 21 official solution sources, and 7 rubrics against the CSV reports.
- Browser checks: desktop 1280px and mobile 390px layouts have no horizontal overflow; unresolved filtering returns 16 tasks; rubric-backed and estimated scoring states render correctly; active exam mode exposes one question source and zero solution links; console warnings/errors are empty.
- Files added or updated: the three CSV inventories/weighting files, `topic-weighting-method.md`, `script-gap-analysis.md`, `final-study-priorities.md`, corpus generator/data, app reliability UI and logic, validators/tests, README/index, and this audit.
- Reliability claim: the priority model is reproducible and more reliable than raw frequency, but the actual 2026 exam scope remains only partially determined until current exercise sheets or an official topic list are supplied.
