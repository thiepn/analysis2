from __future__ import annotations

import hashlib
import csv
import json
import os
import shutil
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import pdfplumber
from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(os.environ.get("ANALYSIS2_EXAM_DIR", ROOT / "local-sources" / "exams"))
CORPUS_DIR = ROOT / "11-exam-corpus"
APP_PDF_DIR = ROOT / "app" / "exam-pdfs"

EXAMS = [
    {"id": "ss18", "title": "Klausur Analysis II SS 2018", "semester": "SS 2018", "lecturer": "Alexander Lytchak", "date": "2018-07-21", "durationMinutes": 180, "allowedAids": "keine", "totalPoints": 50, "file": "Ana2-SS18.pdf", "asset": "ss18.pdf", "textLayer": False, "sourceConfidence": "hoch", "notes": "Bildscan; Deckblatt und Aufgaben visuell geprüft."},
    {"id": "geiges03", "title": "Klausur Analysis II SS 2003", "semester": "SS 2003", "lecturer": "Hansjörg Geiges", "date": None, "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": 100, "file": "AnaII_Geiges_03.pdf", "asset": "geiges03.pdf", "textLayer": False, "sourceConfidence": "mittel", "notes": "Bildscan ohne Deckblatt; 100 Punkte aus den zehn sichtbaren Aufgaben summiert."},
    {"id": "geiges15", "title": "Erstklausur Analysis II SS 2015", "semester": "SS 2015", "lecturer": "Hansjörg Geiges", "date": None, "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": None, "file": "AnaII_Geiges_15_1.pdf", "asset": "geiges15.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Originalklausur."},
    {"id": "marinescu08", "title": "Klausur Analysis II SS 2008", "semester": "SS 2008", "lecturer": "Marinescu / Erat", "date": None, "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": 40, "file": "AnaII_Marinescu_08.pdf", "asset": "marinescu08.pdf", "textLayer": True, "sourceConfidence": "mittel", "notes": "Textschicht ist bei einzelnen Formeln beschädigt; Original-PDF ist maßgeblich."},
    {"id": "sweers10-mix", "title": "Klausur Analysis I + II 2010", "semester": "SS 2010", "lecturer": "Guido Sweers", "date": "2010-07-24", "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": None, "file": "AnaII_Sweers_10_3.pdf", "asset": "sweers10-mix.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Prüfungsstoff kombiniert Analysis I und II."},
    {"id": "sweers10", "title": "Klausur Analysis II 2010", "semester": "SS 2010", "lecturer": "Guido Sweers", "date": "2010-07-24", "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": None, "file": "AnaII_Sweers_10_4.pdf", "asset": "sweers10.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Originalklausur."},
    {"id": "sweers14-1", "title": "Klausur Analysis II 2014", "semester": "SS 2014", "lecturer": "Guido Sweers", "date": "2014-07-19", "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": None, "file": "AnaII_Sweers_14_1.pdf", "asset": "sweers14-1.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Originalklausur."},
    {"id": "sweers14-2", "title": "Weitere Klausur Analysis II 2014", "semester": "SS 2014", "lecturer": "Guido Sweers", "date": None, "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": None, "file": "AnaII_Sweers_14_2.pdf", "asset": "sweers14-2.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Aufgabenblätter ohne Deckblatt."},
    {"id": "thorbergsson13", "title": "Erinnerungsprotokoll Analysis II SS 2013", "semester": "SS 2013", "lecturer": "Gudlaugur Thorbergsson", "date": None, "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": None, "file": "AnaII_Thorbergsson_13.pdf", "asset": "thorbergsson13.pdf", "textLayer": True, "sourceConfidence": "niedrig", "notes": "Nicht offizielles Erinnerungsprotokoll; Quelle vermerkt ausdrücklich 'keine Garantie'."},
    {"id": "ss20", "title": "Klausur Analysis II SS 2020", "semester": "SS 2020", "lecturer": "Marinescu / Zielinski", "date": None, "durationMinutes": None, "allowedAids": "unbekannt", "totalPoints": 53, "file": "klausur1_ss20a.pdf", "asset": "ss20.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Originalklausur."},
    {"id": "ss21", "title": "Klausur Analysis II SS 2021", "semester": "SS 2021", "lecturer": "Silvia Sabatini", "date": "2021-07-24", "durationMinutes": None, "allowedAids": "keine", "totalPoints": 150, "file": "Klausur_Analysis II_SS21_Sabatini.pdf", "asset": "ss21.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Originalklausur mit separatem offiziellem Lösungsvorschlag."},
    {"id": "ss21-nach", "title": "Nachklausur Analysis II SS 2021", "semester": "SS 2021", "lecturer": "Silvia Sabatini", "date": "2021-09-18", "durationMinutes": None, "allowedAids": "keine", "totalPoints": 150, "file": "Nachklausur_Analysis2_SS21_Sabatini.pdf", "asset": "ss21-nach.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Originalklausur mit offiziellen Lösungen und Bewertungsschlüssel."},
    {"id": "ss25", "title": "Klausur Analysis II SS 2025", "semester": "SS 2025", "lecturer": "Silvia Sabatini", "date": "2025-07-26", "durationMinutes": None, "allowedAids": "keine", "totalPoints": 120, "file": "Klausur Analysis II-SS25_Loesungen.pdf", "asset": "ss25-aufgaben.pdf", "textLayer": True, "sourceConfidence": "hoch", "notes": "Die lokale Aufgabenfassung ist oberhalb der eingebetteten Lösungen beschnitten; das vollständige Original wird erst in der Auswertung verlinkt."},
]

SOLUTION_FILES = {
    "ss21": {
        "file": "Lösungsvorschlag Klausur Analysis II-SS21.pdf", "asset": "loesung-ss21.pdf",
        "pages": [(1, 2), (3, 4), (5, 6), (7, 7), (8, 9), (10, 11), (12, 13)],
        "status": "official_solution", "gradingStatus": "source_points_only",
    },
    "ss21-nach": {
        "file": "Lösungsvorschlag Nachklausur Analysis II-SS21.pdf", "asset": "loesung-ss21-nach.pdf",
        "pages": [(2, 2), (3, 4), (5, 7), (8, 8), (9, 9), (10, 11), (12, 13)],
        "status": "official_rubric", "gradingStatus": "official_rubric",
    },
    "ss25": {
        "file": "Klausur Analysis II-SS25_Loesungen.pdf", "asset": "ss25-loesungen.pdf",
        "pages": [(2, 2), (3, 3), (4, 4), (5, 5), (6, 7), (8, 9), (10, 11)],
        "status": "official_solution", "gradingStatus": "source_points_only",
    },
}

SOLUTION_LABELS = {
    "official_solution": "Offizielle Lösung",
    "official_rubric": "Offizielles Bewertungsschema",
    "partial_official_solution": "Teilweise offizielle Lösung",
    "reconstructed_solution": "Rekonstruierte Lösung",
    "ai_generated_solution": "KI-generierte Lösung",
    "no_solution": "Keine verifizierte Lösung",
}

VALID_SCOPE_STATUSES = {
    "confirmed_current", "likely_current", "historically_examined", "likely_outdated", "unresolved",
}

EXAM_AUDIT = {
    "ss18": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "historically_examined"},
    "geiges03": {"completeStatus": "wahrscheinlich_vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "likely_outdated"},
    "geiges15": {"completeStatus": "wahrscheinlich_vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "likely_outdated"},
    "marinescu08": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "likely_outdated"},
    "sweers10-mix": {"completeStatus": "wahrscheinlich_vollständig", "duplicateStatus": "teilweise_nahe_variante_von:sweers10", "currentScopeStatus": "likely_outdated"},
    "sweers10": {"completeStatus": "wahrscheinlich_vollständig", "duplicateStatus": "teilweise_nahe_variante_von:sweers10-mix", "currentScopeStatus": "likely_outdated"},
    "sweers14-1": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "historically_examined"},
    "sweers14-2": {"completeStatus": "wahrscheinlich_vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "historically_examined"},
    "thorbergsson13": {"completeStatus": "unvollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "unresolved"},
    "ss20": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "historically_examined"},
    "ss21": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "historically_examined"},
    "ss21-nach": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "historically_examined"},
    "ss25": {"completeStatus": "vollständig", "duplicateStatus": "eigenständig", "currentScopeStatus": "likely_current"},
}

SCRIPT_GAP_TOPICS = {
    "differentialgleichungen", "mannigfaltigkeiten", "kurven", "mehrdimensionale-integrale", "dynamische-systeme",
}

TOPIC_SCOPE = {
    "differentialgleichungen": "unresolved",
    "mannigfaltigkeiten": "unresolved",
    "mehrdimensionale-integrale": "unresolved",
    "kurven": "likely_outdated",
    "dynamische-systeme": "likely_outdated",
    "analysis-1": "likely_outdated",
    "unsicher": "unresolved",
}

# Families are intentionally conservative: only clear exact duplicates or recurring
# mathematical templates are grouped. Every unlisted task receives its own family.
FAMILY_GROUPS = {
    "exact-sweers10-linear-systems": {"relation": "exact_duplicate", "tasks": ["sweers10-mix-6", "sweers10-5"]},
    "exact-sweers10-lagrange-claim": {"relation": "exact_duplicate", "tasks": ["sweers10-mix-7", "sweers10-6"]},
    "exact-sweers10-taylor-sinxy": {"relation": "exact_duplicate", "tasks": ["sweers10-mix-8", "sweers10-7"]},
    "exact-sweers10-product-factor": {"relation": "exact_duplicate", "tasks": ["sweers10-mix-9", "sweers10-9"]},
    "exact-sweers10-global-extrema": {"relation": "exact_duplicate", "tasks": ["sweers10-mix-10", "sweers10-10"]},
    "template-curve-length": {"relation": "computational_template", "tasks": ["ss18-4", "geiges03-2", "geiges15-1", "sweers10-4", "sweers14-1-1", "sweers14-2-1"]},
    "template-critical-point-classification": {"relation": "computational_template", "tasks": ["geiges03-3", "sweers14-2-2", "ss21-3", "ss25-4"]},
    "template-directional-not-total": {"relation": "proof_template", "tasks": ["geiges03-7", "sweers14-1-5", "thorbergsson13-4", "ss21-4", "ss25-2"]},
    "template-differentiability-definition": {"relation": "theorem_variant", "tasks": ["ss18-1", "geiges03-6", "geiges15-2", "marinescu08-4"]},
    "template-implicit-function-derivatives": {"relation": "computational_template", "tasks": ["geiges03-8", "geiges15-5", "ss20-5", "ss21-6"]},
    "template-lagrange-constrained-extrema": {"relation": "computational_template", "tasks": ["geiges03-9", "geiges15-4", "sweers14-1-6", "sweers14-2-6", "ss20-4", "ss21-nach-3"]},
    "template-inverse-local-invertibility": {"relation": "theorem_variant", "tasks": ["ss18-5", "sweers14-1-7", "sweers14-2-7", "ss21-nach-5"]},
    "template-dgl-separable-ivp": {"relation": "computational_template", "tasks": ["sweers10-1", "sweers14-1-3", "sweers14-2-4", "ss20-3", "ss25-6"]},
    "template-dgl-existence-uniqueness": {"relation": "proof_template", "tasks": ["geiges03-10", "ss21-7", "ss21-nach-7"]},
    "template-manifold-tangent-space": {"relation": "proof_template", "tasks": ["ss21-5", "ss21-nach-6", "ss25-5"]},
    "template-multidimensional-integral": {"relation": "computational_template", "tasks": ["sweers10-8", "sweers14-2-8", "ss25-7"]},
    "template-continuity-vs-differentiability": {"relation": "proof_template", "tasks": ["sweers10-3", "sweers14-1-4", "sweers14-2-5"]},
    "template-topology-definition-classification": {"relation": "theorem_variant", "tasks": ["geiges03-1", "sweers14-2-3", "ss21-2", "ss25-1"]},
    "template-completeness-proof": {"relation": "proof_template", "tasks": ["marinescu08-2", "ss21-nach-2"]},
    "template-improper-integral": {"relation": "computational_template", "tasks": ["sweers10-mix-2", "thorbergsson13-2"]},
}

THEORY = {
    "folgen": ["2.1.1"], "reihen": ["3.4.4"], "gleichmaessige-konvergenz": ["6.1"],
    "integralrechnung": ["6.4.2"], "metrische-raeume": ["7.2.1"], "vollstaendigkeit": ["7.2.9"],
    "topologie": ["7.3.1"], "stetigkeit": ["7.4.1"], "kompaktheit": ["7.5.1"],
    "zusammenhang": ["7.6.2"], "differenzierbarkeit": ["8.1.1"], "richtungsableitungen": ["8.2"],
    "taylor": ["8.5.3"], "extrema": ["8.6.3"], "banach-fixpunkt": ["9.1.2"],
    "umkehrsatz": ["9.2.5"], "implizite-funktionen": ["9.3.1"], "lagrange": ["9.4.1"],
}

TOPIC_LABELS = {
    "folgen": "Folgen", "reihen": "Reihen und Potenzreihen", "gleichmaessige-konvergenz": "Gleichmäßige Konvergenz",
    "integralrechnung": "Integralrechnung", "metrische-raeume": "Metrische Räume", "vollstaendigkeit": "Vollständigkeit",
    "topologie": "Topologie", "stetigkeit": "Stetigkeit", "kompaktheit": "Kompaktheit", "zusammenhang": "Zusammenhang",
    "differenzierbarkeit": "Mehrdimensionale Differenzierbarkeit", "richtungsableitungen": "Richtungsableitungen",
    "taylor": "Taylorentwicklung", "extrema": "Extrema", "banach-fixpunkt": "Banachscher Fixpunktsatz",
    "umkehrsatz": "Umkehrsatz", "implizite-funktionen": "Implizite Funktionen", "lagrange": "Lagrange-Multiplikatoren",
    "komplexe-zahlen": "Komplexe Zahlen", "uneigentliche-integrale": "Uneigentliche Integrale", "kurven": "Kurven und Bogenlänge",
    "differentialgleichungen": "Differentialgleichungen", "dynamische-systeme": "Dynamische Systeme",
    "mehrdimensionale-integrale": "Mehrdimensionale Integrale", "mannigfaltigkeiten": "Untermannigfaltigkeiten",
    "analysis-1": "Analysis-I-Wiederholung", "unsicher": "Unvollständig überlieferte Aufgabe",
}

HINTS = {
    "metrische-raeume": ("Schreibe zuerst die drei Metrikaxiome aus.", "Prüfe positive Definitheit, Symmetrie und Dreiecksungleichung getrennt."),
    "topologie": ("Arbeite direkt mit offenen Umgebungen oder Kugeln.", "Für Gegenbeispiele sind indiskrete Topologien und Folgen oft besonders effizient."),
    "kompaktheit": ("Entscheide zuerst, welche Kompaktheitscharakterisierung hier am kürzesten ist.", "In endlichdimensionalen Räumen helfen Abgeschlossenheit und Beschränktheit; sonst nicht ungeprüft verwenden."),
    "vollstaendigkeit": ("Beginne mit einer beliebigen Cauchy-Folge.", "Konstruiere den punktweisen Grenzwert und zeige anschließend Konvergenz in der gegebenen Norm."),
    "differenzierbarkeit": ("Unterscheide partielle, Richtungs- und totale Differenzierbarkeit.", "Für totale Differenzierbarkeit muss der Restterm nach Division durch die Norm gegen null gehen."),
    "richtungsableitungen": (r"Setze die Gerade $h\mapsto hv$ in die Funktion ein.", "Existenz aller Richtungsableitungen allein beweist noch keine Differenzierbarkeit."),
    "extrema": ("Bestimme zuerst alle inneren kritischen Punkte und vergiss den Rand nicht.", "Klassifiziere mit Hesse-Matrix, geeigneten Kurven oder Lagrange-Bedingungen."),
    "lagrange": ("Formuliere Nebenbedingung und Regularitätsannahme explizit.", r"Löse $\nabla f=\lambda\nabla g$ und vergleiche anschließend alle Kandidaten."),
    "umkehrsatz": ("Berechne die Jacobi-Matrix und ihre Determinante.", "Der Satz liefert lokale, nicht automatisch globale Invertierbarkeit."),
    "implizite-funktionen": ("Trenne freie und aufzulösende Variablen.", "Prüfe die relevante partielle Jacobi-Matrix und differenziere danach die Identität."),
    "banach-fixpunkt": ("Nenne Vollständigkeit und Kontraktionskonstante.", "Zeige Cauchy-Eigenschaft der Iteration, dann Existenz und Eindeutigkeit."),
    "integralrechnung": ("Bestimme zuerst Gebiet und Integrationsreihenfolge.", "Prüfe Existenz und führe Substitution oder Koordinatenwechsel mit Jacobi-Faktor aus."),
    "gleichmaessige-konvergenz": ("Der Index $N$ darf nicht vom Punkt abhängen.", "Suche für Nicht-Gleichmäßigkeit Punkte, die mit $n$ variieren."),
    "differentialgleichungen": ("Bestimme zuerst den DGL-Typ und das maximale Existenzintervall.", "Trennung, Variation der Konstanten oder charakteristische Gleichung liefern den Rechenweg."),
    "kurven": ("Leite die Parametrisierung ab.", r"Die Bogenlänge ist das Integral der Geschwindigkeit $\|\gamma'(t)\|$."),
    "mannigfaltigkeiten": ("Schreibe die Menge als reguläre Niveaumenge oder als Graph.", "Prüfe den Rang der Ableitung; Singularitäten müssen separat behandelt werden."),
}


# exam|number|page|points|topic(s)|technique(s)|relevance|confidence|title
TASK_ROWS = r"""
ss18|1|2|12|differenzierbarkeit,kompaktheit,topologie,vollstaendigkeit|definition|hoch|hoch|Sechs Grunddefinitionen präzise formulieren
ss18|2|3|4|extrema,kompaktheit|satzwiedergabe|hoch|hoch|Extremwertkriterium und Bolzano-Weierstraß angeben
ss18|3|4|10|zusammenhang,integralrechnung|beweis|hoch|hoch|Stetige Bilder zusammenhängender Räume und Hauptsatz beweisen
ss18|4|5|14|kurven,differenzierbarkeit,stetigkeit|berechnung,beweis,gegenbeispiel|mittel|hoch|Zykloidenlänge, partielle Differenzierbarkeit und stetiges Funktional
ss18|5|6|10|umkehrsatz|beweis,satzanwendung|hoch|hoch|Lokale Matrixquadratwurzel mit dem Umkehrsatz beweisen
geiges03|1|1|10|topologie,kompaktheit|definition,klassifikation|hoch|mittel|Offen, abgeschlossen, kompakt und folgenkompakt; Mengen klassifizieren
geiges03|2|1|9|kurven|berechnung|niedrig|mittel|Neilsche Parabel parametrisieren und nach Bogenlänge umparametrisieren
geiges03|3|1|8|extrema|berechnung|hoch|mittel|Stationäre Punkte einer Polynomfunktion bestimmen und klassifizieren
geiges03|4|1|7|metrische-raeume,topologie|beweis|hoch|mittel|Sternmetrik beweisen und ihre offenen Mengen bestimmen
geiges03|5|2|12|extrema|berechnung,beweis|hoch|mittel|Parameterabhängige Extrema einer Exponential-Quadratik untersuchen
geiges03|6|2|9|richtungsableitungen,differenzierbarkeit|definition|hoch|mittel|Richtungsableitung und totale Differenzierbarkeit definieren
geiges03|7|2|10|richtungsableitungen,differenzierbarkeit|berechnung,gegenbeispiel|hoch|mittel|Alle Richtungsableitungen vorhanden, aber keine totale Differenzierbarkeit
geiges03|8|2|9|implizite-funktionen|satzanwendung,berechnung|hoch|mittel|Implizite Funktionen nachweisen und erste sowie zweite Ableitungen berechnen
geiges03|9|2|8|lagrange|beweis,berechnung|hoch|mittel|Flächenmaximales Dreieck bei festem Umfang bestimmen
geiges03|10|2|18|differentialgleichungen|beweis,berechnung|ausserhalb|mittel|Existenz, Variation der Konstanten und lineare DGL zweiter Ordnung
geiges15|1|1||kurven|modellierung,berechnung|niedrig|hoch|Zykloide modellieren und Bogenlänge berechnen
geiges15|2|1||differenzierbarkeit|definition,beweis|hoch|hoch|Differenzierbarkeit definieren und Differential einer quadratischen Form bestimmen
geiges15|3|1||banach-fixpunkt|satzwiedergabe,beweis|hoch|hoch|Banachschen Fixpunktsatz formulieren und beweisen
geiges15|4|1||extrema,lagrange|berechnung,skizze|hoch|hoch|Extrema von $xy$ auf der Einheitskreisscheibe
geiges15|5|1||implizite-funktionen|satzanwendung,berechnung|hoch|hoch|Drei Variablen lokal als Funktionen zweier Parameter auflösen
geiges15|6|2||differentialgleichungen,analysis-1|berechnung,beweis|ausserhalb|hoch|Lineare DGL zweiter Ordnung und trigonometrische Identität
marinescu08|1|1|8|integralrechnung|berechnung|mittel|niedrig|Zwei Integrale berechnen; Formeln nur im Original zuverlässig lesbar
marinescu08|2|1|8|metrische-raeume,vollstaendigkeit,kompaktheit|definition,beweis|hoch|mittel|Cauchy-Folge, Vollständigkeit und kompakt impliziert vollständig
marinescu08|3|1|10|gleichmaessige-konvergenz,reihen|satzwiedergabe,berechnung|hoch|mittel|Grenzwert und Differentiation vertauschen; Reihen berechnen
marinescu08|4|2|4|differenzierbarkeit|definition|hoch|mittel|Differenzierbarkeit in $\mathbb R^n$ definieren
marinescu08|5|2|10|differenzierbarkeit|berechnung,beweis|hoch|niedrig|Partielle Ableitungen und Differential am Ursprung; Formel im PDF prüfen
sweers10-mix|1|1||komplexe-zahlen|berechnung|niedrig|hoch|Komplexe Nullstellen eines Polynoms bestimmen
sweers10-mix|2|1||uneigentliche-integrale|berechnung|mittel|hoch|Uneigentliches Integral auf Konvergenz prüfen und berechnen
sweers10-mix|3|1||folgen|beweis|mittel|hoch|Abzählbarkeit einer durch rationale Quadrate definierten Menge
sweers10-mix|4|1||reihen|berechnung,gegenbeispiel|hoch|hoch|Konvergenzgebiet von Potenzreihen untersuchen
sweers10-mix|5|1||analysis-1|berechnung,skizze|niedrig|hoch|Definitionsgebiete und Graphen von Sinus-Arcussinus-Kompositionen
sweers10-mix|6|1||dynamische-systeme|berechnung,klassifikation|ausserhalb|hoch|Lineare ebene Systeme über Eigenwerte klassifizieren
sweers10-mix|7|2||lagrange|satzanwendung,beweis|hoch|hoch|Behauptetes Nebenbedingungsmaximum mit Lagrange prüfen
sweers10-mix|8|2||taylor|berechnung|hoch|hoch|Taylorpolynom zweiter Ordnung von $\sin(xy)$
sweers10-mix|9|2||differenzierbarkeit|berechnung,beweis|hoch|hoch|Produkt mit nur stetigem Faktor am Ursprung untersuchen
sweers10-mix|10|2||extrema,kompaktheit|beweis,berechnung|hoch|hoch|Globale Extrema auf $\mathbb R^2$ durch Verhalten im Unendlichen
sweers10|1|1||differentialgleichungen|berechnung|ausserhalb|hoch|Anfangswertproblem $y'=t/y$ lösen
sweers10|2|1||implizite-funktionen|berechnung|hoch|hoch|Tangente an eine implizit definierte Kurve bestimmen
sweers10|3|1||differenzierbarkeit,stetigkeit|beweis,gegenbeispiel|hoch|hoch|Stetigkeit und Differenzierbarkeit einer stückweisen Funktion
sweers10|4|1||kurven|definition,berechnung|niedrig|hoch|Bogenlänge einer Raumkurve aufstellen
sweers10|5|2||dynamische-systeme|berechnung,klassifikation|ausserhalb|hoch|Lineare ebene Systeme klassifizieren
sweers10|6|2||lagrange|satzanwendung,beweis|hoch|hoch|Lagrange-Bedingung für ein behauptetes Maximum prüfen
sweers10|7|2||taylor|berechnung|hoch|hoch|Taylorpolynom zweiter Ordnung von $\sin(xy)$
sweers10|8|3||mehrdimensionale-integrale|berechnung|ausserhalb|hoch|Doppelintegral über ein durch Ungleichungen gegebenes Gebiet
sweers10|9|3||differenzierbarkeit|berechnung,beweis|hoch|hoch|Produktfunktion bei schwachen Voraussetzungen untersuchen
sweers10|10|3||extrema,kompaktheit|beweis,berechnung|hoch|hoch|Existenz und Berechnung globaler Extrema auf $\mathbb R^2$
sweers14-1|1|1||kurven|berechnung|niedrig|hoch|Länge einer Raumkurve berechnen
sweers14-1|2|1||extrema|berechnung|hoch|hoch|Parameterwerte für ein Minimum einer quadratischen Form
sweers14-1|3|1||differentialgleichungen|berechnung|ausserhalb|hoch|Alle Lösungen einer separierbaren DGL bestimmen
sweers14-1|4|1||differenzierbarkeit,stetigkeit|beweis,gegenbeispiel|hoch|hoch|Differenzierbarkeit und Stetigkeit logisch vergleichen
sweers14-1|5|2||richtungsableitungen,differenzierbarkeit|berechnung,gegenbeispiel|hoch|hoch|Partielle und Richtungsableitungen versus Differenzierbarkeit
sweers14-1|6|2||lagrange|berechnung|hoch|hoch|Extrema auf einer implizit gegebenen Fläche
sweers14-1|7|2||umkehrsatz|satzanwendung,berechnung|hoch|hoch|Ausnahmemenge lokaler Invertierbarkeit bestimmen
sweers14-1|8|2||zusammenhang|definition,klassifikation|hoch|hoch|Zusammenhang definieren und eine Hyperbel klassifizieren
sweers14-2|1|1||kurven|berechnung|niedrig|hoch|Länge einer sphärischen Raumkurve
sweers14-2|2|2||extrema|berechnung|hoch|hoch|Stationären Punkt einer Funktion klassifizieren
sweers14-2|3|3||topologie|definition,beweis,gegenbeispiel|hoch|hoch|Offenheit, Abgeschlossenheit und Koordinatenprojektionen
sweers14-2|4|4||differentialgleichungen,umkehrsatz|berechnung|ausserhalb|hoch|Nichtlineare DGL mit einer bijektiven Hilfsfunktion lösen
sweers14-2|5|5||stetigkeit,differenzierbarkeit|beweis,gegenbeispiel|hoch|hoch|Stetigkeit und Differenzierbarkeit von $|xy|$
sweers14-2|6|6||lagrange|berechnung|hoch|hoch|Kürzesten Abstand unter der Nebenbedingung $x^2y=2$ bestimmen
sweers14-2|7|7||umkehrsatz|satzanwendung,berechnung|hoch|hoch|Kurven fehlender lokaler Invertierbarkeit bestimmen
sweers14-2|8|8||mehrdimensionale-integrale|berechnung|ausserhalb|hoch|Doppelintegral über ein Dreiecksgebiet
thorbergsson13|1|1||stetigkeit|beweis|hoch|niedrig|Stetigkeit einer Koordinatenprojektion beweisen
thorbergsson13|2|1||uneigentliche-integrale|berechnung|mittel|niedrig|Zwei uneigentliche Integrale untersuchen
thorbergsson13|3|1||metrische-raeume,zusammenhang|beweis,berechnung|hoch|niedrig|Metrik, Durchmesser und zusammenhängende Teilmengen von $\mathbb N$
thorbergsson13|4|1||richtungsableitungen,differenzierbarkeit|berechnung,gegenbeispiel|hoch|niedrig|Richtungsableitungen einer rationalen Funktion am Ursprung
thorbergsson13|5|1||differenzierbarkeit|beweis|hoch|niedrig|Differential einer radialen Funktion in Tangentialrichtung
thorbergsson13|6|1||extrema|berechnung|hoch|niedrig|Kritische Punkte und globale Werte auf dem Quadrat
thorbergsson13|7|1||gleichmaessige-konvergenz,unsicher|unvollstaendig|niedrig|niedrig|Unvollständig überlieferte Aufgabe zur punktweisen Konvergenz
thorbergsson13|8|1||integralrechnung,stetigkeit|beweis|hoch|niedrig|Eine durch ein Integral definierte Funktion ist Lipschitz-stetig
ss20|1|1|7|gleichmaessige-konvergenz|beweis,gegenbeispiel|hoch|hoch|Lokale gleichmäßige Konvergenz einer Funktionenfolge
ss20|2|1|12|kompaktheit,topologie|definition,beweis|hoch|hoch|Kompakte Zylinder und eine uniforme offene Umgebung
ss20|3|1|12|differentialgleichungen|berechnung|ausserhalb|hoch|Anfangswertproblem lösen und verifizieren
ss20|4|1|12|extrema,lagrange|berechnung|hoch|hoch|Lokale und globale Extrema auf einer Ellipse
ss20|5|2|10|implizite-funktionen|satzanwendung,berechnung|hoch|hoch|Implizit definierte Funktionen und ihre Ableitungen
ss21|1|2|20|metrische-raeume|definition,beweis,gegenbeispiel|hoch|hoch|Metrik und Norm: Axiome, Beispiele und induzierte Metrik
ss21|2|5|20|topologie,kompaktheit|definition,beweis,klassifikation|hoch|hoch|Inneres, offene Kugeln, Rand und Kompaktheit konkreter Mengen
ss21|3|8|25|extrema|berechnung|hoch|hoch|Kritische Punkte einer Polynomfunktion vollständig klassifizieren
ss21|4|11|20|richtungsableitungen,differenzierbarkeit|definition,berechnung,gegenbeispiel|hoch|hoch|Richtungsableitungen versus totale Differenzierbarkeit
ss21|5|14|20|mannigfaltigkeiten,differenzierbarkeit|beweis,berechnung|teilweise|hoch|Graph als Untermannigfaltigkeit und Tangentialebene
ss21|6|17|20|implizite-funktionen|beweis,berechnung|hoch|hoch|Ableitungsformel für implizite Funktionen und Anwendung
ss21|7|20|25|differentialgleichungen|beweis,berechnung|ausserhalb|hoch|Lokale Lipschitz-Stetigkeit, Existenz und Variation der Konstanten
ss21-nach|1|2|20|gleichmaessige-konvergenz,stetigkeit|definition,beweis|hoch|hoch|Gleichmäßiger Grenzwert stetiger Funktionen ist stetig
ss21-nach|2|5|20|vollstaendigkeit,metrische-raeume|definition,beweis|hoch|hoch|Cauchy, Vollständigkeit, Banachraum und $C([a,b])$
ss21-nach|3|8|25|extrema,kompaktheit,lagrange|berechnung,skizze,beweis|hoch|hoch|Globale Extrema einer Funktion auf einer Ellipse
ss21-nach|4|11|20|differenzierbarkeit|satzwiedergabe,berechnung|hoch|hoch|Mehrdimensionale Kettenregel anwenden
ss21-nach|5|14|20|umkehrsatz|beweis,berechnung|hoch|hoch|Lokale und globale Invertierbarkeit einer Exponential-Polarabbildung
ss21-nach|6|17|20|mannigfaltigkeiten,implizite-funktionen|beweis,berechnung|teilweise|hoch|Kegel auf Mannigfaltigkeit prüfen und Tangentialebene bestimmen
ss21-nach|7|20|25|differentialgleichungen|beweis,berechnung|ausserhalb|hoch|Existenz, Eindeutigkeit und Lösungen zweier Anfangswertprobleme
ss25|1|2|20|topologie,metrische-raeume|definition,beweis,gegenbeispiel|hoch|hoch|Folgen in topologischen Räumen, Hausdorff-Eindeutigkeit und metrische Topologien
ss25|2|3|15|richtungsableitungen,differenzierbarkeit|berechnung,gegenbeispiel|hoch|hoch|Alle Richtungsableitungen existieren, aber keine totale Differenzierbarkeit
ss25|3|4|15|differenzierbarkeit|beweis,satzanwendung|hoch|hoch|Verschwindender Gradient auf einem Ball impliziert Konstanz
ss25|4|5|15|extrema|berechnung|hoch|hoch|Kritische Punkte einer Polynomfunktion klassifizieren
ss25|5|6|15|mannigfaltigkeiten,extrema|beweis,berechnung|teilweise|hoch|Graph als Untermannigfaltigkeit und globaler Minimalabstand
ss25|6|8|20|differentialgleichungen|berechnung|ausserhalb|hoch|Zwei Anfangswertprobleme samt maximalem Definitionsbereich lösen
ss25|7|10|20|mehrdimensionale-integrale|beweis,berechnung|ausserhalb|hoch|Existenz und Berechnung zweier Doppelintegrale
"""


def family_index() -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    for family_id, family in FAMILY_GROUPS.items():
        for task_id in family["tasks"]:
            if task_id in result:
                raise ValueError(f"Aufgabe {task_id} ist mehreren Familien zugeordnet.")
            result[task_id] = (family_id, family["relation"])
    return result


def scope_status(topics: list[str], relevance: str) -> str:
    explicit = [TOPIC_SCOPE[topic] for topic in topics if topic in TOPIC_SCOPE]
    if "unresolved" in explicit:
        return "unresolved"
    if "likely_outdated" in explicit:
        return "likely_outdated"
    return {
        "hoch": "confirmed_current",
        "mittel": "likely_current",
        "teilweise": "unresolved",
        "niedrig": "historically_examined",
        "ausserhalb": "likely_outdated",
    }[relevance]


def proof_or_computation(techniques: list[str]) -> str:
    proof_markers = {"beweis", "satzwiedergabe", "definition", "gegenbeispiel"}
    computation_markers = {"berechnung", "klassifikation", "modellierung", "skizze"}
    has_proof = bool(proof_markers.intersection(techniques))
    has_computation = bool(computation_markers.intersection(techniques))
    if has_proof and has_computation:
        return "mixed"
    if has_proof:
        return "proof"
    if has_computation:
        return "computation"
    return "unresolved"


def parse_rows() -> list[dict]:
    tasks: list[dict] = []
    exam_map = {exam["id"]: exam for exam in EXAMS}
    solution_index = {key: value for key, value in SOLUTION_FILES.items()}
    families = family_index()
    for raw in TASK_ROWS.strip().splitlines():
        exam_id, number, page, points, topics, techniques, relevance, confidence, title = raw.split("|", 8)
        exam = exam_map[exam_id]
        task_number = int(number)
        topic_list = topics.split(",")
        technique_list = techniques.split(",")
        primary_topic = topic_list[0]
        hint_pair = HINTS.get(primary_topic, ("Formuliere zuerst Voraussetzungen und Ziel der Aufgabe.", "Zerlege die Aufgabe in einen Satz- oder Definitionsschritt und einen Rechenschritt."))
        theory_ids = list(dict.fromkeys(theory_id for topic in topic_list for theory_id in THEORY.get(topic, [])))
        point_value = int(points) if points else None
        if point_value and exam.get("durationMinutes") and exam.get("totalPoints"):
            estimated = round(point_value * exam["durationMinutes"] / exam["totalPoints"])
        elif point_value:
            estimated = max(8, round(point_value * 1.25))
        else:
            estimated = 18
        solution = solution_index.get(exam_id)
        solution_data = None
        solution_status = "no_solution"
        grading_status = "estimated_scoring"
        if solution:
            start, end = solution["pages"][task_number - 1]
            solution_status = solution["status"]
            grading_status = solution["gradingStatus"]
            solution_data = {
                "status": solution_status,
                "kind": SOLUTION_LABELS[solution_status],
                "asset": f"exam-pdfs/{solution['asset']}",
                "pageStart": start,
                "pageEnd": end,
                "summary": "Ein offizieller Bewertungsschlüssel ist im verlinkten Dokument enthalten."
                if solution_status == "official_rubric"
                else "Eine offizielle ausgearbeitete Lösung ist im verlinkten Dokument enthalten; ein detaillierter Bewertungsschlüssel liegt nicht vor.",
            }
        task_id = f"{exam_id}-{task_number}"
        family_id, family_relation = families.get(task_id, (f"unique-{task_id}", "unique"))
        task_scope = scope_status(topic_list, relevance)
        task_notes = ["Eintrag bündelt die Hauptaufgabe einschließlich ihrer Teilaufgaben."]
        if confidence == "niedrig":
            task_notes.append("Aufgabentext oder Formel muss direkt im PDF geprüft werden.")
        if task_scope == "unresolved":
            task_notes.append("Aktueller Prüfungsumfang ist wegen eines Konflikts zwischen Skript und Klausurevidenz ungeklärt.")
        tasks.append({
            "id": task_id, "examId": exam_id, "number": task_number, "subtask": "alle",
            "title": title, "prompt": f"{title}. Bearbeite die vollständige Aufgabenstellung im verlinkten Original-PDF.",
            "pageStart": int(page), "pageEnd": int(page), "points": point_value,
            "estimatedMinutes": estimated, "topics": topic_list, "topicLabels": [TOPIC_LABELS[t] for t in topic_list],
            "topicPrimary": primary_topic, "topicSecondary": topic_list[1:],
            "techniques": technique_list, "theoryIds": theory_ids, "currentRelevance": relevance,
            "currentScopeStatus": task_scope, "scriptCoverage": "missing" if primary_topic in SCRIPT_GAP_TOPICS else "covered",
            "proofOrComputation": proof_or_computation(technique_list),
            "officialSolutionStatus": solution_status, "gradingStatus": grading_status,
            "duplicateFamily": family_id, "familyRelation": family_relation,
            "difficulty": "hoch" if (point_value or 0) >= 18 or "beweis" in technique_list else "mittel",
            "sourceConfidence": confidence, "hints": list(hint_pair), "solution": solution_data,
            "source": {"asset": f"exam-pdfs/{exam['asset']}", "file": exam["file"], "page": task_number if exam_id == "ss25" else int(page), "originalPage": int(page)},
            "notes": " ".join(task_notes),
        })
    return tasks


def file_audit(path: Path, role: str, copied_asset: str | None = None) -> dict:
    reader = PdfReader(str(path))
    chars = sum(len(page.extract_text() or "") for page in reader.pages)
    return {
        "file": path.name, "role": role, "pages": len(reader.pages), "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "textCharacters": chars,
        "hasUsableTextLayer": chars >= max(200, len(reader.pages) * 80), "asset": copied_asset,
    }


def build_ss25_question_pdf(source: Path, target: Path) -> int:
    source_reader = PdfReader(str(source))
    writer = PdfWriter()
    task_pages = [2, 3, 4, 5, 6, 8, 10]
    with pdfplumber.open(str(source)) as pdf:
        for source_page_number in task_pages:
            layout_page = pdf.pages[source_page_number - 1]
            solution_words = [
                word for word in layout_page.extract_words()
                if word["text"].lower().endswith("sung:")
            ]
            if not solution_words:
                raise ValueError(f"Lösungsmarker fehlt auf SS25-Seite {source_page_number}.")
            solution_top = min(word["top"] for word in solution_words)
            page = source_reader.pages[source_page_number - 1]
            height = float(page.mediabox.height)
            page.cropbox.lower_left = (0, height - max(40, solution_top - 8))
            page.cropbox.upper_right = (float(page.mediabox.width), height)
            writer.add_page(page)
    with target.open("wb") as handle:
        writer.write(handle)
    return len(task_pages)


def exam_year(exam: dict) -> int:
    return int(exam["semester"].split()[-1])


def topic_scope_status(topic: str) -> str:
    return TOPIC_SCOPE.get(topic, "confirmed_current")


def topic_script_coverage(topic: str) -> str:
    if topic in SCRIPT_GAP_TOPICS:
        return "missing"
    if topic == "unsicher":
        return "unresolved"
    if topic == "analysis-1":
        return "covered_supporting"
    return "covered"


def build_topic_weighting(exams: list[dict], tasks: list[dict]) -> list[dict]:
    exam_map = {exam["id"]: exam for exam in exams}
    recent_exam_ids = [
        exam["id"] for exam in sorted(exams, key=lambda item: (exam_year(item), item.get("date") or ""), reverse=True)[:3]
    ]
    rows = []
    for topic in TOPIC_LABELS:
        related = [task for task in tasks if topic in task["topics"]]
        if not related:
            continue
        exam_ids = sorted({task["examId"] for task in related}, key=lambda item: exam_year(exam_map[item]), reverse=True)
        family_ids = {task["duplicateFamily"] for task in related}
        known_points = [task for task in related if task["points"] is not None]
        allocated_points = sum(task["points"] / len(task["topics"]) for task in known_points)
        point_exposure = sum(task["points"] for task in known_points)
        latest_year = max(exam_year(exam_map[task["examId"]]) for task in related)
        latest_exam = max(related, key=lambda task: (exam_year(exam_map[task["examId"]]), exam_map[task["examId"]].get("date") or ""))["examId"]
        official_count = sum(task["officialSolutionStatus"] != "no_solution" for task in related)
        rubric_count = sum(task["officialSolutionStatus"] == "official_rubric" for task in related)
        confidence_values = {"hoch": 1.0, "mittel": 0.7, "niedrig": 0.4}
        rows.append({
            "topic": topic,
            "label": TOPIC_LABELS[topic],
            "examCount": len(exam_ids),
            "examIds": exam_ids,
            "rawTaskCount": len(related),
            "uniqueTaskFamilyCount": len(family_ids),
            "totalAllocatedPoints": round(allocated_points, 2),
            "knownPointTaskExposure": point_exposure,
            "knownPointTaskCount": len(known_points),
            "averagePointsPerKnownAppearance": round(point_exposure / len(known_points), 2) if known_points else None,
            "mostRecentAppearance": exam_map[latest_exam]["semester"],
            "mostRecentYear": latest_year,
            "recentExamIds": [exam_id for exam_id in recent_exam_ids if exam_id in exam_ids],
            "recentThreeCount": sum(exam_id in exam_ids for exam_id in recent_exam_ids),
            "officialSolutionCount": official_count,
            "officialRubricCount": rubric_count,
            "scriptCoverage": topic_script_coverage(topic),
            "currentExerciseCoverage": "not_provided",
            "currentScopeStatus": topic_scope_status(topic),
            "sourceConfidence": round(sum(confidence_values[task["sourceConfidence"]] for task in related) / len(related), 3),
        })

    max_families = max(row["uniqueTaskFamilyCount"] for row in rows)
    max_points = max(row["totalAllocatedPoints"] for row in rows)
    current_factor = {
        "confirmed_current": 1.0,
        "likely_current": 0.75,
        "historically_examined": 0.3,
        "likely_outdated": 0.1,
        "unresolved": 0.35,
    }
    for row in rows:
        components = {
            "currentCourse": 25 * current_factor[row["currentScopeStatus"]],
            "recency": 15 * max(0, min(1, (row["mostRecentYear"] - 2003) / 22)),
            "examFrequency": 15 * min(1, row["examCount"] / 6),
            "uniqueFamilies": 15 * row["uniqueTaskFamilyCount"] / max_families,
            "pointWeight": 10 * row["totalAllocatedPoints"] / max_points if max_points else 0,
            "recentThree": 10 * row["recentThreeCount"] / 3,
            "officialSolutions": 5 * row["officialSolutionCount"] / row["rawTaskCount"],
            "sourceConfidence": 5 * row["sourceConfidence"],
            "exerciseEvidence": None,
        }
        row["scoreComponents"] = {key: round(value, 2) if value is not None else None for key, value in components.items()}
        row["weightScore"] = round(sum(value for value in components.values() if value is not None), 2)
        if row["currentScopeStatus"] == "unresolved":
            row["priorityGroup"] = "Ungeklärt"
        elif row["currentScopeStatus"] in {"likely_outdated", "historically_examined"}:
            row["priorityGroup"] = "C"
        elif row["currentScopeStatus"] == "confirmed_current" and (
            row["weightScore"] >= 60 or (row["recentThreeCount"] >= 1 and row["weightScore"] >= 55)
        ):
            row["priorityGroup"] = "A"
        else:
            row["priorityGroup"] = "B"
    return sorted(rows, key=lambda row: (-row["weightScore"], row["label"]))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_exam_inventory(exams: list[dict], source_audit: list[dict]) -> None:
    audit_by_asset = {entry.get("asset"): entry for entry in source_audit if entry.get("asset")}
    rows = []
    for exam in exams:
        source = audit_by_asset.get(exam["asset"], {})
        statuses = {task_status for task_status in exam["solutionStatuses"]}
        rows.append({
            "exam_id": exam["id"], "semester": exam["semester"], "year": exam_year(exam),
            "professor_or_course_version": exam["lecturer"],
            "duration_minutes": exam["durationMinutes"] if exam["durationMinutes"] is not None else "unknown",
            "total_points": exam["totalPoints"] if exam["totalPoints"] is not None else "unknown",
            "number_of_tasks": exam["taskCount"], "complete_status": exam["completeStatus"],
            "official_solutions": "yes" if statuses - {"no_solution"} else "no",
            "grading_rubrics": "yes" if "official_rubric" in statuses else "no",
            "duplicate_status": exam["duplicateStatus"], "current_syllabus_status": exam["currentScopeStatus"],
            "metadata_confidence": exam["sourceConfidence"], "source_file": exam["file"],
            "source_pages": source.get("pages", "unknown"), "notes": exam["notes"],
        })
    fields = [
        "exam_id", "semester", "year", "professor_or_course_version", "duration_minutes", "total_points",
        "number_of_tasks", "complete_status", "official_solutions", "grading_rubrics", "duplicate_status",
        "current_syllabus_status", "metadata_confidence", "source_file", "source_pages", "notes",
    ]
    write_csv(CORPUS_DIR / "exam-inventory.csv", fields, rows)


def write_task_inventory(tasks: list[dict]) -> None:
    rows = [{
        "task_id": task["id"], "exam_id": task["examId"], "task_number": task["number"],
        "subtask": task["subtask"], "topic_primary": task["topicPrimary"],
        "topic_secondary": "|".join(task["topicSecondary"]), "points": task["points"] if task["points"] is not None else "unknown",
        "estimated_time": task["estimatedMinutes"], "difficulty": task["difficulty"],
        "proof_or_computation": task["proofOrComputation"], "official_solution_status": task["officialSolutionStatus"],
        "grading_status": task["gradingStatus"], "source_page": task["source"]["originalPage"],
        "current_scope_status": task["currentScopeStatus"], "duplicate_family": task["duplicateFamily"],
        "family_relation": task["familyRelation"], "confidence": task["sourceConfidence"], "notes": task["notes"],
    } for task in tasks]
    fields = [
        "task_id", "exam_id", "task_number", "subtask", "topic_primary", "topic_secondary", "points",
        "estimated_time", "difficulty", "proof_or_computation", "official_solution_status", "grading_status",
        "source_page", "current_scope_status", "duplicate_family", "family_relation", "confidence", "notes",
    ]
    write_csv(CORPUS_DIR / "task-inventory.csv", fields, rows)


def write_topic_weighting(rows: list[dict]) -> None:
    csv_rows = [{
        "topic": row["topic"], "label": row["label"], "exam_count": row["examCount"],
        "raw_task_count": row["rawTaskCount"], "unique_task_family_count": row["uniqueTaskFamilyCount"],
        "total_points_allocated": row["totalAllocatedPoints"], "known_point_task_exposure": row["knownPointTaskExposure"],
        "average_points_per_known_appearance": row["averagePointsPerKnownAppearance"] if row["averagePointsPerKnownAppearance"] is not None else "unknown",
        "most_recent_appearance": row["mostRecentAppearance"], "appearances_in_three_most_recent_exams": row["recentThreeCount"],
        "official_solution_count": row["officialSolutionCount"], "official_rubric_count": row["officialRubricCount"],
        "script_coverage": row["scriptCoverage"], "current_exercise_coverage": row["currentExerciseCoverage"],
        "current_scope_status": row["currentScopeStatus"], "source_confidence": row["sourceConfidence"],
        "weight_score": row["weightScore"], "priority_group": row["priorityGroup"],
    } for row in rows]
    write_csv(CORPUS_DIR / "topic-weighting.csv", list(csv_rows[0]), csv_rows)


def build_weighting_method() -> str:
    return """# Methode der Themengewichtung

## Evidenzbasis

Die Auswertung verwendet 13 eigenständige Klausuren und 96 gebündelte Hauptaufgaben. Teilaufgaben werden nicht künstlich als eigenständige Aufgaben gezählt. Gleiche Aufgaben und klare Varianten werden zusätzlich über `duplicate_family` zusammengeführt. Dadurch stehen Rohhäufigkeit und Familienhäufigkeit nebeneinander.

## Formel

Der vorläufige Wert liegt zwischen 0 und 100 und ist die Summe dieser Komponenten:

| Komponente | Maximum | Berechnung |
|---|---:|---|
| Aktueller Kurs | 25 | `confirmed_current=25`, `likely_current=18.75`, `unresolved=8.75`, `historically_examined=7.5`, `likely_outdated=2.5` |
| Aktualität | 15 | linear vom ältesten Korpusjahr 2003 bis 2025 |
| Klausurbreite | 15 | Anzahl verschiedener Klausuren, bei 6 Klausuren gedeckelt |
| Einzigartige Aufgabenfamilien | 15 | relativ zum höchsten Familienwert eines Themas |
| Punktgewicht | 10 | anteiliges bekanntes Punktgewicht relativ zum höchsten Themenwert |
| Drei jüngste Klausuren | 10 | Anteil von SS 2025, Nachklausur SS 2021 und Klausur SS 2021 |
| Offizielle Lösungen | 5 | Anteil der Aufgaben mit offizieller Lösung oder offiziellem Schema |
| Quellenvertrauen | 5 | Mittel aus `hoch=1`, `mittel=0.7`, `niedrig=0.4` |

Aktuelle Übungsblätter erhalten nach einem späteren Upload eine eigene Komponente mit maximal 30 Punkten. Dann wird die Summe auf die jeweils verfügbaren Maximalpunkte normiert. Damit wiegt aktuelle Übungsevidenz stärker als jede einzelne historische Komponente. Solange keine Übungsblätter vorliegen, ist der Wert `not_provided`; er wird weder als null Evidenz interpretiert noch in die aktuelle 100-Punkte-Summe eingerechnet.

Die Prioritätsgruppe wird nicht nur aus dem Zahlenwert abgeleitet. `unresolved` bleibt immer **Ungeklärt**, historischer oder wahrscheinlich veralteter Stoff bleibt **C**. **A** verlangt bestätigte Skriptdeckung und entweder mindestens 60 Punkte oder mindestens einen Treffer in den drei jüngsten Klausuren bei mindestens 55 Punkten. Übriger skriptgedeckter Stoff ist **B**.

## Punktzuordnung

Wenn eine Hauptaufgabe mehrere Themen bündelt und keine Teilpunkte pro Thema nennt, werden ihre Punkte gleichmäßig auf die getaggten Themen verteilt. `known_point_task_exposure` enthält zusätzlich die ungeteilte Summe aller bekannten Punkte von Aufgaben, in denen das Thema vorkommt. Beide Werte sind analytische Schätzungen, keine offiziellen Themenpunktzahlen.

## Grenzen

- Nur sechs Klausuren haben vollständige oder rekonstruierbare Gesamtpunktzahlen; unbekannte Punkte werden nicht erfunden.
- SS 2025 ist die jüngste Evidenz, aber kein Beweis für den Prüfungsstoff 2026.
- Das aktuelle Skript bestätigt enthaltene Theorie, ersetzt jedoch keine offizielle Stoffabgrenzung.
- Differentialgleichungen, Mannigfaltigkeiten und mehrdimensionale Integration kommen 2025 vor, fehlen aber im Skript. Sie bleiben deshalb `unresolved` und werden nicht automatisch zu Priorität A.
- Das Thorbergsson-Dokument ist ein unvollständiges Erinnerungsprotokoll mit niedriger Quellenkonfidenz.
- Offizielle Lösungen erhöhen die Verlässlichkeit der Vorbereitung, nicht automatisch die fachliche Relevanz eines Themas.
"""


def build_gap_analysis(topic_rows: list[dict], tasks: list[dict]) -> str:
    row_by_topic = {row["topic"]: row for row in topic_rows}
    details = {
        "differentialgleichungen": ("Nur eine beiläufige eindimensionale DGL in Beispiel 5.2.2; keine DGL-Theorie, Existenz- oder Lösungsmethoden.", "SS 2025 und SS 2021 zeigen starke jüngere Evidenz, aber der Skriptkonflikt verhindert eine Bestätigung."),
        "mannigfaltigkeiten": ("Kapitel 8-9 liefern Differenzierbarkeit und implizite Funktionen, aber keine Definition oder systematische Theorie von Untermannigfaltigkeiten/Tangentialräumen.", "In SS 2025 sowie beiden Klausuren 2021 vorhanden; aktuell relevant möglich, aber nicht aus dem Skript belegbar."),
        "kurven": ("Keine systematische Behandlung parametrisierter Kurven oder der Bogenlänge; nicht unter einem tragfähigen Alternativnamen gefunden.", "Letzte Evidenz SS 2018; ohne aktuelle Übungsblätter wahrscheinlich veraltet."),
        "mehrdimensionale-integrale": ("Kapitel 6 behandelt eindimensionale Integralrechnung; Doppelintegrale, Fubini und Koordinatenwechsel fehlen.", "SS 2025 enthält 20 Punkte dazu; der aktuelle Umfang bleibt wegen der Skriptlücke ungeklärt."),
        "dynamische-systeme": ("Keine Phasenporträts oder Klassifikation linearer ebener Systeme gefunden.", "Nur zwei nahezu identische Aufgaben aus 2010; wahrscheinlich veraltet."),
    }
    lines = [
        "# Analyse der Skriptlücken", "",
        "Diese fünf Themen werden nicht als aktueller Pflichtstoff behauptet. `unresolved` bedeutet: jüngere Klausurevidenz widerspricht der Skriptdeckung; eine Stoffliste oder aktuelle Übungsblätter sind zur Entscheidung nötig.", "",
    ]
    for topic in ["differentialgleichungen", "mannigfaltigkeiten", "kurven", "mehrdimensionale-integrale", "dynamische-systeme"]:
        row = row_by_topic[topic]
        related = [task for task in tasks if topic in task["topics"]]
        task_ids = ", ".join(f"`{task['id']}`" for task in related)
        script_note, relevance_note = details[topic]
        lines += [
            f"## {row['label']}", "",
            f"- **Klausuren/Aufgaben:** {task_ids}.",
            f"- **Punkte:** {row['totalAllocatedPoints']:g} anteilig zugeordnete bekannte Punkte; {row['knownPointTaskExposure']} Punkte Aufgabenkontakt. Aufgaben ohne Punktangabe sind darin nicht enthalten.",
            f"- **Neueste Evidenz:** {row['mostRecentAppearance']}.",
            f"- **Aktuelle Kursversion:** {'in SS 2025 geprüft, aber nicht für 2026 bestätigt' if 'ss25' in row['examIds'] else 'keine Evidenz aus SS 2025'}.",
            f"- **Skriptprüfung:** {script_note}",
            "- **Externes Material:** erforderlich, falls das Thema durch aktuelle Übungsblätter oder eine Stoffliste bestätigt wird.",
            f"- **Relevanzurteil:** `{row['currentScopeStatus']}`. {relevance_note}", "",
        ]
    return "\n".join(lines)


def build_final_priorities(topic_rows: list[dict]) -> str:
    headings = {
        "A": "Priorität A - sicher prüfungsrelevant",
        "B": "Priorität B - wahrscheinlich prüfungsrelevant",
        "C": "Priorität C - ergänzend",
        "Ungeklärt": "Ungeklärt",
    }
    recommendations = {
        "A": ("Definitionen und Sätze abrufbar; Beweise und Anwendungen unter Zeitdruck trainieren.", 5),
        "B": ("Kernideen sichern und mehrere typische Anwendungen rechnen.", 3),
        "C": ("Überblick behalten; nur repräsentative Aufgaben bearbeiten.", 1),
        "Ungeklärt": ("Zuerst Stoffumfang klären; bis dahin höchstens diagnostisch üben.", 2),
    }
    lines = [
        "# Finale Lernprioritäten", "",
        "Stand der Evidenz: bereitgestellte Klausuren bis SS 2025 und das hochgeladene Skript. Aktuelle Übungsblätter und eine Stoffliste fehlen; daher ist keine Priorität allein als Zusage für die nächste Klausur zu lesen.", "",
    ]
    for group in ("A", "B", "C", "Ungeklärt"):
        lines += [f"## {headings[group]}", ""]
        for row in [item for item in topic_rows if item["priorityGroup"] == group]:
            depth, practice = recommendations[group]
            recent = ", ".join(row["recentExamIds"]) or "keine der drei jüngsten"
            solution_text = f"{row['officialSolutionCount']} offizielle Lösung(en), davon {row['officialRubricCount']} mit Bewertungsschlüssel"
            lines += [
                f"### {row['label']} ({row['weightScore']:.1f}/100)", "",
                f"- **Evidenz:** {row['examCount']} Klausuren, {row['rawTaskCount']} Rohaufgaben, {row['uniqueTaskFamilyCount']} Aufgabenfamilien.",
                f"- **Jüngere Klausuren:** {recent}; neueste Evidenz {row['mostRecentAppearance']}.",
                f"- **Punktgewicht:** {row['totalAllocatedPoints']:g} anteilig zugeordnete bekannte Punkte; Punktdaten für {row['knownPointTaskCount']} Aufgaben.",
                f"- **Quellen:** {solution_text}; Quellenvertrauen {row['sourceConfidence']:.2f}.",
                f"- **Lerntiefe:** {depth}",
                f"- **Übungsumfang:** {min(practice, row['uniqueTaskFamilyCount'])} verschiedene Aufgabenfamilien, nicht bloß Varianten derselben Aufgabe.", "",
            ]
        if not any(item["priorityGroup"] == group for item in topic_rows):
            lines += ["Keine Themen in dieser Gruppe.", ""]
    return "\n".join(lines)


def build_blueprint(exams: list[dict], tasks: list[dict], source_audit: list[dict], topic_rows: list[dict]) -> str:
    family_count = len({task["duplicateFamily"] for task in tasks})
    official = sum(task["officialSolutionStatus"] != "no_solution" for task in tasks)
    rubrics = sum(task["officialSolutionStatus"] == "official_rubric" for task in tasks)
    lines = [
        "# Altlausur-Prüfungsprofil", "", "## Abgestimmter Korpus", "",
        f"- Eigenständige Klausuren: {len(exams)}.", f"- Gebündelte Hauptaufgaben: {len(tasks)}.",
        f"- Einzigartige Aufgabenfamilien: {family_count}.", f"- Aufgaben mit offizieller Lösung oder Schema: {official}; davon {rubrics} mit offiziellem Bewertungsschlüssel.",
        f"- Inventarisierte PDF-Dateien einschließlich Lösungen und Archiv: {len(source_audit)}.",
        "- Das 111-seitige `Ana2 Altklausur.pdf` ist ein Duplikatarchiv und keine vierzehnte Klausur.",
        "", "## Gewichtete Themen", "", "| Thema | Klausuren | Rohaufgaben | Familien | Score | Status |", "|---|---:|---:|---:|---:|---|",
    ]
    for row in topic_rows:
        lines.append(f"| {row['label']} | {row['examCount']} | {row['rawTaskCount']} | {row['uniqueTaskFamilyCount']} | {row['weightScore']:.1f} | {row['currentScopeStatus']} |")
    lines += [
        "", "## Verlässlichkeit", "",
        "- SS 2018 und Geiges 2003 wurden visuell geprüft; Geiges 2003 hat 100 aus sichtbaren Aufgaben summierte Punkte, aber kein Deckblatt.",
        "- SS 2021 besitzt offizielle ausgearbeitete Lösungen. Nur die Nachklausur SS 2021 enthält ausdrücklich einen detaillierten `Bewertungsschlüssel`.",
        "- SS 2025 besitzt offizielle Lösungen, aber kein detailliertes Bewertungsschema; die lokale Aufgabenfassung verhindert Lösungslecks.",
        "- Aktuelle Übungsblätter fehlen. Deshalb bleiben drei in SS 2025 vorkommende Skriptlücken ungeklärt.",
        "", "## Weiterführende Berichte", "",
        "- `exam-inventory.csv`: Metadaten und Vollständigkeit aller 13 Klausuren.",
        "- `task-inventory.csv`: Status und Familie aller 96 Hauptaufgaben.",
        "- `topic-weighting.csv` und `topic-weighting-method.md`: Kennzahlen und transparente Formel.",
        "- `script-gap-analysis.md`: Prüfung der fünf Stofflücken.",
        "- `final-study-priorities.md`: evidenzbasierte Lernreihenfolge.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    missing = [entry["file"] for entry in EXAMS if not (SOURCE_DIR / entry["file"]).exists()]
    missing += [entry["file"] for entry in SOLUTION_FILES.values() if not (SOURCE_DIR / entry["file"]).exists()]
    if missing:
        raise FileNotFoundError(f"Fehlende Altlausur-Dateien: {missing}")

    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    APP_PDF_DIR.mkdir(parents=True, exist_ok=True)
    tasks = parse_rows()
    exams = []
    source_audit = []
    for exam in EXAMS:
        copy = dict(exam)
        copy["asset"] = f"exam-pdfs/{exam['asset']}"
        exam_tasks = [task for task in tasks if task["examId"] == exam["id"]]
        copy["taskIds"] = [task["id"] for task in exam_tasks]
        copy["taskCount"] = len(exam_tasks)
        copy["solutionStatuses"] = sorted({task["officialSolutionStatus"] for task in exam_tasks})
        copy.update(EXAM_AUDIT[exam["id"]])
        exams.append(copy)
        source = SOURCE_DIR / exam["file"]
        target = APP_PDF_DIR / exam["asset"]
        packaged_pages = build_ss25_question_pdf(source, target) if exam["id"] == "ss25" else None
        if exam["id"] != "ss25":
            shutil.copy2(source, target)
        audit = file_audit(source, "Klausur", f"exam-pdfs/{exam['asset']}")
        if packaged_pages:
            audit["packagedPages"] = packaged_pages
        source_audit.append(audit)
    for exam_id, solution in SOLUTION_FILES.items():
        target = APP_PDF_DIR / solution["asset"]
        source = SOURCE_DIR / solution["file"]
        exam = next(exam for exam in EXAMS if exam["id"] == exam_id)
        if solution["asset"] != exam["asset"]:
            shutil.copy2(source, target)
        existing = next((entry for entry in source_audit if entry["file"] == source.name), None)
        if existing:
            existing.setdefault("alternateAssets", []).append(f"exam-pdfs/{solution['asset']}")
        else:
            source_audit.append(file_audit(source, "Lösung", f"exam-pdfs/{solution['asset']}"))

    archive = SOURCE_DIR / "Ana2 Altklausur.pdf"
    if archive.exists():
        audit = file_audit(archive, "Sammelarchiv")
        audit["notes"] = "Enthält Duplikate der einzeln inventarisierten Klausuren und Lösungen."
        source_audit.append(audit)

    topic_rows = build_topic_weighting(exams, tasks)
    topic_by_id = {row["topic"]: row for row in topic_rows}
    for task in tasks:
        task["priorityScore"] = round(max(topic_by_id[topic]["weightScore"] for topic in task["topics"]) / 10, 2)

    payload = {
        "schemaVersion": 2, "language": "de", "generatedFrom": "local exam corpus (not included)",
        "exams": exams, "tasks": tasks, "topicLabels": TOPIC_LABELS, "sourceAudit": source_audit,
        "topicWeighting": topic_rows,
        "evidenceSources": {
            "examEvidence": {"status": "provided", "examCount": len(exams), "taskCount": len(tasks)},
            "scriptEvidence": {"status": "provided", "canonical": True},
            "exerciseEvidence": {"status": "not_provided", "files": [], "weightWhenProvided": 30},
            "currentCourseEvidence": {"status": "partial", "basis": "uploaded script and latest supplied exam; no official 2026 scope list"},
        },
        "allowedSolutionStatuses": list(SOLUTION_LABELS),
        "allowedCurrentScopeStatuses": sorted(VALID_SCOPE_STATUSES),
        "studyMix": {"dueReview": 20, "weakHighValue": 50, "mixedExam": 30},
    }
    json_text = json.dumps(payload, ensure_ascii=False, indent=2)
    (CORPUS_DIR / "exam-corpus.json").write_text(json_text + "\n", encoding="utf-8")
    write_exam_inventory(exams, source_audit)
    write_task_inventory(tasks)
    write_topic_weighting(topic_rows)
    (CORPUS_DIR / "exam-blueprint.md").write_text(build_blueprint(exams, tasks, source_audit, topic_rows), encoding="utf-8")
    (CORPUS_DIR / "topic-weighting-method.md").write_text(build_weighting_method(), encoding="utf-8")
    (CORPUS_DIR / "script-gap-analysis.md").write_text(build_gap_analysis(topic_rows, tasks), encoding="utf-8")
    (CORPUS_DIR / "final-study-priorities.md").write_text(build_final_priorities(topic_rows), encoding="utf-8")
    (ROOT / "app" / "exam-data.js").write_text(f"window.EXAM_DATA = {json_text};\n", encoding="utf-8")
    print(f"Korpus erstellt: {len(exams)} Klausuren, {len(tasks)} Aufgaben, {len({task['duplicateFamily'] for task in tasks})} Familien, {len(source_audit)} PDF-Quellen.")


if __name__ == "__main__":
    main()
