# Hardware Refresh Application and User-Data Readiness Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Prove that each persona can access required applications and that approved user data is protected and validated before old-device retirement.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Application inventory | 76 applications; Tier 0/1 owners and packaging path required | Application Lead | Owner, package/version/license/dependency/test |
| Data path | OneDrive Known Folder Move or approved enterprise backup; exceptions for local/app data | Data Lead | Precheck, sync/backup, destination validation |
| User state | Browser profile, bookmarks, certificates, VPN, printers, accessibility and approved settings | Endpoint Lead | Persona checklist |
| Licensing | Named/concurrent/device licensing and activation | Application Owner + Procurement | License capacity and activation test |
| Validation | User + automated evidence before old device release | Business Owner | Task-based acceptance |

## Execution sequence

1. Discover applications from management tools, software inventory, tickets, business owners, and user survey; normalize versions and owners.
2. Classify criticality, packaging/install method, license, identity, network, driver/peripheral, data, and compatibility dependencies.
3. Protect approved Desktop/Documents/Pictures and identified application data; resolve sync errors before appointment.
4. Pilot Tier 0/1 apps and representative personas on each model/build; record defects and workaround expiry.
5. At swap, validate sign-in, data counts/samples, critical tasks, peripherals, VPN/network, printing, and support access.
6. Release old device to retirement only after user/data acceptance or a documented no-data/recovery path.

## Acceptance evidence

- [ ] 76 of 76 applications have a disposition; all Tier 0/1 apps have owner, package, license, test, and fallback.
- [ ] At least 99% of deployed users pass the data checklist or have an approved no-data classification.
- [ ] Zero old device is sanitized while a data validation or legal-hold exception is open.
- [ ] Accessibility and specialized peripheral users accept the new workflow before closure.

## Exception, rollback, and escalation

If sync/backup is incomplete, critical workflow fails, or a local-data/hold question is open, keep the old device in controlled custody and do not sanitize. Reissue the old device if safe or provide an approved spare/workaround; correct the package/data path and retest.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `applications/personas`
- `package/version/license`
- `dependencies/peripherals`
- `data locations/classification`
- `backup/sync policy`
- `precheck`
- `task-based tests`
- `user acceptance`
- `fallback`
- `retirement release`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
