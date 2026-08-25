# M&A Integrated Cutover, Rollback, and Hypercare Runbook

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Provide a time-stamped control path from final readiness through go/no-go, execution, validation, rollback, and operations acceptance.

## Gate criteria

| Gate | Entry evidence | Decision |
| --- | --- | --- |
| T-10 readiness | Roster, inventory, design, vendor plan, communications, test status | Continue, recover, or de-scope |
| T-3 go/no-go | No open Sev 1; Tier 0 tests pass; rollback viable; staffing confirmed | Go, conditional go, hold |
| T-0 release | Backups/snapshots, freeze, monitoring, bridge, approvals | Start cutover |
| Wave validation | Counts, samples, permissions, business workflow, support health | Accept wave or rollback cohort |
| Hypercare exit | SLA stable, aged defects dispositioned, knowledge/ownership accepted | Transfer to operations |

## Command log excerpt — filled example

| Time | Action / checkpoint | Owner | Result | Decision |
| --- | --- | --- | --- | --- |
| Fri 18:00 | Freeze approved collaboration changes | Collaboration Lead | Passed; three emergency changes logged | Continue |
| Fri 19:00 | Confirm source backups/export and destination capacity | Data Lead | Passed | Continue |
| Fri 20:00 | Enable restricted identity/network bridge | IAM + Network | Passed; telemetry visible | Continue |
| Sat 02:00 | Run priority user/data delta and reconciliation | Migration Lead | 99.7% initial; 19 objects retried | Continue with watch |
| Sat 06:00 | Persona and business workflow tests | Business Owners | All Tier 0/1 passed | Release communications |
| Mon 10:00 | Day 1 checkpoint | Command Lead | 665 ready; 15 controlled exceptions | Remain in hypercare |

## Rollback decision

Rollback is assessed per identity cohort, network route/rule group, application, site, and data batch. Trigger examples: security control failure; permission variance above tolerance; data reconciliation below 99.5%; identity failure above 2%; Tier 0 workflow failure; or inability to restore within the approved recovery objective. The command lead calls the decision; accountable technical/business owners approve domain actions; the PM records time, rationale, evidence, and communication.

## Hypercare exit

Exit after five consecutive business days with no Sev 1, priority services inside the agreed service objective, fewer than ten aged migration defects, accepted knowledge/monitoring/on-call, documented residual risks, and business/service-owner signatures.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `cutover scope and batch`
- `freeze window`
- `command roles`
- `prechecks`
- `time-stamped tasks and dependencies`
- `validation scripts`
- `rollback triggers/actions/latest-safe-time`
- `communications`
- `incident model`
- `hypercare exit and handoff`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
