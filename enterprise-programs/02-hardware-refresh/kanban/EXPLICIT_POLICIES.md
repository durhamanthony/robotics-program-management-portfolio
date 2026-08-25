# Hardware Kanban Explicit Policies and Service-Level Expectations

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Make pull, blocking, aging, expedite, quality, and exception rules observable.

## Policies

| Policy | Rule | Reason |
| --- | --- | --- |
| Commitment point | A device enters Ready only with roster, hardware, app/data precheck, appointment path, owner and acceptance | Prevents false demand from consuming capacity |
| Pull | Downstream owner pulls only when below WIP and capacity exists for validation/failure | Protects flow and quality |
| Blocker | Mark reason/owner/start/next action; escalate at one business day, immediately for security/custody | Stops invisible waiting |
| Aging | Review items at 50% of SLE; swarm at 75%; escalate/reshape at 100% | Uses work-item age as leading signal |
| Expedite | One maximum; explicit owner; return to normal after incident containment | Prevents every request becoming urgent |
| Done | User/data/app acceptance plus new/old asset reconciliation and evidence | Avoids deployment-only completion |

## Initial service-level expectations

- Standard staging: 85% within two business days.
- Ready-to-user acceptance: 85% within five business days.
- User acceptance-to-old-asset custody: 85% same day on site; five business days remote.
- Custody-to-sanitization/disposition evidence: 85% within seven business days.

SLEs are planning expectations derived from scenario history, not promises. Recalculate after at least 30 representative completions and segment remote/specialized work where distributions differ.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `workflow policies`
- `commitment/delivery points`
- `WIP limits`
- `classes of service`
- `blocker rule`
- `aging thresholds`
- `SLE percentile/window`
- `done evidence`
- `policy-change cadence`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
