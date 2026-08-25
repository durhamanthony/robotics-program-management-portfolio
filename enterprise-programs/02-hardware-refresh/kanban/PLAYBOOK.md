# Enterprise Hardware Refresh — Kanban Playbook

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Operate the 360-device refresh as a flow system with explicit policies, constrained work in progress, service classes, and evidence-based forecasting.

## Why Kanban

The arrival of ready users, delivered hardware, application fixes, data prechecks, appointments, and exceptions varies. A pull system prevents staging and deployment from outrunning validation, support, return, and sanitization capacity.

## Definition of Workflow

| State | Entry policy | Exit policy | WIP limit |
| --- | --- | --- | --- |
| Options | In-scope user/device demand | Roster and persona assigned | None |
| Ready | Hardware, roster, app/data precheck and appointment feasible | Pulled by staging capacity | 60 |
| Staging | Serialized device and approved build | Build/security/asset test pass | 24 |
| Scheduled | User/site communication and kit ready | Appointment begins | 40 |
| Deploying | Identity verified; old asset in controlled handoff | Task/data/user acceptance | 12 |
| Hypercare | New device accepted | T+5 measures pass; exception assigned | 30 |
| Return/sanitize | Old asset custody established | Disposition evidence accepted | 35 |
| Done | New/old assets reconciled; service and evidence complete | N/A | None |

## Service classes

- Expedite: security failure, lost custody, executive/critical business outage; maximum one in system and named incident lead.
- Fixed date: regulatory/site blackout, user leave, contract or courier date; risk review when within service-level expectation.
- Standard: normal persona/device flow.
- Intangible: automation, knowledge, telemetry, and process debt; reserve at least 10% capacity so flow remains sustainable.

## Cadences and policies

Daily flow review focuses on blocked/aging work and WIP, not person-by-person status. Replenishment twice weekly selects only ready demand. Weekly service-delivery review inspects throughput, cycle-time distribution, work-item age, first-time-right, compliance, returns, and demand/capacity. Monthly operations/steering review changes policies, capacity, or scope.

## Forecast

Forecast with historical throughput and cycle-time percentiles. The scenario’s latest four-week throughput is 38 devices/week and P85 end-to-end cycle time is 6.2 business days after Ready. Forecasts are ranges; blocked exceptions are separately dated by owner.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `work item types`
- `workflow start/finish`
- `states`
- `entry/exit policies`
- `WIP limits`
- `service classes`
- `SLEs`
- `cadences`
- `flow metrics`
- `escalation and improvement`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
