# Hardware Kanban Service Delivery Review

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Use flow, quality, customer, asset, and risk evidence to change the system rather than chase utilization.

## Illustrative review — Week 13

| Signal | Evidence | Interpretation | Decision |
| --- | --- | --- | --- |
| Throughput | 42 devices; four-week mean 38 | Capacity supports normal remaining demand | Do not increase WIP |
| Cycle time | Median 3.4; P85 6.2 business days | Improving after staging limit | Keep staging WIP 24 |
| Aging/blockers | Four blocked; oldest six days | Specialized work differs from standard flow | Create explicit specialized lane |
| Quality | 97.7% first-time-right; 98.5% compliant in 24h | Inside threshold with two repeat app causes | Root-cause app package defects |
| Asset return | 97.1% reconciled | Remote return lag remains | Add prepaid courier pickup and T+3 escalation |

## Improvement experiment

For the next two weeks, cap Scheduled at 30 for remote work, reserve two daily support appointments for accessibility/specialized personas, and trigger courier pickup at user acceptance. Compare P85 cycle time, exception age, and return reconciliation with the prior four weeks.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `review window`
- `demand/throughput`
- `WIP/aging/cycle time`
- `quality/compliance`
- `customer/support`
- `asset/return/sanitization`
- `risks`
- `forecast`
- `policy/capacity decision`
- `improvement experiment`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
