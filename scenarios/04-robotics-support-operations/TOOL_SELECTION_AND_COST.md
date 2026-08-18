# Tool Selection and Cost Model — Robotics Support

Abbreviations used below are Customer Relationship Management (CRM), Customer Service Management (CSM), Field Service Management (FSM), Over-the-Air software delivery (OTA), Continuous Integration (CI), Application Programming Interface (API), and Total Cost of Ownership (TCO). MCAP is the name of the robotics log-container format.

## Recommended target stack

| Layer | Preferred pattern | Why |
|---|---|---|
| Customer/installed base | Salesforce | Existing CRM; owns account, site, asset, contract and entitlement |
| Case/field work | ServiceNow CSM/FSM when enterprise field/asset complexity dominates; Zendesk plus field module for faster support setup | Owns customer case, communication, work order and dispatch |
| Engineering | Jira | Owns reproducible defects, changes and releases—not customer communication |
| Robot evidence | MCAP + Foxglove | Time-aligned robotics log capture, visualization and replay |
| Fleet operations | InOrbit or Formant after structured proof | Multi-robot health, mission and diagnostic operations |
| Observability | Prometheus + Grafana/Loki | Metrics, service/infrastructure dashboards and alerting |
| OTA/device | Mender or balena after architecture/security review | Inventory, controlled release rings and rollback |
| Remote access | Enterprise zero-trust access; Tailscale only for approved noncommercial lab use | Named identity, least privilege and audited path |
| Source/portfolio | GitHub | Code, docs, issues, CI and public portfolio |

Detailed current price snapshots and free/lab options are maintained in [`../../tools/TOOL_COMPARISON.md`](../../tools/TOOL_COMPARISON.md). Prices must be revalidated during procurement.

## Selection method

Score each candidate 1–5 for functional fit, safety/security, evidence/data portability, integrations/API, field/parts/asset depth, deployment model, admin burden, vendor viability, total cost, and exit risk. Weight requirements before demos; use representative workflows and data; require security/legal/procurement review; test export and failure modes; calculate three-year TCO.

## Portfolio lab

Use MuJoCo, MCAP, Foxglove free allowance, Prometheus/Grafana free or local, Jira/JSM free allowance, and GitHub. Simulate correlation from robot event to service case, engineering defect, release, work order and knowledge article. Never present a free/noncommercial tier as production approval.
