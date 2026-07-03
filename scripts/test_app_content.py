from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app_content import (
    build_content_blocks,
    enrich_item,
    normalize_latex,
    parse_metadata,
    strip_pdf_noise,
    validate_latex,
)


BASE_DIR = Path(__file__).resolve().parents[1]


class AppContentTests(unittest.TestCase):
    def test_repeated_pdf_header_is_removed(self):
        source = "Aussage. ANALYSIS I-III, 2011/2013 102 Nächster Satz."
        self.assertEqual(strip_pdf_noise(source), "Aussage. Nächster Satz.")

    def test_next_section_heading_is_removed(self):
        source = "Die Funktion ist streng monoton. 4.2. Der Zwischenwertsatz. Weitere Einleitung."
        self.assertEqual(strip_pdf_noise(source), "Die Funktion ist streng monoton.")

    def test_latex_normalizes_mathbb_arrow_and_sqrt(self):
        source = r"I \subset R, f : I → C, \sqrt 2"
        normalized = normalize_latex(source)
        self.assertIn(r"I \subseteq \mathbb{R}", normalized)
        self.assertIn(r"\to \mathbb{C}", normalized)
        self.assertIn(r"\sqrt{2}", normalized)

    def test_malformed_sqrt_is_detected(self):
        self.assertIn("Wurzel ohne sicheres Argument", validate_latex(r"\sqrt"))

    def test_unmatched_braces_and_delimiters_are_detected(self):
        issues = validate_latex(r"\mathbb{R \(x")
        self.assertIn("nicht geschlossene geschweifte Klammer", issues)
        self.assertIn("nicht passende Inline-Mathematik-Trennzeichen", issues)

    def test_metadata_is_separated(self):
        metadata = parse_metadata(
            "PDF p103; section 6.4. Der Hauptsatz der Differential- und Integralrechnung",
            "6.4. Der Hauptsatz der Differential- und Integralrechnung",
        )
        self.assertEqual(metadata["page"], 103)
        self.assertEqual(metadata["sectionNumber"], "6.4")
        self.assertEqual(metadata["sectionTitle"], "Der Hauptsatz der Differential- und Integralrechnung")

    def test_regression_cards_have_expected_german_schema(self):
        raw = (BASE_DIR / "app" / "data.js").read_text(encoding="utf-8")
        payload = json.loads(raw.split("=", 1)[1])
        items = {item["id"]: item for item in payload["items"]}
        expected = {
            "6.4.3": ("Unbestimmtes Integral", "Diese Definition beschreibt das unbestimmte Integral"),
            "4.1.4": ("Stetigkeit der Umkehrfunktion", "Dieser Satz zeigt"),
            "4.1.6": ("Monoton steigend", "Diese Definition führt monotones"),
        }
        for item_id, (title, summary_start) in expected.items():
            self.assertEqual(items[item_id]["title"], title)
            self.assertTrue(items[item_id]["summary"].startswith(summary_start))
            self.assertFalse(items[item_id]["needsReview"])
            self.assertTrue(any(block["type"] == "math" for block in items[item_id]["contentBlocks"]))

    def test_regression_formulas_are_valid(self):
        cases = [
            r"\int f(x)\,dx = \{F_0 + C : C \in \mathbb{C}\} = F_0 + \mathbb{C}",
            r"g \colon E \to [a,b], \qquad g = f^{-1}",
            r"x \leq y \quad\Longrightarrow\quad f(x) \leq f(y)",
            r"\sqrt[k]{\,\cdot\,}",
        ]
        for formula in cases:
            self.assertEqual(validate_latex(formula), [])

    def test_exam_prerequisite_729_is_manually_verified(self):
        item = enrich_item(
            {
                "id": "7.2.9",
                "kind": "Definition",
                "title": "Vollständigkeit in metrischen Räumen",
                "section": "7.2. Metrische und normierte Räume",
                "source": "PDF p121; section 7.2. Metrische und normierte Räume",
                "statement": "beschädigte OCR-Fassung",
                "warning": "OCR/math symbol normalization should be manually checked.",
            }
        )
        self.assertFalse(item["needsReview"])
        self.assertEqual(item["reviewIssues"], [])
        self.assertNotIn("7.2.10", item["statement"])
        self.assertEqual([block["text"] for block in item["contentBlocks"] if block["type"] == "label"], ["Vollständiger metrischer Raum", "Banachraum", "Hilbertraum"])

    def test_generic_item_is_german_and_header_free(self):
        item = enrich_item(
            {
                "id": "1.2.3",
                "kind": "Definition",
                "title": "unnamed definition in 1.2",
                "section": "1.2. Anordnungsaxiome",
                "source": "PDF p9; section 1.2. Anordnungsaxiome",
                "statement": "Sei x in K. ANALYSIS I-III, 2011/2013 8",
                "exam": "medium",
            }
        )
        self.assertEqual(item["title"], "")
        self.assertIn("Diese Definition", item["summary"])
        self.assertNotIn("ANALYSIS", item["statement"])


if __name__ == "__main__":
    unittest.main()
