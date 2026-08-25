# Hardware Refresh Deployment, Hypercare, and Service Transition Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Execute safe pilot/waves, restore failed users quickly, learn between waves, and transfer stable ownership to operations.

## Wave pattern

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

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `pilot/wave scope`
- `T-10/T-5/T-1 gates`
- `daily runbook`
- `validation/acceptance`
- `incident/rollback`
- `capacity/spares`
- `wave metrics`
- `lessons/change`
- `hypercare exit`
- `service acceptance`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
