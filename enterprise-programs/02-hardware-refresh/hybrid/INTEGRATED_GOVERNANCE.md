# Hardware Hybrid Integrated Governance and Decision Matrix

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Prevent duplicate plans and clarify when a decision belongs to the baseline, wave, or flow system.

## Decision matrix

| Decision | System | Authority | Evidence |
| --- | --- | --- | --- |
| Device quantity/model, budget, final date | Predictive baseline | Steering Committee | Change impact and recommendation |
| Build/security/app/data release | Technical quality gate | Endpoint/Security/App/Data owners | Test and rollback evidence |
| Site wave release | Predictive milestone gate | Business Site + PM + Security | T-5/T-1 readiness |
| Which ready users/devices are pulled next | Adaptive flow | Wave Team | Priority, readiness, WIP and capacity |
| WIP/SLE/capacity policy | Adaptive improvement | Delivery Lead + service owners | Flow/outcome trend and experiment |
| Risk acceptance or sanitization exception | Enterprise control | Designated authority only | Documented residual risk/expiry |

## One source of truth

The baseline owns authorized scope/cost/date. The deployment-wave register owns release quantities and acceptance. The Kanban board owns current work state. Inventory owns device/asset identity. RAID owns exposure. No status is manually reconciled by narrative; dashboards derive from these sources.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `decision categories`
- `systems of record`
- `authorities`
- `thresholds`
- `cadence`
- `escalation`
- `baseline/board reconciliation`
- `evidence`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
