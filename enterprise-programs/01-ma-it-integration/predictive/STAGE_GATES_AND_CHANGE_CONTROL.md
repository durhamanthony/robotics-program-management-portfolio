# M&A Predictive Stage Gates and Integrated Change Control

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Define authorization points and protect baselines while allowing evidence-backed change.

## Stage gates

| Gate | Required evidence | Approvers | Possible decision |
| --- | --- | --- | --- |
| G0 Mandate | Deal intent, clean-team restrictions, sponsor, initial outcomes | CIO + Corp Dev + Legal | Authorize discovery |
| G1 Baseline | Charter, scope/WBS, schedule/cost, risks, governance, target decisions | Steering Committee | Approve baseline / recover |
| G2 Design | Identity/network/data/security designs, vendor plan, test/rollback | Design Authority + Security | Authorize build/pilot |
| G3 Day 1 | Readiness, tests, support, communications, contingency | Sponsor + Security + Business | Go / conditional go / hold |
| G4 Migration waves | Pilot results, batch plan, reconciliation, rollback | Business/Data/Technical Owners | Release batch |
| G5 Decommission | Accepted destination, retention/hold, access/contract plan | Business + Legal + Security | Retire / extend |
| G6 Close | Handoff, financial/vendor closure, risks, lessons, benefit owners | Sponsor + Operations | Accept closure |

## Change thresholds

- Level 1: workstream may approve within existing scope/cost/date and no control impact.
- Level 2: PM/CCB approves cumulative work-package variance up to $25,000 or five business days without final milestone impact.
- Level 3: steering approves scope/target-state/control change, reserve draw, final milestone impact, or forecast above 5%.
- Emergency: incident/change authority acts to protect service/security, then documents retrospective approval and baseline impact.

## Change record minimum

Problem/opportunity, options including no change, scope/schedule/cost/resource/quality/risk/security/privacy/contract/benefit impacts, dependencies, implementation, validation, rollback, recommendation, decision, conditions, and baseline updates.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `gate names and criteria`
- `approvers/quorum`
- `decision options`
- `change thresholds`
- `change form`
- `impact analysis`
- `emergency rule`
- `baseline update`
- `decision log`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
