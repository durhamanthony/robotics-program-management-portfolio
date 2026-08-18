#!/usr/bin/env python3
"""Validate public portfolio safety, required artifacts, and generated-site links."""

from __future__ import annotations

import csv
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.values.append(value)


def check_site_links(errors: list[str]) -> None:
    for page in DOCS.rglob("*.html"):
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))
        for value in parser.values:
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            try:
                target.relative_to(DOCS.resolve())
            except ValueError:
                errors.append(f"Link escapes docs: {page.relative_to(ROOT)} -> {value}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                errors.append(f"Broken site link: {page.relative_to(ROOT)} -> {value}")


def check_public_safety(errors: list[str], warnings: list[str]) -> None:
    blocked = {
        "private phone number": re.compile(r"650[- .]464[- .]9965"),
        "private email": re.compile(r"durhamanthony\s*@\s*gmail\.com", re.I),
        "local Windows user path": re.compile(r"[A-Za-z]:[\\/]Users[\\/]durha", re.I),
    }
    extensions = {".md", ".txt", ".csv", ".html", ".json", ".py", ".bat"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in blocked.items():
            if pattern.search(text):
                errors.append(f"Found {label}: {path.relative_to(ROOT)}")
    placeholders = []
    for path in ROOT.rglob("*"):
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.is_file() and path.suffix.lower() in extensions and "YOUR-GITHUB-USERNAME" in path.read_text(encoding="utf-8", errors="replace"):
            placeholders.append(str(path.relative_to(ROOT)))
    if placeholders:
        warnings.append("Replace GitHub username before publishing: " + ", ".join(placeholders))


def check_public_boundaries(errors: list[str]) -> None:
    blocked_top_level = {"career", "templates"}
    blocked_names = {
        "PUBLISHING_CHECKLIST.md",
        "LINKEDIN_PORTFOLIO_PUBLISHING.md",
        "AI_PROMPT_KIT.md",
        "CAREER_STRATEGY.md",
        "RUN_MUJOCO_WINDOWS.bat",
        "INSTALL_PORTFOLIO_V6.txt",
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in blocked_top_level:
            errors.append(f"Private-only path in public repository: {rel}")
        if path.name in blocked_names:
            errors.append(f"Private-only file in public repository: {rel}")


def check_dashboards(errors: list[str]) -> None:
    pages = (
        "retail-humanoid-backroom.html",
        "quadruped-security-deployment.html",
        "ad01-new-robot-first-sale.html",
        "robotics-support-operations.html",
    )
    for name in pages:
        path = DOCS / "scenarios" / name
        if not path.exists():
            errors.append(f"Missing scenario dashboard: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if text.count("data-tab-target=") != 8 or text.count('class="dashboard-panel') != 8:
            errors.append(f"Dashboard is missing one or more required sections: {path.relative_to(ROOT)}")


def check_scenarios(errors: list[str]) -> None:
    required = {
        "01-humanoid-retail-backroom": ("ARTIFACT_INDEX.md", "STATEMENT_OF_WORK.md", "BUSINESS_CASE_AND_TCO.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "BUDGET.csv", "REQUIREMENTS_TRACEABILITY.csv", "CLOSEOUT_AND_BENEFITS.md"),
        "02-quadruped-security-deployment": ("ARTIFACT_INDEX.md", "STATEMENT_OF_WORK.md", "BUSINESS_CASE_AND_TCO.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "BUDGET.csv", "REQUIREMENTS_TRACEABILITY.csv", "INCIDENT_AND_ESCALATION_PLAN.md"),
        "03-new-robot-first-sale": ("ARTIFACT_INDEX.md", "BUSINESS_CASE.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "PRODUCT_ROADMAP.md", "SYSTEM_REQUIREMENTS_TRACEABILITY.csv", "COMMERCIAL_LAUNCH_PLAN.md"),
        "04-robotics-support-operations": ("ARTIFACT_INDEX.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "OPERATING_BASELINE_AND_COST_ASSUMPTIONS.md", "SERVICE_CATALOG.md", "TOOL_SELECTION_AND_COST.md", "OBSERVABILITY_AND_DATA_PLAN.md", "BUSINESS_CONTINUITY.md"),
    }
    for scenario, files in required.items():
        for name in files:
            path = ROOT / "scenarios" / scenario / name
            if not path.exists():
                errors.append(f"Missing scenario artifact: {path.relative_to(ROOT)}")


def check_recruiter_corrections(errors: list[str]) -> None:
    banned = (
        "Recruiter proof points",
        "not prior production",
        "not a claim of a production",
        "Truck-Unloading Deployment",
        "inside_truck_unloading",
        "within agreed latency",
        "within SLA",
        "contracted threshold",
    )
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".txt", ".csv", ".html", ".py"}:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for phrase in banned:
            if phrase.lower() in content.lower():
                errors.append(f"Stale recruiter-review phrase '{phrase}': {path.relative_to(ROOT)}")
    notice = "These simulations are fictitious generic scenarios for demonstration purposes only."
    index = DOCS / "index.html"
    if index.exists() and notice not in index.read_text(encoding="utf-8", errors="replace"):
        errors.append("Required scenario notice is missing from the generated home page")


def check_csv(errors: list[str]) -> None:
    for path in ROOT.rglob("*.csv"):
        if "docs" in path.parts:
            continue
        with path.open(newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.reader(handle))
        if not rows:
            errors.append(f"Empty CSV: {path.relative_to(ROOT)}")
            continue
        rows = [row for row in rows if any(cell.strip() for cell in row)]
        if not rows:
            errors.append(f"Empty CSV: {path.relative_to(ROOT)}")
            continue
        width = len(rows[0])
        for number, row in enumerate(rows[1:], 2):
            if len(row) != width:
                errors.append(f"CSV width mismatch: {path.relative_to(ROOT)} line {number}")


def check_media(errors: list[str], warnings: list[str]) -> None:
    manifest = ROOT / "media" / "videos" / "video_manifest.csv"
    with manifest.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        path = ROOT / "media" / "videos" / row["filename"]
        if row["status"].upper() == "READY" and not path.exists() and not row.get("hosting_url"):
            errors.append(f"Video marked READY but missing local file/URL: {row['video_id']}")
        if row["status"].upper() != "READY":
            warnings.append(f"Video still {row['status']}: {row['title']}")
    for path in ROOT.rglob("*"):
        if path.is_file() and path.stat().st_size > 50 * 1024 * 1024:
            errors.append(f"File exceeds 50 MB public-portfolio guardrail: {path.relative_to(ROOT)}")


def check_navigation(errors: list[str]) -> None:
    for path in DOCS.rglob("*.html"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "⌂ Home" not in text:
            errors.append(f"Generated page lacks explicit Home control: {path.relative_to(ROOT)}")
        if "← Back" not in text:
            errors.append(f"Generated page lacks explicit Back control: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    for required in (DOCS / "index.html", DOCS / "artifacts.html", ROOT / "governance" / "PUBLIC_ARTIFACT_REGISTER.csv"):
        if not required.exists():
            errors.append(f"Missing generated output: {required.relative_to(ROOT)}")
    check_site_links(errors)
    check_public_safety(errors, warnings)
    check_public_boundaries(errors)
    check_dashboards(errors)
    check_scenarios(errors)
    check_recruiter_corrections(errors)
    check_csv(errors)
    check_media(errors, warnings)
    check_navigation(errors)
    print(f"Validation summary: {len(errors)} error(s), {len(warnings)} warning(s)")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
