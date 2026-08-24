#!/usr/bin/env python3
"""Apply portfolio-wide evidence keys, Markdown table titles, and CSV metadata."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOTS = ("scenarios", "governance", "tools", "portfolio", "simulations", "pm-operating-system", "quality-control")
KEY = "> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved."


def safe_title(value: str) -> str:
    value = re.sub(r"^#+\s*", "", value).strip()
    value = re.sub(r"[*_`]", "", value)
    return value or "Data table"


def normalize_caption(line: str) -> str:
    body = line.strip()
    closing = body.endswith("**")
    inner = body[2:-2] if closing else body[2:]
    if "evidence" not in inner.lower():
        inner += " — Evidence: disclosed row/source notes"
    if "confidence" not in inner.lower():
        inner += "; Confidence: see evidence key and row/source notes"
    return f"**{inner}**"


def update_markdown(path: Path) -> None:
    original = path.read_text(encoding="utf-8", errors="replace")
    lines = original.splitlines()
    if not any("Evidence-confidence key" in line for line in lines[:18]):
        heading = next((i for i, line in enumerate(lines) if re.match(r"^#\s+", line)), None)
        insert_at = heading + 1 if heading is not None else 0
        insertion = ["", KEY, ""]
        lines[insert_at:insert_at] = insertion

    output: list[str] = []
    table_number = 0
    in_fence = False
    for index, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        is_table = (
            not in_fence
            and line.startswith("|")
            and index + 1 < len(lines)
            and bool(re.match(r"^\|?\s*:?-{3,}", lines[index + 1]))
        )
        if is_table:
            table_number += 1
            previous = len(output) - 1
            while previous >= 0 and not output[previous].strip():
                previous -= 1
            if previous >= 0 and re.match(r"^\*\*Table\s+", output[previous].strip(), re.I):
                output[previous] = normalize_caption(output[previous])
            else:
                heading = ""
                for prior in range(index - 1, -1, -1):
                    if re.match(r"^#{1,6}\s+", lines[prior]):
                        heading = safe_title(lines[prior])
                        break
                if output and output[-1].strip():
                    output.append("")
                output.append(f"**Table {table_number}. {heading or safe_title(path.stem)} — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**")
                output.append("")
        output.append(line)
    text = "\n".join(output).rstrip() + "\n"
    if text != original:
        path.write_text(text, encoding="utf-8")


def csv_defaults(path: Path) -> tuple[str, str, str]:
    rel = path.relative_to(ROOT).as_posix()
    if "PUBLIC_ARTIFACT_REGISTER" in path.name:
        return "DC-L", "Low", "Generated from repository source files; validate paths and titles"
    if rel.startswith("quality-control/"):
        return "DC-L", "Low", "Independent checklist logic; execute against the release candidate"
    if "sample_robot_events" in path.name:
        return "SA-L", "Low", "Synthetic events for deterministic workflow demonstration"
    if rel.startswith("pm-operating-system/"):
        return "SA-L", "Low", "Reusable example row; replace with approved project evidence"
    return "SA-L", "Low", "Fictional scenario record; replace assumptions with approved actuals"


def update_csv(path: Path) -> None:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            return
        rows = list(reader)
        original_fields = list(reader.fieldnames)
    required = ["table_title", "evidence_class", "confidence", "source_or_validation"]
    fields = required[:1] + [field for field in original_fields if field not in required] + required[1:]
    evidence_class, confidence, source = csv_defaults(path)
    title = f"Table 1. {path.stem.replace('_', ' ').title()}"
    for row in rows:
        row["table_title"] = row.get("table_title") or title
        row["evidence_class"] = row.get("evidence_class") or evidence_class
        row["confidence"] = row.get("confidence") or confidence
        row["source_or_validation"] = row.get("source_or_validation") or source
    if fields != original_fields or any(not row.get(key) for row in rows for key in required):
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)


def main() -> None:
    markdown_count = 0
    csv_count = 0
    for root_name in SOURCE_ROOTS:
        base = ROOT / root_name
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            update_markdown(path)
            markdown_count += 1
        for path in sorted(base.rglob("*.csv")):
            update_csv(path)
            csv_count += 1
    print(f"Applied evidence/table controls to {markdown_count} Markdown files and {csv_count} CSV files.")


if __name__ == "__main__":
    main()
