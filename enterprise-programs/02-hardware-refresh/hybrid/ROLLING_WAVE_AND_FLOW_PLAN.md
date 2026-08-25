# Hardware Hybrid Rolling-Wave and Flow Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Translate the approved master plan into near-term ready work without overcommitting uncertain exceptions.

## Planning horizons

| Horizon | Detail | Update |
| --- | --- | --- |
| Program — 18 weeks | Milestones, budget, sites, device totals, gates, dependencies | Formal baseline/change |
| Release — next 4 weeks | Site/wave targets, supply/build/app/data/support capacity | Weekly integrated review |
| Delivery — next 2 weeks | Ready user/device cards with acceptance and appointment | Twice-weekly replenishment |
| Daily | WIP, blockers, aging, incidents, returns, sanitization | Daily flow review |

## Flow design

Use Ready → Staging (24) → Scheduled (40) → Deploying (12) → Hypercare (30) → Return/Sanitize (35) → Done. An exception lane has WIP 10 and is ordered by business/security impact, aging, and fixed-date risk. Exceeding WIP requires finishing/swarming or an explicit temporary capacity decision—not silently starting more.

## Wave reconciliation

At T-5, the wave target is split into Ready, controlled exception with new date, and not authorized. At T+5, deployed/accepted, quality/compliance, returns, open exceptions, budget, and lessons update both the baseline forecast and the flow policies.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `planning horizons`
- `wave targets`
- `ready policy`
- `workflow/WIP`
- `exception lane`
- `capacity`
- `replenishment`
- `reconciliation`
- `forecast`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
