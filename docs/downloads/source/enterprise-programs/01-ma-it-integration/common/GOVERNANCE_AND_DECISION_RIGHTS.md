# M&A Governance, RACI, and Decision Rights

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Define how decisions move from workstreams to the integration steering committee without hiding ownership.

## Governance model

| Forum | Cadence | Required decisions | Participants | Output |
| --- | --- | --- | --- | --- |
| Executive steering committee | Weekly through Day 30, biweekly thereafter | Scope, funding, risk acceptance, target-state exceptions, gate decisions | CIO sponsor, Corp Dev, business sponsor, Security, Finance, HR, PM | Decision log and signed gate memo |
| Integration management office | Three times weekly | Cross-workstream dependencies, RAID, schedule, vendor actions | PM and workstream leads | Integrated plan and status |
| Technical design authority | Twice weekly | Identity, network, data, tool architecture, rollback | Infrastructure, IAM, Security, application owners | Approved design / exception |
| Change and readiness | Weekly; daily before Day 1 | Audience, message, training, readiness exceptions | Change lead, HR, Help Desk, site leads | Readiness score and communications |
| Cutover command center | Continuous during cutover | Go/hold/rollback, severity and communications | PM, technical leads, service owner, vendor leads | Time-stamped command log |

## Decision rule

A decision is complete only when the accountable owner, options, recommendation, due date, rationale, downstream impacts, and approval are recorded. Silence is not approval. Conditional approval carries explicit actions and expiry.

## Escalation thresholds

- Any predicted Day 1 miss affecting more than 14 workers or any Tier 0 service goes to steering within four hours.
- Any suspected data exposure, unauthorized cross-tenant access, or legal-hold conflict immediately invokes the security/privacy incident process.
- Forecast variance above 5% or reserve draw above $25,000 requires sponsor/Finance approval.
- A milestone slip greater than five business days with downstream impact requires a recovery plan and baseline decision.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `forums and cadence`
- `decision categories`
- `accountable roles`
- `quorum`
- `thresholds`
- `escalation clock`
- `decision log fields`
- `gate approvers`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
