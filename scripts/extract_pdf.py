import argparse
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract page-delimited text from a local PDF.")
    parser.add_argument("pdf", type=Path, help="Path to the source PDF")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "source-extract.txt")
    args = parser.parse_args()

    reader = PdfReader(str(args.pdf))
    with args.output.open("w", encoding="utf-8") as handle:
        for page_number, page in enumerate(reader.pages, start=1):
            handle.write(f"\n\n<<<PAGE {page_number}>>>\n")
            handle.write(page.extract_text() or "")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
