from __future__ import annotations

import copy
import re
from typing import Any


PDF_HEADER_RE = re.compile(
    r"\bANALYSIS\s+I\s*[-–]\s*III\s*,?\s*2011/2013\s+\d+\b",
    re.IGNORECASE,
)
NEXT_SECTION_RE = re.compile(r"\s+(?=\d+\.\d+\.\s+[A-ZÄÖÜ])")

TITLE_OVERRIDES = {
    "6.4.3": "Unbestimmtes Integral",
    "4.1.4": "Stetigkeit der Umkehrfunktion",
    "4.1.6": "Monoton steigend",
}

SUMMARY_OVERRIDES = {
    "6.4.3": "Diese Definition beschreibt das unbestimmte Integral als Menge aller Stammfunktionen einer Funktion.",
    "4.1.4": "Dieser Satz zeigt: Ist eine Funktion auf einem kompakten Intervall stetig und injektiv, so ist auch ihre Umkehrfunktion stetig.",
    "4.1.6": "Diese Definition führt monotones und streng monotones Wachstum auf Intervallen ein.",
    "7.2.9": "Diese Definition unterscheidet vollständige metrische Räume, Banachräume und Hilberträume.",
}

MANUALLY_VERIFIED_ITEMS = {"7.2.9"}

STATEMENT_OVERRIDES = {
    "7.2.9": "Ein metrischer Raum (X,d) heißt vollständig, wenn jede Cauchy-Folge in X konvergiert. Ein normierter Raum (V,\\|\\cdot\\|) heißt Banachraum, wenn V mit der von der Norm induzierten Metrik vollständig ist. Ein Skalarproduktraum (V,\\langle\\cdot,\\cdot\\rangle) heißt Hilbertraum, wenn V mit der induzierten Norm ein Banachraum ist.",
}

REGRESSION_BLOCKS = {
    "6.4.3": [
        {"type": "text", "text": "Sei I ein Intervall in den reellen Zahlen und f eine stetige komplexwertige Funktion auf I."},
        {"type": "label", "text": "Aussage"},
        {
            "type": "math",
            "tex": r"\int f(x)\,dx = \{F_0 + C : C \in \mathbb{C}\} = F_0 + \mathbb{C}",
        },
        {
            "type": "text",
            "text": "Dabei ist F₀ eine feste Stammfunktion. Üblicherweise werden die Mengenklammern fortgelassen.",
        },
        {"type": "label", "text": "Beispiele"},
        {"type": "math", "tex": r"\int x\,dx = \frac{x^2}{2} + C"},
        {"type": "math", "tex": r"\int \sin(x)\,dx = -\cos(x) + C"},
    ],
    "4.1.4": [
        {
            "type": "text",
            "text": "Sei f auf dem kompakten Intervall [a,b] stetig und injektiv.",
        },
        {"type": "label", "text": "Voraussetzungen"},
        {"type": "math", "tex": r"f \colon [a,b] \to \mathbb{C}"},
        {"type": "math", "tex": r"E = f([a,b]) \subseteq \mathbb{C}"},
        {"type": "label", "text": "Aussage"},
        {
            "type": "math",
            "tex": r"g \colon E \to [a,b], \qquad g = f^{-1}",
        },
        {"type": "text", "text": "Dann ist die Umkehrfunktion g stetig."},
    ],
    "4.1.6": [
        {"type": "text", "text": "Sei I ein Intervall und f eine reellwertige Funktion auf I."},
        {"type": "label", "text": "Monoton steigend"},
        {
            "type": "math",
            "tex": r"x \leq y \quad\Longrightarrow\quad f(x) \leq f(y)",
        },
        {"type": "label", "text": "Streng monoton steigend"},
        {
            "type": "math",
            "tex": r"x < y \quad\Longrightarrow\quad f(x) < f(y)",
        },
        {"type": "label", "text": "Bemerkung"},
        {"type": "text", "text": "Jede streng monotone Funktion ist injektiv."},
        {"type": "label", "text": "Beispiel"},
        {
            "type": "math",
            "tex": r"\sqrt[k]{\,\cdot\,} \colon [a,b] \to [\sqrt[k]{a},\sqrt[k]{b}]",
        },
    ],
    "7.2.9": [
        {"type": "label", "text": "Vollständiger metrischer Raum"},
        {"type": "text", "text": "Ein metrischer Raum (X,d) heißt vollständig, wenn jede Cauchy-Folge in X konvergiert."},
        {"type": "label", "text": "Banachraum"},
        {"type": "text", "text": "Ein normierter Raum heißt Banachraum, wenn er mit der von seiner Norm induzierten Metrik vollständig ist."},
        {"type": "label", "text": "Hilbertraum"},
        {"type": "text", "text": "Ein Skalarproduktraum heißt Hilbertraum, wenn er mit der induzierten Norm ein Banachraum ist."},
    ],
}

GERMAN_KIND = {
    "Definition": "Definition",
    "Satz": "Satz",
    "Lemma": "Lemma",
    "Folgerung": "Folgerung",
    "Korollar": "Korollar",
    "Beispiel": "Beispiel",
    "Bemerkung": "Bemerkung",
    "proof": "Beweis",
}


def strip_pdf_noise(value: str) -> str:
    text = str(value or "")
    text = PDF_HEADER_RE.sub(" ", text)
    text = re.split(r"\s+LITERATUR\b", text, maxsplit=1)[0]
    next_section = NEXT_SECTION_RE.search(text)
    if next_section and next_section.start() > 0:
        text = text[: next_section.start()]
    text = re.sub(r"(?<=[A-Za-zÄÖÜäöüß])-\s+(?=[a-zäöüß])", "", text)
    text = re.sub(r"\b(bzw|d\.h|z\.B)\s+\.", r"\1.", text)
    replacements = {
        "schre iben": "schreiben",
        "unter scheiden": "unterscheiden",
        "wesentli- che": "wesentliche",
        "Mat rix": "Matrix",
        "Speziallfall": "Spezialfall",
        "Aussa gen": "Aussagen",
        "Ab bildung": "Abbildung",
        "Quelltext :": "Quelltext:",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_latex(value: str) -> str:
    text = str(value or "")
    text = text.replace("\\\\", "\\")
    unicode_map = {
        "→": r"\to ",
        "⇒": r"\Rightarrow ",
        "⇔": r"\Longleftrightarrow ",
        "≤": r"\leq ",
        "≥": r"\geq ",
        "∈": r"\in ",
        "⊂": r"\subseteq ",
        "∅": r"\emptyset ",
        "∞": r"\infty ",
    }
    for old, new in unicode_map.items():
        text = text.replace(old, new)
    text = re.sub(r"(?<!\\)mathbb\s*\{?([RNCQZ])\}?", r"\\mathbb{\1}", text)
    text = re.sub(r"\\mathbb\s*([RNCQZ])", r"\\mathbb{\1}", text)
    text = re.sub(r"\\(?:subset|subseteq)\s+R\b", r"\\subseteq \\mathbb{R}", text)
    text = re.sub(r"\\(?:subset|subseteq)\s+C\b", r"\\subseteq \\mathbb{C}", text)
    text = re.sub(r"\\to\s+R\b", r"\\to \\mathbb{R}", text)
    text = re.sub(r"\\to\s+C\b", r"\\to \\mathbb{C}", text)
    text = re.sub(r"\\in\s+R\b", r"\\in \\mathbb{R}", text)
    text = re.sub(r"\\in\s+C\b", r"\\in \\mathbb{C}", text)
    text = re.sub(r"\\in\s+N0\b", r"\\in \\mathbb{N}_0", text)
    text = re.sub(r"\\in\s+N\b", r"\\in \\mathbb{N}", text)
    text = re.sub(r"\b([kn])\\sqrt\s*([A-Za-z0-9]+|·)", lambda m: rf"\sqrt[{m.group(1)}]{{{r'\cdot' if m.group(2) == '·' else m.group(2)}}}", text)
    text = re.sub(r"\\sqrt\s*([A-Za-z0-9]+)", r"\\sqrt{\1}", text)
    text = text.replace(r"\sqrt·", r"\sqrt{\cdot}")
    text = re.sub(r"\\(mapsto|in|exists|forall)(?=[A-Za-z])", r"\\\1 ", text)
    text = text.replace(r"\le ", r"\leq ").replace(r"\ge ", r"\geq ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def validate_latex(value: str) -> list[str]:
    text = str(value or "")
    issues: list[str] = []
    depth = 0
    escaped = False
    for char in text:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                issues.append("schließende Klammer ohne öffnende Klammer")
                depth = 0
    if depth:
        issues.append("nicht geschlossene geschweifte Klammer")
    if re.search(r"\\sqrt(?!\s*(?:\[|\{))", text):
        issues.append("Wurzel ohne sicheres Argument")
    if re.search(r"(?<!\\)\b(?:mathbb|Rightarrow|varepsilon)\b", text):
        issues.append("LaTeX-Befehl ohne Backslash")
    if text.count("$") % 2:
        issues.append("ungerade Anzahl von Dollar-Trennzeichen")
    if text.count(r"\(") != text.count(r"\)"):
        issues.append("nicht passende Inline-Mathematik-Trennzeichen")
    if text.count(r"\[") != text.count(r"\]"):
        issues.append("nicht passende Display-Mathematik-Trennzeichen")
    return list(dict.fromkeys(issues))


def readable_math_fallback(value: str) -> str:
    text = normalize_latex(value)
    replacements = {
        r"\mathbb{R}": "ℝ",
        r"\mathbb{C}": "ℂ",
        r"\mathbb{N}_0": "ℕ₀",
        r"\mathbb{N}": "ℕ",
        r"\mathbb{Q}": "ℚ",
        r"\mathbb{Z}": "ℤ",
        r"\subseteq": "⊆",
        r"\subset": "⊂",
        r"\supset": "⊃",
        r"\in": "∈",
        r"\notin": "∉",
        r"\to": "→",
        r"\mapsto": "↦",
        r"\Rightarrow": "⇒",
        r"\Longleftrightarrow": "⇔",
        r"\leq": "≤",
        r"\geq": "≥",
        r"\emptyset": "∅",
        r"\infty": "∞",
        r"\varepsilon": "ε",
        r"\lambda": "λ",
        r"\xi": "ξ",
        r"\varphi": "φ",
        r"\cap": "∩",
        r"\cup": "∪",
        r"\setminus": "∖",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\\sqrt\[([^]]+)\]\{([^{}]+)\}", r"\1-te Wurzel aus (\2)", text)
    text = re.sub(r"\\sqrt\{([^{}]+)\}", r"√(\1)", text)
    text = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"(\1)/(\2)", text)
    text = re.sub(r"\\([A-Za-z]+)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_metadata(source: str, section: str) -> dict[str, Any]:
    page_match = re.search(r"PDF\s+p(\d+)", source or "")
    if not section:
        source_section = re.search(r";\s*section\s+(.+)$", source or "")
        if source_section:
            section = source_section.group(1).strip()
    section_match = re.match(r"((?:A\.)?\d+\.\d+)\.\s*(.*)", section or "")
    return {
        "document": "PDF",
        "page": int(page_match.group(1)) if page_match else None,
        "sectionNumber": section_match.group(1) if section_match else "",
        "sectionTitle": section_match.group(2).strip() if section_match else (section or ""),
    }


def clean_title(value: str, item_id: str) -> str:
    if item_id in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[item_id]
    title = str(value or "").strip()
    if not title or re.search(r"unnamed|unknown|unbenannt", title, re.IGNORECASE):
        return ""
    if re.match(r"(?:A\.)?\d+\.\d+\.", title):
        return ""
    return title


def german_summary(item: dict[str, Any]) -> str:
    item_id = str(item.get("id", ""))
    if item_id in SUMMARY_OVERRIDES:
        return SUMMARY_OVERRIDES[item_id]
    kind = item.get("kind", "")
    title = clean_title(item.get("title", ""), item_id)
    section = parse_metadata(item.get("source", ""), item.get("section", ""))
    location = f"Abschnitt {section['sectionNumber']}" if section["sectionNumber"] else "diesem Abschnitt"
    if kind == "Definition":
        return f"Diese Definition führt den Begriff „{title}“ präzise ein." if title else f"Diese Definition legt einen zentralen Begriff aus {location} präzise fest."
    if kind in {"Satz", "Lemma", "Folgerung", "Korollar"}:
        return f"Dieses Ergebnis formuliert eine mathematische Aussage aus {location}; vor der Anwendung sind alle Voraussetzungen zu prüfen."
    if kind == "Beispiel":
        return f"Dieses Beispiel veranschaulicht die Begriffe und Verfahren aus {location}."
    if kind == "Bemerkung":
        return f"Diese Bemerkung ergänzt oder präzisiert den Inhalt aus {location}."
    return f"Dieser Lernblock gehört zu {location}."


def _split_paragraphs(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?□])\s+(?=[A-ZÄÖÜ(])", text)
    paragraphs: list[str] = []
    current: list[str] = []
    length = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if current and length + len(part) > 360:
            paragraphs.append(" ".join(current))
            current, length = [], 0
        current.append(part)
        length += len(part) + 1
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def build_content_blocks(item: dict[str, Any]) -> tuple[list[dict[str, str]], list[str]]:
    item_id = str(item.get("id", ""))
    if item_id in REGRESSION_BLOCKS:
        blocks = copy.deepcopy(REGRESSION_BLOCKS[item_id])
        issues = [issue for block in blocks if block["type"] == "math" for issue in validate_latex(block["tex"])]
        return blocks, list(dict.fromkeys(issues))

    cleaned = strip_pdf_noise(item.get("statement", ""))
    normalized = normalize_latex(cleaned)
    issues = validate_latex(normalized)
    blocks: list[dict[str, str]] = []
    marker_re = re.compile(r"\b(Beweis|Beispiele?|Bemerkung|Folgerung|Idee|Anwendung)\s*:\s*", re.IGNORECASE)
    position = 0
    current_label = ""
    for match in marker_re.finditer(normalized):
        before = normalized[position : match.start()].strip()
        if before:
            if current_label:
                blocks.append({"type": "label", "text": current_label})
                current_label = ""
            blocks.extend({"type": "text", "text": readable_math_fallback(p)} for p in _split_paragraphs(before))
        current_label = match.group(1).capitalize()
        position = match.end()
    tail = normalized[position:].strip()
    if current_label:
        blocks.append({"type": "label", "text": current_label})
    if tail:
        blocks.extend({"type": "text", "text": readable_math_fallback(p)} for p in _split_paragraphs(tail))
    if not blocks:
        blocks = [{"type": "text", "text": readable_math_fallback(normalized)}]
    return blocks, issues


def translate_question_text(value: str) -> str:
    text = str(value or "")
    patterns = [
        (r"^State and explain Def ([^:]+): (.+)\.$", r"Gib Definition \1 an und erläutere „\2“."),
        (r"^State (Satz|Lemma|Folgerung|Korollar) ([^:]+): (.+), including assumptions and conclusion\.$", r"Formuliere \1 \2 „\3“ mit allen Voraussetzungen und der Schlussfolgerung."),
        (r"^What must be checked before applying (.+)\?$", r"Welche Voraussetzungen müssen vor der Anwendung von \1 geprüft werden?"),
        (r"^What is the proof idea of (.+)\?$", r"Was ist die Beweisidee von \1?"),
        (r"^What pattern is illustrated by Beispiel (.+)\?$", r"Welches mathematische Muster veranschaulicht Beispiel \1?"),
        (r"^What role does section (.+) play in the dependency chain\?$", r"Welche Rolle spielt Abschnitt \1 in der Abhängigkeitskette?"),
    ]
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    replacements = {
        "Formal statement:": "Formale Aussage:",
        "Explanation:": "Erläuterung:",
        "Assumptions and conclusion are in the statement:": "Voraussetzungen und Schlussfolgerung stehen in der Aussage:",
        "Why it matters:": "Bedeutung:",
        "This is a reusable tool: check its assumptions before applying it in exercises.": "Dieses Ergebnis ist wiederverwendbar; vor der Anwendung sind alle Voraussetzungen zu prüfen.",
        "Proof idea:": "Beweisidee:",
        "Key dependencies:": "Wichtige Voraussetzungen:",
        "The example belongs to": "Das Beispiel gehört zu",
        "Source transcription:": "Quelltext:",
        "Section role:": "Rolle des Abschnitts:",
        "Connect it to earlier prerequisites and later uses before moving on.": "Ordne den Abschnitt vor dem Weiterlernen in seine Voraussetzungen und späteren Anwendungen ein.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return strip_pdf_noise(text)


def enrich_item(item: dict[str, Any]) -> dict[str, Any]:
    enriched = copy.deepcopy(item)
    item_id = str(enriched.get("id", ""))
    enriched["title"] = clean_title(enriched.get("title", ""), str(enriched.get("id", "")))
    enriched["summary"] = german_summary(enriched)
    enriched["intuition"] = enriched["summary"]
    enriched["metadata"] = parse_metadata(enriched.get("source", ""), enriched.get("section", ""))
    enriched["statement"] = STATEMENT_OVERRIDES.get(item_id, strip_pdf_noise(enriched.get("statement", "")))
    blocks, latex_issues = build_content_blocks(enriched)
    enriched["contentBlocks"] = blocks
    existing_warning = enriched.get("warning", "")
    review_issues = list(latex_issues)
    if existing_warning and "No major" not in existing_warning:
        review_issues.append("OCR- oder Extraktionshinweis aus der Quelldatei")
    if item_id in MANUALLY_VERIFIED_ITEMS:
        review_issues = []
        enriched["warning"] = "Manuell gegen PDF-Seite 121 (gedruckte Seite 119) geprüft."
    enriched["reviewIssues"] = list(dict.fromkeys(review_issues))
    enriched["needsReview"] = bool(enriched["reviewIssues"])
    return enriched


def _referenced_item_id(value: str) -> str:
    match = re.search(r"(?:A\.)?\d+\.\d+(?:\.\d+)?", value or "")
    return match.group(0) if match else ""


def enrich_question(question: dict[str, Any], item_index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    enriched = copy.deepcopy(question)
    reference_id = _referenced_item_id(enriched.get("question", ""))
    item = item_index.get(reference_id)
    category = enriched.get("category", "")
    if category == "conceptual connections":
        source = str(enriched.get("source", ""))
        enriched["question"] = f"Welche Rolle spielt {source} im Aufbau des Skripts?" if source else "Welche Rolle spielt dieser Abschnitt im Aufbau des Skripts?"
        enriched["short"] = "Der Abschnitt verbindet frühere Voraussetzungen mit späteren Anwendungen."
        enriched["full"] = "Nenne die benötigten früheren Begriffe, die zentrale neue Aussage und mindestens eine spätere Anwendung im Skript."
        enriched["metadata"] = parse_metadata(enriched.get("source", ""), "")
        enriched["needsReview"] = False
        enriched["reviewIssues"] = []
        return enriched
    if item:
        title = item.get("title", "")
        descriptor = f" „{title}“" if title else ""
        statement = readable_math_fallback(item.get("statement", ""))
        if category == "definitions":
            enriched["question"] = f"Gib Definition {reference_id}{descriptor} an und erläutere ihre Bedeutung."
            enriched["short"] = statement
            enriched["full"] = f"{item['summary']} Formale Definition: {statement}"
        elif category == "theorem statements":
            enriched["question"] = f"Formuliere {item.get('kind', 'Satz')} {reference_id}{descriptor} mit allen Voraussetzungen und der Schlussfolgerung."
            enriched["short"] = statement
            enriched["full"] = f"Aussage: {statement} Vor der Anwendung sind sämtliche Voraussetzungen zu prüfen."
        elif category == "assumptions/conclusions":
            enriched["question"] = f"Welche Voraussetzungen und welche Schlussfolgerung gehören zu {item.get('kind', 'Satz')} {reference_id}{descriptor}?"
            enriched["short"] = "Prüfe die in der Aussage genannten Voraussetzungen vollständig."
            enriched["full"] = f"Nutze die Originalaussage als Prüfliste: {statement}"
        elif category == "proof ideas":
            enriched["question"] = f"Was ist die Beweisidee zu {item.get('kind', 'Satz')} {reference_id}{descriptor}?"
            enriched["short"] = "Ordne Voraussetzungen, zentrale Konstruktion und abschließendes Argument in der Reihenfolge des Skripts."
            enriched["full"] = "Vergleiche die Beweisschritte mit der Beweiskarte und dem PDF; übernimm keine nicht belegte Zwischenbehauptung."
        elif category == "examples":
            enriched["question"] = f"Welches mathematische Muster veranschaulicht Beispiel {reference_id}{descriptor}?"
            enriched["short"] = item["summary"]
            enriched["full"] = f"Quellnaher Inhalt: {statement}"
        else:
            for key in ("question", "short", "full"):
                enriched[key] = translate_question_text(enriched.get(key, ""))
    else:
        for key in ("question", "short", "full"):
            enriched[key] = translate_question_text(enriched.get(key, ""))
        if re.search(r"\b(?:What|State|Explain|Section|Connect|Full|Short|Answer)\b", enriched.get("question", ""), re.IGNORECASE):
            enriched["question"] = "Welche Rolle spielt dieser Inhalt im Aufbau des jeweiligen Abschnitts?"
        if re.search(r"\b(?:This|The|Section|Connect|Use|Check)\b", enriched.get("full", ""), re.IGNORECASE):
            enriched["full"] = "Ordne den Inhalt in seine Voraussetzungen und späteren Anwendungen ein und prüfe ihn anhand der angegebenen PDF-Stelle."
    enriched["metadata"] = parse_metadata(enriched.get("source", ""), "")
    enriched["needsReview"] = bool(enriched.get("warning") and "No major" not in enriched.get("warning", ""))
    enriched["reviewIssues"] = ["OCR- oder Extraktionshinweis aus der Quelldatei"] if enriched["needsReview"] else []
    return enriched


def enrich_proof(proof: dict[str, Any], source_item: dict[str, Any] | None = None) -> dict[str, Any]:
    item = copy.deepcopy(proof)
    item["kind"] = "Beweis"
    item["section"] = re.sub(r"^PDF p\d+; section ", "", item.get("source", ""))
    item["summary"] = "Diese Beweiskarte hebt die Beweisidee und die entscheidenden mathematischen Schritte hervor."
    item["strategy"] = "Arbeite die Voraussetzungen ab, führe die zentrale Konstruktion oder Abschätzung in der Reihenfolge des Skripts aus und begründe anschließend die Schlussfolgerung."
    if source_item:
        item["title"] = source_item.get("title", item.get("title", ""))
        item["statement"] = source_item.get("statement", item.get("statement", ""))
        item["metadata"] = source_item.get("metadata", parse_metadata(item.get("source", ""), item.get("section", "")))
        item["contentBlocks"] = copy.deepcopy(source_item.get("contentBlocks", []))
        item["reviewIssues"] = list(source_item.get("reviewIssues", []))
        item["needsReview"] = bool(item["reviewIssues"])
    else:
        item["metadata"] = parse_metadata(item.get("source", ""), item.get("section", ""))
        blocks, issues = build_content_blocks(item)
        item["contentBlocks"] = blocks
        item["reviewIssues"] = issues
        item["needsReview"] = bool(issues)
    return item


def enrich_app_payload(payload: dict[str, Any]) -> dict[str, Any]:
    enriched = copy.deepcopy(payload)
    enriched["items"] = [enrich_item(item) for item in enriched.get("items", [])]
    item_index = {item["id"]: item for item in enriched["items"]}
    enriched["questions"] = [enrich_question(question, item_index) for question in enriched.get("questions", [])]
    enriched["proofs"] = [enrich_proof(proof, item_index.get(str(proof.get("id", "")))) for proof in enriched.get("proofs", [])]
    enriched["schemaVersion"] = 2
    enriched["language"] = "de"
    return enriched
