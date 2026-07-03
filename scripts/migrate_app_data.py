from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

from app_content import enrich_app_payload


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "app" / "data.js"
BACKUP_PATH = BASE_DIR / "app" / "data.pre-card-redesign.js"


def load_payload(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    prefix = "window.STUDY_DATA = "
    if not raw.startswith(prefix):
        raise ValueError(f"Unerwartetes Datenformat: {path}")
    return json.loads(raw[len(prefix) :])


def is_false_appendix_cross_reference(entry: dict) -> bool:
    item_id = str(entry.get("id", ""))
    source = str(entry.get("source", ""))
    return item_id.startswith("A.") and "section A." not in source


def migrate(data_path: Path = DATA_PATH, create_backup: bool = True) -> dict:
    if create_backup and not BACKUP_PATH.exists():
        shutil.copy2(data_path, BACKUP_PATH)

    payload = load_payload(data_path)
    inventory_payload = json.loads((BASE_DIR / "source-inventory.json").read_text(encoding="utf-8"))
    inventory_by_key = {
        (str(item.get("id", "")), int(item.get("page", 0))): item
        for item in inventory_payload.get("items", [])
    }
    for item in payload.get("items", []):
        page_match = re.search(r"PDF\s+p(\d+)", str(item.get("source", "")))
        page = int(page_match.group(1)) if page_match else 0
        source_item = inventory_by_key.get((str(item.get("id", "")), page))
        if source_item:
            item["statement"] = source_item.get("text", item.get("statement", ""))
            item["warning"] = source_item.get("uncertainty", item.get("warning", ""))
    existing_keys = {
        (str(item.get("id", "")), str(item.get("source", "")))
        for item in payload.get("items", [])
    }
    for source_item in inventory_payload.get("items", []):
        if source_item.get("kind") != "Bemerkung":
            continue
        source = f"PDF p{source_item.get('page')}; section {source_item.get('section_title', '')}"
        key = (str(source_item.get("id", "")), source)
        if key in existing_keys:
            continue
        payload.setdefault("items", []).append(
            {
                "id": source_item.get("id", ""),
                "kind": "Bemerkung",
                "title": source_item.get("name", ""),
                "section": source_item.get("section_title", ""),
                "source": source,
                "statement": source_item.get("text", ""),
                "intuition": "",
                "tags": f"bemerkung sec-{str(source_item.get('section_key', '')).replace('.', '-')} ch-{str(source_item.get('section_key', '')).split('.')[0]}",
                "exam": "low",
                "warning": source_item.get("uncertainty", ""),
            }
        )
    payload["items"] = [
        item for item in payload.get("items", []) if not is_false_appendix_cross_reference(item)
    ]
    payload["questions"] = [
        question
        for question in payload.get("questions", [])
        if not (
            "A.3.10" in str(question.get("question", ""))
            and "section A." not in str(question.get("source", ""))
        )
    ]
    enriched = enrich_app_payload(payload)
    data_path.write_text(
        "window.STUDY_DATA = " + json.dumps(enriched, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return enriched


def main() -> None:
    parser = argparse.ArgumentParser(description="Migriert die App-Daten auf das deutsche Lernkarten-Schema.")
    parser.add_argument("--no-backup", action="store_true", help="Keine Sicherung der bisherigen data.js anlegen.")
    args = parser.parse_args()
    payload = migrate(create_backup=not args.no_backup)
    review_count = sum(1 for item in payload["items"] if item.get("needsReview"))
    print(
        f"Migriert: {len(payload['items'])} Lernblöcke, "
        f"{len(payload['questions'])} Fragen, {len(payload['proofs'])} Beweise; "
        f"{review_count} Lernblöcke zur manuellen Prüfung markiert."
    )


if __name__ == "__main__":
    main()
