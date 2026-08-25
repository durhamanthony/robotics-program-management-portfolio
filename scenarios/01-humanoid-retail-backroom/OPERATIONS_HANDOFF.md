# Operations Handoff — Retail Backroom Pilot

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Accepted operating model

Meridian Store Operations owns the inbound dock window, forklift-to-humanoid zone handoff, daily mission authority, route condition, inventory exceptions, employee right-of-way, and benefit measurement. The vendor Level 1 (L1) service desk owns initial robot triage; Level 2 (L2) engineering owns software/controls escalation; field service owns physical recovery and repair. Safety retains stop-work authority.

## Service targets

**Table 1. Service targets — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Severity | Example | Acknowledge | Restore/workaround | Escalation |
|---|---|---:|---:|---|
| Severity 1 | unsafe behavior, contact, fleet unavailable | 15 minutes | 4 hours | immediate Safety, Program, Engineering, Field |
| Severity 2 | one robot unavailable; human fallback works | 30 minutes | 8 hours | L2 after 30 minutes; field after 2 hours |
| Severity 3 | degraded feature or repeated item exception | 4 business hours | 3 business days | problem record after third repeat |
| Severity 4 | request, report, cosmetic issue | 1 business day | planned release | product backlog |

## Daily controls

Opening inspection; receiving-zone, forklift return path, route, stair, fire-door, courtesy-table, staffed service window, charger/battery, test-request, and open-defect checks. During operation, the dock lead releases stocking only after the forklift has returned into the truck and the receiving zone is clear. At fulfillment handoff, robots place both packages, turn toward the shelves, and hold while the associate bends both arms to collect through the service window, turns around, and walks away; the mission closes only after both packages are removed. Supervisors can pause or recall the fleet. Closing includes unresolved mission reconciliation, exception-zone count, cleaning/inspection, charge, and shift handoff log.

## Mandatory case evidence

Robot or forklift, store, truck/pallet/carton, mission, item, request, rack/drop-off point, service-window pickup, package-removal/custody-close state, configuration, software version, timestamps, fault code, safety state, zone-clear state, last commands, telemetry bundle, photo/video if permitted, operator observation, attempted action, and current fallback.

## Residual risks and owners

Unsupported items and blocked routes transfer to Store Operations. Quote, recurring-cost, and value gaps remain with Finance/Procurement. Software security and access reviews remain with IT Security. Safety events are never closed solely by service restoration.

## Handoff acceptance

Roster, runbook, severity tests, support case drill, spare inventory, vendor contacts, training results, known-error list, configuration baseline, warranties, and residual-risk acknowledgements were signed at week 20. Chain rollout was not authorized.
