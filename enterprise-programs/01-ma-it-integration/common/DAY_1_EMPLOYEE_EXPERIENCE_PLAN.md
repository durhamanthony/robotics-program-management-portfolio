# M&A Day 1 Employee Experience Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Make the first business day productive and supportable for every acquired worker, including documented exceptions.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Authoritative roster | 680 workers; HR-to-IAM reconciliation at T-10, T-3, and T-0 | HR Integration Lead | Signed roster delta |
| Identity and credentials | Company ABC identity or approved temporary bridge; MFA registered | IAM Lead | Authentication test + access review |
| Endpoint path | Re-enroll 510 devices; replace 170; 65 shared/special devices use controlled plan | Endpoint Lead | Device compliance report |
| Collaboration | Mail/calendar, Drive, Slack, task tools, meeting access | Collaboration Lead | Persona-based test script |
| Support | Dedicated queue, bridge, knowledge, site runners, executive route | Service Desk Lead | Staffing roster + ticket taxonomy |

## Execution sequence

1. Freeze the roster baseline and map worker, manager, persona, location, device, license, and special access.
2. Provision accounts in a disabled state; run duplicate, contractor-expiry, and privileged-role checks.
3. Stage devices, credentials, and instructions by site and remote-shipment wave; preserve chain of custody.
4. Run persona tests for standard user, executive, developer/admin, call-center/shared device, and contractor.
5. Open the command center at T-12 hours; release communications only after sponsor and HR approval.
6. At T+2 and T+8 hours, reconcile login, device compliance, collaboration access, and open incidents.

## Acceptance evidence

- [ ] 665 of 680 workers are fully ready (97.8%); 15 exceptions have a tested workaround, owner, and expiry.
- [ ] 674 of 680 workers pass identity authentication (99.1%); failed cases are not counted as ready.
- [ ] 100% of Tier 0/Tier 1 persona tests have time-stamped evidence and owner sign-off.
- [ ] Help Desk staffing, knowledge, queue routing, severity, executive escalation, and vendor contacts are live.

## Exception, rollback, and escalation

Hold affected cohort release if roster-to-identity mismatch exceeds 1%, if a privileged-access path is unapproved, or if support cannot receive cases. Use the approved source account/device path during the time-boxed coexistence period. Rollback never deletes source data; it disables the new route, restores prior routing, and communicates a revised window.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `worker roster and personas`
- `device assignment / delivery`
- `identity and MFA status`
- `license/access bundle`
- `site/remote logistics`
- `communications`
- `support coverage`
- `exception workaround and expiry`
- `Day 1 acceptance signatures`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
