# Application Rationalization & Data/Reporting Consolidation — Command Plan

> **Portfolio truth boundary:** Company ABC and Company XYZ are fictional. Application counts, cost opportunities and progress values are modeled assumptions with low confidence until contracts, telemetry, owners and Finance validate them.

## Executive intent

Create one defensible view of applications, data and reporting; reduce risk and duplication without interrupting business services; and prove benefits only when use, data, contracts and invoices actually change.

## Scenario checkpoint

| Control | Modeled checkpoint | Executive meaning |
|---|---:|---|
| Applications discovered | 142 | Every item still needs an accountable owner and disposition |
| Overlapping capabilities | 37 | Duplicates are candidates, not automatic savings |
| Retire/consolidate targeted | 22 / 37 | Acceptance and contract exit remain prerequisites |
| Owner and disposition confirmed | 128 / 142 | Fourteen decisions remain open |
| Shadow-IT items under review | 11 / 18 | Security/privacy/records review is incomplete |
| Authoritative reporting feeds reconciled | 9 / 12 | Three feeds block unified reporting |

## Complete discovery

Combine SSO/identity catalogs, accounts payable and expense data, procurement/contracts, CASB/browser discovery, endpoint inventory, network/proxy/DNS telemetry, cloud marketplaces, API keys/OAuth grants, CMDB, service desk, data catalogs, audit logs and stakeholder interviews. Preserve confidence and source for every record; avoid treating absence from one tool as proof an application does not exist.

The portfolio register includes application/service, capability, business owner, technical owner, users/utilization, criticality, data classification, countries/residency, authentication/SSO/MFA, privileged access, integrations/dependencies, API/bot/service accounts, vendor, contract/renewal/notice, license count/cost, support/EOL, incidents, controls, recovery objectives, system of record and disposition.

## Decision framework

Allowed dispositions are **retain, migrate, consolidate, replace, retire, coexist or investigate**. Score business fit, technical fit, security/privacy/records, data portability, integration complexity, user impact, reliability/support, contractual constraints, total cost, synergy value and execution risk. A steering decision names the target, transition owner, funding, milestone, acceptance criteria and fallback.

A retirement requires no active dependency, preserved records/holds, exported and reconciled data, approved archive, revoked access/tokens, terminated integrations, contract notice, invoice stop, CMDB/asset update, support update and signed retirement certificate. “Turned off” is not “closed.”

## Shadow IT and license control

For unapproved SaaS, extensions and AI tools, identify owner, users, data shared, OAuth scopes, payment source, subprocessors, residency, retention, security posture and business dependency. Choose approve/control, migrate, block, or retire with Legal/Privacy/Security input. Protect business data during containment.

License optimization compares purchased, assigned, active and required entitlements; role-based need; contract minimums; renewal/notice windows; true-up terms; termination rights; data extraction cost and business transition. Finance validates realized savings after contract and invoice evidence—not when a candidate is placed on a slide.

## Data and reporting consolidation

1. Name authoritative sources and data owners for workforce, applications, assets, identity, finance, service, security and migration status.
2. Define common identifiers, business glossary, data lineage, retention, classification, access and quality rules.
3. Map source-to-target fields and transformations; document exclusions and manual adjustments.
4. Build controlled ingestion/ETL or federation with logging, reconciliation, segregation of duties and failure handling.
5. Reconcile row counts, totals, duplicates, referential integrity, freshness, completeness and risk-based samples.
6. Certify executive dashboards against source systems and publish refresh time, owner and known limitations.
7. Archive or retire duplicate reports only after consumers and records owners approve.

The command dashboard separates **discovered, owned, decided, migrated, accepted, retired, contract closed and benefit realized** so progress cannot be overstated.

## Governance and acceptance

Application/data decisions use an architecture and rationalization board with Business, Enterprise Architecture, Security, Privacy, Records, Data, Finance, Procurement and Operations. Critical changes pass change control and cutover/rollback. Data defects have severity, owner, aging, disposition and accepted residual risk.

## Reusable template fields

**Discovery sources and coverage:** [list]  
**Portfolio denominator:** [count/date]  
**Decision criteria/weights:** [details]  
**Disposition authority:** [roles]  
**Critical dependencies:** [register]  
**Data sources/owners/lineage:** [details]  
**Reconciliation rules:** [details]  
**Contract/renewal calendar:** [details]  
**Retirement certificate requirements:** [list]  
**Benefit owner and proof:** [Finance evidence]  
