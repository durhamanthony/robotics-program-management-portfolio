#!/usr/bin/env python3
"""Build anonymized enterprise-transformation portfolio source artifacts.

The case data in this module is fictional and planning-grade. Career facts are
limited to the experience map and are intentionally separated from modeled
project results.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MA = ROOT / "enterprise-programs" / "01-ma-it-integration"
HW = ROOT / "enterprise-programs" / "02-hardware-refresh"
DATA = ROOT / "portfolio" / "enterprise_dashboard_data.json"
AS_OF = "2026-08-25"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]], title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    standard = ["table_title", *fields, "evidence_class", "confidence", "source_or_validation"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=standard, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            record = {
                "table_title": title,
                "evidence_class": "Scenario assumption",
                "confidence": "Low",
                "source_or_validation": "Replace with approved project records",
            }
            record.update(row)
            writer.writerow(record)


def table(headers: list[str], rows: list[list[object]]) -> str:
    head = "| " + " | ".join(headers) + " |"
    rule = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(str(cell) for cell in row) + " |" for row in rows)
    return f"{head}\n{rule}\n{body}"


def document(title: str, purpose: str, body: str, template_fields: list[str], *, status: str = "Filled example + reusable template") -> str:
    fields = "\n".join(f"- `{field}`" for field in template_fields)
    return f"""# {title}

> **Portfolio case study — {status}.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of {AS_OF}.

## Purpose

{purpose}

{body.strip()}

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

{fields}

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
"""


def domain_plan(title: str, purpose: str, scope_rows: list[list[object]], sequence: list[str], acceptance: list[str], rollback: str, fields: list[str]) -> str:
    sequence_md = "\n".join(f"{index}. {item}" for index, item in enumerate(sequence, 1))
    acceptance_md = "\n".join(f"- [ ] {item}" for item in acceptance)
    body = f"""## Filled example

{table(["Work package", "Scenario baseline", "Accountable owner", "Evidence / gate"], scope_rows)}

## Execution sequence

{sequence_md}

## Acceptance evidence

{acceptance_md}

## Exception, rollback, and escalation

{rollback}

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.
"""
    return document(title, purpose, body, fields)


PMI_SOURCES = [
    ["SRC-PMI-01", "PMI", "PMBOK Guide — Eighth Edition", "https://www.pmi.org/standards/pmbok", "Six principles; seven performance domains; tailoring; value and outcomes", "Official publisher page", AS_OF],
    ["SRC-PMI-02", "PMI", "Process Groups: A Practice Guide", "https://www.pmi.org/standards/process-groups", "Initiating, Planning, Executing, Monitoring and Controlling, Closing for predictive work", "Official practice-guide page", AS_OF],
    ["SRC-PMI-03", "PMI", "Agile Practice Guide — Second Edition", "https://www.pmi.org/standards/agile", "Agile, Lean, Kanban, product delivery, hybrid selection, value and flow", "Official publisher page", AS_OF],
    ["SRC-PMI-04", "PMI", "2026 PMP exam update", "https://www.pmi.org/certifications/project-management-pmp/new-exam", "Current exam emphasizes outcomes/value and predictive, agile, and hybrid application", "Official certification page", AS_OF],
    ["SRC-SCRUM-01", "Scrum Guides", "The Scrum Guide", "https://scrumguides.org/scrum-guide.html", "Accountabilities, events, artifacts, commitments, empiricism", "Official guide", AS_OF],
    ["SRC-KANBAN-01", "Kanban Guides", "The Kanban Guide", "https://kanbanguides.org/the-kanban-guide/", "Definition of Workflow; WIP, throughput, work-item age, cycle time", "Official guide", AS_OF],
]


MA_TECH_SOURCES = [
    ["SRC-NIST-01", "NIST", "Cybersecurity Framework 2.0", "https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20", "Govern, Identify, Protect, Detect, Respond, Recover outcomes", "Official publication", AS_OF],
    ["SRC-MS-01", "Microsoft", "Multiple Microsoft Entra tenant scenarios", "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/multi-tenant/scenarios", "M&A tenant consolidation and coexistence decision context", "Official product guidance", AS_OF],
    ["SRC-MS-02", "Microsoft", "Multitenant organization capabilities", "https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/overview", "Cross-tenant M&A identity/collaboration capabilities", "Official product guidance", AS_OF],
    ["SRC-MS-03", "Microsoft", "Azure VPN Gateway site-to-site guidance", "https://learn.microsoft.com/en-us/azure/vpn-gateway/tutorial-site-to-site-portal", "IPsec/IKE connectivity, non-overlapping address space, active-active design", "Official product guidance", AS_OF],
    ["SRC-GOOGLE-01", "Google Workspace", "Migration tools and resources", "https://workspace.google.com/solutions/migration/", "Admin-managed migration of mail, files, and chat data", "Official product guidance", AS_OF],
    ["SRC-SLACK-01", "Slack", "Migrate workspaces to an Enterprise organization", "https://slack.com/help/articles/115002532808-Migrate-workspaces-to-an-Enterprise-organization", "Availability, history, apps/webhooks, identity, and member communication considerations", "Official product guidance", AS_OF],
    ["SRC-SLACK-02", "Slack", "Move channels between workspaces", "https://slack.com/help/articles/115001946688-Move-channels-between-workspaces-in-an-Enterprise-organization", "Channel history, access, bots/apps, and migration limitations", "Official product guidance", AS_OF],
    ["SRC-ATL-01", "Atlassian", "Migrate Jira users and groups", "https://support.atlassian.com/migration/docs/migrate-users-and-groups/", "Identity matching, group permissions, and migration sequencing", "Official product guidance", AS_OF],
    ["SRC-ASANA-01", "Asana", "Import data from other tools", "https://help.asana.com/s/article/import-data-from-other-tools-to-projects-in-asana", "CSV import structure and field mapping", "Official product guidance", AS_OF],
]


HW_TECH_SOURCES = [
    ["SRC-NIST-02", "NIST", "SP 800-88 Rev. 2 — Guidelines for Media Sanitization", "https://csrc.nist.gov/pubs/sp/800/88/r2/final", "Enterprise sanitization program, validation, disposal/reuse controls", "Official final publication", AS_OF],
    ["SRC-MS-10", "Microsoft", "Windows Autopilot overview", "https://learn.microsoft.com/en-us/autopilot/overview", "OEM image, automated configuration, Entra join, MDM enrollment", "Official product guidance", AS_OF],
    ["SRC-MS-11", "Microsoft", "Windows Autopilot for existing devices", "https://learn.microsoft.com/en-us/autopilot/existing-devices", "Configuration Manager task sequence and Autopilot transition path", "Official product guidance", AS_OF],
    ["SRC-MS-12", "Microsoft", "Intune device compliance policies", "https://learn.microsoft.com/en-us/intune/device-security/compliance/overview", "Platform-specific compliance and Conditional Access signals", "Official product guidance", AS_OF],
    ["SRC-MS-13", "Microsoft", "OneDrive Known Folder Move", "https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders", "Data protection and staged folder redirection/migration", "Official product guidance", AS_OF],
    ["SRC-MS-14", "Microsoft", "Endpoint analytics overview", "https://learn.microsoft.com/en-us/intune/analytics/", "Startup, application reliability, battery, and managed-device experience insights", "Official product guidance", AS_OF],
]


def build_source_register(path: Path, rows: list[list[object]], title: str) -> None:
    write_csv(
        path,
        ["source_id", "publisher", "title", "url", "portfolio_use", "authority", "accessed"],
        [dict(zip(["source_id", "publisher", "title", "url", "portfolio_use", "authority", "accessed"], row)) | {"evidence_class": "Public benchmark", "confidence": "High", "source_or_validation": str(row[3])} for row in rows],
        title,
    )


def build_ma() -> None:
    common = MA / "common"
    agile = MA / "agile"
    predictive = MA / "predictive"

    write(common / "PORTFOLIO_GUIDE.md", document(
        "M&A IT Integration Portfolio Guide",
        "Explain how to review the shared control pack and the two complete delivery playbooks.",
        f"""## Case boundary

Company ABC acquires Company XYZ. The modeled integration covers 680 employees, 745 endpoints, three offices, two identity/collaboration domains, and 142 discovered applications. It begins before legal close with clean-team restrictions and ends after Day 1, migration waves, application dispositions, hypercare, service transition, and benefits ownership.

## How the package is organized

{table(["Layer", "What it contains", "Why it is shared or separate"], [
    ["Shared control pack", "Charter, Day 1, identity, network, collaboration, applications, security, change, cutover, RAID, RACI, dependencies, budget, validation", "These controls do not become optional when the delivery method changes"],
    ["Agile playbook", "Outcome roadmap, prioritized backlog, two-week sprints, reviews, retrospectives, release readiness", "Best when requirements and technical discovery evolve while Day 1 remains fixed"],
    ["Predictive / Waterfall playbook", "PMBOK 8 alignment, WBS, integrated master schedule, stage gates, baselines, change control, earned value", "Best when scope is sufficiently known and approvals require formal baselines"],
  ])}

## Recruiter review path

1. Open either dashboard and review the outcome, dates, budget, top risks, and decision status.
2. Inspect the shared controls to see how Day 1, security, data, and rollback are governed.
3. Compare the Agile backlog and metrics with the Predictive WBS, baselines, and stage gates.
4. Download the control workbook for filterable registers and formulas.

## Truth boundary

This is an experience-informed fictional case, not a claim that Company ABC or Company XYZ was a client. The author's supplied career evidence includes nine enterprise M&A endpoint integrations, digital-workplace leadership across 37,000 Macs and 300,000 Windows devices, a 45-person portfolio, a $14 million operating portfolio, collaboration-platform migrations, endpoint standards, security/audit partnership, and cross-functional work with HR, facilities, procurement, finance, and support. Those verified career facts informed the control design; every case result remains a scenario assumption.
""",
        ["deal thesis and integration intent", "legal-close date and clean-team restrictions", "employee/site/application/device baselines", "Day 1 minimum viable experience", "target-state decisions", "success measures and benefit owners", "delivery method and tailoring rationale"],
    ))

    write(common / "ASSUMPTIONS_AND_EXPERIENCE_MAP.md", document(
        "M&A Assumptions, Evidence, and Experience Map",
        "Prevent modeled results from being confused with career evidence or vendor-confirmed facts.",
        f"""## Evidence classes

{table(["Class", "Meaning", "Example in this case"], [
    ["Verified experience", "Outcome or scale supported by the supplied resume/profile", "Nine enterprise M&A endpoint integrations"],
    ["Public source", "Current primary-source guidance", "PMI PMBOK 8, NIST CSF 2.0, and product migration documentation"],
    ["Scenario assumption", "Fictional planning input", "680 employees and a $1.86M authorization"],
    ["Derived calculation", "Reproducible arithmetic from identified inputs", "665 / 680 Day 1 ready = 97.8%"],
    ["Unknown / validation needed", "Must come from discovery, contract, test, or accountable approval", "Actual mailbox volume, legal-hold population, subnet map, and API dependencies"],
  ])}

## Experience-to-control trace

{table(["Experience evidence", "How it informs the case", "What is not claimed"], [
    ["Nine enterprise M&A endpoint integrations", "Day 1, access, device, support, standards, and continuity controls", "No prior employer or acquired company is identified"],
    ["37K Macs / 300K Windows modern management", "Inventory, compliance, deployment, telemetry, and support handoff", "The case scale of 745 endpoints is fictional"],
    ["Google Workspace, Slack, Box, Microsoft 365, Teams, OneDrive, Jira, Confluence", "Collaboration discovery, identity mapping, pilot, delta, validation, and decommission steps", "No claim of migrating the exact modeled volumes"],
    ["$14M portfolio / vendor savings", "Budget, forecast, contingency, vendor milestones, and benefits governance", "The $1.86M case authorization is not an actual spend"],
    ["Security policy and audit partnership", "Least privilege, logging, access review, data retention, and evidence gates", "The package is not a certification or legal opinion"],
  ])}

## Scenario assumptions requiring validation

- Legal close occurs at the end of Week 4; no personal or restricted data crosses before approval.
- Company XYZ has 680 in-scope workers: 620 employees and 60 contractors.
- 745 endpoints are in scope; 65 are shared, lab, kiosk, or loaner devices.
- Company ABC is the target identity, endpoint, service-management, and collaboration control plane.
- Coexistence bridges are time-boxed and removed after migration acceptance.
- No production connection is authorized until address collisions, firewall rules, identity controls, monitoring, and rollback are approved.
""",
        ["claim or number", "evidence class", "source or owner", "confidence", "validation date", "decision affected", "replacement evidence required"],
    ))

    write(common / "PROJECT_CHARTER.md", document(
        "M&A IT Integration Project Charter",
        "Authorize the program, establish outcomes and boundaries, and assign accountable decisions.",
        f"""## Filled example

{table(["Charter element", "Approved scenario baseline"], [
    ["Sponsor", "Company ABC Chief Information Officer"],
    ["Business outcome", "680 Company XYZ workers can securely perform priority work on Day 1 while Company ABC integrates infrastructure and removes redundant technology without an uncontrolled outage"],
    ["Program manager", "M&A IT Technical Project Manager"],
    ["Authorization", "$1,860,000 planning baseline including $60,000 management reserve"],
    ["Target window", "Pre-close Week 1 through post-close Week 24; Day 1 at end of Week 4"],
    ["In scope", "Employee onboarding, endpoint/access bridge, identity, network, Google Workspace, Slack, Asana/Jira, application rationalization, data/reporting, vendors, change, cutover, hypercare"],
    ["Out of scope", "ERP legal-entity redesign, product engineering roadmap, facilities construction, and business-process redesign not required for continuity"],
  ])}

## Measurable objectives

- Day 1 readiness: at least 98% of 680 workers have a validated identity, required device path, collaboration access, and support route; every exception has a named owner and workaround.
- Priority access: at least 99% of Tier 0/Tier 1 access tests pass before release.
- Migration quality: at least 99.5% object-count reconciliation for in-scope data and zero unresolved Sev 1 security defects at go/no-go.
- Business continuity: no unplanned outage longer than 30 minutes for a Tier 0 service attributable to the integration.
- Rationalization: every one of 142 discovered applications has an accountable disposition; realized savings are reported only after Finance validates removed cost.

## Constraints and authority

Clean-team and legal restrictions override schedule pressure. Security, Privacy/Legal, HR, and system owners retain approval rights. The program manager may sequence work, call gates, stop unsafe cutovers, and escalate missing decisions; the program manager may not waive legal hold, security risk, or business acceptance.

## Exit criteria

Charter closure requires accepted service ownership, reconciled identities/devices/applications, completed access removal, approved open-risk transfer, vendor closure, financial reconciliation, and named benefit owners.
""",
        ["sponsor and program manager", "business case and outcomes", "scope / exclusions", "milestones", "budget and reserve", "success measures", "constraints / assumptions", "authority and escalation", "signatures / approval dates"],
    ))

    write(common / "GOVERNANCE_AND_DECISION_RIGHTS.md", document(
        "M&A Governance, RACI, and Decision Rights",
        "Define how decisions move from workstreams to the integration steering committee without hiding ownership.",
        f"""## Governance model

{table(["Forum", "Cadence", "Required decisions", "Participants", "Output"], [
    ["Executive steering committee", "Weekly through Day 30, biweekly thereafter", "Scope, funding, risk acceptance, target-state exceptions, gate decisions", "CIO sponsor, Corp Dev, business sponsor, Security, Finance, HR, PM", "Decision log and signed gate memo"],
    ["Integration management office", "Three times weekly", "Cross-workstream dependencies, RAID, schedule, vendor actions", "PM and workstream leads", "Integrated plan and status"],
    ["Technical design authority", "Twice weekly", "Identity, network, data, tool architecture, rollback", "Infrastructure, IAM, Security, application owners", "Approved design / exception"],
    ["Change and readiness", "Weekly; daily before Day 1", "Audience, message, training, readiness exceptions", "Change lead, HR, Help Desk, site leads", "Readiness score and communications"],
    ["Cutover command center", "Continuous during cutover", "Go/hold/rollback, severity and communications", "PM, technical leads, service owner, vendor leads", "Time-stamped command log"],
  ])}

## Decision rule

A decision is complete only when the accountable owner, options, recommendation, due date, rationale, downstream impacts, and approval are recorded. Silence is not approval. Conditional approval carries explicit actions and expiry.

## Escalation thresholds

- Any predicted Day 1 miss affecting more than 14 workers or any Tier 0 service goes to steering within four hours.
- Any suspected data exposure, unauthorized cross-tenant access, or legal-hold conflict immediately invokes the security/privacy incident process.
- Forecast variance above 5% or reserve draw above $25,000 requires sponsor/Finance approval.
- A milestone slip greater than five business days with downstream impact requires a recovery plan and baseline decision.
""",
        ["forums and cadence", "decision categories", "accountable roles", "quorum", "thresholds", "escalation clock", "decision log fields", "gate approvers"],
    ))

    write(common / "DAY_1_EMPLOYEE_EXPERIENCE_PLAN.md", domain_plan(
        "M&A Day 1 Employee Experience Plan",
        "Make the first business day productive and supportable for every acquired worker, including documented exceptions.",
        [
            ["Authoritative roster", "680 workers; HR-to-IAM reconciliation at T-10, T-3, and T-0", "HR Integration Lead", "Signed roster delta"],
            ["Identity and credentials", "Company ABC identity or approved temporary bridge; MFA registered", "IAM Lead", "Authentication test + access review"],
            ["Endpoint path", "Re-enroll 510 devices; replace 170; 65 shared/special devices use controlled plan", "Endpoint Lead", "Device compliance report"],
            ["Collaboration", "Mail/calendar, Drive, Slack, task tools, meeting access", "Collaboration Lead", "Persona-based test script"],
            ["Support", "Dedicated queue, bridge, knowledge, site runners, executive route", "Service Desk Lead", "Staffing roster + ticket taxonomy"],
        ],
        [
            "Freeze the roster baseline and map worker, manager, persona, location, device, license, and special access.",
            "Provision accounts in a disabled state; run duplicate, contractor-expiry, and privileged-role checks.",
            "Stage devices, credentials, and instructions by site and remote-shipment wave; preserve chain of custody.",
            "Run persona tests for standard user, executive, developer/admin, call-center/shared device, and contractor.",
            "Open the command center at T-12 hours; release communications only after sponsor and HR approval.",
            "At T+2 and T+8 hours, reconcile login, device compliance, collaboration access, and open incidents.",
        ],
        [
            "665 of 680 workers are fully ready (97.8%); 15 exceptions have a tested workaround, owner, and expiry.",
            "674 of 680 workers pass identity authentication (99.1%); failed cases are not counted as ready.",
            "100% of Tier 0/Tier 1 persona tests have time-stamped evidence and owner sign-off.",
            "Help Desk staffing, knowledge, queue routing, severity, executive escalation, and vendor contacts are live.",
        ],
        "Hold affected cohort release if roster-to-identity mismatch exceeds 1%, if a privileged-access path is unapproved, or if support cannot receive cases. Use the approved source account/device path during the time-boxed coexistence period. Rollback never deletes source data; it disables the new route, restores prior routing, and communicates a revised window.",
        ["worker roster and personas", "device assignment / delivery", "identity and MFA status", "license/access bundle", "site/remote logistics", "communications", "support coverage", "exception workaround and expiry", "Day 1 acceptance signatures"],
    ))

    write(common / "IDENTITY_AND_ACCESS_PLAN.md", domain_plan(
        "M&A Identity and Access Integration Plan",
        "Establish a controlled identity bridge, converge accounts and entitlements, and remove temporary access after acceptance.",
        [
            ["Identity source", "Company ABC HR/IAM becomes authoritative after approved roster cut", "HR + IAM", "Joiner/mover/leaver reconciliation"],
            ["Coexistence", "Cross-tenant or federation bridge limited to approved groups for 90 days", "IAM Architect", "Access package + expiry"],
            ["Authentication", "MFA and device-compliance controls; break-glass accounts excluded and monitored", "Security", "Policy test and logs"],
            ["Privileges", "Named admin accounts, just-in-time elevation, no shared credentials", "Security + system owner", "Privileged access review"],
            ["Deprovisioning", "Source access removed only after destination validation and legal approval", "IAM Operations", "Disablement evidence"],
        ],
        [
            "Inventory directories, domains, identity providers, account types, groups, roles, service principals, keys, and emergency accounts.",
            "Normalize unique identity keys; resolve duplicate email addresses and contractor ownership before migration.",
            "Map personas to least-privilege role bundles and separate birthright, requestable, privileged, and service access.",
            "Pilot with 25 non-privileged and five privileged personas; review logs, token lifetime, conditional access, and recovery.",
            "Stage identities before application/data cutovers; reconcile entitlements after each wave.",
            "Disable the bridge and orphaned accounts only after business owner, IAM, and Security acceptance.",
        ],
        [
            "680 roster records reconcile to a unique destination identity or an approved exception.",
            "100% of privileged roles have named owners, approval, MFA, logging, and expiry where applicable.",
            "No orphaned service principal, unmanaged shared account, or unresolved duplicate identity remains at closure.",
            "Access-review evidence shows source, destination, exception, and approver for each critical entitlement.",
        ],
        "If authentication failure exceeds 2% in a wave, privileged-role mapping differs from approval, or logging is incomplete, stop the wave. Re-enable the approved source route for that cohort, preserve logs, and correct mapping before retry. Security incidents use the enterprise incident process, not the project issue log alone.",
        ["authoritative sources", "unique identity key", "domain strategy", "persona bundles", "MFA / conditional access", "privileged access", "service identities", "coexistence expiry", "reconciliation queries", "decommission approval"],
    ))

    write(common / "NETWORK_INFRASTRUCTURE_PLAN.md", domain_plan(
        "M&A Network and Infrastructure Integration Plan",
        "Create secure, observable connectivity without introducing route, DNS, segmentation, or perimeter failures.",
        [
            ["Discovery", "Three sites, two cloud environments, four overlapping subnets identified", "Network Lead", "Validated L2/L3, WAN, DNS, DHCP, firewall, Wi-Fi, VoIP inventory"],
            ["Interconnect", "Redundant IPsec/IKE site-to-site tunnels with restricted routes", "Network Architect", "Tunnel, failover, latency, throughput tests"],
            ["Collision remediation", "NAT/renumber plan for four conflicts; no overlapping routes advertised", "Network Lead", "Approved address plan"],
            ["Segmentation", "Default deny; user, server, management, guest, voice, and migration zones", "Security", "Firewall rule review"],
            ["Observability", "Flow, DNS, firewall, VPN, and availability telemetry routed to Company ABC", "Network Operations", "Dashboard and alert test"],
        ],
        [
            "Discover topology, circuits, public IPs, routes, subnets, VLANs, DNS zones/forwarders, firewalls, Wi-Fi, voice, certificates, and cloud gateways.",
            "Classify required flows by application, source, destination, port/protocol, data class, owner, duration, and removal date.",
            "Resolve address collisions before route exchange; validate forward and reverse DNS and split-horizon behavior.",
            "Build redundant tunnels and deny-by-default rules in a non-production path; enable monitoring before traffic.",
            "Pilot business flows, failure/failback, bandwidth, packet loss, name resolution, and security detections.",
            "Enable production by site; reconcile rules and routes; remove temporary migration access after acceptance.",
        ],
        [
            "Zero unresolved overlapping routes at go/no-go; all four collision plans are tested.",
            "Tier 0/Tier 1 flows pass functional, failover, logging, and owner acceptance tests.",
            "Every temporary firewall rule has an owner, ticket, purpose, expiry, and removal evidence.",
            "Network Operations accepts diagrams, configurations, monitoring, backup, vendor, and incident procedures.",
        ],
        "Immediately withdraw new routes and disable the affected tunnel/rule set for asymmetric routing, unapproved lateral movement, unresolved DNS corruption, or Sev 1 performance impact. Restore the prior path, keep evidence, and reconvene the technical design authority. Rollback checkpoints are defined per site and per rule group—not as one all-or-nothing instruction.",
        ["topology / circuit inventory", "IP address and collision plan", "required flow matrix", "DNS/DHCP design", "segmentation", "firewall rules and expiry", "VPN/SD-WAN design", "monitoring", "test scripts", "rollback and operations acceptance"],
    ))

    write(common / "COLLABORATION_MIGRATION_PLAN.md", domain_plan(
        "M&A Collaboration and Workspace Migration Plan",
        "Migrate or consolidate Google Workspace, Slack, Asana, and Jira with identity, history, retention, integrations, and user experience controlled together.",
        [
            ["Google Workspace", "610 users; Gmail, Calendar, My Drive, Shared Drives, Groups; pilot + pre-stage + delta", "Workspace Lead", "Object counts, permissions, mail flow, sharing, legal hold"],
            ["Slack", "520 users; 286 channels; private/shared channels identified; apps and webhooks mapped", "Collaboration Lead", "Membership, history, files, retention, bot/webhook test"],
            ["Asana", "280 users; portfolio/project disposition and CSV/API mapping", "Business Apps Lead", "Task, owner, due date, custom-field reconciliation"],
            ["Jira", "190 users; identity/group migration before project content where supported", "Atlassian Owner", "Permissions, apps, filters, boards, automation, references"],
        ],
        [
            "Inventory data volume, owners, retention, legal hold, external sharing, groups/channels/projects, apps, bots, webhooks, automation, and unsupported objects.",
            "Approve destination information architecture and identity mapping; resolve duplicate names and inaccessible owners.",
            "Run representative pilots including executives, delegates, shared resources, external guests, restricted projects, and automation owners.",
            "Pre-stage supported content, freeze high-change objects only when required, then run the final delta.",
            "Validate counts, samples, permissions, links, mail/calendar behavior, integrations, retention, and search with accountable owners.",
            "Keep source read-only for the approved retention window; remove licenses and integrations only after acceptance and legal approval.",
        ],
        [
            "At least 99.5% reconciled object counts per in-scope data class, with excluded/unsupported objects documented.",
            "100% of critical bots, apps, webhooks, calendars, groups, shared drives, and automations have an owner and test result.",
            "No critical permission escalation or loss of legal-hold coverage remains unresolved.",
            "Business owners accept searchability, permissions, representative samples, and support instructions.",
        ],
        "Pause a cohort if identity mapping is ambiguous, retention/hold behavior is unapproved, permission variance exceeds the approved threshold, or critical integrations fail. Keep the source authoritative or read-only as designed, reverse routing where supported, and issue a user notice with the next decision time. Deletion is never a rollback mechanism.",
        ["source/destination tenants", "licenses", "data classes / volumes", "identity mapping", "retention / legal hold", "information architecture", "apps/bots/webhooks", "pilot cohorts", "freeze/delta timing", "validation and decommission"],
    ))

    write(common / "APPLICATION_RATIONALIZATION_AND_DATA_PLAN.md", domain_plan(
        "M&A Application Rationalization and Data Consolidation Plan",
        "Give every application an accountable disposition and ensure data, integration, security, license, and support impacts are resolved before retirement.",
        [
            ["Discovery", "142 applications; owner, users, cost, contract, data, integration, risk, criticality", "Application Lead", "Owner-attested inventory"],
            ["Disposition", "Retain, migrate, consolidate, retire, replace, or temporary coexistence", "Business + Architecture", "Signed decision record"],
            ["Overlap cohort", "37 overlapping tools; 22 targeted for retirement/consolidation", "Steering Committee", "Business case and exit plan"],
            ["Shadow IT", "Unmanaged apps are quarantined for review, not silently connected", "Security", "Risk disposition"],
            ["Reporting", "Unified license, cost, owner, risk, migration, and realization view", "PMO + Finance", "Reconciled dashboard"],
        ],
        [
            "Discover through SSO, expense/AP, contracts, browser/CASB, endpoint inventory, network, interviews, and CMDB; reconcile duplicates.",
            "Classify criticality, data sensitivity, regulatory/hold obligations, integration dependencies, supportability, contract dates, and technical debt.",
            "Score fit, cost, risk, migration effort, user impact, and target-state alignment; obtain owner and architecture disposition.",
            "Build migration, archive, export, integration-remediation, communication, support, and rollback work for each change.",
            "Validate destination data and business workflow before source access or contract termination.",
            "Finance validates avoided cash cost after invoice/contract removal; released capacity is not reported as savings without evidence.",
        ],
        [
            "142 of 142 applications have an owner, criticality, disposition, date, dependency status, and approval.",
            "Every retirement has accepted data retention/export, integration removal, access removal, support update, and contract action.",
            "No Tier 0/Tier 1 application closes with an unknown owner, unsupported recovery path, or untested critical interface.",
            "Benefits register separates forecast, committed, invoiced, and realized values.",
        ],
        "If destination workflow, data reconciliation, audit trail, or critical integration fails, stop retirement, restore the prior access/routing/license within the contract window, and keep the source read-only or active as approved. A license-renewal deadline is not authority to delete data or bypass acceptance.",
        ["application inventory", "business/technical owner", "criticality and data class", "contract and cost", "integrations", "target disposition", "migration/archive", "validation", "decommission", "benefit evidence"],
    ))

    write(common / "SECURITY_PRIVACY_AND_LEGAL_HOLD.md", document(
        "M&A Security, Privacy, and Legal-Hold Control Plan",
        "Embed risk governance, evidence, and stop conditions across discovery, coexistence, migration, and decommissioning.",
        f"""## NIST CSF 2.0 control map

{table(["Function", "M&A application", "Required evidence"], [
    ["Govern", "Risk appetite, decision rights, due diligence, vendor clauses, privacy/hold authority", "Approved risk and control owners"],
    ["Identify", "Assets, identities, data, apps, networks, third parties, vulnerabilities, dependencies", "Reconciled inventory and classification"],
    ["Protect", "MFA, least privilege, compliant devices, segmentation, encryption, backups, change control", "Policy/config/test evidence"],
    ["Detect", "Cross-tenant authentication, privileged events, data transfer, VPN/firewall, endpoint and SaaS logs", "Alert and log ingestion tests"],
    ["Respond", "Security bridge, severity, evidence preservation, regulatory/legal decision path", "Incident runbook and contacts"],
    ["Recover", "Rollback, restore, service priorities, communications, lessons", "Tested recovery and restoration evidence"],
  ])}

## Mandatory gates

- No production interconnect before asset/flow inventory, segmentation, logging, vulnerability review, collision remediation, and Security approval.
- No data movement before data classification, legal hold/retention, destination access, encryption, processor/vendor, and validation requirements are approved.
- No privileged migration account without named ownership, least privilege, MFA, logging, key/secret custody, and expiry.
- No source deletion or tenant decommission before business, records/legal, Security, and service-owner acceptance.

## Privacy by design

Use the minimum data required for discovery and testing; mask samples where feasible; record jurisdiction/residency and controller/processor responsibilities; restrict clean-team access; retain migration logs according to approved policy; and delete temporary working copies only through an approved evidence-backed process.

## Risk acceptance

The project manager documents and escalates risk; only the designated business/security authority may accept it. Acceptance includes scope, rationale, compensating controls, owner, expiry, review date, and residual rating.
""",
        ["security framework/profile", "asset and data classifications", "control owners", "identity/privilege", "network segmentation", "logging/monitoring", "vulnerability and third-party risk", "privacy/retention/legal hold", "incident and recovery", "exceptions and risk acceptance"],
    ))

    write(common / "CHANGE_COMMUNICATIONS_AND_TRAINING.md", document(
        "M&A Change, Communications, Training, and Support Plan",
        "Prepare each audience for what changes, when it changes, what they must do, and how support restores productivity.",
        f"""## Audience and journey

{table(["Audience", "Change impact", "Touchpoints", "Readiness evidence"], [
    ["All Company XYZ workers", "New identity, MFA, support, collaboration, device policy", "T-20/T-10/T-3/Day 1/T+3 messages; quick start; office hours", "Acknowledgment, login test, help demand"],
    ["People managers", "Roster and persona validation, escalation, productivity exceptions", "Manager kit and readiness review", "Roster sign-off and exception owners"],
    ["Executives/admins", "Delegation, calendars, mobile, high-touch support", "Concierge rehearsal", "Persona test and day-of contact"],
    ["Developers/admins", "Privileged access, repositories, automation, network flows", "Technical labs and access review", "Critical workflow test"],
    ["Help Desk/site support", "New queue, tools, scripts, severity, vendor escalation", "Train-the-trainer, simulations, daily brief", "Knowledge test and staffing acceptance"],
  ])}

## Communication controls

Messages state who is affected, exact local time, expected interruption, preparation, what success looks like, support route, privacy/security cautions, and next update. HR/Legal approves employee language; technical owners approve steps; the PM controls the calendar and version.

## Adoption and support measures

- Day 1 login and collaboration success by persona/site, with numerator and denominator.
- Ticket contact rate per 100 migrated users, first-contact resolution, reopen rate, aged backlog, and top cause.
- Training attendance and task-based proficiency, not attendance alone.
- Sentiment pulse with comments triaged into defects, knowledge, training, or policy decisions.

## Hypercare staffing model

One command lead, one incident coordinator, identity/network/collaboration/application leads, vendor representatives, site runners, Help Desk queue lead, change lead, and executive support. Shift handoff records open incidents, user count affected, next action, owner, due time, workaround, and communications.
""",
        ["stakeholder segments", "change impact", "message owner/approver", "send date/time/channel", "required user action", "training objective and proficiency check", "support model", "adoption metrics", "feedback and escalation"],
    ))

    write(common / "CUTOVER_ROLLBACK_HYPERCARE.md", document(
        "M&A Integrated Cutover, Rollback, and Hypercare Runbook",
        "Provide a time-stamped control path from final readiness through go/no-go, execution, validation, rollback, and operations acceptance.",
        f"""## Gate criteria

{table(["Gate", "Entry evidence", "Decision"], [
    ["T-10 readiness", "Roster, inventory, design, vendor plan, communications, test status", "Continue, recover, or de-scope"],
    ["T-3 go/no-go", "No open Sev 1; Tier 0 tests pass; rollback viable; staffing confirmed", "Go, conditional go, hold"],
    ["T-0 release", "Backups/snapshots, freeze, monitoring, bridge, approvals", "Start cutover"],
    ["Wave validation", "Counts, samples, permissions, business workflow, support health", "Accept wave or rollback cohort"],
    ["Hypercare exit", "SLA stable, aged defects dispositioned, knowledge/ownership accepted", "Transfer to operations"],
  ])}

## Command log excerpt — filled example

{table(["Time", "Action / checkpoint", "Owner", "Result", "Decision"], [
    ["Fri 18:00", "Freeze approved collaboration changes", "Collaboration Lead", "Passed; three emergency changes logged", "Continue"],
    ["Fri 19:00", "Confirm source backups/export and destination capacity", "Data Lead", "Passed", "Continue"],
    ["Fri 20:00", "Enable restricted identity/network bridge", "IAM + Network", "Passed; telemetry visible", "Continue"],
    ["Sat 02:00", "Run priority user/data delta and reconciliation", "Migration Lead", "99.7% initial; 19 objects retried", "Continue with watch"],
    ["Sat 06:00", "Persona and business workflow tests", "Business Owners", "All Tier 0/1 passed", "Release communications"],
    ["Mon 10:00", "Day 1 checkpoint", "Command Lead", "665 ready; 15 controlled exceptions", "Remain in hypercare"],
  ])}

## Rollback decision

Rollback is assessed per identity cohort, network route/rule group, application, site, and data batch. Trigger examples: security control failure; permission variance above tolerance; data reconciliation below 99.5%; identity failure above 2%; Tier 0 workflow failure; or inability to restore within the approved recovery objective. The command lead calls the decision; accountable technical/business owners approve domain actions; the PM records time, rationale, evidence, and communication.

## Hypercare exit

Exit after five consecutive business days with no Sev 1, priority services inside the agreed service objective, fewer than ten aged migration defects, accepted knowledge/monitoring/on-call, documented residual risks, and business/service-owner signatures.
""",
        ["cutover scope and batch", "freeze window", "command roles", "prechecks", "time-stamped tasks and dependencies", "validation scripts", "rollback triggers/actions/latest-safe-time", "communications", "incident model", "hypercare exit and handoff"],
    ))

    write(common / "VENDOR_PROCUREMENT_AND_BUDGET.md", document(
        "M&A Vendor, Procurement, Contract, and Budget Plan",
        "Tie external work, licenses, milestones, invoices, contingency, and exit obligations to acceptance evidence.",
        f"""## Commercial control model

{table(["Package", "Commercial basis", "Acceptance basis", "Control"], [
    ["Migration specialist", "Milestone fixed fee plus approved variable volume", "Pilot, batch, reconciliation, defect and handoff evidence", "No milestone invoice on tool-success message alone"],
    ["Network/MSP", "Design/build/test milestones", "Approved design, config, failover, monitoring, runbook", "Temporary rules and hardware have removal/ownership"],
    ["Licenses", "Named user/device and bridge period", "Reconciled active use and exit dates", "Prevent dual-license tail"],
    ["Hardware/logistics", "Serialized receipt and delivery", "Custody, image/compliance, worker acceptance", "Lost/damaged exceptions tracked"],
  ])}

## Budget governance

The $1.86M authorization is a scenario assumption. Work-package owners forecast estimate-to-complete weekly. Finance validates purchase order, invoice, accrual, and contract termination. The PM reports baseline, commitments, actuals, estimate-to-complete, estimate-at-completion, variance, and reserve separately.

## Vendor exit criteria

Accepted data/configuration, admin access removed, secrets rotated, accounts disabled, logs and evidence retained, open defects assigned, knowledge transferred, licenses reconciled, invoices matched to acceptance, and confidentiality/data-return obligations completed.
""",
        ["statement of work and deliverables", "rate/milestone/volume assumptions", "acceptance evidence", "service levels and escalation", "security/privacy terms", "data return/deletion", "invoice control", "budget baseline/forecast", "reserve authority", "vendor exit"],
    ))

    write_csv(common / "RAID_REGISTER.csv", ["id", "type", "statement", "probability_1_5", "impact_1_5", "score", "owner", "response", "trigger", "due", "status"], [
        {"id":"MA-R-001","type":"Risk","statement":"Identity duplicates or stale contractor records block Day 1 access","probability_1_5":4,"impact_1_5":5,"score":20,"owner":"IAM Lead","response":"T-10/T-3/T-0 roster reconciliation; named exception path","trigger":"Duplicate/unknown identities above 1%","due":"Week 4","status":"Mitigating"},
        {"id":"MA-R-002","type":"Risk","statement":"Overlapping subnets cause routing or DNS failure after interconnect","probability_1_5":3,"impact_1_5":5,"score":15,"owner":"Network Lead","response":"Collision register, NAT/renumber, isolated pilot, route withdrawal rollback","trigger":"Any unapproved overlap at go/no-go","due":"Week 7","status":"Mitigating"},
        {"id":"MA-R-003","type":"Risk","statement":"Slack/Workspace/Jira permissions or retention change during migration","probability_1_5":3,"impact_1_5":5,"score":15,"owner":"Collaboration Lead","response":"Identity-first mapping, legal hold review, pilot, counts/samples/permissions validation","trigger":"Critical permission variance or hold gap","due":"Week 14","status":"Mitigating"},
        {"id":"MA-I-004","type":"Issue","statement":"Fifteen workers lack final device/access package at Day 1 checkpoint","probability_1_5":5,"impact_1_5":3,"score":15,"owner":"Day 1 Lead","response":"Tested loaner/temporary access; daily burn-down; manager communication","trigger":"Exception exceeds expiry","due":"Day 3","status":"Open"},
        {"id":"MA-A-005","type":"Assumption","statement":"Company ABC is the target collaboration and endpoint control plane","probability_1_5":3,"impact_1_5":4,"score":12,"owner":"CIO Sponsor","response":"Confirm target-state decision before design baseline","trigger":"Architecture strategy changes","due":"Week 2","status":"Validated for scenario"},
        {"id":"MA-D-006","type":"Dependency","statement":"Legal approves data movement and source retention by T-15","probability_1_5":2,"impact_1_5":5,"score":10,"owner":"Legal/Privacy","response":"Decision package with data classes, holds, destinations, processors, dates","trigger":"Approval absent at T-15","due":"Week 2","status":"Open"},
    ], "M&A shared RAID register — filled example")

    write_csv(common / "DEPENDENCY_MATRIX.csv", ["dependency_id", "predecessor", "successor", "required_by", "owner", "acceptance", "fallback", "status"], [
        {"dependency_id":"DEP-001","predecessor":"Legal close / clean-team approval","successor":"Enable identity and network bridges","required_by":"Week 4","owner":"Legal + Corp Dev","acceptance":"Written release with approved scope","fallback":"Keep staged changes disabled","status":"Open"},
        {"dependency_id":"DEP-002","predecessor":"Roster and unique identity reconciliation","successor":"Provision accounts and licenses","required_by":"T-10","owner":"HR + IAM","acceptance":"680 records resolved or excepted","fallback":"Exclude unresolved identities","status":"In progress"},
        {"dependency_id":"DEP-003","predecessor":"Subnet collision remediation","successor":"Advertise cross-entity routes","required_by":"Week 7","owner":"Network Lead","acceptance":"Zero unresolved overlap; failover test","fallback":"Restricted proxy/NAT or no route","status":"In progress"},
        {"dependency_id":"DEP-004","predecessor":"Identity/group migration","successor":"Jira/Slack/content migration","required_by":"Week 10","owner":"IAM + Collaboration","acceptance":"Unique IDs and permission mapping approved","fallback":"Read-only source and delayed cohort","status":"Open"},
        {"dependency_id":"DEP-005","predecessor":"Data validation and legal acceptance","successor":"Source decommission/license termination","required_by":"Week 22","owner":"Data + Legal + Business","acceptance":"Counts/samples/permissions/hold accepted","fallback":"Extend read-only retention","status":"Open"},
    ], "M&A cross-workstream dependency matrix — filled example")

    write_csv(common / "RACI.csv", ["deliverable", "sponsor", "program_manager", "corp_dev", "hr", "security", "iam", "network", "collaboration", "app_owners", "service_desk", "finance_legal"], [
        {"deliverable":"Charter / integration outcomes","sponsor":"A","program_manager":"R","corp_dev":"C","hr":"C","security":"C","iam":"I","network":"I","collaboration":"I","app_owners":"C","service_desk":"I","finance_legal":"C"},
        {"deliverable":"Day 1 employee readiness","sponsor":"A","program_manager":"R","corp_dev":"I","hr":"R","security":"C","iam":"R","network":"R","collaboration":"R","app_owners":"R","service_desk":"R","finance_legal":"C"},
        {"deliverable":"Identity / privileged access","sponsor":"I","program_manager":"C","corp_dev":"I","hr":"C","security":"A","iam":"R","network":"I","collaboration":"C","app_owners":"C","service_desk":"I","finance_legal":"I"},
        {"deliverable":"Network interconnect","sponsor":"I","program_manager":"C","corp_dev":"I","hr":"I","security":"A","iam":"C","network":"R","collaboration":"C","app_owners":"C","service_desk":"I","finance_legal":"I"},
        {"deliverable":"Collaboration migration","sponsor":"I","program_manager":"R","corp_dev":"I","hr":"C","security":"C","iam":"R","network":"C","collaboration":"A/R","app_owners":"C","service_desk":"C","finance_legal":"C"},
        {"deliverable":"Application disposition / retirement","sponsor":"A","program_manager":"R","corp_dev":"C","hr":"I","security":"C","iam":"C","network":"C","collaboration":"C","app_owners":"R","service_desk":"C","finance_legal":"C"},
        {"deliverable":"Go/no-go / rollback","sponsor":"A","program_manager":"R","corp_dev":"I","hr":"C","security":"A","iam":"R","network":"R","collaboration":"R","app_owners":"R","service_desk":"R","finance_legal":"C"},
    ], "M&A shared RACI — A accountable, R responsible, C consulted, I informed")

    write_csv(common / "APPLICATION_PORTFOLIO.csv", ["app_id", "application", "users", "criticality", "data_class", "owner", "overlap", "disposition", "target", "migration_wave", "contract_action", "validation", "status"], [
        {"app_id":"APP-001","application":"Company XYZ Google Workspace","users":610,"criticality":"Tier 0","data_class":"Confidential / hold population","owner":"Collaboration Lead","overlap":"Yes","disposition":"Migrate and retire source after retention","target":"Company ABC Workspace","migration_wave":"Waves 1-4","contract_action":"Terminate after acceptance","validation":"Counts, samples, permissions, mail/calendar, hold","status":"In progress"},
        {"app_id":"APP-002","application":"Company XYZ Slack","users":520,"criticality":"Tier 1","data_class":"Confidential","owner":"Collaboration Lead","overlap":"Yes","disposition":"Consolidate","target":"Company ABC enterprise organization","migration_wave":"Wave 3","contract_action":"Reconcile licenses","validation":"Channels, members, files, history, bots, webhooks","status":"Planned"},
        {"app_id":"APP-003","application":"Company XYZ Jira","users":190,"criticality":"Tier 1","data_class":"Internal / restricted projects","owner":"Engineering Apps","overlap":"Yes","disposition":"Migrate selected projects","target":"Company ABC Jira","migration_wave":"Wave 4","contract_action":"End source subscription after archive","validation":"Users/groups, permissions, issues, attachments, apps","status":"Planned"},
        {"app_id":"APP-004","application":"Company XYZ Asana","users":280,"criticality":"Tier 2","data_class":"Internal","owner":"Business Apps","overlap":"Yes","disposition":"Consolidate active work; archive closed","target":"Company ABC Asana","migration_wave":"Wave 2","contract_action":"Reduce licenses","validation":"Projects, tasks, assignees, dates, fields","status":"Planned"},
        {"app_id":"APP-005","application":"Specialized design SaaS","users":42,"criticality":"Tier 1","data_class":"Restricted IP","owner":"Design VP","overlap":"No","disposition":"Retain with SSO/control uplift","target":"Existing SaaS","migration_wave":"Day 1 bridge","contract_action":"Novate contract","validation":"SSO, groups, export, vendor security","status":"Conditional retain"},
        {"app_id":"APP-006","application":"Legacy expense tool","users":640,"criticality":"Tier 2","data_class":"Confidential financial","owner":"Finance","overlap":"Yes","disposition":"Retire after archive","target":"Company ABC expense platform","migration_wave":"Wave 5","contract_action":"Terminate renewal","validation":"Open items, audit trail, archive, reimbursement","status":"Planned"},
    ], "M&A application rationalization register — representative rows from 142-app scenario")

    write_csv(common / "DAY1_READINESS.csv", ["cohort", "population", "identity_ready", "device_ready", "collaboration_ready", "support_ready", "fully_ready", "exceptions", "owner", "workaround", "status"], [
        {"cohort":"HQ Site A","population":280,"identity_ready":279,"device_ready":274,"collaboration_ready":277,"support_ready":280,"fully_ready":272,"exceptions":8,"owner":"Site A Lead","workaround":"Loaners + temporary approved access","status":"Amber"},
        {"cohort":"Office Site B","population":190,"identity_ready":189,"device_ready":187,"collaboration_ready":188,"support_ready":190,"fully_ready":186,"exceptions":4,"owner":"Site B Lead","workaround":"On-site runner and spare devices","status":"Amber"},
        {"cohort":"Office Site C","population":110,"identity_ready":109,"device_ready":108,"collaboration_ready":109,"support_ready":110,"fully_ready":107,"exceptions":3,"owner":"Site C Lead","workaround":"Concierge appointments","status":"Amber"},
        {"cohort":"Remote","population":100,"identity_ready":97,"device_ready":100,"collaboration_ready":99,"support_ready":100,"fully_ready":100,"exceptions":0,"owner":"Remote Lead","workaround":"Courier and virtual support","status":"Green"},
        {"cohort":"TOTAL","population":680,"identity_ready":674,"device_ready":669,"collaboration_ready":673,"support_ready":680,"fully_ready":665,"exceptions":15,"owner":"Day 1 Lead","workaround":"All 15 have owner and expiry","status":"Amber"},
    ], "M&A Day 1 readiness by cohort — filled example")

    write_csv(common / "MIGRATION_VALIDATION.csv", ["validation_id", "platform", "data_class", "source_count", "destination_count", "variance", "sample_size", "permission_test", "business_test", "owner", "disposition", "status"], [
        {"validation_id":"VAL-001","platform":"Google Workspace","data_class":"Mail items — pilot","source_count":128450,"destination_count":128442,"variance":8,"sample_size":120,"permission_test":"Pass","business_test":"Pass","owner":"Workspace Lead","disposition":"Eight unsupported/corrupt items documented","status":"Accepted"},
        {"validation_id":"VAL-002","platform":"Google Drive","data_class":"Files — pilot","source_count":38210,"destination_count":38210,"variance":0,"sample_size":150,"permission_test":"Pass with 2 corrected groups","business_test":"Pass","owner":"Workspace Lead","disposition":"Group corrections retested","status":"Accepted"},
        {"validation_id":"VAL-003","platform":"Slack","data_class":"Channels — pilot","source_count":42,"destination_count":42,"variance":0,"sample_size":42,"permission_test":"Pass","business_test":"Two webhooks pending","owner":"Slack Lead","disposition":"Hold production until webhook test","status":"Conditional"},
        {"validation_id":"VAL-004","platform":"Jira","data_class":"Issues — pilot","source_count":18760,"destination_count":18760,"variance":0,"sample_size":80,"permission_test":"Pass","business_test":"Automation regression open","owner":"Atlassian Owner","disposition":"Fix and rerun","status":"Open"},
    ], "M&A migration validation and reconciliation — filled example")

    write_csv(common / "BUDGET.csv", ["cost_id", "work_package", "baseline_usd", "committed_usd", "actual_to_date_usd", "estimate_to_complete_usd", "forecast_usd", "variance_usd", "owner", "basis"], [
        {"cost_id":"C-001","work_package":"Program management and integration office","baseline_usd":220000,"committed_usd":210000,"actual_to_date_usd":132000,"estimate_to_complete_usd":78000,"forecast_usd":210000,"variance_usd":10000,"owner":"Program Manager","basis":"Scenario staffing plan"},
        {"cost_id":"C-002","work_package":"Identity, onboarding, and endpoint","baseline_usd":275000,"committed_usd":269000,"actual_to_date_usd":181000,"estimate_to_complete_usd":88000,"forecast_usd":269000,"variance_usd":6000,"owner":"IAM/Endpoint Lead","basis":"Scenario volume and vendor estimate"},
        {"cost_id":"C-003","work_package":"Network and infrastructure","baseline_usd":310000,"committed_usd":304000,"actual_to_date_usd":228000,"estimate_to_complete_usd":76000,"forecast_usd":304000,"variance_usd":6000,"owner":"Network Lead","basis":"Three-site scenario"},
        {"cost_id":"C-004","work_package":"Google Workspace migration","baseline_usd":240000,"committed_usd":232000,"actual_to_date_usd":142000,"estimate_to_complete_usd":90000,"forecast_usd":232000,"variance_usd":8000,"owner":"Workspace Lead","basis":"610-user scenario"},
        {"cost_id":"C-005","work_package":"Slack, Asana, and Jira","baseline_usd":185000,"committed_usd":178000,"actual_to_date_usd":104000,"estimate_to_complete_usd":74000,"forecast_usd":178000,"variance_usd":7000,"owner":"Collaboration Lead","basis":"Tool migration scenario"},
        {"cost_id":"C-006","work_package":"Application rationalization and data","baseline_usd":230000,"committed_usd":221000,"actual_to_date_usd":108000,"estimate_to_complete_usd":113000,"forecast_usd":221000,"variance_usd":9000,"owner":"Application Lead","basis":"142-app scenario"},
        {"cost_id":"C-007","work_package":"Security, privacy, and compliance","baseline_usd":160000,"committed_usd":158000,"actual_to_date_usd":96000,"estimate_to_complete_usd":62000,"forecast_usd":158000,"variance_usd":2000,"owner":"Security Lead","basis":"Scenario control plan"},
        {"cost_id":"C-008","work_package":"Change, training, and hypercare","baseline_usd":120000,"committed_usd":113000,"actual_to_date_usd":64000,"estimate_to_complete_usd":49000,"forecast_usd":113000,"variance_usd":7000,"owner":"Change Lead","basis":"Scenario support model"},
        {"cost_id":"C-009","work_package":"Hardware and logistics allowance","baseline_usd":60000,"committed_usd":57000,"actual_to_date_usd":51000,"estimate_to_complete_usd":6000,"forecast_usd":57000,"variance_usd":3000,"owner":"Endpoint Lead","basis":"Scenario exceptions"},
        {"cost_id":"C-010","work_package":"Management reserve","baseline_usd":60000,"committed_usd":40000,"actual_to_date_usd":20000,"estimate_to_complete_usd":20000,"forecast_usd":40000,"variance_usd":20000,"owner":"Sponsor","basis":"Draw only by approved change"},
    ], "M&A integration budget baseline and forecast — filled example")

    build_source_register(common / "SOURCE_REGISTER.csv", [*PMI_SOURCES, *MA_TECH_SOURCES], "M&A authoritative source register")

    build_ma_agile(agile, common)
    build_ma_predictive(predictive, common)


def build_ma_agile(base: Path, common: Path) -> None:
    write(base / "PLAYBOOK.md", document(
        "M&A IT Integration — Agile Delivery Playbook",
        "Run the same controlled M&A scope through outcome-based, iterative delivery while preserving fixed legal-close and Day 1 gates.",
        f"""## Tailoring decision

Use Agile where discovery changes the solution: identity mapping, network flows, collaboration edge cases, application dispositions, and user experience. Treat legal close, Day 1, security/privacy approvals, contract dates, and destructive decommission actions as fixed constraints. This is not ungoverned continuous change.

## Product goal and value streams

**Product goal:** acquired workers perform priority work securely on Day 1, then Company ABC progressively converges technology and removes temporary risk/cost with measured acceptance.

{table(["Value stream", "Outcome", "Increment"], [
    ["Employee experience", "Ready identity, device, tools, support", "Persona-tested cohort"],
    ["Secure connectivity", "Required flows with least privilege and monitoring", "Approved site/application route set"],
    ["Collaboration", "Accessible, reconciled, policy-compliant content", "Accepted migration batch"],
    ["Application portfolio", "Owned dispositions and safe retirements", "Accepted app decision/migration/decommission"],
    ["Operations", "Stable service and closed temporary controls", "Handoff package + benefits owner"],
  ])}

## Cadence

- Two-week sprints; daily 15-minute workstream synchronization; twice-weekly cross-stream dependency review.
- Sprint planning commits only ready work within capacity. Day 1 blockers receive highest class of service.
- Sprint review demonstrates working evidence to business/security/service owners: login, route, migrated content, application workflow, dashboard, or runbook—not slide completion.
- Retrospective selects one measurable improvement and an owner; the next sprint verifies its effect.
- Steering reviews outcome burn-up, fixed-date confidence, budget/forecast, critical risks, benefit evidence, and decisions.

## Release model

Sprint increments accumulate into four releases: readiness foundation, Day 1 minimum viable experience, migration waves, and convergence/closure. Each release uses the shared go/no-go, rollback, security, data, and operations gates.

## Agile controls

Backlog items link to outcome, acceptance, owner, dependency, evidence, risk, and target release. Scope may be reordered; acceptance and regulatory controls are not deleted to preserve velocity. Forecasts use completed evidence and flow, not optimistic percentage complete.
""",
        ["product goal", "outcomes/value streams", "roles/accountabilities", "sprint length and events", "backlog fields", "release map", "fixed constraints", "definition of ready/done", "metrics", "governance and escalation"],
    ))

    write(base / "WORKING_AGREEMENT_AND_CEREMONIES.md", document(
        "M&A Agile Working Agreement and Ceremonies",
        "Make cross-functional behavior, evidence, escalation, and meeting outputs explicit.",
        f"""## Working agreement

- One prioritized integration backlog; workstream spreadsheets may support execution but may not create hidden commitments.
- Work starts only with an owner, acceptance, dependency state, data/security classification, and target release.
- No more than two active critical items per workstream; finish validation before starting another migration batch.
- A blocker older than one business day is escalated to the Integration Management Office; a Day 1 blocker is escalated immediately.
- Technical evidence is attached to the item; dashboards never infer green from a meeting statement.

## Event design

{table(["Event", "Timebox", "Required input", "Output"], [
    ["Sprint planning", "2 hours", "Ordered ready backlog, capacity, fixed-date risks", "Sprint goal and forecast"],
    ["Daily integration sync", "15 minutes", "Blockers, dependency changes, next validation", "Owner/action/escalation updates"],
    ["Backlog refinement", "90 minutes weekly", "Discovery, acceptance, risk, size", "Ready candidates and split items"],
    ["Sprint review", "90 minutes", "Working evidence", "Acceptance, feedback, backlog change"],
    ["Retrospective", "60 minutes", "Flow, quality, incident, feedback data", "One improvement experiment"],
    ["Release readiness", "Per gate", "Shared control pack", "Go/conditional go/hold"],
  ])}
""",
        ["team norms", "start/finish policies", "WIP expectations", "blocker escalation", "event timeboxes", "required attendees", "inputs/outputs", "decision recording", "retrospective follow-through"],
    ))

    write(base / "DEFINITION_OF_READY_DONE.md", document(
        "M&A Agile Definition of Ready and Definition of Done",
        "Stop ambiguous work from entering delivery and stop partially validated work from being reported as complete.",
        """## Definition of Ready

- Outcome/user or service is identified; accountable owner and acceptance authority are named.
- Scope, affected cohort/system/data, dependencies, assumptions, risks, and target release are visible.
- Security, privacy, legal hold, architecture, procurement, and change impacts are classified; required reviewers are engaged.
- Test data/environment and rollback approach are feasible; external vendor capacity is confirmed where required.
- Acceptance is observable and measurable, with numerator/denominator or specific test evidence.

## Definition of Done

- Build/configuration/migration is completed and peer reviewed under change control.
- Functional, security, data reconciliation, permission, monitoring, failure, and business workflow tests pass or have an approved exception.
- Documentation, CMDB/inventory, ownership, knowledge, communications, and support routing are updated.
- Temporary access, files, rules, licenses, and migration accounts have an owner and expiry.
- Acceptance evidence is attached; accountable business/technical owner accepts; dashboard source is updated.

## Not done

Tool reports success but counts/permissions are unvalidated; a pilot passes without representative personas; a defect has no owner/due date/workaround; a source is disabled without accepted data/recovery; or a document is complete without an operating control.
""",
        ["ready criteria", "done criteria", "required evidence", "approvers", "exception rule", "quality thresholds", "operational updates", "temporary-control closure"],
    ))

    write_csv(base / "OUTCOME_ROADMAP.csv", ["release", "sprints", "outcome", "scope", "exit_evidence", "fixed_date", "owner", "status"], [
        {"release":"R1 Foundation","sprints":"1-2","outcome":"Known, governed integration baseline","scope":"Roster, inventory, target decisions, designs, pilots, support readiness","exit_evidence":"Charter, maps, risks, pilot results, Day 1 forecast","fixed_date":"T-1 sprint","owner":"Program Manager","status":"Complete"},
        {"release":"R2 Day 1","sprints":"3-4","outcome":"Secure minimum viable employee experience","scope":"Identities, devices, collaboration bridge, priority apps, support","exit_evidence":"665/680 fully ready; 15 controlled exceptions","fixed_date":"Legal close + Day 1","owner":"Day 1 Lead","status":"Accepted with exceptions"},
        {"release":"R3 Migration waves","sprints":"5-8","outcome":"Accepted data/tool/site increments","scope":"Workspace, Slack, Asana, Jira, network, app cohorts","exit_evidence":"Batch reconciliation, business acceptance, rollback closed","fixed_date":"None; contract milestones","owner":"Workstream Leads","status":"In progress"},
        {"release":"R4 Converge and close","sprints":"9-10","outcome":"Temporary controls removed; operations and benefits owned","scope":"Decommission, license exit, handoff, financial close, lessons","exit_evidence":"Service acceptance and benefits owners","fixed_date":"Week 20","owner":"Program Manager","status":"Planned"},
    ], "M&A Agile outcome roadmap — filled example")

    write_csv(base / "PRODUCT_BACKLOG.csv", ["item_id", "epic", "story_or_enabler", "outcome", "priority", "estimate_points", "acceptance", "dependency", "risk", "target_sprint", "owner", "status"], [
        {"item_id":"MAA-001","epic":"Day 1","story_or_enabler":"Reconcile HR roster to destination identity","outcome":"Every worker has one controlled identity path","priority":"Must","estimate_points":13,"acceptance":"680 resolved or approved exception; duplicate report zero critical","dependency":"Legal clean-team scope","risk":"MA-R-001","target_sprint":1,"owner":"IAM Lead","status":"Done"},
        {"item_id":"MAA-002","epic":"Network","story_or_enabler":"Resolve four overlapping subnet ranges","outcome":"Safe route exchange","priority":"Must","estimate_points":21,"acceptance":"No overlap advertised; fail/failback and logging pass","dependency":"Complete topology","risk":"MA-R-002","target_sprint":2,"owner":"Network Lead","status":"Done"},
        {"item_id":"MAA-003","epic":"Collaboration","story_or_enabler":"Pilot Workspace mail/calendar/Drive migration","outcome":"Evidence-backed migration pattern","priority":"Must","estimate_points":13,"acceptance":"99.5%+ reconciliation; permissions and holds accepted","dependency":"Identity mapping","risk":"MA-R-003","target_sprint":3,"owner":"Workspace Lead","status":"Done"},
        {"item_id":"MAA-004","epic":"Employee experience","story_or_enabler":"Close 15 Day 1 exceptions","outcome":"Full productivity or approved durable path","priority":"Expedite","estimate_points":8,"acceptance":"Each worker accepted; workaround removed; dashboard reconciled","dependency":"Device/access owners","risk":"MA-I-004","target_sprint":5,"owner":"Day 1 Lead","status":"In progress"},
        {"item_id":"MAA-005","epic":"Slack","story_or_enabler":"Reconfigure critical bots/webhooks after workspace move","outcome":"Critical collaboration automations work","priority":"Must","estimate_points":13,"acceptance":"Owner test for 18 critical integrations","dependency":"Channel/user mapping","risk":"MA-R-003","target_sprint":6,"owner":"Slack Lead","status":"Ready"},
        {"item_id":"MAA-006","epic":"Applications","story_or_enabler":"Retire legacy expense tool after audit archive","outcome":"Remove redundant cost without control loss","priority":"Should","estimate_points":21,"acceptance":"Open items closed; archive/audit/business accepted; contract stopped","dependency":"Finance workflow migration","risk":"Data loss","target_sprint":9,"owner":"Finance App Owner","status":"Refining"},
    ], "M&A Agile product backlog — representative filled example")

    write_csv(base / "SPRINT_PLAN.csv", ["sprint", "weeks", "sprint_goal", "forecast_points", "completed_points", "key_increment", "day1_confidence", "top_blocker", "review_decision", "status"], [
        {"sprint":1,"weeks":"1-2","sprint_goal":"Establish trusted baselines and decisions","forecast_points":62,"completed_points":58,"key_increment":"Roster/inventory/control baseline","day1_confidence":"72%","top_blocker":"Legal data-movement scope","review_decision":"Continue; split legal-dependent work","status":"Complete"},
        {"sprint":2,"weeks":"3-4","sprint_goal":"Prove Day 1 paths and safe connectivity","forecast_points":64,"completed_points":61,"key_increment":"Persona pilots and collision plan","day1_confidence":"91%","top_blocker":"Three device exceptions","review_decision":"Conditional Day 1 go","status":"Complete"},
        {"sprint":3,"weeks":"5-6","sprint_goal":"Stabilize Day 1 and prove migration patterns","forecast_points":60,"completed_points":57,"key_increment":"Hypercare + Workspace/Slack pilots","day1_confidence":"Accepted","top_blocker":"Jira automation regression","review_decision":"Hold Jira production wave","status":"Complete"},
        {"sprint":4,"weeks":"7-8","sprint_goal":"Accept first production migration cohorts","forecast_points":59,"completed_points":0,"key_increment":"Workspace/Asana batches and network site","day1_confidence":"Accepted","top_blocker":"Pending legal-hold sample","review_decision":"Open","status":"Active"},
    ], "M&A Agile sprint plan and review record — filled example")

    write_csv(base / "AGILE_METRICS.csv", ["period", "planned_points", "done_points", "throughput_items", "median_cycle_days", "p85_cycle_days", "escaped_defects", "blocked_items", "outcome_measure", "interpretation"], [
        {"period":"Sprint 1","planned_points":62,"done_points":58,"throughput_items":17,"median_cycle_days":4.1,"p85_cycle_days":8.6,"escaped_defects":1,"blocked_items":3,"outcome_measure":"Roster confidence 96.4%","interpretation":"Split legal-dependent work earlier"},
        {"period":"Sprint 2","planned_points":64,"done_points":61,"throughput_items":19,"median_cycle_days":3.8,"p85_cycle_days":7.2,"escaped_defects":2,"blocked_items":2,"outcome_measure":"Day 1 ready 97.8%","interpretation":"Device exceptions need earlier logistics trigger"},
        {"period":"Sprint 3","planned_points":60,"done_points":57,"throughput_items":18,"median_cycle_days":3.5,"p85_cycle_days":6.9,"escaped_defects":1,"blocked_items":1,"outcome_measure":"Pilot reconciliation 99.7%","interpretation":"Keep identity-first sequencing"},
    ], "M&A Agile delivery and outcome metrics — filled example")

    write(base / "EXECUTIVE_STATUS.md", document(
        "M&A Agile Executive Status — Illustrative Checkpoint",
        "Show an executive decision view that connects flow, value, fixed-date confidence, risk, finance, and asks.",
        f"""## Overall: Amber — controlled exceptions, migration pattern proven

{table(["Dimension", "Status", "Evidence", "Decision / next action"], [
    ["Day 1", "Accepted with exceptions", "665/680 fully ready; all 15 exceptions owned", "Close exceptions by Day 3"],
    ["Identity/network", "Green", "674/680 authentication; four collisions resolved", "Remove bridge only after wave acceptance"],
    ["Collaboration", "Amber", "Workspace pilot accepted; Slack webhooks/Jira automation open", "Hold affected production scope"],
    ["Applications", "Amber", "142 discovered; dispositions progressing", "Escalate five ownerless Tier 2 apps"],
    ["Finance", "Green", "$1.782M forecast vs $1.860M authorization", "Protect reserve; validate realized savings"],
  ])}

## Sprint evidence

Three sprints completed 176 of 186 forecast points, but the steering decision uses accepted increments and business outcomes—not velocity alone. P85 cycle time improved from 8.6 to 6.9 business days; one active blocker is the Jira automation regression.

## Decisions requested

1. Approve a one-sprint delay to the Jira production cohort without moving the final program date.
2. Confirm retention extension for the source collaboration environment until legal-hold sampling closes.
3. Confirm the five ownerless Tier 2 applications may be restricted pending accountable ownership.
""",
        ["reporting period", "overall health and rationale", "outcome measures", "release/sprint evidence", "budget/forecast", "top risks/issues", "decisions/asks", "next milestones", "confidence and source links"],
    ))

    write(base / "ARTIFACT_INDEX.md", document(
        "M&A Agile Playbook Artifact Index",
        "Provide the ordered review sequence for a complete Agile M&A integration.",
        """## Method-specific sequence

1. `PLAYBOOK.md` — tailoring, product goal, cadence, release model, and controls.
2. `OUTCOME_ROADMAP.csv` — releases and value evidence.
3. `PRODUCT_BACKLOG.csv` — prioritized, accepted work.
4. `SPRINT_PLAN.csv` — sprint goals, forecasts, reviews, and decisions.
5. `WORKING_AGREEMENT_AND_CEREMONIES.md` — flow and meeting outputs.
6. `DEFINITION_OF_READY_DONE.md` — quality boundaries.
7. `AGILE_METRICS.csv` — flow, quality, and outcome evidence.
8. `EXECUTIVE_STATUS.md` — steering view and asks.

## Shared controls used by this playbook

The complete playbook also includes every artifact in `../common/`: charter, governance, Day 1, identity, network, collaboration, applications, security/privacy, change/training, cutover/hypercare, vendor/budget, RAID, dependencies, RACI, application portfolio, readiness, validation, budget, and source register.
""",
        ["method artifacts", "shared controls", "artifact owner", "status/version", "approval", "dashboard link", "archive/retention"],
    ))


def build_ma_predictive(base: Path, common: Path) -> None:
    write(base / "PLAYBOOK.md", document(
        "M&A IT Integration — Predictive / Waterfall Playbook",
        "Run the controlled M&A integration through formal predictive baselines, stage gates, and integrated change control aligned to PMBOK Guide Eighth Edition.",
        f"""## Tailoring decision

Use predictive delivery when scope and target architecture can be baselined, vendor milestones and legal-close dates require formal dependencies, and steering expects phase authorization. Discovery still occurs early; unknowns are not forced into false precision. Approved change control protects—not prevents—necessary adaptation.

## PMBOK 8 alignment

{table(["PMBOK 8 element", "Applied control"], [
    ["Six principles", "Holistic integration view; value outcomes; quality embedded in acceptance; accountable leadership; sustainability/asset reuse; empowered cross-functional teams"],
    ["Seven performance domains", "Governance, scope, schedule, finance, stakeholders, resources, and risk each have baselines, owners, measures, and evidence"],
    ["Predictive process groups", "Initiating, Planning, Executing, Monitoring and Controlling, Closing provide the lifecycle spine"],
    ["Tailoring", "Formal gates for legal/security/data/decommissioning; rolling-wave detail only where discovery is incomplete"],
  ])}

## Phase model

1. Initiate and due diligence: mandate, clean-team scope, assumptions, stakeholder and risk framing.
2. Plan and design: baselines, requirements, architecture, procurement, quality, change, cutover, and operations plans.
3. Build and test: identities, endpoints, network, migration factories, application actions, pilots, and readiness.
4. Day 1 and execute waves: controlled release, validation, issues, rollback, and communications.
5. Monitor/control and converge: performance, changes, risk, financials, data, vendor, quality, and benefits.
6. Close: operations acceptance, source decommission, financial/vendor closure, lessons, and benefits ownership.

## Integrated change control

Any change to approved scope, milestone, budget, acceptance, security/privacy control, target state, or benefit requires impact on dependencies, risk, resources, contracts, communications, operations, and rollback. The Change Control Board recommends; the sponsor or delegated authority approves within threshold.
""",
        ["tailoring rationale", "process groups and performance domains", "scope/WBS baseline", "schedule/cost baseline", "quality/acceptance", "governance/stage gates", "change control", "risk/resource/stakeholder controls", "closure and benefits"],
    ))

    write(base / "PMBOK8_ALIGNMENT.md", document(
        "M&A Predictive PMBOK 8 Alignment Matrix",
        "Show how the playbook operationalizes the current standard without reproducing or misrepresenting it.",
        f"""## Principles

{table(["Principle", "Portfolio application", "Evidence"], [
    ["Adopt a holistic view", "One dependency model across people, identity, device, network, SaaS, applications, contracts, support, and benefits", "Dependency matrix and integrated schedule"],
    ["Focus on value", "Day 1 productivity, secure continuity, rationalized cost, and accepted operations", "Charter measures and benefits ownership"],
    ["Embed quality", "Acceptance, reconciliation, permissions, rollback, monitoring, and business workflow built into each work package", "Quality plan and validation register"],
    ["Lead accountably", "Named decision authorities and risk acceptance", "Governance/RACI/decision log"],
    ["Integrate sustainability", "Reuse viable assets, prevent dual-license tail, dispose of hardware/data responsibly", "Application, asset, contract, and closure controls"],
    ["Build empowered teams", "Workstream leads own evidence and may stop unsafe work", "Charter authority and gate model"],
  ])}

## Performance domains

{table(["Domain", "Primary plan/control", "Measure"], [
    ["Governance", "Charter, decision rights, stage gates, change control", "Decision age and gate conditions"],
    ["Scope", "Requirements, WBS, application/data boundary", "Accepted deliverables and change"],
    ["Schedule", "Integrated master schedule and dependencies", "Critical path, SPI, milestone variance"],
    ["Finance", "Budget, commitments, actuals, ETC/EAC, reserve", "CPI and forecast variance"],
    ["Stakeholders", "Stakeholder/change/support plan", "Readiness, adoption, unresolved decisions"],
    ["Resources", "Named workstreams, vendor capacity, command staffing", "Capacity and skill gaps"],
    ["Risk", "RAID, security/privacy, rollback and contingency", "Exposure, aging, trigger response"],
  ])}

## Terminology note

PMBOK Guide Eighth Edition is delivery-approach neutral. This portfolio calls the plan “Predictive / Waterfall” because work is baselined and sequenced through formal gates; it does not claim PMBOK mandates waterfall.
""",
        ["standard/version/date", "principles", "performance domains", "process groups", "tailoring choices", "artifact/control mapping", "evidence and owner", "gaps/exceptions"],
    ))

    write(base / "STAGE_GATES_AND_CHANGE_CONTROL.md", document(
        "M&A Predictive Stage Gates and Integrated Change Control",
        "Define authorization points and protect baselines while allowing evidence-backed change.",
        f"""## Stage gates

{table(["Gate", "Required evidence", "Approvers", "Possible decision"], [
    ["G0 Mandate", "Deal intent, clean-team restrictions, sponsor, initial outcomes", "CIO + Corp Dev + Legal", "Authorize discovery"],
    ["G1 Baseline", "Charter, scope/WBS, schedule/cost, risks, governance, target decisions", "Steering Committee", "Approve baseline / recover"],
    ["G2 Design", "Identity/network/data/security designs, vendor plan, test/rollback", "Design Authority + Security", "Authorize build/pilot"],
    ["G3 Day 1", "Readiness, tests, support, communications, contingency", "Sponsor + Security + Business", "Go / conditional go / hold"],
    ["G4 Migration waves", "Pilot results, batch plan, reconciliation, rollback", "Business/Data/Technical Owners", "Release batch"],
    ["G5 Decommission", "Accepted destination, retention/hold, access/contract plan", "Business + Legal + Security", "Retire / extend"],
    ["G6 Close", "Handoff, financial/vendor closure, risks, lessons, benefit owners", "Sponsor + Operations", "Accept closure"],
  ])}

## Change thresholds

- Level 1: workstream may approve within existing scope/cost/date and no control impact.
- Level 2: PM/CCB approves cumulative work-package variance up to $25,000 or five business days without final milestone impact.
- Level 3: steering approves scope/target-state/control change, reserve draw, final milestone impact, or forecast above 5%.
- Emergency: incident/change authority acts to protect service/security, then documents retrospective approval and baseline impact.

## Change record minimum

Problem/opportunity, options including no change, scope/schedule/cost/resource/quality/risk/security/privacy/contract/benefit impacts, dependencies, implementation, validation, rollback, recommendation, decision, conditions, and baseline updates.
""",
        ["gate names and criteria", "approvers/quorum", "decision options", "change thresholds", "change form", "impact analysis", "emergency rule", "baseline update", "decision log"],
    ))

    write(base / "QUALITY_MANAGEMENT_PLAN.md", document(
        "M&A Predictive Quality Management Plan",
        "Plan prevention, verification, validation, acceptance, defect control, and audit evidence across every workstream.",
        f"""## Quality objectives

{table(["Object", "Quality requirement", "Measure / acceptance"], [
    ["Identity", "Unique, least-privilege, recoverable, logged", "100% roster disposition; privileged access review"],
    ["Network", "Non-overlapping, restricted, available, observable", "No unresolved collisions; Tier 0/1 flow/failover/log tests"],
    ["Data", "Complete within defined exclusions, permission-correct, retained", "99.5%+ counts plus samples, permissions, holds"],
    ["Applications", "Critical workflows and integrations work; owner/support known", "Owner acceptance and regression tests"],
    ["Employee experience", "Priority personas productive and supported", "98% ready; 99% priority access or approved exception"],
    ["Operations", "Monitoring, knowledge, on-call, CMDB and vendors accepted", "Service-owner signature and stable hypercare"],
  ])}

## Assurance flow

Requirements trace to design, build/configuration, test script, result, defect, acceptance, and operating evidence. Technical completion is verified by the delivery team; business suitability is validated by the accountable business/service owner. Defects are classified by user/service/security impact and may not be downgraded to protect a milestone.

## Audit sample

At each gate, Quality samples 10% or at least five deliverables per workstream, plus 100% of Tier 0, privileged, legal-hold, and destructive actions. Findings have owners and due dates; repeat failures trigger process correction, not just item correction.
""",
        ["quality objectives", "standards/policies", "requirements traceability", "verification/validation methods", "sampling", "defect severity/SLA", "acceptance authorities", "quality reporting", "continuous improvement"],
    ))

    write_csv(base / "WBS.csv", ["wbs", "control_account", "work_package", "deliverable", "owner", "planned_start", "planned_finish", "acceptance", "predecessor", "budget_usd", "status"], [
        {"wbs":"1.0","control_account":"Program governance","work_package":"Initiation and baselines","deliverable":"Approved charter, governance, scope, IMS, cost and risk baselines","owner":"Program Manager","planned_start":"W1","planned_finish":"W4","acceptance":"G1 approval","predecessor":"Deal mandate","budget_usd":220000,"status":"Complete"},
        {"wbs":"2.0","control_account":"Day 1","work_package":"Roster, identity, device, access, support","deliverable":"Day 1 minimum viable employee experience","owner":"Day 1 Lead","planned_start":"W1","planned_finish":"W6","acceptance":"G3; 98% ready and controlled exceptions","predecessor":"Legal close","budget_usd":335000,"status":"Accepted with exceptions"},
        {"wbs":"3.0","control_account":"Infrastructure","work_package":"Network/site/cloud integration","deliverable":"Secure interconnect, standardized network and operations handoff","owner":"Network Lead","planned_start":"W3","planned_finish":"W14","acceptance":"Design, functional, failover, monitoring, owner acceptance","predecessor":"Collision remediation","budget_usd":310000,"status":"In progress"},
        {"wbs":"4.0","control_account":"Collaboration","work_package":"Workspace/Slack/Asana/Jira migrations","deliverable":"Accepted users/data/integrations and source exit plan","owner":"Collaboration Lead","planned_start":"W4","planned_finish":"W18","acceptance":"99.5% reconciliation and business acceptance","predecessor":"Identity mapping","budget_usd":425000,"status":"In progress"},
        {"wbs":"5.0","control_account":"Applications/data","work_package":"Rationalize 142 applications","deliverable":"Disposition, migrations/archives, retirements, reporting","owner":"Application Lead","planned_start":"W2","planned_finish":"W22","acceptance":"142/142 dispositions; safe retirement evidence","predecessor":"Owner/data discovery","budget_usd":230000,"status":"In progress"},
        {"wbs":"6.0","control_account":"Assurance/change","work_package":"Security, privacy, training, hypercare","deliverable":"Control evidence, adoption, support and stable service","owner":"Security + Change Leads","planned_start":"W1","planned_finish":"W24","acceptance":"No unresolved Sev 1; service acceptance","predecessor":"All work packages","budget_usd":280000,"status":"In progress"},
        {"wbs":"7.0","control_account":"Reserve","work_package":"Management reserve","deliverable":"Sponsor-controlled uncertainty response","owner":"Sponsor","planned_start":"W1","planned_finish":"W24","acceptance":"Approved draws only","predecessor":"Approved change","budget_usd":60000,"status":"Protected"},
    ], "M&A Predictive work breakdown structure and control accounts — filled example")

    write_csv(base / "INTEGRATED_MASTER_SCHEDULE.csv", ["activity_id", "wbs", "activity", "duration_days", "predecessors", "baseline_start", "baseline_finish", "forecast_finish", "critical", "owner", "acceptance", "status"], [
        {"activity_id":"IMS-001","wbs":"1.0","activity":"Authorize mandate and clean-team discovery","duration_days":5,"predecessors":"None","baseline_start":"W1","baseline_finish":"W1","forecast_finish":"W1","critical":"Yes","owner":"Sponsor/Legal","acceptance":"G0 approval","status":"Complete"},
        {"activity_id":"IMS-010","wbs":"1.0","activity":"Baseline scope, WBS, schedule, cost, governance and risk","duration_days":15,"predecessors":"IMS-001","baseline_start":"W2","baseline_finish":"W4","forecast_finish":"W4","critical":"Yes","owner":"Program Manager","acceptance":"G1 approval","status":"Complete"},
        {"activity_id":"IMS-020","wbs":"2.0","activity":"Reconcile roster, identities, devices and persona access","duration_days":20,"predecessors":"IMS-001","baseline_start":"W1","baseline_finish":"W4","forecast_finish":"W4","critical":"Yes","owner":"Day 1 Lead","acceptance":"Readiness baseline","status":"Complete"},
        {"activity_id":"IMS-030","wbs":"2.0","activity":"Execute Day 1 and two-week hypercare","duration_days":10,"predecessors":"IMS-020, legal close","baseline_start":"W5","baseline_finish":"W6","forecast_finish":"W6","critical":"Yes","owner":"Command Lead","acceptance":"G3 + hypercare exit","status":"Complete with exceptions"},
        {"activity_id":"IMS-040","wbs":"3.0","activity":"Design/test network interconnect and collision remediation","duration_days":30,"predecessors":"IMS-010","baseline_start":"W4","baseline_finish":"W9","forecast_finish":"W9","critical":"Yes","owner":"Network Lead","acceptance":"G2 and site pilot","status":"In progress"},
        {"activity_id":"IMS-050","wbs":"4.0","activity":"Pilot collaboration migrations","duration_days":20,"predecessors":"IMS-020","baseline_start":"W5","baseline_finish":"W8","forecast_finish":"W8","critical":"Yes","owner":"Collaboration Lead","acceptance":"Pilot reconciliation/business sign-off","status":"In progress"},
        {"activity_id":"IMS-060","wbs":"4.0","activity":"Execute collaboration production waves","duration_days":50,"predecessors":"IMS-050, IMS-040","baseline_start":"W9","baseline_finish":"W18","forecast_finish":"W19","critical":"Yes","owner":"Collaboration Lead","acceptance":"Batch acceptance","status":"Forecast +1 week"},
        {"activity_id":"IMS-070","wbs":"5.0","activity":"Approve and execute application dispositions","duration_days":75,"predecessors":"IMS-010","baseline_start":"W6","baseline_finish":"W20","forecast_finish":"W21","critical":"No","owner":"Application Lead","acceptance":"142/142 disposition/evidence","status":"In progress"},
        {"activity_id":"IMS-080","wbs":"6.0","activity":"Decommission temporary controls and transfer services","duration_days":15,"predecessors":"IMS-060, IMS-070","baseline_start":"W21","baseline_finish":"W23","forecast_finish":"W23","critical":"Yes","owner":"Operations Leads","acceptance":"G5/service acceptance","status":"Planned"},
        {"activity_id":"IMS-090","wbs":"1.0","activity":"Close program and transfer benefits","duration_days":5,"predecessors":"IMS-080","baseline_start":"W24","baseline_finish":"W24","forecast_finish":"W24","critical":"Yes","owner":"Program Manager","acceptance":"G6","status":"Planned"},
    ], "M&A Predictive integrated master schedule — filled example")

    write_csv(base / "EARNED_VALUE.csv", ["status_period", "bac_usd", "pv_usd", "ev_usd", "ac_usd", "sv_usd", "cv_usd", "spi", "cpi", "eac_usd", "vac_usd", "milestone_forecast", "management_interpretation"], [
        {"status_period":"End Week 8","bac_usd":1860000,"pv_usd":710000,"ev_usd":682000,"ac_usd":668000,"sv_usd":-28000,"cv_usd":14000,"spi":0.96,"cpi":1.02,"eac_usd":1824000,"vac_usd":36000,"milestone_forecast":"Final Week 24 unchanged; collaboration +1 week recovered in float","management_interpretation":"Schedule watch; cost favorable; validate quality and do not trade control for SPI"},
        {"status_period":"End Week 12","bac_usd":1860000,"pv_usd":1080000,"ev_usd":1048000,"ac_usd":1029000,"sv_usd":-32000,"cv_usd":19000,"spi":0.97,"cpi":1.02,"eac_usd":1782000,"vac_usd":78000,"milestone_forecast":"Final Week 24","management_interpretation":"Jira scope held; reserve remains protected"},
    ], "M&A Predictive earned value status — filled example")

    write(base / "EXECUTIVE_STATUS.md", document(
        "M&A Predictive Executive Status — Illustrative Checkpoint",
        "Show baseline, variance, forecast, controls, and decisions for the predictive playbook.",
        f"""## Overall: Amber — schedule watch inside final milestone

{table(["Control", "Baseline / target", "Current evidence", "Forecast / action"], [
    ["Schedule", "Week 24 finish", "SPI 0.97 at Week 12; collaboration wave +1 week", "Recover within available float; hold Jira cohort"],
    ["Cost", "$1.860M BAC", "CPI 1.02; $1.782M EAC", "$78K favorable if remaining assumptions hold"],
    ["Day 1", "98% ready", "665/680 = 97.8%; 15 controlled exceptions", "Close by Day 3; no change to acceptance truth"],
    ["Quality", "99.5% data reconciliation", "Workspace pilot 99.7%; Jira automation regression open", "No production Jira release"],
    ["Risk", "No unowned critical exposure", "Identity/network mitigations active", "Steering decisions due this week"],
  ])}

## Baseline and change

No Level 3 change has been approved. One Level 2 schedule recovery moves a noncritical application-disposition activity within float. The Jira production cohort is held by quality control and is not counted as complete.

## Decisions requested

1. Approve the source-retention extension while legal-hold sampling completes.
2. Confirm five ownerless Tier 2 applications may be restricted until ownership is assigned.
3. Endorse the recovery plan that preserves the Week 24 finish without reducing tests or rollback.
""",
        ["status date", "overall health", "baseline/actual/forecast", "EVM and milestones", "quality/acceptance", "RAID", "changes", "decisions", "next gates", "evidence/confidence"],
    ))

    write(base / "ARTIFACT_INDEX.md", document(
        "M&A Predictive Playbook Artifact Index",
        "Provide the ordered review sequence for a complete PMBOK 8-aligned predictive M&A integration.",
        """## Method-specific sequence

1. `PLAYBOOK.md` — tailoring, lifecycle, baselines, and change control.
2. `PMBOK8_ALIGNMENT.md` — principles, performance domains, process groups, and terminology.
3. `WBS.csv` — control accounts and accepted deliverables.
4. `INTEGRATED_MASTER_SCHEDULE.csv` — dependencies, critical path, baseline, and forecast.
5. `STAGE_GATES_AND_CHANGE_CONTROL.md` — authorization and baseline protection.
6. `QUALITY_MANAGEMENT_PLAN.md` — prevention, verification, validation, and acceptance.
7. `EARNED_VALUE.csv` — PV/EV/AC, SPI/CPI, EAC/VAC and interpretation.
8. `EXECUTIVE_STATUS.md` — steering view and decisions.

## Shared controls used by this playbook

The complete playbook also includes every artifact in `../common/`: charter, governance, Day 1, identity, network, collaboration, applications, security/privacy, change/training, cutover/hypercare, vendor/budget, RAID, dependencies, RACI, application portfolio, readiness, validation, budget, and source register.
""",
        ["method artifacts", "shared controls", "artifact owner", "baseline/version", "approval", "dashboard link", "archive/retention"],
    ))


def build_hardware() -> None:
    common = HW / "common"
    kanban = HW / "kanban"
    scrum = HW / "scrum"
    predictive = HW / "predictive"
    hybrid = HW / "hybrid"

    write(common / "PORTFOLIO_GUIDE.md", document(
        "Enterprise Hardware Refresh Portfolio Guide",
        "Explain how to review one real-world endpoint control pack through Kanban, Scrum, Predictive, and Hybrid operating models.",
        f"""## Case boundary

Company ABC refreshes 360 end-user devices across four sites: 270 laptops, 60 desktops, and 30 mobile phones. The scope includes requirements, standards, procurement, staging, imaging/provisioning, application and data readiness, user communications, deployment waves, exceptions, hypercare, asset reconciliation, secure sanitization, operations transition, and closure.

## Playbook architecture

{table(["Layer", "Contents", "Method decision"], [
    ["Shared execution controls", "Charter, device standard, procurement/logistics, application/data readiness, security/compliance, communications, deployment, service transition, retirement, RAID/RACI/inventory/waves/validation/sanitization/budget", "Mandatory regardless of method"],
    ["Kanban", "Pull system, WIP limits, service classes, explicit policies, flow metrics", "Best for continuous site/device demand with variable exceptions"],
    ["Scrum", "Product goal, backlog, nine two-week Sprints, working increments, review/retro", "Best when the cross-functional team can deliver accepted wave increments"],
    ["Predictive / Waterfall", "PMBOK 8-aligned WBS, IMS, baselines, stage gates, change control, EVM", "Best for fixed multi-site sequence and procurement commitments"],
    ["Hybrid", "Predictive guardrails and gates plus rolling-wave pull delivery", "Best for fixed compliance/procurement with uncertain user/app exceptions"],
  ])}

## Scenario truth boundary

This is a fictional case informed by verified supplied experience: modern management across 37,000 Macs and 300,000 Windows devices; zero-touch deployment; Jamf, Intune, SCCM/MECM, ServiceNow, BeyondTrust, Tanium, and endpoint telemetry; 98% OS compliance; endpoint standards; audit partnership; onboarding; multi-site/store/pharmacy support; vendor and budget management; and Scrum/Kanban leadership. The 360-device results, dates, rates, and costs below are planning assumptions, not prior-employer claims.

## Review path

Open a method dashboard, inspect its delivery controls, then open shared inventory, wave, application, data, sanitization, RAID, budget, and closeout evidence. Compare how the same scope changes under each operating model without weakening security or asset accountability.
""",
        ["business mandate", "site/device/persona baseline", "device and security standards", "delivery-method rationale", "budget/schedule", "success measures", "operating transition", "benefit owner"],
    ))

    write(common / "ASSUMPTIONS_AND_EXPERIENCE_MAP.md", document(
        "Hardware Refresh Assumptions, Evidence, and Experience Map",
        "Separate career evidence, public guidance, scenario inputs, calculations, and discovery unknowns.",
        f"""## Experience-to-control trace

{table(["Verified experience", "Control informed", "Scenario boundary"], [
    ["37K Macs / 300K Windows modern management", "Scale-aware inventory, deployment, policy, telemetry, and support", "Only 360 devices are modeled here"],
    ["98% OS compliance", "Compliance definition and post-deployment reporting", "The case compliance rate is fictional"],
    ["Intune, SCCM/MECM, Jamf, ServiceNow, Tanium, BeyondTrust", "Provisioning, device management, workflow, remote support, telemetry", "Tool availability/licensing must be verified at Company ABC"],
    ["Endpoint standards and audit partnership", "Device build, encryption, least privilege, evidence, sanitization", "No certification or regulatory opinion is claimed"],
    ["Scrum and Kanban leadership", "Backlog, ceremonies, flow, WIP, metrics, and continuous improvement", "Method outcomes are modeled"],
  ])}

## Scenario baseline

- Four sites; 360 devices: 270 laptops, 60 desktops, 30 phones.
- Company ABC uses Microsoft Intune/Entra for the target Windows/mobile control plane and SCCM/MECM for selected existing-device reimage/co-management paths; a final design must validate actual tenant/licensing and device mix.
- OneDrive Known Folder Move or the approved enterprise backup path protects user data before swap; application data outside approved locations requires explicit handling.
- 344 devices are deployed at the illustrative checkpoint; 16 are controlled exceptions, not silently removed from scope.
- Secure reuse/disposal follows the organization’s sanitization program aligned to NIST SP 800-88 Rev. 2 and approved standards/vendors.

## Unknowns before a real baseline

Actual user/device assignment, hardware age/warranty, remote users, accessibility needs, application/package readiness, local data, network/staging capacity, procurement lead times, licensing, tax/shipping, e-waste requirements, data classification, legal hold, union/work rules, blackout periods, and site operating calendars.
""",
        ["evidence item", "class", "source/owner", "confidence", "validation date", "planning impact", "replacement evidence"],
    ))

    write(common / "PROJECT_CHARTER.md", document(
        "Enterprise Hardware Refresh Project Charter",
        "Authorize the 360-device, four-site refresh and define outcome, scope, authority, budget, and acceptance.",
        f"""## Filled example

{table(["Charter element", "Scenario baseline"], [
    ["Sponsor", "Company ABC Vice President, Information Technology"],
    ["Project manager", "Technical Project Manager — Endpoint Refresh"],
    ["Outcome", "360 users/device assignments transition to supported, secure, business-ready hardware with minimal disruption and full asset accountability"],
    ["Authorization", "$792,000 including $60,000 management reserve"],
    ["Delivery window", "18 weeks; pilot in Week 6; four production waves Weeks 8-15; hypercare/closure Weeks 16-18"],
    ["In scope", "Laptops, desktops, phones, procurement, staging, provisioning, data/app readiness, waves, exceptions, hypercare, returns, sanitization, reconciliation, transition"],
    ["Out of scope", "Enterprise application replacement, network redesign beyond deployment capacity, unsupported personal-device migration, and office construction"],
  ])}

## Success measures

- 360 of 360 devices have an accountable disposition; 344 deployed and 16 controlled exceptions at the checkpoint.
- At least 97% first-time-right deployments; at least 99% data validation pass or documented no-data path.
- At least 98% devices compliant within 24 hours; zero unresolved Sev 1 security findings at wave release.
- At least 98% returned devices reconciled within five business days; 100% retired media has custody and sanitization/disposition evidence.
- User-impact outage median below 90 minutes and no site-level critical business interruption attributable to the refresh.

## Authority and constraints

The project manager coordinates plans, waves, vendors, status, change, and issue escalation and may stop an unsafe wave. InfoSec owns control approval; Procurement owns sourcing/contracting; Asset Management owns record acceptance; application/business owners accept workflows; Service Operations accepts support transition; authorized records/security owners approve sanitization and disposition.
""",
        ["sponsor/PM", "business outcome", "scope/exclusions", "sites/devices/personas", "milestones", "budget/reserve", "success measures", "constraints/assumptions", "authority", "approvals"],
    ))

    write(common / "GOVERNANCE_AND_DECISION_RIGHTS.md", document(
        "Hardware Refresh Governance, RACI, and Decision Rights",
        "Provide practical steering, delivery, change, exception, and operations forums.",
        f"""## Forums

{table(["Forum", "Cadence", "Decisions", "Output"], [
    ["Steering committee", "Biweekly; weekly during rollout", "Funding, scope, site sequence, risk acceptance, exceptions over threshold", "Decision log and status approval"],
    ["Core delivery", "Twice weekly", "Procurement, build, apps, logistics, communications, wave readiness", "Integrated action/RAID update"],
    ["Technical/change authority", "Weekly and per wave", "Build, policy, application, data, deployment and rollback changes", "Approved change and test evidence"],
    ["Wave go/no-go", "T-5 and T-1 business days", "Release/hold/de-scope/rollback readiness", "Signed wave decision"],
    ["Hypercare review", "Daily during waves", "Incident priorities, root causes, communications, staffing", "Incident and improvement actions"],
  ])}

## Thresholds

- Sponsor/steering: budget forecast above 5%, reserve draw above $15,000, final milestone movement, site sequence change, or risk acceptance.
- Project manager/change authority: within approved scope, no final milestone/control impact, and cumulative work-package change within $15,000.
- Wave lead: same-day operational adjustments within approved runbook and WIP/capacity; no control waiver.
- Immediate stop: suspected data loss/exposure, failed encryption/compliance, missing custody, critical application failure, or site business-impact threshold.
""",
        ["forums", "cadence/quorum", "decision rights", "thresholds", "escalation clock", "change authority", "wave stop authority", "decision log fields"],
    ))

    write(common / "DEVICE_BUILD_AND_PROVISIONING_STANDARD.md", domain_plan(
        "Hardware Refresh Device Build and Provisioning Standard",
        "Define a reproducible business-ready configuration and evidence path for laptops, desktops, and phones.",
        [
            ["Windows laptops/desktops", "OEM image transformed through Windows Autopilot/Intune where feasible; SCCM/MECM task sequence for approved reimage path", "Endpoint Engineering", "Enrollment, policy, app, update, compliance and user test"],
            ["Mobile phones", "Corporate enrollment, required apps, configuration/compliance and number/line validation", "Mobility Lead", "MDM and call/data test"],
            ["Identity", "Microsoft Entra join or approved existing-state transition; standard user by default", "IAM + Security", "Join, MFA, conditional access test"],
            ["Security", "Encryption, supported OS/patch, Defender/EDR, firewall, screen lock, local-admin control", "InfoSec", "Compliance and risk report"],
            ["Supportability", "Asset tag, warranty, owner/site, remote support, monitoring, knowledge and recovery", "Service Operations", "CMDB/inventory and support acceptance"],
        ],
        [
            "Approve persona and model standards, hardware minimums, accessories, warranty, and exception process.",
            "Freeze versioned provisioning profiles, required/available apps, scripts, policies, updates, drivers, and dependencies.",
            "Run clean-device, upgrade/reimage, remote, executive, accessibility, and shared-device pilots.",
            "Capture automated deployment and compliance reports plus manual business workflow evidence.",
            "Release build version only after Endpoint, Security, application owners, Service Desk, and Change approval.",
            "Track build drift; change version and retest affected personas before the next wave.",
        ],
        [
            "Required apps/configuration install successfully or have approved post-login path and owner.",
            "Device reports encryption, supported OS/update, EDR, firewall, and compliance before business release.",
            "Standard user, executive/delegate, shared-device, remote/VPN, accessibility, and Tier 1 app personas pass.",
            "Asset tag/serial/user/site/warranty/build version and management identifiers reconcile.",
        ],
        "Quarantine any device with identity mismatch, missing encryption/EDR, failed critical app, unknown custody, or unsupported configuration. Reissue the prior device where safe, use a validated spare, or re-run the approved build. Do not bypass compliance to meet an appointment metric.",
        ["personas/models", "OS/build/version", "join/enrollment", "security policies", "apps/scripts", "updates/drivers", "accessories", "test matrix", "release approval", "exception/quarantine"],
    ))

    write(common / "PROCUREMENT_STAGING_AND_LOGISTICS.md", domain_plan(
        "Hardware Refresh Procurement, Staging, and Logistics Plan",
        "Control forecasts, purchase orders, receipts, serialized custody, capacity, site kits, shipping, and spares.",
        [
            ["Procurement", "360 devices plus 5% temporary spares where approved; model/accessory standards", "Procurement", "PO, price, lead time, warranty, terms"],
            ["Receipt", "Serialized scan against PO/ASN; damage and shortage exceptions", "Asset Management", "Receipt reconciliation"],
            ["Staging", "Capacity 40 devices/day; network/power/benches/secure storage", "Endpoint Lead", "Daily input/output/defect counts"],
            ["Distribution", "Site kits and remote courier with appointment/user mapping", "Logistics Lead", "Custody scan and delivery confirmation"],
            ["Returns", "Old device collected, quarantine and asset record updated", "Asset Management", "Return aging and chain of custody"],
        ],
        [
            "Forecast by model/persona/site/wave plus spares; validate budget, contract, tax, delivery, warranty, and return terms.",
            "Place and track purchase orders; reconcile order acknowledgment, advanced shipping notice, receipt, invoice, and asset records.",
            "Securely stage, tag, enroll, configure, test, pack, and scan devices against the wave roster.",
            "Pre-position site kits only in approved secure storage; keep user/device/accessory mapping intact.",
            "Record handoff signatures and immediately triage no-show, damage, loss, or wrong-device exceptions.",
            "Reconcile new issue and old return daily; investigate any serial without one authoritative state.",
        ],
        [
            "PO, receipt, invoice, and asset serial quantities reconcile or have approved exceptions.",
            "No device leaves controlled custody without asset tag, assignee/site/wave, build status, and scan.",
            "Staging capacity and defect/rework do not exceed the next wave demand and WIP limit.",
            "Remote delivery and return have tracking, identity verification, and exception escalation.",
        ],
        "Hold shipment or site release for serial mismatch, lost custody, damaged/tampered package, failed build/security, or user mismatch. Quarantine and investigate. Use controlled spare inventory; never substitute an untracked device.",
        ["demand/model forecast", "PO/vendor/price/lead time", "receipt/ASN/invoice", "staging capacity and WIP", "secure storage", "asset scan", "site/remote distribution", "spares", "returns", "exceptions"],
    ))

    write(common / "APPLICATION_AND_DATA_READINESS.md", domain_plan(
        "Hardware Refresh Application and User-Data Readiness Plan",
        "Prove that each persona can access required applications and that approved user data is protected and validated before old-device retirement.",
        [
            ["Application inventory", "76 applications; Tier 0/1 owners and packaging path required", "Application Lead", "Owner, package/version/license/dependency/test"],
            ["Data path", "OneDrive Known Folder Move or approved enterprise backup; exceptions for local/app data", "Data Lead", "Precheck, sync/backup, destination validation"],
            ["User state", "Browser profile, bookmarks, certificates, VPN, printers, accessibility and approved settings", "Endpoint Lead", "Persona checklist"],
            ["Licensing", "Named/concurrent/device licensing and activation", "Application Owner + Procurement", "License capacity and activation test"],
            ["Validation", "User + automated evidence before old device release", "Business Owner", "Task-based acceptance"],
        ],
        [
            "Discover applications from management tools, software inventory, tickets, business owners, and user survey; normalize versions and owners.",
            "Classify criticality, packaging/install method, license, identity, network, driver/peripheral, data, and compatibility dependencies.",
            "Protect approved Desktop/Documents/Pictures and identified application data; resolve sync errors before appointment.",
            "Pilot Tier 0/1 apps and representative personas on each model/build; record defects and workaround expiry.",
            "At swap, validate sign-in, data counts/samples, critical tasks, peripherals, VPN/network, printing, and support access.",
            "Release old device to retirement only after user/data acceptance or a documented no-data/recovery path.",
        ],
        [
            "76 of 76 applications have a disposition; all Tier 0/1 apps have owner, package, license, test, and fallback.",
            "At least 99% of deployed users pass the data checklist or have an approved no-data classification.",
            "Zero old device is sanitized while a data validation or legal-hold exception is open.",
            "Accessibility and specialized peripheral users accept the new workflow before closure.",
        ],
        "If sync/backup is incomplete, critical workflow fails, or a local-data/hold question is open, keep the old device in controlled custody and do not sanitize. Reissue the old device if safe or provide an approved spare/workaround; correct the package/data path and retest.",
        ["applications/personas", "package/version/license", "dependencies/peripherals", "data locations/classification", "backup/sync policy", "precheck", "task-based tests", "user acceptance", "fallback", "retirement release"],
    ))

    write(common / "SECURITY_COMPLIANCE_AND_SANITIZATION.md", document(
        "Hardware Refresh Security, Compliance, and Sanitization Plan",
        "Protect access and data on new and returned devices and maintain auditable custody through reuse or disposal.",
        f"""## New-device controls

{table(["Control", "Release requirement", "Evidence"], [
    ["Identity/management", "Approved join/enrollment; unique device and user assignment", "Entra/Intune/SCCM/MDM record"],
    ["Protection", "Encryption, supported OS/update, EDR, firewall, screen lock, standard user", "Compliance and security report"],
    ["Access", "Conditional access validated in report-only/pilot before enforcement as applicable", "Policy result and exception"],
    ["Data", "Approved backup/sync complete; protected locations known", "Migration checklist and user validation"],
    ["Evidence", "Asset, build, policy, owner, site, warranty, support identifiers reconciled", "CMDB/inventory acceptance"],
  ])}

## Returned-device controls

NIST SP 800-88 Rev. 2 is used as program-level guidance: classify media/data, select an organization-approved sanitization method/standard, authorize tools/vendors, preserve custody, validate effectiveness, retain evidence, and manage reuse/disposal. The project does not prescribe a destructive technique without the organization’s security and records requirements.

## Chain of custody

Scan at user handoff, site secure storage, transport pickup, processing receipt, sanitization start/finish, validation, and final reuse/recycle/destruction. Record serial/asset/media identifiers, people/organizations, date/time/location, seal/container, method/tool/version, result, validation, exception, and certificate/reference.

## Stop conditions

Unknown identity/serial, missing legal-hold release, encryption/EDR/compliance failure, suspected loss/tamper, unsuccessful sanitization validation, or vendor evidence gap. Quarantine the asset and invoke Security/Records/Asset Management; never mark complete from a vendor invoice alone.
""",
        ["new-device controls", "compliance policy and exceptions", "data classification/hold", "sanitization program authority", "approved methods/standards/vendors", "custody events", "validation", "certificate/evidence retention", "failed media", "final disposition"],
    ))

    write(common / "COMMUNICATIONS_TRAINING_AND_SUPPORT.md", document(
        "Hardware Refresh Communications, Training, and Support Plan",
        "Coordinate managers, users, site leaders, support, and vendors around appointments, preparation, disruption, acceptance, and recovery.",
        f"""## Communication journey

{table(["Timing", "Audience", "Message / action", "Evidence"], [
    ["T-30 days", "Managers/site leads", "Validate roster, blackout dates, personas, local needs", "Manager sign-off"],
    ["T-14 days", "Users", "Appointment, preparation, data/app checklist, impact, accessibility contact", "Delivery/read receipt + response"],
    ["T-5 days", "Users/managers", "Readiness exceptions and reschedule rule", "Precheck result"],
    ["T-1 day", "Users", "Exact location/time, bring old device/accessories, support route", "Reminder sent"],
    ["Day 0", "Users", "Task-based validation and acceptance", "Signed/electronic checklist"],
    ["T+1/T+5", "Users/managers", "Follow-up, survey, return reminder, support", "Response and exception closure"],
  ])}

## Support model

Dedicated ServiceNow queue/category, site walk-up/appointment support, remote support, executive route, known-error articles, spare pool, application/vendor escalation, severity/response rules, and daily hypercare review. Ticket categories distinguish appointment/no-show, hardware, build, identity, compliance, application, data, peripheral, network, training, return, and sanitization.

## User acceptance

The user or authorized business representative validates identity, email/collaboration, approved data, Tier 0/1 tasks, VPN/network/printing/peripherals, accessibility, and remote support. “Device powered on” is not acceptance.
""",
        ["audiences/owners", "wave calendar", "message templates and approvals", "preparation checklist", "training/proficiency", "appointment logistics", "support queue/staffing", "escalation", "survey/adoption", "return reminders"],
    ))

    write(common / "DEPLOYMENT_HYPERCARE_AND_SERVICE_TRANSITION.md", document(
        "Hardware Refresh Deployment, Hypercare, and Service Transition Plan",
        "Execute safe pilot/waves, restore failed users quickly, learn between waves, and transfer stable ownership to operations.",
        f"""## Wave pattern

1. T-10: roster/app/data/device readiness; capacity and inventory reconciliation.
2. T-5: user prechecks, communication, site kit and support staffing; exceptions moved out of denominator only with approval and a new date.
3. T-1: go/no-go using security, build, application, data, logistics, support, and business criteria.
4. Day 0: identity verification, old-device custody, new-device issue, task validation, acceptance, and incident routing.
5. T+1/T+5: compliance, tickets, data, returns, satisfaction, defects, and lessons; authorize or adjust the next wave.

## Go/no-go thresholds

- At least 98% of wave devices staged and passed build/security; every missing unit has an assigned spare/reschedule.
- 100% Tier 0 and at least 98% Tier 1 persona tests pass; open defects have accepted workaround/expiry.
- User data prechecks pass or the user is removed to the controlled exception queue.
- Site/staging/network/support capacity can absorb the wave plus a 20% incident surge.
- Rollback/reissue/spare path and old-device custody are ready.

## Hypercare exit

Five business days without Sev 1; first-time-right at least 97%; compliance at least 98% within 24 hours; open defects owned and aging inside the agreed service objective; return and sanitization backlog inside capacity; Service Operations accepts knowledge, monitoring, queue, vendors, spares, on-call, KPIs, and known risks.
""",
        ["pilot/wave scope", "T-10/T-5/T-1 gates", "daily runbook", "validation/acceptance", "incident/rollback", "capacity/spares", "wave metrics", "lessons/change", "hypercare exit", "service acceptance"],
    ))

    write(common / "ASSET_RETIREMENT_AND_CLOSEOUT.md", document(
        "Hardware Refresh Asset Retirement, Reconciliation, and Closeout Plan",
        "Close the control loop from issued device through old-asset return, sanitization, disposition, financial closure, lessons, and benefits.",
        f"""## Reconciliation model

{table(["State", "Definition", "Evidence"], [
    ["Assigned", "New serial/asset linked to user/site/wave", "Inventory/CMDB and handoff"],
    ["Accepted", "User/business task validation completed", "Acceptance checklist"],
    ["Old returned", "Old asset transferred to controlled custody", "Scan/signature/date/location"],
    ["Sanitized", "Approved method completed and validated", "Certificate/log and validator"],
    ["Disposed/reused", "Final destination accepted", "Recycle/destruction/redeployment record"],
    ["Exception", "One or more states incomplete", "Owner, reason, due date, risk, escalation"],
  ])}

## Closeout checklist

- 360 of 360 new and old asset dispositions reconciled; duplicates/unknowns resolved.
- User data and legal holds released before sanitization; certificates/evidence retained.
- Purchase orders, receipts, invoices, credits, warranties, and vendor deliverables reconciled.
- Open issues/risks/changes transferred with accepting owner, due date, funding, and communication.
- Service Operations accepts inventory/CMDB, build, knowledge, queue, monitoring, spares, vendor, and escalation.
- Sponsor accepts scope/schedule/cost/quality results and benefit owners; lessons are prioritized into actions.

## Benefits

Track supported-device rate, compliance, startup/app reliability, ticket/contact rate, user satisfaction, repair/warranty, and avoided support/maintenance cost. Forecast values become realized only when Finance and the operational benefit owner validate source records.
""",
        ["asset state model", "reconciliation queries", "return aging", "sanitization/disposition", "financial/vendor closure", "operations acceptance", "open-item transfer", "lessons/actions", "benefit measures/owners", "sponsor sign-off"],
    ))

    write_csv(common / "RAID_REGISTER.csv", ["id", "type", "statement", "probability_1_5", "impact_1_5", "score", "owner", "response", "trigger", "due", "status"], [
        {"id":"HW-R-001","type":"Risk","statement":"Procurement delay misses a site wave","probability_1_5":3,"impact_1_5":4,"score":12,"owner":"Procurement","response":"Dual-approved models; order tracking; wave reorder; protected spares","trigger":"Confirmed delivery later than T-10","due":"Week 5","status":"Mitigating"},
        {"id":"HW-R-002","type":"Risk","statement":"Local or application data is not protected before old-device retirement","probability_1_5":3,"impact_1_5":5,"score":15,"owner":"Data Lead","response":"Precheck, KFM/backup, app-data inventory, validation, sanitize hold","trigger":"Sync/backup error or unknown local data","due":"Per wave","status":"Mitigating"},
        {"id":"HW-R-003","type":"Risk","statement":"Critical app, driver, VPN, or peripheral fails on the new build","probability_1_5":4,"impact_1_5":4,"score":16,"owner":"Application Lead","response":"Persona pilot, versioned package, fallback and owner acceptance","trigger":"Tier 0/1 test failure","due":"T-5 each wave","status":"Mitigating"},
        {"id":"HW-R-004","type":"Risk","statement":"Returned device custody or sanitization evidence is incomplete","probability_1_5":2,"impact_1_5":5,"score":10,"owner":"Asset Manager","response":"Serial scans, secure storage, vendor evidence validation, quarantine","trigger":"Unknown scan state over 24 hours","due":"Daily","status":"Mitigating"},
        {"id":"HW-I-005","type":"Issue","statement":"Sixteen devices remain as application, accessibility, leave, or logistics exceptions","probability_1_5":5,"impact_1_5":3,"score":15,"owner":"Exception Manager","response":"Named owner/date/workaround; weekly steering burn-down","trigger":"Exception exceeds committed date","due":"Week 18","status":"Open"},
        {"id":"HW-D-006","type":"Dependency","statement":"Site managers confirm user rosters and blackout periods","probability_1_5":3,"impact_1_5":4,"score":12,"owner":"Business Change Lead","response":"T-30/T-14 attestations; unconfirmed users not scheduled","trigger":"Roster unapproved at T-14","due":"Per site","status":"Open"},
    ], "Hardware refresh shared RAID register — filled example")

    write_csv(common / "RACI.csv", ["deliverable", "sponsor", "project_manager", "endpoint", "infosec", "procurement", "asset_management", "applications", "service_desk", "business_site", "vendor"], [
        {"deliverable":"Charter / budget / method","sponsor":"A","project_manager":"R","endpoint":"C","infosec":"C","procurement":"C","asset_management":"C","applications":"C","service_desk":"C","business_site":"C","vendor":"I"},
        {"deliverable":"Device standard / build","sponsor":"I","project_manager":"C","endpoint":"A/R","infosec":"C","procurement":"C","asset_management":"C","applications":"C","service_desk":"C","business_site":"I","vendor":"R"},
        {"deliverable":"Security/compliance release","sponsor":"I","project_manager":"C","endpoint":"R","infosec":"A","procurement":"I","asset_management":"C","applications":"C","service_desk":"I","business_site":"I","vendor":"C"},
        {"deliverable":"Application/data readiness","sponsor":"I","project_manager":"R","endpoint":"R","infosec":"C","procurement":"I","asset_management":"I","applications":"A/R","service_desk":"C","business_site":"C","vendor":"C"},
        {"deliverable":"Wave go/no-go","sponsor":"A","project_manager":"R","endpoint":"R","infosec":"A","procurement":"C","asset_management":"R","applications":"R","service_desk":"R","business_site":"A","vendor":"C"},
        {"deliverable":"Asset return/sanitization","sponsor":"I","project_manager":"C","endpoint":"C","infosec":"A","procurement":"C","asset_management":"R","applications":"I","service_desk":"I","business_site":"R","vendor":"R"},
        {"deliverable":"Service transition/closure","sponsor":"A","project_manager":"R","endpoint":"R","infosec":"C","procurement":"C","asset_management":"R","applications":"C","service_desk":"A/R","business_site":"C","vendor":"C"},
    ], "Hardware refresh RACI — A accountable, R responsible, C consulted, I informed")

    inventory_rows = []
    for idx, (site, model, persona, status, old_state) in enumerate([
        ("Site A","Laptop Standard","Knowledge Worker","Deployed","Returned — sanitize pending"),
        ("Site A","Laptop Performance","Engineer","Deployed","Sanitized — certificate received"),
        ("Site B","Desktop Standard","Shared Station","Staged","In use"),
        ("Site C","Mobile Phone","Field Leader","Exception — leave","In use"),
        ("Remote","Laptop Standard","Remote Worker","Deployed","Courier return in transit"),
        ("Site B","Laptop Accessibility","Accessibility","Exception — peripheral","In use"),
    ], 1):
        inventory_rows.append({"asset_id":f"NEW-{idx:04d}","serial":f"XYZ{2026000+idx}","device_type":model,"site":site,"assigned_persona":persona,"user_id":f"USER-{idx:04d}","wave":"Pilot" if idx <= 2 else "Wave 2","build_version":"WIN11-26H2-R3" if "Mobile" not in model else "MOB-26-R2","management_id":f"MDM-{idx:04d}","compliance":"Compliant" if "Exception" not in status else "Pending","deployment_status":status,"old_asset_id":f"OLD-{idx:04d}","old_asset_state":old_state,"exception_owner":"" if "Exception" not in status else "Exception Manager"})
    write_csv(common / "INVENTORY_AND_ASSET_RECONCILIATION.csv", ["asset_id", "serial", "device_type", "site", "assigned_persona", "user_id", "wave", "build_version", "management_id", "compliance", "deployment_status", "old_asset_id", "old_asset_state", "exception_owner"], inventory_rows, "Hardware refresh inventory and asset reconciliation — representative filled rows")

    write_csv(common / "APPLICATION_READINESS.csv", ["app_id", "application", "tier", "personas", "package_or_delivery", "license_ready", "identity_network_dependency", "test_result", "defect", "fallback", "owner", "status"], [
        {"app_id":"APP-001","application":"Microsoft 365 Apps","tier":"0","personas":"All Windows","package_or_delivery":"Intune required app","license_ready":"Yes","identity_network_dependency":"Entra / internet","test_result":"Pass","defect":"None","fallback":"Web apps","owner":"Productivity Owner","status":"Ready"},
        {"app_id":"APP-002","application":"VPN client","tier":"0","personas":"Remote / engineer","package_or_delivery":"Win32 package","license_ready":"Yes","identity_network_dependency":"Certificate + gateway","test_result":"Pass after certificate fix","defect":"Closed DEF-014","fallback":"Old device / approved VDI","owner":"Network Apps","status":"Ready"},
        {"app_id":"APP-003","application":"Finance thick client","tier":"1","personas":"Finance","package_or_delivery":"SCCM/Intune package","license_ready":"Yes","identity_network_dependency":"Legacy database","test_result":"Conditional","defect":"DEF-021 printer driver","fallback":"Prior device retained","owner":"Finance App Owner","status":"Watch"},
        {"app_id":"APP-004","application":"Accessibility suite","tier":"1","personas":"Accessibility","package_or_delivery":"Manual assisted install","license_ready":"Yes","identity_network_dependency":"License service","test_result":"Peripheral test open","defect":"DEF-026","fallback":"Reschedule / old device","owner":"Accessibility Lead","status":"Open"},
        {"app_id":"APP-005","application":"Endpoint protection","tier":"0","personas":"All","package_or_delivery":"Security policy","license_ready":"Yes","identity_network_dependency":"Intune/Defender","test_result":"Pass","defect":"None","fallback":"Quarantine if missing","owner":"InfoSec","status":"Ready"},
    ], "Hardware refresh application readiness — representative rows from 76-app scenario")

    write_csv(common / "DEPLOYMENT_WAVES.csv", ["wave", "site", "planned_devices", "ready_t_minus_5", "deployed", "first_time_right", "data_pass", "compliant_24h", "old_returns", "open_exceptions", "go_no_go", "owner", "status"], [
        {"wave":"Pilot","site":"Site A","planned_devices":20,"ready_t_minus_5":20,"deployed":20,"first_time_right":19,"data_pass":20,"compliant_24h":20,"old_returns":20,"open_exceptions":0,"go_no_go":"Go","owner":"Pilot Lead","status":"Complete"},
        {"wave":"Wave 1","site":"Site A","planned_devices":95,"ready_t_minus_5":94,"deployed":94,"first_time_right":92,"data_pass":94,"compliant_24h":93,"old_returns":92,"open_exceptions":1,"go_no_go":"Conditional go","owner":"Site A Lead","status":"Complete"},
        {"wave":"Wave 2","site":"Site B","planned_devices":90,"ready_t_minus_5":87,"deployed":87,"first_time_right":85,"data_pass":86,"compliant_24h":86,"old_returns":84,"open_exceptions":3,"go_no_go":"Conditional go","owner":"Site B Lead","status":"Complete"},
        {"wave":"Wave 3","site":"Site C","planned_devices":75,"ready_t_minus_5":71,"deployed":71,"first_time_right":69,"data_pass":71,"compliant_24h":70,"old_returns":68,"open_exceptions":4,"go_no_go":"Conditional go","owner":"Site C Lead","status":"Complete"},
        {"wave":"Wave 4","site":"Remote / all sites","planned_devices":80,"ready_t_minus_5":72,"deployed":72,"first_time_right":71,"data_pass":71,"compliant_24h":70,"old_returns":70,"open_exceptions":8,"go_no_go":"Partial release","owner":"Remote Lead","status":"In progress"},
        {"wave":"TOTAL","site":"Four sites","planned_devices":360,"ready_t_minus_5":344,"deployed":344,"first_time_right":336,"data_pass":342,"compliant_24h":339,"old_returns":334,"open_exceptions":16,"go_no_go":"N/A","owner":"Project Manager","status":"Amber"},
    ], "Hardware refresh deployment wave dashboard source — filled example")

    write_csv(common / "USER_DATA_VALIDATION.csv", ["validation_id", "user_id", "wave", "precheck", "source_data_gb", "destination_data_gb", "file_sample", "critical_apps", "user_acceptance", "old_device_release", "owner", "status"], [
        {"validation_id":"UDV-001","user_id":"USER-0001","wave":"Pilot","precheck":"Pass","source_data_gb":42.6,"destination_data_gb":42.6,"file_sample":"20/20 pass","critical_apps":"Pass","user_acceptance":"Accepted","old_device_release":"Yes","owner":"Migration Tech","status":"Complete"},
        {"validation_id":"UDV-002","user_id":"USER-0002","wave":"Pilot","precheck":"Pass","source_data_gb":18.2,"destination_data_gb":18.2,"file_sample":"20/20 pass","critical_apps":"Pass","user_acceptance":"Accepted","old_device_release":"Yes","owner":"Migration Tech","status":"Complete"},
        {"validation_id":"UDV-003","user_id":"USER-0003","wave":"Wave 2","precheck":"Warning — local app data","source_data_gb":67.4,"destination_data_gb":65.9,"file_sample":"18/20; two app files pending","critical_apps":"Conditional","user_acceptance":"Pending","old_device_release":"No — custody hold","owner":"Data Lead","status":"Exception"},
    ], "Hardware refresh user-data validation — representative filled rows")

    write_csv(common / "SANITIZATION_CHAIN_OF_CUSTODY.csv", ["record_id", "old_asset_id", "serial", "user_handoff_time", "site_storage", "transport_reference", "processor_receipt", "data_hold_released", "approved_method", "tool_or_vendor", "result", "validation", "certificate_reference", "final_disposition", "owner", "status"], [
        {"record_id":"SAN-001","old_asset_id":"OLD-0001","serial":"OLDXYZ001","user_handoff_time":"2026-06-02 10:14","site_storage":"Cage A / Seal 104","transport_reference":"TRK-4431","processor_receipt":"2026-06-03 08:42","data_hold_released":"Yes","approved_method":"Organization-approved purge","tool_or_vendor":"Approved processor","result":"Success","validation":"Passed independent sample","certificate_reference":"CERT-88001","final_disposition":"Redeploy","owner":"Asset Manager","status":"Closed"},
        {"record_id":"SAN-002","old_asset_id":"OLD-0002","serial":"OLDXYZ002","user_handoff_time":"2026-06-02 11:03","site_storage":"Cage A / Seal 104","transport_reference":"TRK-4431","processor_receipt":"2026-06-03 08:43","data_hold_released":"Yes","approved_method":"Organization-approved clear","tool_or_vendor":"Internal approved tool v6","result":"Success","validation":"Log verified","certificate_reference":"LOG-55102","final_disposition":"Internal reuse","owner":"Asset Manager","status":"Closed"},
        {"record_id":"SAN-003","old_asset_id":"OLD-0003","serial":"OLDXYZ003","user_handoff_time":"2026-06-04 15:20","site_storage":"Cage B / Seal 107","transport_reference":"Pending","processor_receipt":"","data_hold_released":"No — validation open","approved_method":"TBD after release","tool_or_vendor":"TBD","result":"Not started","validation":"Not started","certificate_reference":"","final_disposition":"Quarantine","owner":"Data + Asset Leads","status":"Hold"},
    ], "Hardware refresh sanitization chain of custody — filled example")

    write_csv(common / "EXCEPTION_LOG.csv", ["exception_id", "user_or_asset", "category", "description", "business_impact", "workaround", "owner", "target_date", "risk_acceptor", "next_update", "status"], [
        {"exception_id":"EX-001","user_or_asset":"USER-0317","category":"Application","description":"Finance printer driver not validated","business_impact":"Cannot print regulated report","workaround":"Retain old device on controlled network","owner":"Finance App Owner","target_date":"Week 16","risk_acceptor":"Finance Director","next_update":"Daily","status":"Open"},
        {"exception_id":"EX-002","user_or_asset":"USER-0332","category":"Accessibility","description":"Specialized peripheral shipment delayed","business_impact":"New device not usable","workaround":"Keep old device and reschedule","owner":"Accessibility Lead","target_date":"Week 17","risk_acceptor":"HR/Business","next_update":"Every 2 days","status":"Open"},
        {"exception_id":"EX-003","user_or_asset":"OLD-0003","category":"Data","description":"Local application data validation incomplete","business_impact":"Old device cannot be sanitized","workaround":"Secure custody hold","owner":"Data Lead","target_date":"Week 16","risk_acceptor":"Security","next_update":"Daily","status":"Open"},
        {"exception_id":"EX-004","user_or_asset":"8 remote users","category":"Logistics","description":"Courier appointment not completed","business_impact":"Refresh deferred","workaround":"Existing supported device remains in service","owner":"Remote Lead","target_date":"Week 17","risk_acceptor":"Project Manager","next_update":"Weekly","status":"Open"},
    ], "Hardware refresh exception log — representative filled rows")

    write_csv(common / "BUDGET.csv", ["cost_id", "work_package", "baseline_usd", "committed_usd", "actual_to_date_usd", "estimate_to_complete_usd", "forecast_usd", "variance_usd", "owner", "basis"], [
        {"cost_id":"HW-C-01","work_package":"Devices","baseline_usd":491000,"committed_usd":480000,"actual_to_date_usd":459000,"estimate_to_complete_usd":21000,"forecast_usd":480000,"variance_usd":11000,"owner":"Procurement","basis":"Scenario model/device mix"},
        {"cost_id":"HW-C-02","work_package":"Accessories/docks/displays","baseline_usd":54000,"committed_usd":52000,"actual_to_date_usd":48000,"estimate_to_complete_usd":4000,"forecast_usd":52000,"variance_usd":2000,"owner":"Procurement","basis":"Scenario kits"},
        {"cost_id":"HW-C-03","work_package":"Shipping and site logistics","baseline_usd":22000,"committed_usd":21500,"actual_to_date_usd":18000,"estimate_to_complete_usd":3500,"forecast_usd":21500,"variance_usd":500,"owner":"Logistics","basis":"Four-site/remote scenario"},
        {"cost_id":"HW-C-04","work_package":"Staging and engineering labor","baseline_usd":63000,"committed_usd":62000,"actual_to_date_usd":51000,"estimate_to_complete_usd":11000,"forecast_usd":62000,"variance_usd":1000,"owner":"Endpoint Lead","basis":"Capacity model"},
        {"cost_id":"HW-C-05","work_package":"Migration and hypercare support","baseline_usd":70000,"committed_usd":68000,"actual_to_date_usd":56000,"estimate_to_complete_usd":12000,"forecast_usd":68000,"variance_usd":2000,"owner":"Service Desk","basis":"Wave staffing"},
        {"cost_id":"HW-C-06","work_package":"Sanitization/recycling","baseline_usd":18000,"committed_usd":17000,"actual_to_date_usd":13000,"estimate_to_complete_usd":4000,"forecast_usd":17000,"variance_usd":1000,"owner":"Asset Manager","basis":"Scenario vendor rate"},
        {"cost_id":"HW-C-07","work_package":"Communications/training","baseline_usd":14000,"committed_usd":13000,"actual_to_date_usd":11000,"estimate_to_complete_usd":2000,"forecast_usd":13000,"variance_usd":1000,"owner":"Change Lead","basis":"Scenario materials/site support"},
        {"cost_id":"HW-C-08","work_package":"Management reserve","baseline_usd":60000,"committed_usd":34900,"actual_to_date_usd":19500,"estimate_to_complete_usd":15400,"forecast_usd":34900,"variance_usd":25100,"owner":"Sponsor","basis":"Approved draws only"},
    ], "Hardware refresh budget baseline and forecast — filled example")

    build_source_register(common / "SOURCE_REGISTER.csv", [*PMI_SOURCES, *HW_TECH_SOURCES], "Hardware refresh authoritative source register")

    build_hw_kanban(kanban)
    build_hw_scrum(scrum)
    build_hw_predictive(predictive)
    build_hw_hybrid(hybrid)


def build_hw_kanban(base: Path) -> None:
    write(base / "PLAYBOOK.md", document(
        "Enterprise Hardware Refresh — Kanban Playbook",
        "Operate the 360-device refresh as a flow system with explicit policies, constrained work in progress, service classes, and evidence-based forecasting.",
        f"""## Why Kanban

The arrival of ready users, delivered hardware, application fixes, data prechecks, appointments, and exceptions varies. A pull system prevents staging and deployment from outrunning validation, support, return, and sanitization capacity.

## Definition of Workflow

{table(["State", "Entry policy", "Exit policy", "WIP limit"], [
    ["Options", "In-scope user/device demand", "Roster and persona assigned", "None"],
    ["Ready", "Hardware, roster, app/data precheck and appointment feasible", "Pulled by staging capacity", "60"],
    ["Staging", "Serialized device and approved build", "Build/security/asset test pass", "24"],
    ["Scheduled", "User/site communication and kit ready", "Appointment begins", "40"],
    ["Deploying", "Identity verified; old asset in controlled handoff", "Task/data/user acceptance", "12"],
    ["Hypercare", "New device accepted", "T+5 measures pass; exception assigned", "30"],
    ["Return/sanitize", "Old asset custody established", "Disposition evidence accepted", "35"],
    ["Done", "New/old assets reconciled; service and evidence complete", "N/A", "None"],
  ])}

## Service classes

- Expedite: security failure, lost custody, executive/critical business outage; maximum one in system and named incident lead.
- Fixed date: regulatory/site blackout, user leave, contract or courier date; risk review when within service-level expectation.
- Standard: normal persona/device flow.
- Intangible: automation, knowledge, telemetry, and process debt; reserve at least 10% capacity so flow remains sustainable.

## Cadences and policies

Daily flow review focuses on blocked/aging work and WIP, not person-by-person status. Replenishment twice weekly selects only ready demand. Weekly service-delivery review inspects throughput, cycle-time distribution, work-item age, first-time-right, compliance, returns, and demand/capacity. Monthly operations/steering review changes policies, capacity, or scope.

## Forecast

Forecast with historical throughput and cycle-time percentiles. The scenario’s latest four-week throughput is 38 devices/week and P85 end-to-end cycle time is 6.2 business days after Ready. Forecasts are ranges; blocked exceptions are separately dated by owner.
""",
        ["work item types", "workflow start/finish", "states", "entry/exit policies", "WIP limits", "service classes", "SLEs", "cadences", "flow metrics", "escalation and improvement"],
    ))

    write(base / "EXPLICIT_POLICIES.md", document(
        "Hardware Kanban Explicit Policies and Service-Level Expectations",
        "Make pull, blocking, aging, expedite, quality, and exception rules observable.",
        f"""## Policies

{table(["Policy", "Rule", "Reason"], [
    ["Commitment point", "A device enters Ready only with roster, hardware, app/data precheck, appointment path, owner and acceptance", "Prevents false demand from consuming capacity"],
    ["Pull", "Downstream owner pulls only when below WIP and capacity exists for validation/failure", "Protects flow and quality"],
    ["Blocker", "Mark reason/owner/start/next action; escalate at one business day, immediately for security/custody", "Stops invisible waiting"],
    ["Aging", "Review items at 50% of SLE; swarm at 75%; escalate/reshape at 100%", "Uses work-item age as leading signal"],
    ["Expedite", "One maximum; explicit owner; return to normal after incident containment", "Prevents every request becoming urgent"],
    ["Done", "User/data/app acceptance plus new/old asset reconciliation and evidence", "Avoids deployment-only completion"],
  ])}

## Initial service-level expectations

- Standard staging: 85% within two business days.
- Ready-to-user acceptance: 85% within five business days.
- User acceptance-to-old-asset custody: 85% same day on site; five business days remote.
- Custody-to-sanitization/disposition evidence: 85% within seven business days.

SLEs are planning expectations derived from scenario history, not promises. Recalculate after at least 30 representative completions and segment remote/specialized work where distributions differ.
""",
        ["workflow policies", "commitment/delivery points", "WIP limits", "classes of service", "blocker rule", "aging thresholds", "SLE percentile/window", "done evidence", "policy-change cadence"],
    ))

    write_csv(base / "KANBAN_BOARD.csv", ["card_id", "work_type", "site_or_user", "class_of_service", "state", "entered_state", "work_item_age_days", "sle_days", "blocked", "block_reason", "owner", "next_action", "due", "status"], [
        {"card_id":"KB-317","work_type":"Device refresh","site_or_user":"USER-0317","class_of_service":"Fixed date","state":"Deploying","entered_state":"2026-08-21","work_item_age_days":4,"sle_days":5,"blocked":"Yes","block_reason":"Finance printer driver","owner":"Finance App Owner","next_action":"Validate driver and workflow","due":"2026-08-27","status":"At risk"},
        {"card_id":"KB-332","work_type":"Accessibility refresh","site_or_user":"USER-0332","class_of_service":"Fixed date","state":"Ready","entered_state":"2026-08-20","work_item_age_days":5,"sle_days":7,"blocked":"Yes","block_reason":"Peripheral shipment","owner":"Accessibility Lead","next_action":"Confirm courier receipt","due":"2026-08-28","status":"Watch"},
        {"card_id":"KB-341","work_type":"Remote refresh","site_or_user":"USER-0341","class_of_service":"Standard","state":"Scheduled","entered_state":"2026-08-24","work_item_age_days":1,"sle_days":5,"blocked":"No","block_reason":"","owner":"Remote Lead","next_action":"Complete virtual appointment","due":"2026-08-26","status":"On track"},
        {"card_id":"KB-SAN-003","work_type":"Sanitization hold","site_or_user":"OLD-0003","class_of_service":"Expedite","state":"Return/sanitize","entered_state":"2026-08-24","work_item_age_days":1,"sle_days":2,"blocked":"Yes","block_reason":"Data validation/hold release","owner":"Data + Asset Leads","next_action":"Complete file validation; Security release","due":"2026-08-26","status":"Expedite"},
        {"card_id":"KB-IMPR-01","work_type":"Knowledge automation","site_or_user":"All sites","class_of_service":"Intangible","state":"Staging","entered_state":"2026-08-22","work_item_age_days":3,"sle_days":8,"blocked":"No","block_reason":"","owner":"Service Desk Lead","next_action":"Publish automated precheck article","due":"2026-08-29","status":"On track"},
    ], "Hardware Kanban board — representative filled cards")

    write_csv(base / "FLOW_METRICS.csv", ["week", "throughput_devices", "wip", "median_cycle_days", "p85_cycle_days", "oldest_item_age_days", "blocked_items", "first_time_right_pct", "compliant_24h_pct", "returns_reconciled_pct", "management_action"], [
        {"week":"W10","throughput_devices":34,"wip":82,"median_cycle_days":4.2,"p85_cycle_days":7.4,"oldest_item_age_days":9,"blocked_items":7,"first_time_right_pct":96.8,"compliant_24h_pct":98.1,"returns_reconciled_pct":96.5,"management_action":"Lower Scheduled WIP; swarm app blockers"},
        {"week":"W11","throughput_devices":37,"wip":73,"median_cycle_days":3.9,"p85_cycle_days":6.8,"oldest_item_age_days":8,"blocked_items":5,"first_time_right_pct":97.2,"compliant_24h_pct":98.4,"returns_reconciled_pct":97.0,"management_action":"Maintain WIP; add return courier slots"},
        {"week":"W12","throughput_devices":39,"wip":66,"median_cycle_days":3.6,"p85_cycle_days":6.4,"oldest_item_age_days":7,"blocked_items":4,"first_time_right_pct":97.5,"compliant_24h_pct":98.6,"returns_reconciled_pct":97.3,"management_action":"Keep capacity split; monitor accessibility queue"},
        {"week":"W13","throughput_devices":42,"wip":61,"median_cycle_days":3.4,"p85_cycle_days":6.2,"oldest_item_age_days":6,"blocked_items":4,"first_time_right_pct":97.7,"compliant_24h_pct":98.5,"returns_reconciled_pct":97.1,"management_action":"Forecast remaining standard work; isolate 16 exceptions"},
    ], "Hardware Kanban flow and outcome metrics — filled example")

    write(base / "SERVICE_DELIVERY_REVIEW.md", document(
        "Hardware Kanban Service Delivery Review",
        "Use flow, quality, customer, asset, and risk evidence to change the system rather than chase utilization.",
        f"""## Illustrative review — Week 13

{table(["Signal", "Evidence", "Interpretation", "Decision"], [
    ["Throughput", "42 devices; four-week mean 38", "Capacity supports normal remaining demand", "Do not increase WIP"],
    ["Cycle time", "Median 3.4; P85 6.2 business days", "Improving after staging limit", "Keep staging WIP 24"],
    ["Aging/blockers", "Four blocked; oldest six days", "Specialized work differs from standard flow", "Create explicit specialized lane"],
    ["Quality", "97.7% first-time-right; 98.5% compliant in 24h", "Inside threshold with two repeat app causes", "Root-cause app package defects"],
    ["Asset return", "97.1% reconciled", "Remote return lag remains", "Add prepaid courier pickup and T+3 escalation"],
  ])}

## Improvement experiment

For the next two weeks, cap Scheduled at 30 for remote work, reserve two daily support appointments for accessibility/specialized personas, and trigger courier pickup at user acceptance. Compare P85 cycle time, exception age, and return reconciliation with the prior four weeks.
""",
        ["review window", "demand/throughput", "WIP/aging/cycle time", "quality/compliance", "customer/support", "asset/return/sanitization", "risks", "forecast", "policy/capacity decision", "improvement experiment"],
    ))

    write(base / "EXECUTIVE_STATUS.md", document(
        "Hardware Kanban Executive Status — Illustrative Checkpoint",
        "Translate flow evidence into an executive outcome, forecast, risk, and decision view.",
        f"""## Overall: Amber — standard flow healthy; 16 exceptions require owned dates

{table(["Outcome", "Evidence", "Status / action"], [
    ["Deployment", "344/360 deployed; latest throughput 42/week", "Standard work forecast complete in one week"],
    ["Quality", "336/344 first-time-right = 97.7%", "Meets target; correct repeat package causes"],
    ["Compliance", "339/344 compliant within 24h = 98.5%", "Meets target; five remediated/owned"],
    ["Asset return", "334/344 returned = 97.1%", "Below target; remote courier action"],
    ["Exceptions", "16 open; four blocked in active flow", "Named dates; specialized lane approved"],
    ["Finance", "$748.4K forecast vs $792K authorization", "Green; reserve protected"],
  ])}

## Decisions requested

Approve specialized-persona capacity through Week 18, require remote return pickup at T+3, and confirm that no exception is removed from the 360-device denominator until final disposition.
""",
        ["status period", "outcome/flow/quality measures", "remaining forecast", "exceptions/aging", "budget", "risks", "policy/capacity decisions", "next review"],
    ))

    write(base / "ARTIFACT_INDEX.md", document(
        "Hardware Kanban Playbook Artifact Index",
        "Provide the complete Kanban-specific review order plus the shared execution controls.",
        """## Method-specific artifacts

1. `PLAYBOOK.md`
2. `EXPLICIT_POLICIES.md`
3. `KANBAN_BOARD.csv`
4. `FLOW_METRICS.csv`
5. `SERVICE_DELIVERY_REVIEW.md`
6. `EXECUTIVE_STATUS.md`

## Shared controls

Use every artifact in `../common/`, including charter, governance, build, procurement/logistics, application/data readiness, security/sanitization, communications/support, deployment/hypercare/transition, retirement/closeout, RAID, RACI, inventory, application readiness, waves, validation, custody, exceptions, budget, and source register.
""",
        ["method artifacts", "shared controls", "owners", "policy/version", "dashboard", "archive"],
    ))


def build_hw_scrum(base: Path) -> None:
    write(base / "PLAYBOOK.md", document(
        "Enterprise Hardware Refresh — Scrum Playbook",
        "Deliver accepted endpoint-refresh increments through one Product Goal, one ordered Product Backlog, nine two-week Sprints, empiricism, and clear accountabilities.",
        f"""## Product Goal

By the end of Sprint 9, all 360 device assignments have an accepted secure replacement or approved final exception, all old assets are reconciled through custody and disposition, and Service Operations owns the stable product/service.

## Accountabilities

{table(["Accountability", "Scenario role", "Focus"], [
    ["Product Owner", "Endpoint Service Owner", "Orders value, risk, persona and site outcomes; accepts backlog outcomes"],
    ["Scrum Master", "Agile Delivery Lead", "Establishes Scrum, removes system impediments, improves effectiveness"],
    ["Developers", "Endpoint, Security, Apps, Data, Asset, Logistics, Service Desk, Change specialists", "Create a usable accepted Increment each Sprint"],
  ])}

## Sprint design

Each two-week Sprint has one Sprint Goal and produces a usable Increment: an accepted pilot/wave cohort plus security, data, asset, support, and evidence. Procurement and business calendars constrain the backlog but do not create a second hidden plan. Sprint Planning selects work; Daily Scrum adapts the plan; Sprint Review inspects working outcomes with stakeholders; Retrospective improves quality and delivery.

## Artifacts and commitments

- Product Backlog / Product Goal: complete outcome and ordered work.
- Sprint Backlog / Sprint Goal: current forecast and plan by Developers.
- Increment / Definition of Done: accepted devices/users/assets/evidence, not staged equipment.

## Release controls

The Product Owner may reorder scope; Security/records/asset acceptance and destructive-action gates remain mandatory. A Sprint can complete with an unmet forecast, but no incomplete item is counted in the Increment. Fixed site waves are releases composed of Done backlog items.
""",
        ["Product Goal", "Scrum accountabilities", "Sprint length/events", "Product Backlog", "Sprint Goals", "Definition of Done", "release/wave mapping", "stakeholder review", "metrics/improvement", "mandatory gates"],
    ))

    write(base / "DEFINITION_OF_DONE.md", document(
        "Hardware Scrum Definition of Done",
        "Define the minimum evidence for a device/user/asset Increment to be usable and releasable.",
        """## A refresh item is Done only when

- User/device/old-asset identities reconcile to the wave roster and authoritative inventory.
- New device has the approved build, enrollment, encryption, supported update, EDR, firewall, compliance, required apps, and support identifiers.
- User passes task-based identity, data, Tier 0/1 app, network/VPN, peripheral, accessibility, and remote-support validation—or an approved no-data/not-applicable path is recorded.
- Old device is in controlled custody; data/hold release and sanitization/disposition next state are owned.
- User/manager accepts, communications are complete, ticket/defect is linked, knowledge/CMDB/inventory are updated.
- Evidence is attached and Product Owner accepts. Failed or conditional items return to the Product Backlog; they are not partial Done.

## Increment quality

The Sprint Increment includes the accepted cohort plus updated automation/configuration, documentation, dashboards, defects, operations evidence, and lessons. Releasing a site wave additionally requires the shared go/no-go gate.
""",
        ["device/build/security", "data/app/user acceptance", "asset/custody", "documentation/operations", "evidence", "Product Owner acceptance", "release gate", "exception rule"],
    ))

    write_csv(base / "PRODUCT_BACKLOG.csv", ["pbi", "epic", "item", "outcome", "order", "estimate_points", "acceptance", "dependency", "risk", "target_sprint", "owner", "status"], [
        {"pbi":"HWS-001","epic":"Foundation","item":"Approve persona/model/build/security standard","outcome":"One supportable release baseline","order":1,"estimate_points":21,"acceptance":"All core personas and control owners approve","dependency":"Hardware/license discovery","risk":"Build drift","target_sprint":1,"owner":"Endpoint PO","status":"Done"},
        {"pbi":"HWS-002","epic":"Pilot","item":"Deliver 20-device representative pilot Increment","outcome":"Proven wave system","order":2,"estimate_points":34,"acceptance":"20 accepted; security/data/app/asset/support evidence","dependency":"Build and app Tier 0","risk":"HW-R-003","target_sprint":3,"owner":"Developers","status":"Done"},
        {"pbi":"HWS-003","epic":"Site A","item":"Deliver accepted 95-device Site A wave","outcome":"Site A refreshed with stable service","order":3,"estimate_points":55,"acceptance":"Wave exit thresholds and asset custody","dependency":"Pilot lessons","risk":"Support capacity","target_sprint":4,"owner":"Site A Team","status":"Done"},
        {"pbi":"HWS-004","epic":"Site B","item":"Resolve Finance package/peripheral and complete 90-device wave","outcome":"Site B users productive","order":4,"estimate_points":55,"acceptance":"Tier 0/1 task tests and Done evidence","dependency":"DEF-021","risk":"HW-R-003","target_sprint":5,"owner":"Site B Team","status":"Done with 3 returned PBIs"},
        {"pbi":"HWS-005","epic":"Remote","item":"Complete remote device and return logistics cohort","outcome":"Remote users refreshed and assets reconciled","order":6,"estimate_points":45,"acceptance":"Courier, virtual validation, return scan, compliance","dependency":"Courier slots","risk":"HW-R-004","target_sprint":8,"owner":"Remote Team","status":"In progress"},
        {"pbi":"HWS-006","epic":"Closure","item":"Resolve 16 exceptions and transfer service","outcome":"Full disposition and durable ownership","order":7,"estimate_points":34,"acceptance":"360/360 disposition; operations/benefits acceptance","dependency":"Exception owners","risk":"HW-I-005","target_sprint":9,"owner":"Product Owner","status":"Ready"},
    ], "Hardware Scrum Product Backlog — representative filled example")

    write_csv(base / "SPRINT_PLAN.csv", ["sprint", "weeks", "sprint_goal", "forecast_points", "done_points", "accepted_devices", "increment", "top_impediment", "review_outcome", "retro_improvement", "status"], [
        {"sprint":1,"weeks":"1-2","sprint_goal":"Create a supportable product and evidence baseline","forecast_points":58,"done_points":54,"accepted_devices":0,"increment":"Approved standards, inventory, backlog and controls","top_impediment":"Two unknown app owners","review_outcome":"Foundation accepted with owner actions","retro_improvement":"Add owner SLA to refinement","status":"Complete"},
        {"sprint":2,"weeks":"3-4","sprint_goal":"Prove provisioning/data/app paths","forecast_points":62,"done_points":60,"accepted_devices":0,"increment":"Representative lab evidence and pilot-ready build","top_impediment":"VPN certificate","review_outcome":"Pilot authorized after fix","retro_improvement":"Run certificate test earlier","status":"Complete"},
        {"sprint":3,"weeks":"5-6","sprint_goal":"Deliver accepted 20-device pilot Increment","forecast_points":64,"done_points":64,"accepted_devices":20,"increment":"20 Done refreshes + wave changes","top_impediment":"One reinstall","review_outcome":"Scale to Site A","retro_improvement":"Pre-cache app content","status":"Complete"},
        {"sprint":4,"weeks":"7-8","sprint_goal":"Complete Site A wave without overloading support","forecast_points":72,"done_points":69,"accepted_devices":94,"increment":"94 Done; one PBI returned","top_impediment":"One late shipment","review_outcome":"Site accepted; exception re-ordered","retro_improvement":"T-10 device buffer","status":"Complete"},
        {"sprint":5,"weeks":"9-10","sprint_goal":"Deliver Site B Increment and fix repeat package defects","forecast_points":73,"done_points":68,"accepted_devices":87,"increment":"87 Done; 3 PBIs returned","top_impediment":"Finance printer driver","review_outcome":"Conditional site acceptance","retro_improvement":"Persona-specific regression suite","status":"Complete"},
        {"sprint":6,"weeks":"11-12","sprint_goal":"Deliver Site C and improve asset return flow","forecast_points":70,"done_points":66,"accepted_devices":71,"increment":"71 Done; return policy changed","top_impediment":"Accessibility peripheral","review_outcome":"Site accepted with four exceptions","retro_improvement":"Specialized item refinement two Sprints ahead","status":"Complete"},
        {"sprint":7,"weeks":"13-14","sprint_goal":"Start remote/all-site final cohort","forecast_points":68,"done_points":61,"accepted_devices":72,"increment":"72 Done; 8 logistics/app PBIs returned","top_impediment":"Courier appointments","review_outcome":"Continue remote cohort","retro_improvement":"User self-scheduling window","status":"Complete"},
        {"sprint":8,"weeks":"15-16","sprint_goal":"Close standard scope and burn down exceptions","forecast_points":58,"done_points":0,"accepted_devices":0,"increment":"In progress","top_impediment":"16 exception PBIs","review_outcome":"Open","retro_improvement":"Open","status":"Active"},
    ], "Hardware Scrum Sprint plan and review record — filled example")

    write_csv(base / "SCRUM_METRICS.csv", ["sprint", "done_points", "accepted_devices", "first_time_right_pct", "compliant_24h_pct", "data_pass_pct", "returns_reconciled_pct", "escaped_defects", "sprint_goal", "goal_result", "interpretation"], [
        {"sprint":3,"done_points":64,"accepted_devices":20,"first_time_right_pct":95.0,"compliant_24h_pct":100.0,"data_pass_pct":100.0,"returns_reconciled_pct":100.0,"escaped_defects":1,"sprint_goal":"Pilot","goal_result":"Met","interpretation":"Pre-cache content and retain validation"},
        {"sprint":4,"done_points":69,"accepted_devices":94,"first_time_right_pct":97.9,"compliant_24h_pct":98.9,"data_pass_pct":100.0,"returns_reconciled_pct":97.9,"escaped_defects":2,"sprint_goal":"Site A","goal_result":"Met","interpretation":"Improve delivery buffer"},
        {"sprint":5,"done_points":68,"accepted_devices":87,"first_time_right_pct":97.7,"compliant_24h_pct":98.9,"data_pass_pct":98.9,"returns_reconciled_pct":96.6,"escaped_defects":2,"sprint_goal":"Site B","goal_result":"Partially met","interpretation":"Returned PBIs remain visible; fix Finance package"},
        {"sprint":6,"done_points":66,"accepted_devices":71,"first_time_right_pct":97.2,"compliant_24h_pct":98.6,"data_pass_pct":100.0,"returns_reconciled_pct":95.8,"escaped_defects":1,"sprint_goal":"Site C","goal_result":"Met with exceptions","interpretation":"Refine specialized personas earlier"},
        {"sprint":7,"done_points":61,"accepted_devices":72,"first_time_right_pct":98.6,"compliant_24h_pct":97.2,"data_pass_pct":98.6,"returns_reconciled_pct":97.2,"escaped_defects":1,"sprint_goal":"Remote cohort","goal_result":"Partially met","interpretation":"Courier/self-scheduling constraint"},
    ], "Hardware Scrum outcome and delivery metrics — filled example")

    write(base / "EXECUTIVE_STATUS.md", document(
        "Hardware Scrum Executive Status — Illustrative Checkpoint",
        "Show Product Goal progress, accepted Increments, quality, finance, impediments, and decisions.",
        f"""## Overall: Amber — 344 accepted devices; 16 PBIs remain visible

{table(["Evidence", "Current", "Interpretation"], [
    ["Product Goal", "344/360 accepted device assignments", "95.6%; remaining scope is exception-heavy"],
    ["Increment quality", "336/344 first-time-right; 342/344 data pass", "Quality thresholds met overall"],
    ["Compliance", "339/344 compliant within 24h", "Five owned remediations"],
    ["Asset return", "334/344 returned", "Remote return flow needs action"],
    ["Finance", "$748.4K forecast vs $792K", "Reserve available for specialized closure"],
  ])}

## Product Owner decisions

Keep the 16 exception PBIs ordered by business impact and risk; allocate Sprint 9 capacity to accessibility, Finance, data-hold, and remote-return outcomes; do not convert deferred PBIs into Done. Service transition begins only when the shared acceptance package is usable.
""",
        ["Product Goal", "Sprint Goal/Increment", "quality/outcome measures", "backlog/impediments", "budget", "stakeholder feedback", "decisions", "next Sprint/release"],
    ))

    write(base / "ARTIFACT_INDEX.md", document(
        "Hardware Scrum Playbook Artifact Index",
        "Provide the Scrum-specific review order plus the complete shared control pack.",
        """## Method-specific artifacts

1. `PLAYBOOK.md`
2. `PRODUCT_BACKLOG.csv`
3. `SPRINT_PLAN.csv`
4. `DEFINITION_OF_DONE.md`
5. `SCRUM_METRICS.csv`
6. `EXECUTIVE_STATUS.md`

## Shared controls

Use every artifact in `../common/`. Scrum changes how work is planned, inspected, and adapted; it does not remove device security, data, application, asset, procurement, sanitization, budget, support, or closeout controls.
""",
        ["Scrum artifacts/events/accountabilities", "shared controls", "owners", "version", "dashboard", "archive"],
    ))


def build_hw_predictive(base: Path) -> None:
    write(base / "PLAYBOOK.md", document(
        "Enterprise Hardware Refresh — Predictive / Waterfall Playbook",
        "Baseline and control the 360-device refresh through PMBOK 8-aligned principles/domains, predictive process groups, WBS, integrated schedule, stage gates, change, and earned value.",
        f"""## Tailoring

The device quantity, sites, budget, procurement, build, and wave calendar are sufficiently known to baseline. Application, data, and user exceptions use rolling-wave detail inside controlled work packages. PMBOK Guide Eighth Edition is approach-neutral; “Predictive / Waterfall” describes this portfolio’s sequential baseline and formal gates, not a PMI mandate.

## Lifecycle

{table(["Process group / phase", "Primary outputs", "Authorization"], [
    ["Initiating", "Charter, stakeholder/assumption/risk framing", "Sponsor authorizes project"],
    ["Planning", "Requirements, WBS, IMS, cost, quality, resources, communications, procurement, risk, change, deployment/retirement", "Baseline gate"],
    ["Executing", "Procure, receive, stage, build, pilot, deploy, support, return, sanitize", "Wave gates"],
    ["Monitoring and Controlling", "Performance, EVM, quality, RAID, change, forecast, acceptance, vendor/asset reconciliation", "CCB/steering decisions"],
    ["Closing", "Service/asset/vendor/financial acceptance, lessons, benefits", "Sponsor closure"],
  ])}

## PMBOK 8 domains

Governance uses gates/decision rights; scope uses requirements/WBS; schedule uses IMS/critical path; finance uses cost baseline/EVM; stakeholders use communications/readiness; resources use capacity/vendor plans; risk uses RAID, security, data, rollback, and contingency.

## Baseline rule

No activity is reported complete until its deliverable acceptance is met. A quantity change, site/wave move, model/build/control change, cost/schedule threshold breach, or acceptance change enters integrated change control with impacts and rollback.
""",
        ["tailoring", "principles/domains/process groups", "scope/WBS", "IMS/critical path", "cost/EVM", "quality", "resources/procurement", "stakeholders", "risk/change", "closure/benefits"],
    ))

    write(base / "PMBOK8_ALIGNMENT.md", document(
        "Hardware Predictive PMBOK 8 Alignment Matrix",
        "Map the current standard’s six principles and seven performance domains to executable refresh controls.",
        f"""## Principles and evidence

{table(["Principle", "Refresh application", "Evidence"], [
    ["Holistic view", "User, device, app, data, identity, logistics, support, old asset, vendor and benefit as one outcome", "Integrated plan and reconciliation"],
    ["Value", "Supported secure productivity and lower lifecycle risk", "Charter outcomes and benefit owners"],
    ["Quality", "Build/security/app/data/user/asset evidence embedded in each wave", "Quality and acceptance plan"],
    ["Accountability", "Named sponsor, PM, control owners, user/site acceptance and risk authority", "Governance/RACI"],
    ["Sustainability", "Reuse viable assets, efficient logistics, controlled recycling/disposal", "Disposition and vendor evidence"],
    ["Empowered teams", "Wave leads may stop unsafe work and own evidence", "Charter and gate authority"],
  ])}

## Domains

{table(["Domain", "Control", "Measure"], [
    ["Governance", "Charter, forums, stage gates, CCB", "Decision/gate aging"],
    ["Scope", "360-device baseline, requirements, WBS", "Accepted quantities/change"],
    ["Schedule", "IMS, dependencies, site waves", "Critical milestone/SPI"],
    ["Finance", "$792K baseline, commitments/actuals/ETC/EAC", "CPI/forecast/reserve"],
    ["Stakeholders", "Managers/users/sites/support/vendors", "Readiness, acceptance, ticket/satisfaction"],
    ["Resources", "Staging, desks, support, vendors, spares", "Capacity/WIP/utilization constraints"],
    ["Risk", "RAID, security, data, asset, supply, rollback", "Exposure, triggers, closure"],
  ])}
""",
        ["standard/version", "principle mapping", "domain mapping", "process groups", "tailoring decisions", "artifact/evidence", "gaps/exceptions"],
    ))

    write(base / "STAGE_GATES_AND_CHANGE_CONTROL.md", document(
        "Hardware Predictive Stage Gates and Change Control",
        "Define formal authorization from business case through pilot, waves, retirement, and closure.",
        f"""## Gates

{table(["Gate", "Evidence", "Decision"], [
    ["G0 Charter", "Outcome, scope, sponsor, PM, assumptions, initial risk", "Authorize planning"],
    ["G1 Baseline", "Requirements, WBS, IMS, cost, quality, procurement, communications, risk, change", "Approve baseline"],
    ["G2 Build/pilot", "Approved models/build/security/apps/data/test/support/rollback", "Authorize pilot"],
    ["G3 Scale", "Pilot acceptance and corrected defects/process", "Authorize production waves"],
    ["G4 Wave", "T-5/T-1 readiness and capacity", "Go/conditional go/hold"],
    ["G5 Retirement", "Data/user release, custody, sanitization authority", "Authorize disposition"],
    ["G6 Close", "360 dispositions, service/vendor/financial acceptance, lessons/benefits", "Close/transfer"],
  ])}

## Change thresholds

Workstream leads may adjust tasks inside accepted work packages with no baseline/control effect. PM/CCB controls changes up to $15K or five business days without final milestone impact. Steering approves device count/model/site sequence, final milestone, reserve, control/acceptance, or forecast changes above 5%. Emergency security/service action is documented after containment.
""",
        ["gate criteria/approvers", "change thresholds", "change request fields", "impact analysis", "emergency rule", "baseline update", "decision log"],
    ))

    write(base / "QUALITY_MANAGEMENT_PLAN.md", document(
        "Hardware Predictive Quality Management Plan",
        "Plan and assure build, security, application, data, user, asset, and service quality.",
        f"""## Quality matrix

{table(["Quality object", "Requirement", "Acceptance"], [
    ["Device build", "Versioned, reproducible, supported", "Pilot/model/persona results and release approval"],
    ["Security/compliance", "Required controls before business release", "At least 98% within 24h; owned remediation"],
    ["Applications/data", "Tier 0/1 workflows and approved data present", "At least 99% data pass; business task acceptance"],
    ["User experience", "Minimal disruption and supportable handoff", "At least 97% first-time-right; median impact under 90 min"],
    ["Assets", "New/old serials and custody/disposition reconciled", "100% final disposition; no unknown custody"],
    ["Operations", "Knowledge, queue, monitoring, spares, vendor and on-call accepted", "Service-owner sign-off"],
  ])}

## Defects and sampling

All Tier 0, security, data-hold, custody, and destructive actions receive 100% evidence review. Quality samples at least 10% of other wave records and all repeat-failure causes. Sev 1 blocks release; Sev 2 requires approved workaround and date; lower defects remain visible and are analyzed for trend.
""",
        ["quality objectives", "standards", "verification/validation", "sampling", "defect severity/SLA", "acceptance authority", "audit trail", "improvement"],
    ))

    write_csv(base / "WBS.csv", ["wbs", "control_account", "work_package", "deliverable", "owner", "start", "finish", "acceptance", "predecessor", "budget_usd", "status"], [
        {"wbs":"1.0","control_account":"Governance","work_package":"Initiate and plan","deliverable":"Approved baselines and controls","owner":"Project Manager","start":"W1","finish":"W4","acceptance":"G1","predecessor":"Mandate","budget_usd":48000,"status":"Complete"},
        {"wbs":"2.0","control_account":"Supply/logistics","work_package":"Procure, receive, stage logistics","deliverable":"360 controlled device kits plus approved spares","owner":"Procurement/Asset","start":"W2","finish":"W10","acceptance":"PO/receipt/serial reconciliation","predecessor":"Model standard","budget_usd":567000,"status":"In progress"},
        {"wbs":"3.0","control_account":"Engineering/readiness","work_package":"Build, security, apps, data, pilot","deliverable":"Released build and accepted pilot","owner":"Endpoint Lead","start":"W2","finish":"W6","acceptance":"G2/G3","predecessor":"Standards and hardware","budget_usd":63000,"status":"Complete"},
        {"wbs":"4.0","control_account":"Deployment","work_package":"Four production waves and hypercare","deliverable":"340 production + 20 pilot accepted devices","owner":"Deployment Lead","start":"W7","finish":"W16","acceptance":"Wave gates and user evidence","predecessor":"Pilot","budget_usd":84000,"status":"In progress"},
        {"wbs":"5.0","control_account":"Retirement","work_package":"Returns, sanitization, disposition, reconciliation","deliverable":"360 old-asset dispositions","owner":"Asset Manager","start":"W6","finish":"W18","acceptance":"G5 and final reconciliation","predecessor":"User/data release","budget_usd":18000,"status":"In progress"},
        {"wbs":"6.0","control_account":"Reserve","work_package":"Management reserve","deliverable":"Approved uncertainty response","owner":"Sponsor","start":"W1","finish":"W18","acceptance":"Approved draw","predecessor":"Change","budget_usd":12000,"status":"Protected portion"},
    ], "Hardware Predictive work breakdown structure — filled example")

    write_csv(base / "INTEGRATED_MASTER_SCHEDULE.csv", ["activity_id", "wbs", "activity", "duration_days", "predecessors", "baseline_start", "baseline_finish", "forecast_finish", "critical", "owner", "acceptance", "status"], [
        {"activity_id":"HWI-001","wbs":"1.0","activity":"Charter and discovery","duration_days":10,"predecessors":"None","baseline_start":"W1","baseline_finish":"W2","forecast_finish":"W2","critical":"Yes","owner":"PM","acceptance":"G0","status":"Complete"},
        {"activity_id":"HWI-010","wbs":"1.0","activity":"Baseline WBS/IMS/cost/quality/risk/procurement/change","duration_days":10,"predecessors":"HWI-001","baseline_start":"W3","baseline_finish":"W4","forecast_finish":"W4","critical":"Yes","owner":"PM","acceptance":"G1","status":"Complete"},
        {"activity_id":"HWI-020","wbs":"2.0","activity":"Procure and receive devices","duration_days":35,"predecessors":"HWI-001","baseline_start":"W2","baseline_finish":"W8","forecast_finish":"W8","critical":"Yes","owner":"Procurement","acceptance":"Receipt/serials","status":"Complete"},
        {"activity_id":"HWI-030","wbs":"3.0","activity":"Build, apps, data and pilot","duration_days":25,"predecessors":"HWI-010, HWI-020 partial","baseline_start":"W2","baseline_finish":"W6","forecast_finish":"W6","critical":"Yes","owner":"Endpoint Lead","acceptance":"G2/G3","status":"Complete"},
        {"activity_id":"HWI-040","wbs":"4.0","activity":"Site A Wave 1","duration_days":10,"predecessors":"HWI-030","baseline_start":"W7","baseline_finish":"W8","forecast_finish":"W8","critical":"Yes","owner":"Site A Lead","acceptance":"Wave exit","status":"Complete"},
        {"activity_id":"HWI-050","wbs":"4.0","activity":"Site B Wave 2","duration_days":10,"predecessors":"HWI-040","baseline_start":"W9","baseline_finish":"W10","forecast_finish":"W10","critical":"Yes","owner":"Site B Lead","acceptance":"Wave exit","status":"Complete"},
        {"activity_id":"HWI-060","wbs":"4.0","activity":"Site C Wave 3","duration_days":10,"predecessors":"HWI-050","baseline_start":"W11","baseline_finish":"W12","forecast_finish":"W12","critical":"Yes","owner":"Site C Lead","acceptance":"Wave exit","status":"Complete"},
        {"activity_id":"HWI-070","wbs":"4.0","activity":"Remote/all-sites Wave 4","duration_days":15,"predecessors":"HWI-060","baseline_start":"W13","baseline_finish":"W15","forecast_finish":"W16","critical":"Yes","owner":"Remote Lead","acceptance":"Wave exit","status":"Forecast +1 week"},
        {"activity_id":"HWI-080","wbs":"5.0","activity":"Exception, return and sanitization closure","duration_days":15,"predecessors":"HWI-070","baseline_start":"W16","baseline_finish":"W18","forecast_finish":"W18","critical":"Yes","owner":"Exception/Asset Leads","acceptance":"360 dispositions","status":"In progress"},
        {"activity_id":"HWI-090","wbs":"1.0","activity":"Service and sponsor closure","duration_days":5,"predecessors":"HWI-080","baseline_start":"W18","baseline_finish":"W18","forecast_finish":"W18","critical":"Yes","owner":"PM","acceptance":"G6","status":"Planned"},
    ], "Hardware Predictive integrated master schedule — filled example")

    write_csv(base / "EARNED_VALUE.csv", ["period", "bac_usd", "pv_usd", "ev_usd", "ac_usd", "sv_usd", "cv_usd", "spi", "cpi", "eac_usd", "vac_usd", "forecast", "interpretation"], [
        {"period":"End Week 10","bac_usd":792000,"pv_usd":612000,"ev_usd":598000,"ac_usd":586000,"sv_usd":-14000,"cv_usd":12000,"spi":0.98,"cpi":1.02,"eac_usd":776000,"vac_usd":16000,"forecast":"Week 18","interpretation":"Small schedule watch; cost favorable; no quality reduction"},
        {"period":"End Week 15","bac_usd":792000,"pv_usd":730000,"ev_usd":708000,"ac_usd":689000,"sv_usd":-22000,"cv_usd":19000,"spi":0.97,"cpi":1.03,"eac_usd":748400,"vac_usd":43600,"forecast":"Week 18 with exception closure","interpretation":"Wave 4 +1 week uses planned closure window; 16 exceptions visible"},
    ], "Hardware Predictive earned value status — filled example")

    write(base / "EXECUTIVE_STATUS.md", document(
        "Hardware Predictive Executive Status — Illustrative Checkpoint",
        "Present baseline performance, acceptance, forecast, risk, changes, and decisions.",
        f"""## Overall: Amber — final milestone held; exception work is critical path

{table(["Control", "Evidence", "Forecast/action"], [
    ["Scope", "344/360 deployed; 16 controlled exceptions", "360 dispositions by Week 18"],
    ["Schedule", "SPI 0.97; Wave 4 forecast +1 week", "Use closure window; no final date change"],
    ["Cost", "CPI 1.03; EAC $748.4K vs BAC $792K", "$43.6K favorable forecast"],
    ["Quality", "97.7% first-time-right; 99.4% data pass", "Thresholds met; specialized defects open"],
    ["Assets", "334/344 returns", "Remote returns and holds on critical path"],
  ])}

## Changes and decisions

No baseline quantity is reduced. One Level 2 schedule change uses planned closure float for Wave 4. Steering approval is requested for specialized support capacity and remote courier escalation; sanitization remains blocked for any open data/hold item.
""",
        ["status date", "scope/schedule/cost baselines", "EVM", "quality/acceptance", "RAID", "changes", "decisions", "next gates", "confidence"],
    ))

    write(base / "ARTIFACT_INDEX.md", document(
        "Hardware Predictive Playbook Artifact Index",
        "Provide the PMBOK 8-aligned predictive review order plus shared controls.",
        """## Method-specific artifacts

1. `PLAYBOOK.md`
2. `PMBOK8_ALIGNMENT.md`
3. `WBS.csv`
4. `INTEGRATED_MASTER_SCHEDULE.csv`
5. `STAGE_GATES_AND_CHANGE_CONTROL.md`
6. `QUALITY_MANAGEMENT_PLAN.md`
7. `EARNED_VALUE.csv`
8. `EXECUTIVE_STATUS.md`

## Shared controls

Every file in `../common/` remains part of the complete playbook. Predictive planning does not replace endpoint, security, data, application, asset, sanitization, user, vendor, or service acceptance.
""",
        ["method artifacts", "shared controls", "baseline/version", "owners", "approval", "dashboard", "archive"],
    ))


def build_hw_hybrid(base: Path) -> None:
    write(base / "PLAYBOOK.md", document(
        "Enterprise Hardware Refresh — Hybrid Playbook",
        "Combine predictive procurement, security, architecture, cost, and site gates with rolling-wave pull delivery and rapid exception learning.",
        f"""## Why Hybrid is the recommended case approach

The 360-device quantity, budget, standards, vendor orders, security controls, site blackouts, and sanitization obligations need formal baselines. User readiness, application defects, local data, appointments, and remote returns are variable and benefit from continuous pull, WIP limits, and short feedback loops.

## Operating model

{table(["Layer", "Predictive control", "Adaptive control"], [
    ["Portfolio guardrails", "Charter, 360 scope, $792K cost, Week 18, standards, control/acceptance baselines", "Steering reprioritizes cohorts inside approved thresholds"],
    ["Supply/build", "PO, receipt, build release, pilot and wave gates", "Daily staging pull with WIP 24 and defect learning"],
    ["Deployment", "Four site/wave milestones and T-5/T-1 go/no-go", "Two-week rolling-wave planning; device cards pulled by readiness/capacity"],
    ["Exceptions", "Risk/change authority and final disposition requirement", "Kanban exception lane; aging/SLE and swarming"],
    ["Control/reporting", "Baseline/forecast, quality, RAID, budget, acceptance", "Flow/outcome metrics and retrospectives"],
  ])}

## Cadence

- Steering biweekly; CCB and build/security authority weekly/as needed.
- Two-week wave-planning horizon; twice-weekly replenishment; daily flow/incident review.
- T-5/T-1 wave gates remain formal. After each wave, a review/retro changes policies/build/backlog before the next release.
- Monthly benefit/operations review continues after project closure.

## Decision rights

Baseline changes use predictive integrated change control. The delivery team may reorder ready cards and adjust WIP/capacity within an approved wave. Security, data, custody, sanitization, and user/business acceptance are immutable completion conditions. Exceptions remain in the 360 denominator until accepted disposition.
""",
        ["predictive guardrails", "adaptive work types", "cadences", "baseline/change thresholds", "workflow/WIP", "wave gates", "exception lane", "metrics", "governance", "closure/benefits"],
    ))

    write(base / "INTEGRATED_GOVERNANCE.md", document(
        "Hardware Hybrid Integrated Governance and Decision Matrix",
        "Prevent duplicate plans and clarify when a decision belongs to the baseline, wave, or flow system.",
        f"""## Decision matrix

{table(["Decision", "System", "Authority", "Evidence"], [
    ["Device quantity/model, budget, final date", "Predictive baseline", "Steering Committee", "Change impact and recommendation"],
    ["Build/security/app/data release", "Technical quality gate", "Endpoint/Security/App/Data owners", "Test and rollback evidence"],
    ["Site wave release", "Predictive milestone gate", "Business Site + PM + Security", "T-5/T-1 readiness"],
    ["Which ready users/devices are pulled next", "Adaptive flow", "Wave Team", "Priority, readiness, WIP and capacity"],
    ["WIP/SLE/capacity policy", "Adaptive improvement", "Delivery Lead + service owners", "Flow/outcome trend and experiment"],
    ["Risk acceptance or sanitization exception", "Enterprise control", "Designated authority only", "Documented residual risk/expiry"],
  ])}

## One source of truth

The baseline owns authorized scope/cost/date. The deployment-wave register owns release quantities and acceptance. The Kanban board owns current work state. Inventory owns device/asset identity. RAID owns exposure. No status is manually reconciled by narrative; dashboards derive from these sources.
""",
        ["decision categories", "systems of record", "authorities", "thresholds", "cadence", "escalation", "baseline/board reconciliation", "evidence"],
    ))

    write(base / "ROLLING_WAVE_AND_FLOW_PLAN.md", document(
        "Hardware Hybrid Rolling-Wave and Flow Plan",
        "Translate the approved master plan into near-term ready work without overcommitting uncertain exceptions.",
        f"""## Planning horizons

{table(["Horizon", "Detail", "Update"], [
    ["Program — 18 weeks", "Milestones, budget, sites, device totals, gates, dependencies", "Formal baseline/change"],
    ["Release — next 4 weeks", "Site/wave targets, supply/build/app/data/support capacity", "Weekly integrated review"],
    ["Delivery — next 2 weeks", "Ready user/device cards with acceptance and appointment", "Twice-weekly replenishment"],
    ["Daily", "WIP, blockers, aging, incidents, returns, sanitization", "Daily flow review"],
  ])}

## Flow design

Use Ready → Staging (24) → Scheduled (40) → Deploying (12) → Hypercare (30) → Return/Sanitize (35) → Done. An exception lane has WIP 10 and is ordered by business/security impact, aging, and fixed-date risk. Exceeding WIP requires finishing/swarming or an explicit temporary capacity decision—not silently starting more.

## Wave reconciliation

At T-5, the wave target is split into Ready, controlled exception with new date, and not authorized. At T+5, deployed/accepted, quality/compliance, returns, open exceptions, budget, and lessons update both the baseline forecast and the flow policies.
""",
        ["planning horizons", "wave targets", "ready policy", "workflow/WIP", "exception lane", "capacity", "replenishment", "reconciliation", "forecast"],
    ))

    write_csv(base / "INTEGRATED_PLAN.csv", ["plan_id", "level", "work_or_milestone", "baseline_week", "rolling_window", "target_qty", "ready_qty", "accepted_qty", "wip", "forecast_week", "owner", "gate_or_policy", "status"], [
        {"plan_id":"HY-001","level":"Program","work_or_milestone":"Approved 360-device scope and Week 18 close","baseline_week":"W18","rolling_window":"18 weeks","target_qty":360,"ready_qty":344,"accepted_qty":344,"wip":16,"forecast_week":"W18","owner":"PM","gate_or_policy":"G6 closure","status":"Amber"},
        {"plan_id":"HY-010","level":"Release","work_or_milestone":"Remote/all-sites Wave 4","baseline_week":"W13-W15","rolling_window":"4 weeks","target_qty":80,"ready_qty":72,"accepted_qty":72,"wip":8,"forecast_week":"W16","owner":"Remote Lead","gate_or_policy":"T-5/T-1 + WIP","status":"Watch"},
        {"plan_id":"HY-020","level":"Delivery","work_or_milestone":"Standard remaining refresh cards","baseline_week":"N/A","rolling_window":"2 weeks","target_qty":8,"ready_qty":8,"accepted_qty":0,"wip":8,"forecast_week":"W16","owner":"Wave Team","gate_or_policy":"Ready/pull/DoD","status":"On track"},
        {"plan_id":"HY-030","level":"Exception","work_or_milestone":"Application/accessibility/data/logistics exceptions","baseline_week":"W18 closure","rolling_window":"Daily","target_qty":16,"ready_qty":4,"accepted_qty":0,"wip":10,"forecast_week":"W17-W18","owner":"Exception Manager","gate_or_policy":"Exception WIP 10 / aging","status":"Amber"},
    ], "Hardware Hybrid integrated baseline and rolling-wave plan — filled example")

    write_csv(base / "HYBRID_METRICS.csv", ["period", "baseline_finish", "forecast_finish", "baseline_budget_usd", "forecast_usd", "accepted_devices", "remaining_exceptions", "throughput_week", "p85_cycle_days", "first_time_right_pct", "compliant_24h_pct", "returns_pct", "decision"], [
        {"period":"End W12","baseline_finish":"W18","forecast_finish":"W18","baseline_budget_usd":792000,"forecast_usd":759000,"accepted_devices":272,"remaining_exceptions":17,"throughput_week":39,"p85_cycle_days":6.4,"first_time_right_pct":97.5,"compliant_24h_pct":98.6,"returns_pct":97.3,"decision":"Keep wave milestone; cap staging WIP"},
        {"period":"End W15","baseline_finish":"W18","forecast_finish":"W18","baseline_budget_usd":792000,"forecast_usd":748400,"accepted_devices":344,"remaining_exceptions":16,"throughput_week":42,"p85_cycle_days":6.2,"first_time_right_pct":97.7,"compliant_24h_pct":98.5,"returns_pct":97.1,"decision":"Shift capacity to exception/remote return lanes"},
    ], "Hardware Hybrid baseline, flow, quality, and outcome metrics — filled example")

    write(base / "EXECUTIVE_STATUS.md", document(
        "Hardware Hybrid Executive Status — Illustrative Checkpoint",
        "Combine baseline confidence and flow evidence into one decision view.",
        f"""## Overall: Amber — Week 18 and budget remain controlled; exception system is the constraint

{table(["Lens", "Evidence", "Management response"], [
    ["Baseline", "360 devices, $792K, Week 18 unchanged", "Protect scope truth and control gates"],
    ["Forecast", "$748.4K; final Week 18", "Use available reserve only by approved change"],
    ["Flow", "42/week; P85 6.2 days; WIP 61", "Stop starting standard work; finish exceptions/returns"],
    ["Outcome", "344 accepted; 97.7% FTR; 98.5% compliant", "Quality thresholds met"],
    ["Constraint", "16 exceptions; 334/344 returns", "Specialized capacity and courier escalation"],
  ])}

## Steering decisions

Approve temporary exception-lane specialists through Week 18, require T+3 courier escalation for remote returns, and keep any open data/hold item quarantined from sanitization. No change to the 360 denominator is requested.
""",
        ["baseline/forecast", "flow/WIP/SLE", "outcome/quality", "exceptions/risks", "budget/reserve", "decisions", "next gates", "evidence"],
    ))

    write(base / "ARTIFACT_INDEX.md", document(
        "Hardware Hybrid Playbook Artifact Index",
        "Provide the Hybrid review order plus the complete shared control pack.",
        """## Method-specific artifacts

1. `PLAYBOOK.md`
2. `INTEGRATED_GOVERNANCE.md`
3. `ROLLING_WAVE_AND_FLOW_PLAN.md`
4. `INTEGRATED_PLAN.csv`
5. `HYBRID_METRICS.csv`
6. `EXECUTIVE_STATUS.md`

## Shared controls

Every file in `../common/` is part of the playbook. Hybrid changes planning and decision cadence; it does not create two competing truths or weaken security, data, asset, sanitization, user, financial, or service acceptance.
""",
        ["method artifacts", "shared controls", "systems of record", "owners", "version", "dashboard", "archive"],
    ))


def enterprise_scenario(
    *, code: str, slug: str, title: str, methodology: str, home_anchor: str,
    duration: str, timeline_max: int, budget: str, tco: str, status: str,
    health: str, summary: str, decision: str, metrics: list[dict[str, str]],
    phases: list[dict[str, object]], financials: list[dict[str, object]],
    financial_note: str, risks: list[dict[str, object]], team: list[dict[str, str]],
    artifacts: list[dict[str, str]], closure: dict[str, object], role: str,
) -> dict[str, object]:
    return {
        "code": code,
        "slug": slug,
        "title": title,
        "methodology": methodology,
        "home_anchor": home_anchor,
        "program_type": "Experience-informed enterprise transformation case study",
        "client": "Company ABC / Company XYZ — anonymized fictional scenario",
        "role": role,
        "status": status,
        "health": health,
        "duration": duration,
        "budget": budget,
        "tco": tco,
        "summary": summary,
        "decision": decision,
        "metrics": metrics,
        "timeline_unit": "Week",
        "timeline_max": timeline_max,
        "phases": phases,
        "financials": financials,
        "financial_note": financial_note,
        "risks": risks,
        "team": team,
        "artifacts": artifacts,
        "closure": closure,
    }


def ma_artifacts(method: str) -> list[dict[str, str]]:
    base = MA / method
    common = MA / "common"
    method_labels = {
        "agile": [
            ("PLAYBOOK.md", "Method", "Agile delivery playbook"),
            ("OUTCOME_ROADMAP.csv", "Roadmap", "Outcome and release roadmap"),
            ("PRODUCT_BACKLOG.csv", "Backlog", "Prioritized integration backlog"),
            ("SPRINT_PLAN.csv", "Delivery", "Sprint plan and review record"),
            ("DEFINITION_OF_READY_DONE.md", "Quality", "Definition of Ready and Done"),
            ("AGILE_METRICS.csv", "Metrics", "Flow, quality, and outcome metrics"),
            ("EXECUTIVE_STATUS.md", "Reporting", "Agile executive status"),
        ],
        "predictive": [
            ("PLAYBOOK.md", "Method", "Predictive / Waterfall playbook"),
            ("PMBOK8_ALIGNMENT.md", "PMBOK 8", "PMBOK 8 alignment matrix"),
            ("WBS.csv", "Scope", "Work breakdown structure"),
            ("INTEGRATED_MASTER_SCHEDULE.csv", "Schedule", "Integrated master schedule"),
            ("STAGE_GATES_AND_CHANGE_CONTROL.md", "Governance", "Stage gates and change control"),
            ("QUALITY_MANAGEMENT_PLAN.md", "Quality", "Quality management plan"),
            ("EARNED_VALUE.csv", "Metrics", "Earned value status"),
            ("EXECUTIVE_STATUS.md", "Reporting", "Predictive executive status"),
        ],
    }[method]
    shared = [
        (MA / "M_AND_A_IT_INTEGRATION_PLAYBOOKS.docx", "Guide", "Download the two-playbook Word guide"),
        (MA / "M_AND_A_INTEGRATION_CONTROL_WORKBOOK.xlsx", "Workbook", "Download the M&A control workbook"),
        (common / "PORTFOLIO_GUIDE.md", "Orientation", "Portfolio guide and truth boundary"),
        (common / "PROJECT_CHARTER.md", "Initiate", "Project charter"),
        (common / "DAY_1_EMPLOYEE_EXPERIENCE_PLAN.md", "Day 1", "Employee experience plan"),
        (common / "IDENTITY_AND_ACCESS_PLAN.md", "Identity", "Identity and access plan"),
        (common / "NETWORK_INFRASTRUCTURE_PLAN.md", "Network", "Network and infrastructure plan"),
        (common / "COLLABORATION_MIGRATION_PLAN.md", "Migration", "Collaboration migration plan"),
        (common / "APPLICATION_RATIONALIZATION_AND_DATA_PLAN.md", "Applications", "Application rationalization and data plan"),
        (common / "SECURITY_PRIVACY_AND_LEGAL_HOLD.md", "Assurance", "Security, privacy, and legal-hold plan"),
        (common / "CUTOVER_ROLLBACK_HYPERCARE.md", "Cutover", "Cutover, rollback, and hypercare runbook"),
        (common / "RAID_REGISTER.csv", "Controls", "RAID register"),
        (common / "APPLICATION_PORTFOLIO.csv", "Inventory", "Application portfolio and dispositions"),
        (common / "SOURCE_REGISTER.csv", "Research", "Authoritative source register"),
    ]
    return [artifact(path, category, label) for path, category, label in shared] + [artifact(base / name, category, label) for name, category, label in method_labels]


def hw_artifacts(method: str) -> list[dict[str, str]]:
    base = HW / method
    common = HW / "common"
    method_labels = {
        "kanban": [
            ("PLAYBOOK.md", "Method", "Kanban delivery playbook"),
            ("EXPLICIT_POLICIES.md", "Flow", "Explicit policies and SLEs"),
            ("KANBAN_BOARD.csv", "Board", "Representative Kanban board"),
            ("FLOW_METRICS.csv", "Metrics", "Flow and outcome metrics"),
            ("SERVICE_DELIVERY_REVIEW.md", "Governance", "Service delivery review"),
            ("EXECUTIVE_STATUS.md", "Reporting", "Kanban executive status"),
        ],
        "scrum": [
            ("PLAYBOOK.md", "Method", "Scrum delivery playbook"),
            ("PRODUCT_BACKLOG.csv", "Backlog", "Product Backlog"),
            ("SPRINT_PLAN.csv", "Delivery", "Sprint plan and review record"),
            ("DEFINITION_OF_DONE.md", "Quality", "Definition of Done"),
            ("SCRUM_METRICS.csv", "Metrics", "Sprint outcome and quality metrics"),
            ("EXECUTIVE_STATUS.md", "Reporting", "Scrum executive status"),
        ],
        "predictive": [
            ("PLAYBOOK.md", "Method", "Predictive / Waterfall playbook"),
            ("PMBOK8_ALIGNMENT.md", "PMBOK 8", "PMBOK 8 alignment matrix"),
            ("WBS.csv", "Scope", "Work breakdown structure"),
            ("INTEGRATED_MASTER_SCHEDULE.csv", "Schedule", "Integrated master schedule"),
            ("STAGE_GATES_AND_CHANGE_CONTROL.md", "Governance", "Stage gates and change control"),
            ("QUALITY_MANAGEMENT_PLAN.md", "Quality", "Quality management plan"),
            ("EARNED_VALUE.csv", "Metrics", "Earned value status"),
            ("EXECUTIVE_STATUS.md", "Reporting", "Predictive executive status"),
        ],
        "hybrid": [
            ("PLAYBOOK.md", "Method", "Hybrid delivery playbook"),
            ("INTEGRATED_GOVERNANCE.md", "Governance", "Integrated decision matrix"),
            ("ROLLING_WAVE_AND_FLOW_PLAN.md", "Planning", "Rolling-wave and flow plan"),
            ("INTEGRATED_PLAN.csv", "Plan", "Integrated baseline and rolling-wave plan"),
            ("HYBRID_METRICS.csv", "Metrics", "Baseline, flow, quality, and outcome metrics"),
            ("EXECUTIVE_STATUS.md", "Reporting", "Hybrid executive status"),
        ],
    }[method]
    shared = [
        (HW / "HARDWARE_REFRESH_FOUR_PLAYBOOKS.docx", "Guide", "Download the four-playbook Word guide"),
        (HW / "HARDWARE_REFRESH_CONTROL_WORKBOOK.xlsx", "Workbook", "Download the hardware control workbook"),
        (common / "PORTFOLIO_GUIDE.md", "Orientation", "Portfolio guide and truth boundary"),
        (common / "PROJECT_CHARTER.md", "Initiate", "Project charter"),
        (common / "DEVICE_BUILD_AND_PROVISIONING_STANDARD.md", "Engineering", "Device build and provisioning standard"),
        (common / "PROCUREMENT_STAGING_AND_LOGISTICS.md", "Supply", "Procurement, staging, and logistics plan"),
        (common / "APPLICATION_AND_DATA_READINESS.md", "Readiness", "Application and data readiness plan"),
        (common / "SECURITY_COMPLIANCE_AND_SANITIZATION.md", "Assurance", "Security, compliance, and sanitization plan"),
        (common / "DEPLOYMENT_HYPERCARE_AND_SERVICE_TRANSITION.md", "Deployment", "Deployment, hypercare, and transition plan"),
        (common / "ASSET_RETIREMENT_AND_CLOSEOUT.md", "Closeout", "Asset retirement and closeout plan"),
        (common / "RAID_REGISTER.csv", "Controls", "RAID register"),
        (common / "INVENTORY_AND_ASSET_RECONCILIATION.csv", "Inventory", "Inventory and asset reconciliation"),
        (common / "DEPLOYMENT_WAVES.csv", "Dashboard", "Deployment wave source data"),
        (common / "SANITIZATION_CHAIN_OF_CUSTODY.csv", "Custody", "Sanitization chain of custody"),
        (common / "SOURCE_REGISTER.csv", "Research", "Authoritative source register"),
    ]
    return [artifact(path, category, label) for path, category, label in shared] + [artifact(base / name, category, label) for name, category, label in method_labels]


def build_dashboard_data() -> None:
    ma_team = [
        {"role":"Executive Sponsor / Steering Committee","accountability":"Outcome, funding, target state, risk acceptance, and gate decisions."},
        {"role":"M&A IT Technical Project Manager","accountability":"Integrated plan, dependencies, RAID, vendors, status, cutover command, and closure."},
        {"role":"Corp Dev / Legal / Privacy / HR","accountability":"Deal restrictions, roster, legal hold, privacy, communications, and people decisions."},
        {"role":"IAM / Endpoint / Network / Cloud","accountability":"Day 1 identity/device and secure, observable infrastructure integration."},
        {"role":"Collaboration / Application / Data Owners","accountability":"Migration, rationalization, workflow, retention, validation, and decommission acceptance."},
        {"role":"Security / Service Operations / Vendors","accountability":"Control approval, monitoring, support, rollback, hypercare, and durable handoff."},
    ]
    hw_team = [
        {"role":"Executive Sponsor / Steering Committee","accountability":"Outcome, funding, scope/date, risk acceptance, and escalated exceptions."},
        {"role":"Technical Project Manager","accountability":"Integrated delivery, methods, RAID, waves, vendors, reporting, and closure."},
        {"role":"Endpoint Engineering / IAM / InfoSec","accountability":"Build, provisioning, join, policy, compliance, test, and release authority."},
        {"role":"Procurement / Logistics / Asset Management","accountability":"Orders, receipts, serialized custody, staging, distribution, returns, and disposition."},
        {"role":"Application / Data / Business Site Owners","accountability":"Persona readiness, data protection, task validation, user acceptance, and site impacts."},
        {"role":"Service Desk / Field Support / Vendors","accountability":"Appointments, incident restoration, spares, knowledge, escalation, and service transition."},
    ]
    ma_financials = [
        {"label":"Authorized baseline","value":1860000,"display":"$1.860M","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Current commitments","value":1782000,"display":"$1.782M","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Actual to checkpoint","value":1126000,"display":"$1.126M","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Forecast at completion","value":1782000,"display":"$1.782M","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Forecast variance","value":78000,"display":"$78K favorable","evidence_class":"Derived calculation","confidence":"Low"},
    ]
    hw_financials = [
        {"label":"Authorized baseline","value":792000,"display":"$792K","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Current commitments","value":748400,"display":"$748.4K","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Actual to checkpoint","value":675500,"display":"$675.5K","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Forecast at completion","value":748400,"display":"$748.4K","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Forecast variance","value":43600,"display":"$43.6K favorable","evidence_class":"Derived calculation","confidence":"Low"},
    ]
    ma_risks = [
        {"id":"MA-R-001","risk":"Identity duplicates or stale contractor records block Day 1 access","score":20,"status":"Mitigating","response":"Roster reconciliation at T-10/T-3/T-0; named exception path."},
        {"id":"MA-R-002","risk":"Overlapping subnets disrupt routing or DNS","score":15,"status":"Mitigating","response":"Collision register, NAT/renumber, isolated test, route-withdrawal rollback."},
        {"id":"MA-R-003","risk":"Collaboration permissions, retention, or integrations differ after migration","score":15,"status":"Mitigating","response":"Identity-first mapping, legal review, pilot, counts/samples/permission validation."},
        {"id":"MA-I-004","risk":"Fifteen workers remain on controlled Day 1 exceptions","score":15,"status":"Open","response":"Tested workarounds, named owners/expiry, daily burn-down and manager communication."},
    ]
    hw_risks = [
        {"id":"HW-R-003","risk":"Critical application, driver, VPN, or peripheral fails on the new build","score":16,"status":"Mitigating","response":"Persona pilot, versioned package, fallback, and owner acceptance."},
        {"id":"HW-R-002","risk":"Local or application data is not protected before retirement","score":15,"status":"Mitigating","response":"Precheck, approved backup/KFM, validation, and sanitization hold."},
        {"id":"HW-I-005","risk":"Sixteen application, accessibility, leave, or logistics exceptions remain","score":15,"status":"Open","response":"Named owners/dates/workarounds; specialized capacity and weekly steering."},
        {"id":"HW-R-004","risk":"Returned-device custody or sanitization evidence is incomplete","score":10,"status":"Mitigating","response":"Serial scans, secure storage, evidence validation, and quarantine."},
    ]
    ma_metrics = [
        {"label":"Day 1 fully ready","value":"665 / 680","note":"97.8%; 15 controlled exceptions","state":"watch","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Authentication success","value":"674 / 680","note":"99.1% at Day 1 checkpoint","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Pilot reconciliation","value":"99.7%","note":"Workspace pilot; defined exclusions retained","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Applications discovered","value":"142","note":"Every app requires owner and disposition","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Overlaps targeted","value":"22 / 37","note":"Retire or consolidate after acceptance","state":"watch","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Forecast vs baseline","value":"$1.782M","note":"$78K below $1.860M authorization","state":"pass","evidence_class":"Derived calculation","confidence":"Low"},
    ]
    hw_metrics = [
        {"label":"Devices deployed","value":"344 / 360","note":"95.6%; 16 controlled exceptions","state":"watch","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"First-time-right","value":"336 / 344","note":"97.7% accepted without rework","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Data validation","value":"342 / 344","note":"99.4% pass or approved no-data path","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Compliant within 24h","value":"339 / 344","note":"98.5%; five owned remediations","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Old devices returned","value":"334 / 344","note":"97.1%; remote return action open","state":"watch","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Forecast vs baseline","value":"$748.4K","note":"$43.6K below $792K authorization","state":"pass","evidence_class":"Derived calculation","confidence":"Low"},
    ]

    ma_agile = enterprise_scenario(
        code="M&A 01A", slug="ma-it-integration-agile", title="M&A IT Integration — Agile Playbook",
        methodology="Agile", home_anchor="ma-integration", duration="20 weeks / 10 two-week sprints",
        timeline_max=20, budget="$1.860M modeled authorization", tco="Modeled forecast: $1.782M",
        status="Illustrative checkpoint — Amber", health="Amber",
        summary="Integrate Company XYZ into Company ABC through outcome-based releases: secure Day 1 employee experience, identity and network bridges, Google Workspace/Slack/Asana/Jira migration, application rationalization, hypercare, and controlled convergence.",
        decision="Continue the migration release plan; hold the Jira production cohort until automation regression passes, close 15 Day 1 exceptions, and preserve source retention until legal-hold validation is accepted.",
        metrics=ma_metrics,
        phases=[
            {"name":"Foundation and discovery","start":1,"end":4,"status":"Complete"},
            {"name":"Day 1 minimum viable experience","start":3,"end":6,"status":"Accepted with exceptions"},
            {"name":"Pilot migrations and secure interconnect","start":5,"end":8,"status":"In progress"},
            {"name":"Production migration waves","start":9,"end":16,"status":"Planned / rolling"},
            {"name":"Convergence, decommission, and closure","start":17,"end":20,"status":"Planned"},
        ], financials=ma_financials,
        financial_note="All amounts are fictional planning assumptions. The Agile forecast is refreshed from accepted increments, vendor commitments, remaining backlog, reserve, and identified uncertainty. No projected license reduction is a realized saving until Finance validates the stopped invoice or contract.",
        risks=ma_risks, team=ma_team, artifacts=ma_artifacts("agile"),
        closure={"schedule":"Forecast Week 20", "budget":"Forecast $1.782M vs $1.860M",
                 "acceptance":["Day 1 employee readiness and exception evidence","Accepted identity/network/collaboration/application increments","Source/temporary control removal only after approval","Operations and benefits owners named"],
                 "lessons":["Identity-first sequencing reduces migration ambiguity","Fixed gates and adaptive discovery can coexist","Completion requires business, data, permission, and support evidence"]},
        role="M&A IT Technical Project Manager — Agile integration lead",
    )
    ma_predictive = enterprise_scenario(
        code="M&A 01P", slug="ma-it-integration-predictive", title="M&A IT Integration — Predictive / Waterfall Playbook",
        methodology="Predictive / Waterfall — PMBOK 8 aligned", home_anchor="ma-integration", duration="24 weeks / seven stage gates",
        timeline_max=24, budget="$1.860M modeled BAC", tco="Modeled EAC: $1.782M",
        status="Illustrative checkpoint — Amber", health="Amber",
        summary="Deliver the same Company ABC/XYZ integration through formal scope, WBS, schedule and cost baselines; staged design, Day 1, migration, decommission, and closeout gates; integrated change control; quality assurance; and earned value reporting.",
        decision="Maintain the Week 24 baseline and hold Jira production release. Use available schedule float for the collaboration recovery plan; do not reduce validation, rollback, or legal-hold controls to improve SPI.",
        metrics=[
            {"label":"Schedule performance","value":"SPI 0.97","note":"Week 24 finish remains forecast","state":"watch","evidence_class":"Derived calculation","confidence":"Low"},
            {"label":"Cost performance","value":"CPI 1.02","note":"Modeled EAC $1.782M","state":"pass","evidence_class":"Derived calculation","confidence":"Low"},
            *ma_metrics[:4],
        ],
        phases=[
            {"name":"Initiate and due diligence","start":1,"end":3,"status":"Complete"},
            {"name":"Plan, design, and baseline","start":2,"end":6,"status":"Complete"},
            {"name":"Build, pilot, and Day 1","start":5,"end":10,"status":"Accepted with exceptions"},
            {"name":"Migration production waves","start":9,"end":19,"status":"In progress"},
            {"name":"Converge and decommission","start":18,"end":23,"status":"Planned"},
            {"name":"Close and transfer benefits","start":24,"end":24,"status":"Planned"},
        ], financials=ma_financials,
        financial_note="BAC, PV, EV, AC, EAC, and VAC are fictional. Earned value is credited only for accepted deliverables at the defined measurement rule; financial favorability never substitutes for quality, security, data, or business acceptance.",
        risks=ma_risks, team=ma_team, artifacts=ma_artifacts("predictive"),
        closure={"schedule":"Baseline and forecast Week 24", "budget":"EAC $1.782M vs BAC $1.860M",
                 "acceptance":["Gates G0–G6 have documented decisions","WBS deliverables trace to quality and acceptance evidence","Changes update affected baselines and stakeholders","Operations, risks, contracts, financials, and benefits transferred"],
                 "lessons":["Rolling-wave detail protects an honest predictive baseline","EVM needs acceptance-based earning rules","Decommission is a governed deliverable, not an administrative afterthought"]},
        role="M&A IT Technical Project Manager — Predictive integration lead",
    )

    method_metric = {
        "kanban": {"label":"Latest throughput","value":"42 / week","note":"P85 cycle time 6.2 business days","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
        "scrum": {"label":"Product Goal progress","value":"344 / 360","note":"Accepted Increments; 16 PBIs remain","state":"watch","evidence_class":"Scenario assumption","confidence":"Low"},
        "predictive": {"label":"Schedule / cost","value":"0.97 / 1.03","note":"SPI / CPI at Week 15","state":"watch","evidence_class":"Derived calculation","confidence":"Low"},
        "hybrid": {"label":"Baseline + flow","value":"W18 / 42 week","note":"Final forecast / latest throughput","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
    }
    hw_titles = {
        "kanban":"Enterprise Hardware Refresh — Kanban Playbook",
        "scrum":"Enterprise Hardware Refresh — Scrum Playbook",
        "predictive":"Enterprise Hardware Refresh — Predictive / Waterfall Playbook",
        "hybrid":"Enterprise Hardware Refresh — Hybrid Playbook",
    }
    hw_codes = {"kanban":"HW 02K","scrum":"HW 02S","predictive":"HW 02P","hybrid":"HW 02H"}
    hw_slugs = {key:f"hardware-refresh-{key}" for key in hw_titles}
    hw_methods = {"kanban":"Kanban","scrum":"Scrum","predictive":"Predictive / Waterfall — PMBOK 8 aligned","hybrid":"Hybrid — recommended operating model"}
    hw_summaries = {
        "kanban":"Run the 360-device, four-site refresh as a pull system with WIP limits, service classes, explicit policies, aging and cycle-time evidence, while retaining full security, data, asset, sanitization, support, and closure controls.",
        "scrum":"Deliver the same refresh through one Product Goal, an ordered Product Backlog, nine two-week Sprints, working accepted device/user/asset Increments, reviews, retrospectives, and a strict Definition of Done.",
        "predictive":"Deliver the same refresh through PMBOK 8-aligned predictive baselines, WBS, integrated schedule, procurement and wave stage gates, quality management, integrated change control, and earned value reporting.",
        "hybrid":"Combine fixed 360-device, budget, procurement, security, site, and sanitization guardrails with two-week rolling-wave planning, Kanban pull/WIP, exception aging, and wave retrospectives.",
    }
    hw_decisions = {
        "kanban":"Stop starting standard work; direct capacity to the 16 exception and remote-return items while preserving WIP limits and custody controls.",
        "scrum":"Keep 16 exception PBIs in the Product Backlog, allocate Sprint 9 to specialized closure, and do not count deferred items in the Increment.",
        "predictive":"Use planned closure float to absorb the Wave 4 slip, maintain the Week 18 milestone, and approve specialized support without reducing acceptance or sanitization controls.",
        "hybrid":"Maintain the Week 18/$792K baseline, shift rolling-wave capacity to exception/return lanes, and preserve formal security, data, custody, and closure gates.",
    }
    hw_phases = {
        "kanban":[
            {"name":"Design workflow, policy, and standards","start":1,"end":4,"status":"Complete"},
            {"name":"Supply, build, and pilot flow","start":3,"end":6,"status":"Complete"},
            {"name":"Continuous site/device delivery","start":7,"end":15,"status":"344 accepted"},
            {"name":"Exception, return, and service closure","start":16,"end":18,"status":"In progress"},
        ],
        "scrum":[
            {"name":"Sprints 1–2: foundation and pilot-ready build","start":1,"end":4,"status":"Complete"},
            {"name":"Sprint 3: accepted pilot Increment","start":5,"end":6,"status":"Complete"},
            {"name":"Sprints 4–7: site/wave Increments","start":7,"end":14,"status":"344 accepted"},
            {"name":"Sprints 8–9: exceptions, transition, closure","start":15,"end":18,"status":"Active"},
        ],
        "predictive":[
            {"name":"Initiate, plan, and baseline","start":1,"end":4,"status":"Complete"},
            {"name":"Procure, build, test, and pilot","start":2,"end":6,"status":"Complete"},
            {"name":"Production waves","start":7,"end":16,"status":"344 accepted"},
            {"name":"Retirement, transition, and close","start":16,"end":18,"status":"In progress"},
        ],
        "hybrid":[
            {"name":"Baseline guardrails and release system","start":1,"end":4,"status":"Complete"},
            {"name":"Pilot and flow calibration","start":3,"end":6,"status":"Complete"},
            {"name":"Gated rolling-wave delivery","start":7,"end":16,"status":"344 accepted"},
            {"name":"Exception/asset/service closure","start":16,"end":18,"status":"In progress"},
        ],
    }
    hw_scenarios = []
    for method in ("kanban", "scrum", "predictive", "hybrid"):
        hw_scenarios.append(enterprise_scenario(
            code=hw_codes[method], slug=hw_slugs[method], title=hw_titles[method], methodology=hw_methods[method],
            home_anchor="hardware-refresh", duration="18 weeks / four sites / 360 devices", timeline_max=18,
            budget="$792K modeled authorization", tco="Modeled forecast: $748.4K",
            status="Illustrative checkpoint — Amber", health="Amber", summary=hw_summaries[method], decision=hw_decisions[method],
            metrics=[method_metric[method], *hw_metrics[:5]], phases=hw_phases[method], financials=hw_financials,
            financial_note="All values are fictional planning assumptions. The $792K authorization and $748.4K forecast require real purchase orders, invoices, labor, tax/shipping, credits, warranty, and reserve approvals before use. User productivity or released capacity is not cash savings without Finance validation.",
            risks=hw_risks, team=hw_team, artifacts=hw_artifacts(method),
            closure={"schedule":"Forecast Week 18", "budget":"Forecast $748.4K vs $792K",
                     "acceptance":["360 of 360 device assignments have accepted final disposition","New build, security, app, data, and user evidence accepted","Old assets reconcile through custody and sanitization/disposition","Service, vendor, financial, risks, lessons, and benefits transferred"],
                     "lessons":["Readiness and downstream capacity must govern wave size","A device is not Done at handoff; old-asset disposition closes the loop","Specialized personas and remote returns need explicit capacity and earlier discovery"]},
            role=f"Technical Project Manager — {hw_methods[method]} hardware refresh lead",
        ))

    data = {
        "notice":"Enterprise case studies are anonymized, experience-informed fictional scenarios. Company ABC and Company XYZ are placeholders; modeled dates, costs, counts, and results are not prior-employer claims.",
        "sections":[
            {"id":"ma-integration","eyebrow":"Real-world technology transformation · Scenario 01","title":"M&A IT Integration — Two Complete Delivery Playbooks","intro":"A full IT-integration control pack from deal restrictions and Day 1 through identity, network, collaboration migrations, application rationalization, hypercare, decommissioning, and benefits—shown once in Agile and once in Predictive / Waterfall.","notice":"PMBOK Guide Eighth Edition is approach-neutral. The Predictive / Waterfall playbook is PMBOK 8 aligned; the Agile playbook uses iterative value delivery while retaining fixed legal, security, data, and Day 1 gates.","scenarios":[ma_agile, ma_predictive]},
            {"id":"hardware-refresh","eyebrow":"Real-world digital workplace delivery · Scenario 02","title":"Desktop, Laptop, and Phone Refresh — Four Complete Delivery Playbooks","intro":"One 360-device, four-site program with a shared technical/control pack and four distinct operating systems: Kanban, Scrum, Predictive / Waterfall, and Hybrid. Each has its own dashboard, planning artifacts, metrics, and executive status.","notice":"All four methods use the same mandatory endpoint, data, security, asset, sanitization, procurement, user, support, and closeout controls. Method selection changes how work is planned and governed—not whether those controls exist.","scenarios":hw_scenarios},
        ],
    }
    write(DATA, json.dumps(data, indent=2))


def artifact(path: Path, category: str, label: str) -> dict[str, str]:
    return {"path": path.relative_to(ROOT).as_posix(), "category": category, "label": label}


def main() -> None:
    build_ma()
    build_hardware()
    build_dashboard_data()
    print("Built enterprise portfolio source artifacts and dashboard data.")


if __name__ == "__main__":
    main()
