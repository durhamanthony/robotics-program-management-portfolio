#!/usr/bin/env python3
"""Build self-contained, read-only Claude and Grok portfolio QC packages."""

from __future__ import annotations

import csv
import hashlib
import io
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QC = ROOT / "quality-control"
SOURCE_DIRS = ("scenarios", "governance", "portfolio", "simulations", "tools", "pm-operating-system", "docs")
SOURCE_FILES = (
    "README.md",
    "LICENSE",
    "COLLABORATION_GUIDE.md",
    "CONTRIBUTING.md",
    "VALIDATE_PORTFOLIO_WINDOWS.bat",
    "RUN_RETAIL_DEMO_WINDOWS.bat",
    "RENDER_RETAIL_VIDEO_WINDOWS.bat",
    "RUN_SUPPORT_WORKFLOW_WINDOWS.bat",
    "RENDER_ALL_MUJOCO_VIDEOS_WINDOWS.bat",
    "media/videos/video_manifest.csv",
    "scripts/validate_portfolio.py",
    "scripts/build_portfolio_site.py",
    "scripts/build_pm_spreadsheet.mjs",
    "scripts/build_case03_financial_model.mjs",
    "scripts/render_mujoco_videos.py",
    "scripts/apply_approved_rebuild.py",
    "scripts/apply_evidence_and_table_titles.py",
)
EXCLUDED_SUFFIXES = {".mp4", ".pyc", ".zip"}
EXCLUDED_PARTS = {"__pycache__", "qa", ".git", ".venv", "outputs", "deliverables"}


def include(path: Path) -> bool:
    if not path.is_file() or path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    rel = path.relative_to(ROOT)
    return not any(part in EXCLUDED_PARTS for part in rel.parts)


def source_paths() -> list[Path]:
    paths: set[Path] = set()
    for directory in SOURCE_DIRS:
        base = ROOT / directory
        if base.exists():
            paths.update(path for path in base.rglob("*") if include(path))
    for name in SOURCE_FILES:
        path = ROOT / name
        if include(path):
            paths.add(path)
    return sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix().lower())


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest_bytes(paths: list[Path]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(("table_title", "path", "bytes", "sha256", "evidence_class", "confidence", "source_or_validation"))
    for path in paths:
        data = path.read_bytes()
        writer.writerow((
            "Table 1. QC package file manifest",
            f"portfolio-source/{path.relative_to(ROOT).as_posix()}",
            len(data),
            sha256(data),
            "DC-L",
            "Low",
            "Hash calculated from the packaged release-candidate file",
        ))
    return stream.getvalue().encode("utf-8")


def media_hash_bytes() -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(("table_title", "path", "bytes", "sha256", "evidence_class", "confidence", "source_or_validation"))
    for path in sorted((ROOT / "media" / "videos").glob("*.mp4")):
        data = path.read_bytes()
        writer.writerow(("Table 1. Excluded media binary hashes", path.relative_to(ROOT).as_posix(), len(data), sha256(data), "DC-L", "Low", "Video binary excluded from compact QC package; compare hash to release candidate"))
    return stream.getvalue().encode("utf-8")


def build(reviewer: str, prompt_path: Path, output: Path) -> None:
    paths = source_paths()
    readme = (
        f"{reviewer.upper()} ROBOTICS PORTFOLIO QC PACKAGE\r\n\r\n"
        "Read REVIEW_PROMPT.md first. Review portfolio-source as a read-only release candidate.\r\n"
        "Use common/QC_CHECKLIST.csv and return the schema in common/EXPECTED_RESPONSE_SCHEMA.json.\r\n"
        "Large MP4 binaries are excluded; MEDIA_FILE_HASHES.csv records their release-candidate hashes.\r\n"
        "The package contains fictional scenarios and reusable templates, not production approvals.\r\n"
    ).encode("utf-8")
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr("PACKAGE_README.txt", readme)
        archive.writestr("REVIEW_PROMPT.md", prompt_path.read_bytes())
        for common in ("QC_CHECKLIST.csv", "EVIDENCE_LABEL_STANDARD.md", "EXPECTED_RESPONSE_SCHEMA.json"):
            archive.writestr(f"common/{common}", (QC / "common" / common).read_bytes())
        archive.writestr("FILE_MANIFEST.csv", manifest_bytes(paths))
        archive.writestr("MEDIA_FILE_HASHES.csv", media_hash_bytes())
        for path in paths:
            archive.write(path, f"portfolio-source/{path.relative_to(ROOT).as_posix()}")
    print(f"Built {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes)")


def main() -> None:
    build("Claude", QC / "claude" / "CLAUDE_QC_PROMPT.md", QC / "CLAUDE_QC_PACKAGE.zip")
    build("Grok", QC / "grok" / "GROK_QC_PROMPT.md", QC / "GROK_QC_PACKAGE.zip")


if __name__ == "__main__":
    main()
