# M&A Agile Definition of Ready and Definition of Done

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Stop ambiguous work from entering delivery and stop partially validated work from being reported as complete.

## Definition of Ready

- Outcome/user or service is identified; accountable owner and acceptance authority are named.
- Scope, affected cohort/system/data, dependencies, assumptions, risks, and target release are visible.
- Security, privacy, legal hold, architecture, procurement, and change impacts are classified; required reviewers are engaged.
- Test data/environment and rollback approach are feasible; external vendor capacity is confirmed where required.
- Acceptance is observable and measurable, with numerator/denominator or specific test evidence.

## Definition of Done

- Build/configuration/migration is completed and peer reviewed under change control.
- Functional, security, data reconciliation, permission, monitoring, failure, and business workflow tests pass or have an approved exception.
- Documentation, CMDB/inventory, ownership, knowledge, communications, and support routing are updated.
- Temporary access, files, rules, licenses, and migration accounts have an owner and expiry.
- Acceptance evidence is attached; accountable business/technical owner accepts; dashboard source is updated.

## Not done

Tool reports success but counts/permissions are unvalidated; a pilot passes without representative personas; a defect has no owner/due date/workaround; a source is disabled without accepted data/recovery; or a document is complete without an operating control.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `ready criteria`
- `done criteria`
- `required evidence`
- `approvers`
- `exception rule`
- `quality thresholds`
- `operational updates`
- `temporary-control closure`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
