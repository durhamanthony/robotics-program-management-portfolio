# Hardware Predictive Quality Management Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Plan and assure build, security, application, data, user, asset, and service quality.

## Quality matrix

| Quality object | Requirement | Acceptance |
| --- | --- | --- |
| Device build | Versioned, reproducible, supported | Pilot/model/persona results and release approval |
| Security/compliance | Required controls before business release | At least 98% within 24h; owned remediation |
| Applications/data | Tier 0/1 workflows and approved data present | At least 99% data pass; business task acceptance |
| User experience | Minimal disruption and supportable handoff | At least 97% first-time-right; median impact under 90 min |
| Assets | New/old serials and custody/disposition reconciled | 100% final disposition; no unknown custody |
| Operations | Knowledge, queue, monitoring, spares, vendor and on-call accepted | Service-owner sign-off |

## Defects and sampling

All Tier 0, security, data-hold, custody, and destructive actions receive 100% evidence review. Quality samples at least 10% of other wave records and all repeat-failure causes. Sev 1 blocks release; Sev 2 requires approved workaround and date; lower defects remain visible and are analyzed for trend.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `quality objectives`
- `standards`
- `verification/validation`
- `sampling`
- `defect severity/SLA`
- `acceptance authority`
- `audit trail`
- `improvement`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
