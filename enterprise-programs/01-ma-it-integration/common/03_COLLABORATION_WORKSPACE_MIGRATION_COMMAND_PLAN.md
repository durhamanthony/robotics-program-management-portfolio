# Collaboration & Workspace Migrations — Command Plan

> **Portfolio truth boundary:** Company ABC and Company XYZ are fictional. User, channel, repository, project and migration counts are modeled assumptions with low confidence until tool exports and owner validation replace them.

## Executive intent

Move collaboration content and working practices without losing identity, permissions, retention, legal holds, auditability, integrations or employee productivity. The runbook covers Google Workspace, Slack, Asana, Jira, GitHub, Microsoft 365/Teams/SharePoint/OneDrive and connected tools.

## Scenario checkpoint

| Platform/control | Modeled checkpoint | Current decision |
|---|---:|---|
| Google pilot reconciliation | 99.7% | Continue with defined exclusions and delta migration |
| Slack identities matched | 512 / 520 | Resolve guests, duplicates and inactive accounts |
| Slack channels mapped | 286 / 286 | Private/shared channels use separate approval paths |
| Critical Slack bots/webhooks passed | 16 / 18 | Hold affected production channels |
| Jira automations/regressions passed | 47 / 49 | Jira cohort remains on hold |
| GitHub critical repositories classified | 73 / 81 | Resolve secrets, Actions and external collaborators |
| Microsoft workloads assessed | 6 / 6 | Coexistence required before tenant consolidation |

## Cross-platform control model

Each platform uses the same control spine: authoritative identity map; source/target inventory; scope and exclusions; ownership; legal/retention/eDiscovery approval; content/metadata/permission mapping; app/integration mapping; pilot; reconciliation; user acceptance; production wave; delta/freeze; rollback or read-only fallback; hypercare; source retention; and decommission approval.

### Google Workspace

Map Gmail, calendars, contacts, Drive/My Drive, Shared Drives, Groups, delegated mailboxes, aliases, resources, sharing links, ownership, Vault holds and third-party apps. Validate counts, samples, permissions, timestamps, labels/metadata where supported, calendar delegates/resources, group delivery and external sharing. Document vendor-tool supported and unsupported items rather than assuming perfect parity.

### Slack

Maintain registers for 520 identities, 286 channels and 18 critical bots/webhooks/integrations. Classify users as active, inactive, guest, multi-channel guest, bot, service identity, duplicate or external. Classify channels as public, private, Slack Connect/shared, archived, regulated or excluded. Record source/target names, owner, purpose, retention, legal hold, history range, member map, files, canvases/workflows, bookmarks, apps and decision.

Slack export/import capability depends on plan, role, legal authority and workspace type. Export packages can contain file links rather than the files themselves, and private/DM data requires the appropriate plan and approvals. Never present a channel as accepted until membership, history, searchable samples, retention, file access and required bot/webhook behavior pass.

### Asana and Jira

Map organizations/sites, projects, boards, spaces, issue/work-item types, custom fields, statuses, workflows, automations, forms, dashboards, attachments, comments, watchers/followers, groups, permissions, service accounts, marketplace apps and webhooks. Use rehearsal migrations and reconciliation. Hold a wave when workflow or automation differences can change business outcomes.

### GitHub

Inventory enterprises/organizations, repositories, teams, members, outside collaborators, branch protections/rulesets, environments, secrets, deploy keys, GitHub Apps/OAuth apps, Actions workflows/runners, packages, Pages, webhooks, audit/log retention, Advanced Security settings, billing and legal/data residency. Test clone/push, CI/CD, protected branch, release, package and incident rollback before transfer or migration.

### Microsoft tools

Assess Entra ID, Exchange Online, Teams, SharePoint, OneDrive, Microsoft 365 Groups, Power Platform, Intune dependencies, guest/B2B access, sensitivity labels, Purview retention/eDiscovery, Defender, enterprise applications and Azure subscriptions. Choose coexistence, cross-tenant capability, migration or consolidation per workload; do not assume a single tenant move covers every service.

## Wave design and command bridge

Segment by business criticality, geography, identity complexity, data/retention constraints and integration dependency. A production wave needs signed scope, identity map, capacity/license check, retention approval, migration-tool configuration, tested rollback/fallback, communications, help-desk scripts and platform/vendor coverage.

The command dashboard shows users/items planned, migrated, reconciled, accepted and failed; data volume; error categories; permission defects; integration tests; support contacts; rollback decisions; and source-retention expiry.

## Acceptance and source retirement

Acceptance is business and control evidence—not tool completion. Require reconciled counts with explained exclusions, risk-based samples, permissions, retention/legal-hold behavior, search, integrations, owner UAT, support knowledge and no unresolved Sev-1/2 defect. Keep the source read-only for the approved retention window; remove access and contracts only after Legal, Security, Records, platform and business owners approve.

## Reusable template fields

**Platform/workload:** [name]  
**Source/target tenant or workspace:** [IDs]  
**Users/items/data volume:** [counts]  
**Identity exceptions:** [list]  
**Retention/legal hold:** [decision]  
**Supported/unsupported mapping:** [list]  
**Apps/bots/webhooks/workflows:** [register]  
**Pilot cohort and acceptance threshold:** [details]  
**Freeze/delta plan:** [details]  
**Rollback/read-only fallback:** [details]  
**Source retirement approval:** [roles/evidence]  
