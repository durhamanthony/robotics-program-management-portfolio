# M&A Collaboration and Workspace Migration Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Migrate or consolidate Google Workspace, Slack, Asana, and Jira with identity, history, retention, integrations, and user experience controlled together.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Google Workspace | 610 users; Gmail, Calendar, My Drive, Shared Drives, Groups; pilot + pre-stage + delta | Workspace Lead | Object counts, permissions, mail flow, sharing, legal hold |
| Slack | 520 users; 286 channels; private/shared channels identified; apps and webhooks mapped | Collaboration Lead | Membership, history, files, retention, bot/webhook test |
| Asana | 280 users; portfolio/project disposition and CSV/API mapping | Business Apps Lead | Task, owner, due date, custom-field reconciliation |
| Jira | 190 users; identity/group migration before project content where supported | Atlassian Owner | Permissions, apps, filters, boards, automation, references |

## Execution sequence

1. Inventory data volume, owners, retention, legal hold, external sharing, groups/channels/projects, apps, bots, webhooks, automation, and unsupported objects.
2. Approve destination information architecture and identity mapping; resolve duplicate names and inaccessible owners.
3. Run representative pilots including executives, delegates, shared resources, external guests, restricted projects, and automation owners.
4. Pre-stage supported content, freeze high-change objects only when required, then run the final delta.
5. Validate counts, samples, permissions, links, mail/calendar behavior, integrations, retention, and search with accountable owners.
6. Keep source read-only for the approved retention window; remove licenses and integrations only after acceptance and legal approval.

## Acceptance evidence

- [ ] At least 99.5% reconciled object counts per in-scope data class, with excluded/unsupported objects documented.
- [ ] 100% of critical bots, apps, webhooks, calendars, groups, shared drives, and automations have an owner and test result.
- [ ] No critical permission escalation or loss of legal-hold coverage remains unresolved.
- [ ] Business owners accept searchability, permissions, representative samples, and support instructions.

## Exception, rollback, and escalation

Pause a cohort if identity mapping is ambiguous, retention/hold behavior is unapproved, permission variance exceeds the approved threshold, or critical integrations fail. Keep the source authoritative or read-only as designed, reverse routing where supported, and issue a user notice with the next decision time. Deletion is never a rollback mechanism.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `source/destination tenants`
- `licenses`
- `data classes / volumes`
- `identity mapping`
- `retention / legal hold`
- `information architecture`
- `apps/bots/webhooks`
- `pilot cohorts`
- `freeze/delta timing`
- `validation and decommission`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
