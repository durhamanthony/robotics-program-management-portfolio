#!/usr/bin/env python3
"""Create the validated Windows-sync portfolio ZIP and SHA-256 manifest."""

from __future__ import annotations

import csv
import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DELIVERABLES = ROOT / "deliverables"
MANIFEST = ROOT / "WINDOWS_SYNC_MANIFEST.csv"
OUTPUT = DELIVERABLES / "robotics-program-management-portfolio-windows-sync-2026-08-23.zip"
TOP = "robotics-program-management-portfolio-main"
EXCLUDED_PARTS = {".git", ".venv", ".render-venv", "__pycache__", "qa", "deliverables"}
EXCLUDED_SUFFIXES = {".pyc", ".inspect.ndjson"}


def included(path: Path) -> bool:
    if not path.is_file():
        return False
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if path.name == MANIFEST.name:
        return False
    if path.suffix.lower() == ".pyc" or path.name.endswith(".inspect.ndjson"):
        return False
    if rel.parts and rel.parts[0] == "outputs" and path.name != ".gitkeep":
        return False
    return True


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    files = sorted((path for path in ROOT.rglob("*") if included(path)), key=lambda path: path.relative_to(ROOT).as_posix().lower())
    with MANIFEST.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("table_title", "path", "bytes", "sha256", "evidence_class", "confidence", "source_or_validation"))
        for path in files:
            writer.writerow((
                "Table 1. Windows sync release manifest",
                path.relative_to(ROOT).as_posix(),
                path.stat().st_size,
                digest(path),
                "DC-L",
                "Low",
                "SHA-256 calculated from the packaged release-candidate file",
            ))
    files.append(MANIFEST)
    DELIVERABLES.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda item: item.relative_to(ROOT).as_posix().lower()):
            archive.write(path, f"{TOP}/{path.relative_to(ROOT).as_posix()}")
    print(f"Built {OUTPUT} ({OUTPUT.stat().st_size:,} bytes; sha256={digest(OUTPUT)})")


if __name__ == "__main__":
    main()
