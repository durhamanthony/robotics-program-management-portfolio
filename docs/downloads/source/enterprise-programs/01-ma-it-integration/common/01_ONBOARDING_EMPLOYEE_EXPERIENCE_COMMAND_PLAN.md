# Onboarding & Employee Experience — Command Plan

> **Portfolio truth boundary:** Company ABC and Company XYZ are anonymized fictional organizations. Dates, counts, results, costs, and status values are scenario assumptions with low confidence until replaced by approved project evidence.

## Executive intent

Give every transferring worker a secure, supportable way to work on Day 1 without bypassing legal, privacy, identity, endpoint, or separation-of-duties controls. The Project Manager owns the integrated outcome; HR owns the authoritative roster; IAM, Endpoint, Service Desk, Security, Facilities, Legal/Privacy, and business managers own their acceptance evidence.

## Scenario checkpoint

| Control | Modeled checkpoint | Acceptance rule | Owner | Executive meaning |
|---|---:|---|---|---|
| Workers in authoritative scope | 680 | Signed HR/Legal roster and worker type | HR integration lead | Nobody is silently omitted |
| Fully ready at Day 1 | 665 / 680 | Device, identity, MFA, network and critical apps proven | M&A IT PM | 15 people use controlled exceptions |
| Authentication successful | 674 / 680 | Successful sign-in and MFA evidence | IAM lead | Six access defects remain |
| Hardware kits delivered | 672 / 680 | Chain of custody and delivery confirmation | Endpoint lead | Eight kits require local handoff |
| Controlled exceptions | 15 | Named owner, workaround, risk, expiry and daily review | Service Desk lead | Exceptions are managed, not hidden |

## Integrated work packages

1. **Population and policy:** reconcile employees, contractors, interns, privileged users, remote workers, countries, works councils, privacy restrictions, accessibility needs, executive/VIP handling, and leavers through T-0.
2. **Identity:** create or bridge accounts; map source-to-target identities; assign licenses, groups and roles; register MFA; test conditional access, password recovery, and privileged access.
3. **Endpoint and hardware:** select retain/replace/reimage; stage approved builds; enroll MDM; enable encryption, EDR, patching, certificates, VPN/ZTNA, printers and approved peripherals; record custody.
4. **Productivity and critical applications:** map role-based access bundles; test Google/Microsoft productivity, Slack, Jira, Asana, GitHub, finance, HR and line-of-business applications.
5. **Employee communications:** send manager briefings, T-10/T-3/T-1 instructions, credential instructions through an approved secure channel, office/remote logistics, known limitations, support contacts and phishing warnings.
6. **Day 1 floor command:** use site leads, virtual rooms, triage queues, scripts, spare pools, priority rules, dashboards, shift handoffs and executive escalation.
7. **Hypercare and handoff:** burn down defects and exceptions daily; measure time-to-productivity, repeat contacts and sentiment; transfer knowledge and close only after service ownership accepts.

## Readiness gates

| Gate | Required evidence | No-go condition |
|---|---|---|
| T-20 scope lock | Roster, countries, locations, roles, worker types, legal constraints | Unowned population or unresolved transfer restriction |
| T-10 build readiness | Hardware forecast, image/build, license capacity, access bundles, support staffing | Critical stock, image, licensing or staffing gap |
| T-3 final reconciliation | HR delta, identities, devices, MFA path, critical-app tests, communications | Material roster variance or critical app failure |
| T-1 go/no-go | Signed checklist, exception list, rollback/workaround, bridge and contacts | Uncontrolled privileged access or missing support coverage |
| Day 1 acceptance | Worker-level evidence and incident/exception dashboard | Critical safety, security, payroll or business-continuity failure |
| Hypercare exit | Trend within threshold, knowledge accepted, expired bridges removed | Repeating Sev-1/2 issue or unowned exception |

## Exception design

Every exception records worker, site, business impact, control affected, workaround, security approval when required, owner, target date, expiry, communication status and closure evidence. Temporary credentials, source-tenant access, loaner devices and security bypasses must have explicit expiry and automated removal wherever possible.

## Dashboard measures

Use population-denominator metrics: fully ready / in scope; authentication / attempts; kits delivered / required; critical-app pass / tests; exceptions by age and severity; Day 1 contacts per 100 users; mean time to restore productivity; and employee pulse. Show both numerator and denominator so an executive can see scale.

## Reusable template fields

**Project:** [name]  
**Acquirer / target:** [Company ABC / Company XYZ]  
**Day 1 date:** [date]  
**Authoritative population:** [count and source]  
**Countries / sites / remote workers:** [list]  
**Critical roles and applications:** [list]  
**Readiness thresholds:** [metric / target / owner / evidence]  
**Exception authority:** [role]  
**Support model and hours:** [details]  
**Hypercare exit criteria:** [details]  
**Approvers:** [HR / Legal / Privacy / Security / IT / business]  
