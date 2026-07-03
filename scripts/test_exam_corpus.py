import csv
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_exam_corpus", ROOT / "scripts" / "build_exam_corpus.py")
CORPUS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORPUS)


class ExamCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tasks = CORPUS.parse_rows()
        cls.exams = []
        for exam in CORPUS.EXAMS:
            copy = dict(exam)
            copy["asset"] = f"exam-pdfs/{exam['asset']}"
            exam_tasks = [task for task in cls.tasks if task["examId"] == exam["id"]]
            copy["taskIds"] = [task["id"] for task in exam_tasks]
            copy["taskCount"] = len(exam_tasks)
            copy["solutionStatuses"] = sorted({task["officialSolutionStatus"] for task in exam_tasks})
            copy.update(CORPUS.EXAM_AUDIT[exam["id"]])
            cls.exams.append(copy)
        cls.topics = CORPUS.build_topic_weighting(cls.exams, cls.tasks)

    def test_reconciled_counts_and_ids(self):
        self.assertEqual(len(self.exams), 13)
        self.assertEqual(len(self.tasks), 96)
        self.assertEqual(len({task["id"] for task in self.tasks}), 96)
        self.assertEqual(len({task["duplicateFamily"] for task in self.tasks}), 48)

    def test_solution_and_rubric_provenance(self):
        self.assertEqual(sum(task["officialSolutionStatus"] != "no_solution" for task in self.tasks), 21)
        self.assertEqual(sum(task["officialSolutionStatus"] == "official_rubric" for task in self.tasks), 7)
        self.assertTrue(all(task["officialSolutionStatus"] == "official_rubric" for task in self.tasks if task["examId"] == "ss21-nach"))
        self.assertTrue(all(task["officialSolutionStatus"] == "official_solution" for task in self.tasks if task["examId"] in {"ss21", "ss25"}))

    def test_exact_duplicates_are_family_collapsed(self):
        exact = [task for task in self.tasks if task["familyRelation"] == "exact_duplicate"]
        self.assertEqual(len(exact), 10)
        self.assertEqual(len({task["duplicateFamily"] for task in exact}), 5)

    def test_scope_conflicts_remain_unresolved(self):
        status = {row["topic"]: row["currentScopeStatus"] for row in self.topics}
        self.assertEqual(status["differentialgleichungen"], "unresolved")
        self.assertEqual(status["mannigfaltigkeiten"], "unresolved")
        self.assertEqual(status["mehrdimensionale-integrale"], "unresolved")
        self.assertEqual(status["kurven"], "likely_outdated")
        self.assertEqual(status["dynamische-systeme"], "likely_outdated")

    def test_weighting_uses_families_and_consistent_components(self):
        for row in self.topics:
            self.assertLessEqual(row["uniqueTaskFamilyCount"], row["rawTaskCount"])
            total = sum(value for value in row["scoreComponents"].values() if value is not None)
            self.assertAlmostEqual(row["weightScore"], total, delta=0.06)
            self.assertEqual(row["currentExerciseCoverage"], "not_provided")

    def test_exam_metadata_correction_and_inferred_points(self):
        exam = {item["id"]: item for item in self.exams}
        self.assertEqual(exam["ss18"]["lecturer"], "Alexander Lytchak")
        self.assertEqual(exam["geiges03"]["totalPoints"], 100)
        geiges_points = sum(task["points"] for task in self.tasks if task["examId"] == "geiges03")
        self.assertEqual(geiges_points, 100)

    def test_generated_csv_counts_match_data(self):
        with (ROOT / "11-exam-corpus" / "exam-inventory.csv").open(encoding="utf-8-sig", newline="") as handle:
            self.assertEqual(len(list(csv.DictReader(handle, delimiter=";"))), 13)
        with (ROOT / "11-exam-corpus" / "task-inventory.csv").open(encoding="utf-8-sig", newline="") as handle:
            self.assertEqual(len(list(csv.DictReader(handle, delimiter=";"))), 96)
        with (ROOT / "11-exam-corpus" / "topic-weighting.csv").open(encoding="utf-8-sig", newline="") as handle:
            self.assertEqual(len(list(csv.DictReader(handle, delimiter=";"))), len(self.topics))


if __name__ == "__main__":
    unittest.main()
