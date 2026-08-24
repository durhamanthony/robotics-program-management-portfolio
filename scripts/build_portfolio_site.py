#!/usr/bin/env python3
"""Build the public GitHub Pages portfolio from completed scenario evidence."""

from __future__ import annotations

import csv
import html
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LIBRARY = DOCS / "library"
DOWNLOADS = DOCS / "downloads" / "source"
DATA_FILE = ROOT / "portfolio" / "scenario_dashboard_data.json"
SOURCE_DIRS = ("scenarios", "tools", "pm-operating-system", "quality-control")
SOURCE_FILES = (
    "portfolio/EXECUTIVE_PORTFOLIO.md",
    "simulations/README.md",
    "simulations/retail_humanoids/README.md",
    "simulations/quadruped_security/README.md",
    "simulations/open_quadruped_raas/README.md",
    "tools/support-operations-lab/README.md",
    "simulations/restroom_cleaning/README.md",
    "simulations/warehouse_capability/README.md",
)
GOVERNANCE_FILES = (
    "governance/README.md",
    "governance/PROGRAM_MANAGEMENT_PLAN.md",
    "governance/QUALITY_MANAGEMENT_PLAN.md",
    "governance/COMMUNICATIONS_AND_MEETING_PLAN.md",
    "governance/RESOURCE_AND_CAPACITY_PLAN.md",
    "governance/PROCUREMENT_VENDOR_MANAGEMENT.md",
    "governance/CHANGE_CONFIGURATION_CONTROL.md",
    "governance/CYBERSECURITY_DATA_GOVERNANCE.md",
    "governance/TRAINING_CHANGE_ADOPTION.md",
    "governance/BENEFITS_AND_CLOSEOUT.md",
    "governance/NUMBER_ASSURANCE_AND_EVIDENCE_RULES.md",
    "governance/FINANCIAL_EVIDENCE_CLASSIFICATION.md",
)


def evidence_legend() -> str:
    return """<div class="evidence-box" role="note" aria-label="How to interpret portfolio numbers">
<div><strong>How to read these numbers</strong><p>Financial figures are planning-grade unless explicitly identified as an actual result or binding quotation.</p></div>
<div class="evidence-grid">
<span class="evidence-item evidence-public"><b>Public benchmark</b> Published external reference used only as a reasonableness check.</span>
<span class="evidence-item evidence-estimate"><b>Research-based estimate</b> Best estimate informed by published evidence, but not customer- or vendor-confirmed.</span>
<span class="evidence-item evidence-assumption"><b>Scenario assumption</b> Fictional input selected to make the demonstration model complete.</span>
<span class="evidence-item evidence-derived"><b>Derived calculation</b> Reproducible arithmetic calculated from identified inputs.</span>
<span class="evidence-item evidence-unknown"><b>Unknown / pending validation</b> Requires a time study, customer data, competitive quote, or contract.</span>
</div><p><b>Confidence:</b> High = authoritative source or controlled fact; Medium = reasoned estimate/control design; Low = fictional or unvalidated scenario input. A calculation inherits its least-certain material input.</p></div>"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def esc(value: object) -> str:
    return html.escape(str(value))


def title_for(path: Path) -> str:
    if path.suffix.lower() == ".md":
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return path.stem.replace("_", " ").replace("-", " ").title()


def lifecycle_for(name: str) -> str:
    key = name.lower()
    mapping = (
        (("charter", "business_case", "statement_of_work", "customer_discovery", "case_study"), "Initiate / Discover"),
        (("product_brief", "requirements", "roadmap", "architecture", "site_readiness", "integration"), "Plan / Design"),
        (("schedule", "budget", "raci", "raid", "resource", "procurement", "supplier"), "Plan / Control"),
        (("deployment", "training", "status", "runbook", "communication"), "Execute / Deploy"),
        (("safety", "privacy", "quality", "verification", "acceptance", "cybersecurity", "security"), "Assure / Validate"),
        (("support", "service", "incident", "diagnostic", "observability", "rma", "continuity", "knowledge"), "Operate / Support"),
        (("handoff", "closeout", "benefits", "lessons", "maturity"), "Close / Learn"),
    )
    for words, phase in mapping:
        if any(word in key for word in words):
            return phase
    return "Govern / Reference"


def scenario_name(path: Path) -> str:
    rel = path.relative_to(ROOT)
    if rel.parts[0] != "scenarios":
        return "Portfolio controls"
    return {
        "01-humanoid-retail-backroom": "Case 01 — Retail backroom",
        "02-quadruped-security-deployment": "Case 02 — Security",
        "03-open-source-quadruped-raas-productization": "Case 03 — Open-source RaaS productization",
        "04-robotics-support-operations": "Case 04 — Support",
        "05-airport-restroom-humanoid-deployment": "Case 05 — Airport restroom",
    }.get(rel.parts[1], rel.parts[1])


def collect_sources() -> list[Path]:
    paths: set[Path] = set()
    for directory in SOURCE_DIRS:
        base = ROOT / directory
        if base.exists():
            paths.update(p for p in base.rglob("*") if p.suffix.lower() in {".md", ".csv"})
    for item in (*SOURCE_FILES, *GOVERNANCE_FILES):
        path = ROOT / item
        if path.exists():
            paths.add(path)
    return sorted(paths, key=lambda p: (scenario_name(p), str(p.relative_to(ROOT)).lower()))


def build_register(paths: list[Path]) -> None:
    register = ROOT / "governance" / "PUBLIC_ARTIFACT_REGISTER.csv"
    rows = []
    for index, path in enumerate(paths, 1):
        rel = path.relative_to(ROOT).as_posix()
        rows.append({
            "artifact_id": f"PUB-{index:03d}",
            "scenario": scenario_name(path),
            "lifecycle": lifecycle_for(path.name),
            "artifact": title_for(path),
            "path": rel,
            "status": "Completed scenario evidence",
            "owner": "Program Manager",
            "public_safe": "Yes",
            "table_title": "Public artifact register",
            "evidence_class": "Derived calculation",
            "confidence": "High",
            "source_or_validation": "Generated from the repository source inventory",
        })
    register.parent.mkdir(parents=True, exist_ok=True)
    with register.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_fragment(path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm", "--to=html5", "--wrap=none", str(path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    fragment = re.sub(
        r'href="([^"?#]+)\.(?:md|csv)([?#][^"]*)?"',
        lambda match: f'href="{match.group(1)}.html{match.group(2) or ""}"',
        result.stdout,
        flags=re.IGNORECASE,
    )
    return re.sub(
        r"<p><strong>(Table\s+[^<]+)</strong></p>\s*(?=<table>)",
        r'<p class="table-title"><strong>\1</strong></p>',
        fragment,
        flags=re.IGNORECASE,
    )


def csv_fragment(path: Path) -> str:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return "<p>No rows.</p>"
    headers = rows[0]
    title = title_for(path)
    if "table_title" in headers:
        title_index = headers.index("table_title")
        if len(rows) > 1 and title_index < len(rows[1]) and rows[1][title_index].strip():
            title = rows[1][title_index].strip()
        headers = [cell for index, cell in enumerate(headers) if index != title_index]
        rows = [rows[0]] + [[cell for index, cell in enumerate(row) if index != title_index] for row in rows[1:]]
    head = "".join(f"<th>{esc(cell)}</th>" for cell in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{esc(cell)}</td>" for cell in row) + "</tr>"
        for row in rows[1:]
    )
    return f'<p class="table-title"><strong>{esc(title)}</strong></p><div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def shell(title: str, body: str, depth: int = 0, description: str = "") -> str:
    prefix = "../" * depth
    desc = esc(description or "Robotics deployment, new-product introduction, and service-operations portfolio by Anthony Durham.")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | Anthony Durham</title><meta name="description" content="{desc}">
<link rel="stylesheet" href="{prefix}styles.css"><script defer src="{prefix}app.js"></script></head><body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><nav class="nav" aria-label="Primary"><a class="brand" href="{prefix}index.html">Anthony Durham</a>
<div class="nav-actions"><button class="nav-back" type="button" data-go-back data-fallback="{prefix}index.html">← Back</button>
<div class="nav-links"><a class="home-link" href="{prefix}index.html">⌂ Home</a><a href="{prefix}index.html#cases">Scenarios</a><a href="{prefix}artifacts.html">Artifacts</a><a href="{prefix}videos.html">Demos</a><a href="{prefix}about.html">About</a></div></div></nav></header>
{body}
<footer><div class="container"><strong>Anthony Durham — Robotics Program Leadership</strong><br>
These simulations are fictitious generic scenarios for demonstration purposes only. <a href="https://www.linkedin.com/in/anthonydurham">LinkedIn</a></div></footer>
</body></html>"""


def page_for_source(path: Path) -> tuple[Path, str]:
    rel = path.relative_to(ROOT)
    out = LIBRARY / rel.with_suffix(".html")
    depth = len(out.relative_to(DOCS).parents) - 1
    raw = DOWNLOADS / rel
    raw.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, raw)
    raw_link = Path(*([".."] * depth), "downloads", "source", *rel.parts).as_posix()
    scenario_returns = {
        "01-humanoid-retail-backroom": "retail-humanoid-backroom",
        "02-quadruped-security-deployment": "quadruped-security-deployment",
        "03-open-source-quadruped-raas-productization": "open-source-quadruped-raas-productization",
        "04-robotics-support-operations": "robotics-support-operations",
        "05-airport-restroom-humanoid-deployment": "airport-restroom-humanoid-deployment",
    }
    if rel.parts[0] == "scenarios" and len(rel.parts) > 1 and rel.parts[1] in scenario_returns:
        return_link = Path(*([".."] * depth), "scenarios", f"{scenario_returns[rel.parts[1]]}.html").as_posix() + "#artifacts"
        return_label = "← Back to scenario artifacts"
    else:
        return_link = Path(*([".."] * depth), "artifacts.html").as_posix()
        return_label = "← Back to artifact library"
    fragment = markdown_fragment(path) if path.suffix.lower() == ".md" else csv_fragment(path)
    body = f"""<main id="main" class="container"><div class="artifact-tools"><div class="artifact-context"><a class="context-back" href="{return_link}">{return_label}</a><div><span class="tag">{esc(scenario_name(path))}</span> <span class="tag muted-tag">{esc(lifecycle_for(path.name))}</span></div></div>
<div class="artifact-actions"><a class="button secondary-light" href="{Path(*([".."] * depth), "index.html").as_posix()}">⌂ Home</a><a class="button" href="{raw_link}" download>Download {esc(path.suffix.upper()[1:])}</a></div></div>
<article class="article">{fragment}</article></main>"""
    return out, shell(title_for(path), body, depth=depth)


def artifact_url(source_path: str, dashboard_depth: int = 1) -> str:
    source = Path(source_path)
    rel = source if source.suffix.lower() in {".docx", ".xlsx", ".zip", ".json", ".txt"} else source.with_suffix(".html")
    return "../" * dashboard_depth + (Path("library") / rel).as_posix()


def metric_cards(scenario: dict) -> str:
    return "".join(
        f'<article class="kpi-card {esc(item.get("state", ""))}"><span>{esc(item["label"])}</span><strong>{esc(item["value"])}</strong><small>{esc(item["note"])}</small><em class="evidence-meta">{esc(item.get("evidence_class", "Unknown"))} · {esc(item.get("confidence", "Open"))} confidence</em></article>'
        for item in scenario["metrics"]
    )


def gantt(scenario: dict) -> str:
    max_value = scenario["timeline_max"]
    rows = []
    for phase in scenario["phases"]:
        left = ((phase["start"] - 1) / max_value) * 100
        width = max(((phase["end"] - phase["start"] + 1) / max_value) * 100, 2.5)
        rows.append(f"""<div class="gantt-row"><div class="gantt-label"><strong>{esc(phase['name'])}</strong><small>{esc(scenario['timeline_unit'])} {phase['start']}–{phase['end']} · {esc(phase['status'])}</small></div>
<div class="gantt-track" aria-label="{esc(phase['name'])}: {esc(scenario['timeline_unit'])} {phase['start']} through {phase['end']}"><span style="left:{left:.2f}%;width:{width:.2f}%"></span></div></div>""")
    ticks = "".join(
        f"<span>{n}</span>" for n in range(1, max_value + 1) if n == 1 or n == max_value or n % max(1, max_value // 6) == 0
    )
    return f'<div class="gantt-scale"><span>{esc(scenario["timeline_unit"])}</span><div>{ticks}</div></div><div class="gantt">{"".join(rows)}</div>'


def financial_chart(scenario: dict) -> str:
    highest = max(item["value"] for item in scenario["financials"])
    rows = []
    for item in scenario["financials"]:
        width = max((item["value"] / highest) * 100, 3)
        rows.append(f"""<div class="finance-row"><div><span>{esc(item['label'])}</span><strong>{esc(item['display'])}</strong><em class="evidence-meta">{esc(item.get('evidence_class', 'Unknown'))} · {esc(item.get('confidence', 'Open'))} confidence</em></div><div class="finance-track"><span style="width:{width:.2f}%"></span></div></div>""")
    return "".join(rows)


def risk_rows(scenario: dict) -> str:
    return "".join(
        f'<tr><td><strong>{esc(item["id"])}</strong></td><td>{esc(item["risk"])}</td><td><span class="risk-score score-{("high" if item["score"] >= 15 else "medium")}">{item["score"]}</span></td><td>{esc(item["status"])}</td><td>{esc(item["response"])}</td></tr>'
        for item in scenario["risks"]
    )


def artifact_cards(scenario: dict) -> str:
    return "".join(
        f'<a class="artifact-card" href="{artifact_url(item["path"])}"><span>{esc(item["category"])}</span><strong>{esc(item["label"])}</strong><small>Open completed artifact →</small></a>'
        for item in scenario["artifacts"]
    )


def demo_markup(scenario: dict) -> str:
    source = ROOT / "media" / "videos" / scenario["demo"]["filename"]
    if source.exists():
        target = DOCS / "media" / "videos" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        player = f'<video controls preload="metadata"><source src="../media/videos/{esc(source.name)}" type="video/mp4">Your browser does not support embedded video.</video>'
    else:
        player = '<div class="video-placeholder"><span>Demo recording in production</span><strong>No terminal or software installation is required.</strong><p>The final MP4 will play directly in this panel.</p></div>'
    steps = "".join(f'<li><span>{i}</span>{esc(step)}</li>' for i, step in enumerate(scenario["demo"]["sequence"], 1))
    model_link = artifact_url(scenario["demo"]["model_source"])
    evidence_type = scenario["demo"].get("type", "MuJoCo operations visualization")
    link_label = "Open workflow lab notes" if "workflow" in evidence_type.lower() else "Open MuJoCo model notes"
    return f'<div class="demo-grid"><div>{player}</div><div><span class="tag">{esc(evidence_type)}</span><h3>{esc(scenario["demo"]["title"])}</h3><p>{esc(scenario["demo"]["caption"])}</p><p><a href="{model_link}">{esc(link_label)} →</a></p><ol class="sequence">{steps}</ol></div></div>'


def build_dashboard(scenario: dict) -> None:
    team = "".join(f'<article><strong>{esc(item["role"])}</strong><p>{esc(item["accountability"])}</p></article>' for item in scenario["team"])
    perspectives = scenario.get("perspectives", [])
    perspective_tab = '<button data-tab-target="perspectives">Three PM Views</button>' if perspectives else ""
    perspective_cards = "".join(
        f'<article><span class="panel-kicker">Accountable decision</span><h3>{esc(item["name"])}</h3><p><strong>{esc(item["decision"])}</strong></p><p>{esc(item["outcome"])}</p><p><a href="{artifact_url(item["artifact"])}">Open completed Project Manager plan →</a></p></article>'
        for item in perspectives
    )
    perspective_panel = (
        f'<section id="perspectives" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Three accountable delivery viewpoints</span><h2>Seller, manufacturer, and airport Project Manager decisions</h2></div></div><p class="section-intro">One integrated program, with separate contractual, product-release, and owner-operator accountabilities. Each card links to a completed plan with its own budget, schedule, risks, acceptance evidence, and handoff.</p><div class="team-grid">{perspective_cards}</div></section>'
        if perspectives else ""
    )
    accept = "".join(f"<li>{esc(item)}</li>" for item in scenario["closure"]["acceptance"])
    lessons = "".join(f"<li>{esc(item)}</li>" for item in scenario["closure"]["lessons"])
    body = f"""<main id="main">
<section class="scenario-hero"><div class="container"><div class="scenario-links"><a class="back-link" href="../index.html#cases">← All scenarios</a><a class="back-link" href="../index.html">⌂ Home</a></div><div class="scenario-eyebrow">{esc(scenario['code'])} · {esc(scenario['program_type'])}</div>
<h1>{esc(scenario['title'])}</h1><p class="lead">{esc(scenario['client'])} · {esc(scenario['role'])}</p>
<div class="status-row"><span class="status status-{esc(scenario['health'].lower())}">{esc(scenario['status'])}</span><span>{esc(scenario['duration'])}</span><span>{esc(scenario['budget'])}</span><span>{esc(scenario['tco'])}</span></div></div></section>
<div class="dashboard-nav-wrap"><nav class="dashboard-nav container" aria-label="Scenario sections">
<button class="active" data-tab-target="overview">Overview</button><button data-tab-target="schedule">Schedule</button><button data-tab-target="financials">Financials</button><button data-tab-target="risks">Risks</button><button data-tab-target="team">Team</button>{perspective_tab}<button data-tab-target="artifacts">Artifacts</button><button data-tab-target="demo">Demo</button><button data-tab-target="closeout">Closeout</button>
</nav></div>
<div class="container dashboard-shell">
<section id="overview" class="dashboard-panel active"><div class="panel-heading"><div><span class="panel-kicker">Executive view</span><h2>Program outcome and acceptance</h2></div><span class="health health-{esc(scenario['health'].lower())}">{esc(scenario['health'])}</span></div>
<div class="overview-grid"><article class="summary-card"><h3>Scope</h3><p>{esc(scenario['summary'])}</p></article><article class="decision-card"><h3>Closeout decision</h3><p>{esc(scenario['decision'])}</p></article></div>
<div class="kpi-grid">{metric_cards(scenario)}</div></section>
<section id="schedule" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Integrated plan</span><h2>Schedule and stage gates</h2></div><span class="tag">{esc(scenario['duration'])}</span></div>{gantt(scenario)}</section>
<section id="financials" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Decision economics</span><h2>Budget and Total Cost of Ownership</h2></div></div>{evidence_legend()}<div class="finance-chart">{financial_chart(scenario)}</div><div class="callout"><strong>Decision rule and confidence limits</strong><p>{esc(scenario['financial_note'])}</p></div></section>
<section id="risks" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Program controls</span><h2>Top risks and disposition</h2></div></div><p class="table-title"><strong>Table: Top scenario risks and closeout controls</strong></p><div class="table-wrap"><table><thead><tr><th>ID</th><th>Risk</th><th>Score</th><th>Closeout status</th><th>Response / control</th></tr></thead><tbody>{risk_rows(scenario)}</tbody></table></div></section>
<section id="team" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Governance</span><h2>Accountability and delivery team</h2></div></div><div class="team-grid">{team}</div><p class="caption">Detailed Responsible, Accountable, Consulted, and Informed assignments are available in the scenario artifact package.</p></section>
{perspective_panel}
<section id="artifacts" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Completed evidence</span><h2>Project and program artifacts</h2></div><span class="tag">{len(scenario['artifacts'])} highlighted</span></div><p class="section-intro">These are completed scenario documents—not empty templates. Open a rendered page or download its source file.</p><div class="artifact-grid">{artifact_cards(scenario)}</div></section>
<section id="demo" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Visual evidence</span><h2>Browser-playable operations evidence</h2></div></div>{demo_markup(scenario)}</section>
<section id="closeout" class="dashboard-panel"><div class="panel-heading"><div><span class="panel-kicker">Formal closure</span><h2>Acceptance, handoff, and lessons</h2></div></div><div class="closure-summary"><article><span>Schedule</span><strong>{esc(scenario['closure']['schedule'])}</strong></article><article><span>Budget</span><strong>{esc(scenario['closure']['budget'])}</strong></article></div><div class="two-columns"><article><h3>Acceptance and handoff evidence</h3><ul class="check-list">{accept}</ul></article><article><h3>Lessons carried forward</h3><ul>{lessons}</ul></article></div></section>
</div></main>"""
    write(DOCS / "scenarios" / f"{scenario['slug']}.html", shell(scenario["title"], body, depth=1, description=scenario["summary"]))


def build_index(data: dict, count: int) -> None:
    scenario_count = len(data["scenarios"])
    cards = []
    for scenario in data["scenarios"]:
        metric = scenario["metrics"][0]
        cards.append(f"""<article class="case-card"><div class="case-top"><span>{esc(scenario['code'])}</span><span class="health health-{esc(scenario['health'].lower())}">{esc(scenario['health'])}</span></div><h3>{esc(scenario['title'])}</h3><p>{esc(scenario['summary'])}</p><div class="case-facts"><span>{esc(scenario['duration'])}</span><span>{esc(scenario['budget'])}</span><span>{esc(metric['label'])}: {esc(metric['value'])}</span></div><a class="card-link" href="scenarios/{esc(scenario['slug'])}.html">Open program dashboard →</a></article>""")
    body = f"""<section class="hero"><div class="hero-grid"><div><div class="eyebrow">Robotics deployment · product introduction · service operations</div>
<h1>Turning complex robotics into reliable operations.</h1><p class="lead">A project and program management portfolio showing how Anthony Durham turns a robotics concept or customer order into a governed, measurable operating outcome.</p>
<div class="button-row"><a class="button" href="#cases">Explore {scenario_count} scenarios</a><a class="button secondary" href="artifacts.html">Open completed artifacts</a></div></div>
<img class="hero-photo" src="media/images/anthony-cstu-humanoid.jpeg" alt="Anthony Durham beside a humanoid robot during hands-on robotics training"></div></section>
<main id="main" class="container"><section><h2>Enterprise experience applied to robotics</h2><div class="metrics"><div class="metric"><strong>45 people</strong><span>Five-team technology portfolio</span></div><div class="metric"><strong>$14M</strong><span>Portfolio financial ownership</span></div><div class="metric"><strong>37,000</strong><span>Endpoints scaled from about 1,000</span></div><div class="metric"><strong>$2M</strong><span>Annual savings delivered</span></div></div></section>
<section id="cases"><div class="section-heading"><div><span class="panel-kicker">Portfolio work</span><h2>{scenario_count} complete operating scenarios</h2></div><span class="tag">{count} public artifacts</span></div><div class="truth-banner">{esc(data['portfolio_notice'])}</div>{evidence_legend()}<p class="section-intro">Each scenario opens to a decision-oriented dashboard with scope, status, schedule, financials, risks, team accountability, browser-playable operations evidence, completed artifacts, and formal closeout.</p><div class="case-grid">{''.join(cards)}</div></section>
<section class="how-section"><div><span class="panel-kicker">How to review</span><h2>One operating story, with evidence behind every decision</h2></div><div class="review-steps"><article><span>01</span><strong>Open a dashboard</strong><p>See the executive outcome, current status, cost, schedule, and acceptance results.</p></article><article><span>02</span><strong>Inspect the evidence</strong><p>Open completed charters, schedules, budgets, risks, requirements, acceptance plans, and closeout records.</p></article><article><span>03</span><strong>Watch or run evidence</strong><p>Play browser videos or inspect the data-only support workflow; no terminal is required for website review.</p></article></div></section></main>"""
    write(DOCS / "index.html", shell("Robotics Program Management Portfolio", body))


def build_artifact_page(paths: list[Path]) -> None:
    items = []
    for path in paths:
        rel = path.relative_to(ROOT)
        url = (Path("library") / rel.with_suffix(".html")).as_posix()
        title = title_for(path)
        search = esc(f"{title} {rel} {lifecycle_for(path.name)} {scenario_name(path)}".lower())
        items.append(f'<article class="artifact-item" data-search="{search}"><div><span class="tag">{esc(scenario_name(path))}</span><span class="tag muted-tag">{esc(lifecycle_for(path.name))}</span></div><h3><a href="{url}">{esc(title)}</a></h3><p>{esc(rel.as_posix())}</p></article>')
    body = f"""<main id="main" class="container"><section class="page-intro"><div class="eyebrow dark">Completed evidence library</div><h1>Project, program, product, and service artifacts</h1>
<p class="section-intro">Search {len(paths)} completed scenario documents, reusable PM operating-system tools, quality-control packages, and supporting program controls. Internal career materials and publishing instructions are excluded.</p>
<input id="artifact-search" class="search" type="search" placeholder="Search by scenario, artifact, phase, or file" aria-label="Search artifacts"></section>
<section class="artifact-list" id="artifact-list">{''.join(items)}</section></main>"""
    write(DOCS / "artifacts.html", shell("Completed Artifact Library", body))


def build_about(scenario_count: int) -> None:
    body = f"""<main id="main" class="container"><article class="article about-article"><div class="eyebrow dark">About Anthony Durham</div><h1>Program leadership at the boundary of technology and operations</h1>
<p>Anthony led a 45-person, five-team Walmart technology portfolio spanning engineering, Level 2 support, remote-support tools, telemetry, and call-center technology. He managed a $14 million portfolio, delivered $2 million in annual savings, scaled a platform from approximately 1,000 to 37,000 endpoints, and supported telemetry strategy across 300,000 Windows devices.</p>
<p>He is applying that experience to robotics deployment and service operations through hands-on robotics training, advanced online coursework, Project Management Professional exam preparation, and the {scenario_count} operating scenarios in this portfolio.</p>
<h2>Robotics and project-management development</h2><ul><li>CSTU and Robofix five-day hands-on robotics bootcamp — completed August 2026.</li><li>Mangates Learn Robotics one-day hands-on training — completed July 30, 2026; eight professional development units.</li><li>AI Robotics Edu Advanced Robotics Training with Ray Tang, PhD — ten-week online program in progress.</li><li>Project Management Academy Project Management Professional exam-preparation course — completed; exam preparation in progress.</li></ul>
<h2>Recent AI project work</h2><p>Mercor — AI Data Annotation Contributor / IT Management Subject Matter Expert, December 2025–January 2026. Assigned contributor applying IT-management expertise to confidential evaluation scenarios and image-labeling work.</p>
<p><a class="button" href="https://www.linkedin.com/in/anthonydurham">View LinkedIn profile</a></p></article></main>"""
    write(DOCS / "about.html", shell("About", body))


def build_videos(data: dict) -> None:
    cards = []
    entries = [
        {
            "code": scenario["code"],
            "title": scenario["demo"]["title"],
            "caption": scenario["demo"]["caption"],
            "filename": scenario["demo"]["filename"],
            "href": f'scenarios/{scenario["slug"]}.html#demo',
            "model_source": scenario["demo"]["model_source"],
            "type": scenario["demo"].get("type", "MuJoCo operations visualization"),
            "label": "Open case dashboard",
        }
        for scenario in data["scenarios"]
    ] + data.get("capability_demos", [])
    for entry in entries:
        source = ROOT / "media" / "videos" / entry["filename"]
        if source.exists():
            target = DOCS / "media" / "videos" / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            media = f'<video controls preload="metadata"><source src="media/videos/{esc(source.name)}" type="video/mp4">Your browser does not support embedded video.</video>'
        else:
            media = '<div class="video-placeholder compact"><span>Recording in production</span><strong>Browser playback will appear here.</strong></div>'
        model_url = (Path("library") / Path(entry["model_source"]).with_suffix(".html")).as_posix()
        links = f'<a href="{esc(entry["href"])}">{esc(entry["label"])} →</a>'
        if entry["href"] != model_url:
            note_label = "Workflow lab notes" if "workflow" in entry.get("type", "").lower() else "MuJoCo model notes"
            links += f' · <a href="{esc(model_url)}">{esc(note_label)} →</a>'
        cards.append(f'<article class="demo-card">{media}<div><span class="panel-kicker">{esc(entry["code"])} · {esc(entry.get("type", "Operations visualization"))}</span><h2>{esc(entry["title"])}</h2><p>{esc(entry["caption"])}</p><p>{links}</p></div></article>')
    body = f"""<main id="main" class="container"><section class="page-intro"><div class="eyebrow dark">Visual evidence</div><h1>Robotics Operations Evidence Gallery</h1><p class="section-intro">The gallery contains scripted physics-simulator operations visualizations plus a data-workflow support animation. Simulator clips are not learned locomotion, grasp-performance validation, certified controls, or vendor digital twins. The support workflow uses synthetic event data and never authorizes robot action. Recruiters can play every clip directly in the browser.</p></section><section class="demo-list">{''.join(cards)}</section></main>"""
    write(DOCS / "videos.html", shell("Robotics Operations Evidence Gallery", body))


def copy_binary_assets() -> None:
    allowed = {".docx", ".xlsx", ".zip", ".json", ".txt"}
    for directory in ("scenarios", "pm-operating-system", "quality-control"):
        base = ROOT / directory
        if not base.exists():
            continue
        for source in base.rglob("*"):
            if not source.is_file() or source.suffix.lower() not in allowed:
                continue
            rel = source.relative_to(ROOT)
            for target_root in (LIBRARY, DOWNLOADS):
                target = target_root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    LIBRARY.mkdir(parents=True)
    DOWNLOADS.mkdir(parents=True)
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    paths = collect_sources()
    build_register(paths)
    for path in paths:
        out, content = page_for_source(path)
        write(out, content)
    copy_binary_assets()
    shutil.copy2(ROOT / "site" / "styles.css", DOCS / "styles.css")
    shutil.copy2(ROOT / "site" / "app.js", DOCS / "app.js")
    for image in (ROOT / "media" / "images").glob("*"):
        if image.is_file() and image.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            target = DOCS / "media" / "images" / image.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(image, target)
    write(DOCS / ".nojekyll", "")
    build_index(data, len(paths))
    for scenario in data["scenarios"]:
        build_dashboard(scenario)
    build_artifact_page(paths)
    build_about(len(data["scenarios"]))
    build_videos(data)
    search = [{"title": title_for(p), "path": (Path("library") / p.relative_to(ROOT).with_suffix(".html")).as_posix()} for p in paths]
    write(DOCS / "search-index.json", json.dumps(search, indent=2))
    print(f"Built public GitHub Pages site: {len(data['scenarios'])} dashboards, {len(paths)} artifacts")


if __name__ == "__main__":
    main()
