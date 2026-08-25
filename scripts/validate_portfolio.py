#!/usr/bin/env python3
"""Validate public portfolio safety, required artifacts, and generated-site links."""

from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IGNORED_PARTS = {".git", ".venv", ".render-venv", "__pycache__"}


def ignored(path: Path) -> bool:
    return any(part in IGNORED_PARTS for part in path.parts)


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
        if not path.is_file() or ignored(path) or path.suffix.lower() not in extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in blocked.items():
            if pattern.search(text):
                errors.append(f"Found {label}: {path.relative_to(ROOT)}")
    placeholders = []
    for path in ROOT.rglob("*"):
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.is_file() and not ignored(path) and path.suffix.lower() in extensions and "YOUR-GITHUB-USERNAME" in path.read_text(encoding="utf-8", errors="replace"):
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
        if not path.is_file() or ignored(path):
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
        "open-source-quadruped-raas-productization.html",
        "robotics-support-operations.html",
        "airport-restroom-humanoid-deployment.html",
    )
    for name in pages:
        path = DOCS / "scenarios" / name
        if not path.exists():
            errors.append(f"Missing scenario dashboard: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        expected = 9 if name == "airport-restroom-humanoid-deployment.html" else 8
        if text.count("data-tab-target=") != expected or text.count('class="dashboard-panel') != expected:
            errors.append(f"Dashboard is missing one or more required sections: {path.relative_to(ROOT)}")


def check_scenarios(errors: list[str]) -> None:
    required = {
        "01-humanoid-retail-backroom": ("ARTIFACT_INDEX.md", "STATEMENT_OF_WORK.md", "BUSINESS_CASE_AND_TCO.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "BUDGET.csv", "REQUIREMENTS_TRACEABILITY.csv", "CLOSEOUT_AND_BENEFITS.md"),
        "02-quadruped-security-deployment": ("ARTIFACT_INDEX.md", "STATEMENT_OF_WORK.md", "BUSINESS_CASE_AND_TCO.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "BUDGET.csv", "REQUIREMENTS_TRACEABILITY.csv", "INCIDENT_AND_ESCALATION_PLAN.md"),
        "03-open-source-quadruped-raas-productization": ("ARTIFACT_INDEX.md", "BUSINESS_CASE.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "PRODUCT_ROADMAP.md", "SYSTEM_REQUIREMENTS_TRACEABILITY.csv", "COMMERCIAL_LAUNCH_PLAN.md", "OPEN_SOURCE_COMPLIANCE_AND_SBOM.md", "RAAS_SERVICE_DESIGN.md"),
        "04-robotics-support-operations": ("ARTIFACT_INDEX.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "OPERATING_BASELINE_AND_COST_ASSUMPTIONS.md", "SERVICE_CATALOG.md", "TOOL_SELECTION_AND_COST.md", "OBSERVABILITY_AND_DATA_PLAN.md", "BUSINESS_CONTINUITY.md"),
        "05-airport-restroom-humanoid-deployment": ("ARTIFACT_INDEX.md", "CASE_STUDY.md", "INTEGRATED_PROGRAM_CHARTER.md", "STATEMENT_OF_WORK.md", "BUSINESS_CASE_AND_TCO.md", "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", "RESEARCH_AND_ASSUMPTIONS.md", "BUDGET.csv", "REQUIREMENTS_TRACEABILITY.csv", "SELLER_INTEGRATOR_PROJECT_PLAN.md", "MANUFACTURER_PROJECT_PLAN.md", "AIRPORT_OWNER_IMPLEMENTATION_PLAN.md", "SAFETY_QUALITY_AND_ACCEPTANCE_PLAN.md", "CLOSEOUT_AND_HANDOFF.md"),
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
        if not path.is_file() or ignored(path) or path.suffix.lower() not in {".md", ".txt", ".csv", ".html", ".py"}:
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
        if "docs" in path.parts or ignored(path):
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
        required_evidence = {"table_title", "evidence_class", "confidence", "source_or_validation"}
        missing_evidence = required_evidence - set(rows[0])
        if missing_evidence:
            errors.append(f"CSV missing table/evidence fields {sorted(missing_evidence)}: {path.relative_to(ROOT)}")
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
        if path.is_file() and not ignored(path) and path.stat().st_size > 50 * 1024 * 1024:
            errors.append(f"File exceeds 50 MB public-portfolio guardrail: {path.relative_to(ROOT)}")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load validation module: {path.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def check_retail_story(errors: list[str]) -> None:
    inbound = load_module(ROOT / "simulations" / "retail_inbound" / "retail_inbound_sequence.py", "retail_inbound_validation")
    orders = load_module(ROOT / "simulations" / "retail_humanoids" / "retail_sequence.py", "retail_order_validation")
    inbound_report = inbound.route_validation_report()
    order_report = orders.route_clearance_report()
    for key, value in inbound_report.items():
        if isinstance(value, bool) and not value:
            errors.append(f"Retail inbound validation failed: {key}")
    for key, value in order_report.items():
        if isinstance(value, bool) and not value:
            errors.append(f"Retail order-picking validation failed: {key}")

    data = json.loads((ROOT / "portfolio" / "scenario_dashboard_data.json").read_text(encoding="utf-8"))
    if data.get("capability_demos"):
        errors.append("Standalone capability card remains after retail-story consolidation")
    retail_demo = data["scenarios"][0]["demo"]
    required_copy = ("Unload truck", "raised racks", "courtesy drop-off table", "service window")
    searchable = f"{retail_demo.get('caption', '')} {' '.join(retail_demo.get('sequence', []))}".lower()
    for phrase in required_copy:
        if phrase.lower() not in searchable:
            errors.append(f"Retail dashboard is missing required workflow copy: {phrase}")

    with (ROOT / "media" / "videos" / "video_manifest.csv").open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    retail_rows = [row for row in rows if row.get("video_id") == "retail"]
    if len(retail_rows) != 1 or retail_rows[0].get("duration_target_seconds") != "40":
        errors.append("Retail video manifest must contain one 40-second composed story")
    if any(row.get("video_id") == "warehouse" for row in rows):
        errors.append("Standalone loading capability remains in the video manifest")


def check_navigation(errors: list[str]) -> None:
    for path in DOCS.rglob("*.html"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "⌂ Home" not in text:
            errors.append(f"Generated page lacks explicit Home control: {path.relative_to(ROOT)}")
        if "← Back" not in text:
            errors.append(f"Generated page lacks explicit Back control: {path.relative_to(ROOT)}")


def check_rebuild_acceptance(errors: list[str]) -> None:
    searchable = {".md", ".txt", ".csv", ".html", ".json", ".py", ".bat"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ignored(path) or path.suffix.lower() not in searchable:
            continue
        if path.resolve() == Path(__file__).resolve() or "docs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if re.search(r"\bAD-?01\b|ad01-new-robot|new_robot_npi|03-new-robot-first-sale", text, re.I):
            errors.append(f"Retired AD-01 reference remains: {path.relative_to(ROOT)}")
    for obsolete in (
        ROOT / "scenarios" / "03-new-robot-first-sale",
        ROOT / "simulations" / "new_robot_npi",
        ROOT / "simulations" / "support_lab",
        ROOT / "simulations" / "warehouse_capability",
        ROOT / "media" / "videos" / "ad01-new-robot-npi.mp4",
        ROOT / "media" / "videos" / "warehouse-palletizing-truck-loading.mp4",
    ):
        if obsolete.exists():
            errors.append(f"Retired path remains: {obsolete.relative_to(ROOT)}")

    support_paths = [
        ROOT / "scenarios" / "04-robotics-support-operations",
        ROOT / "tools" / "support-operations-lab",
    ]
    for base in support_paths:
        for path in base.rglob("*") if base.exists() else []:
            if path.is_file() and path.suffix.lower() in searchable:
                text = path.read_text(encoding="utf-8", errors="replace")
                if "mujoco" in text.lower() and "no mujoco" not in text.lower():
                    errors.append(f"Support case still depends on MuJoCo: {path.relative_to(ROOT)}")
    data = json.loads((ROOT / "portfolio" / "scenario_dashboard_data.json").read_text(encoding="utf-8"))
    for scenario in data["scenarios"]:
        for item in (*scenario.get("metrics", []), *scenario.get("financials", [])):
            if not item.get("evidence_class") or not item.get("confidence"):
                errors.append(f"Dashboard item lacks evidence/confidence: {scenario['slug']} -> {item.get('label')}")
    support = data["scenarios"][3]
    if "mujoco" in json.dumps(support.get("demo", {})).lower():
        errors.append("Support dashboard demo still claims MuJoCo")


def check_table_titles_and_evidence(errors: list[str]) -> None:
    source_roots = ("scenarios", "governance", "tools", "portfolio", "simulations", "pm-operating-system", "quality-control")
    for root_name in source_roots:
        base = ROOT / root_name
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            if not any("Evidence-confidence key" in line for line in lines[:14]):
                errors.append(f"Markdown lacks evidence-confidence key: {path.relative_to(ROOT)}")
            for index, line in enumerate(lines):
                if not line.startswith("|") or index + 1 >= len(lines) or not re.match(r"^\|?\s*:?-{3,}", lines[index + 1]):
                    continue
                previous = index - 1
                while previous >= 0 and not lines[previous].strip():
                    previous -= 1
                title = lines[previous].strip() if previous >= 0 else ""
                if not re.match(r"^\*\*Table\s+", title, re.I):
                    errors.append(f"Markdown table lacks title immediately above it: {path.relative_to(ROOT)} line {index + 1}")
                elif "evidence" not in title.lower() or "confidence" not in title.lower():
                    errors.append(f"Markdown table title lacks evidence/confidence: {path.relative_to(ROOT)} line {index + 1}")
    for page in DOCS.rglob("*.html"):
        text = page.read_text(encoding="utf-8", errors="replace")
        if text.count("<table") > text.count('class="table-title"'):
            errors.append(f"Generated table lacks a visible title above it: {page.relative_to(ROOT)}")


def check_operating_system_and_qc(errors: list[str]) -> None:
    required = (
        "pm-operating-system/README.md",
        "pm-operating-system/word/ROBOTICS_PROGRAM_BRIEF.docx",
        "pm-operating-system/word/STAGE_GATE_DECISION_MEMO.docx",
        "pm-operating-system/word/WEEKLY_EXECUTIVE_STATUS.docx",
        "pm-operating-system/word/SITE_ACCEPTANCE_TEST_PLAN.docx",
        "pm-operating-system/excel/ROBOTICS_PM_OPERATING_SYSTEM.xlsx",
        "pm-operating-system/csv/RAID_REGISTER.csv",
        "pm-operating-system/csv/REQUIREMENTS_TRACEABILITY.csv",
        "pm-operating-system/csv/INTEGRATED_MASTER_SCHEDULE.csv",
        "pm-operating-system/csv/BUDGET_TCO.csv",
        "pm-operating-system/csv/BENEFITS_REGISTER.csv",
        "pm-operating-system/csv/EVIDENCE_REGISTER.csv",
        "pm-operating-system/ai/AI_WORKFLOW_PLAYBOOK.md",
        "quality-control/CLAUDE_QC_PACKAGE.zip",
        "quality-control/GROK_QC_PACKAGE.zip",
    )
    for item in required:
        path = ROOT / item
        if not path.exists() and item.startswith("quality-control/") and item.endswith("_QC_PACKAGE.zip"):
            # The published, reusable package is intentionally stored in the
            # generated download tree to avoid a second multi-megabyte binary
            # copy in the source directory.
            published = DOCS / "downloads" / "source" / item
            if published.exists() and published.stat().st_size:
                continue
        if not path.exists() or (path.is_file() and path.stat().st_size == 0):
            errors.append(f"Missing reusable operating-system/QC deliverable: {item}")

    for batch in ("RUN_RETAIL_DEMO_WINDOWS.bat", "RENDER_RETAIL_VIDEO_WINDOWS.bat", "RUN_SUPPORT_WORKFLOW_WINDOWS.bat", "VALIDATE_PORTFOLIO_WINDOWS.bat"):
        path = ROOT / batch
        if not path.exists():
            errors.append(f"Missing Windows workflow: {batch}")
        elif "%~dp0" not in path.read_text(encoding="utf-8", errors="replace"):
            errors.append(f"Windows workflow is not repository-relative: {batch}")


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
    check_retail_story(errors)
    check_navigation(errors)
    check_rebuild_acceptance(errors)
    check_table_titles_and_evidence(errors)
    check_operating_system_and_qc(errors)
    print(f"Validation summary: {len(errors)} error(s), {len(warnings)} warning(s)")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
