# Quality Management Plan

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Quality objective

Deliver a robotics product or deployment that is traceable to approved requirements, safe within its intended operating envelope, repeatable in the target workflow, supportable after launch, and accepted with objective evidence.

## Quality controls by phase

**Table 1. Quality controls by phase — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Phase | Prevention | Detection | Required record |
|---|---|---|---|
| Requirements | Defined operating envelope and measurable acceptance | Cross-functional review and ambiguity check | Approved requirements baseline and RTM |
| Design | Design standards, hazard controls, interface ownership | Design/FMEA/security reviews | Review minutes and action closure |
| Build/configure | Approved BOM/configuration and work instructions | Incoming inspection, unit/integration test | Build record and nonconformance log |
| FAT/verification | Versioned procedures and calibrated equipment | Witnessed pass/fail execution | Test report, raw evidence, defects |
| Site/SAT/UAT | Site readiness and approved cutover | Safety, functional, performance, recovery tests | Signed SAT/UAT and exception list |
| Hypercare | On-call, telemetry, known-error guidance | KPI, incident, intervention and defect trends | Daily report and handoff evidence |

## Defect classes

- Critical: unsafe condition, regulatory/security breach, or loss of required protective function; blocks use and release.
- High: prevents contracted workflow or recovery; blocks acceptance unless formally deferred with containment.
- Medium: degraded function with approved workaround; scheduled correction and tracked acceptance exception.
- Low: cosmetic or minor usability issue with no safety or contracted-performance effect.

## Entry and exit rules

- A test phase begins only when its environment, configuration, data, staff, safety controls, and procedures are ready.
- Failed tests produce defect IDs; they are not silently rerun until passing.
- Retest evidence references the corrected configuration and original defect.
- Acceptance exceptions state owner, workaround, due date, warranty/support impact, and authorized approver.

## Portfolio simulation quality

MuJoCo smoke tests verify model compilation. Scenario acceptance summaries verify scripted states and evidence generation. Windows recordings provide separate visual QA because a passing state-machine test does not prove that camera framing, payload contact, or object appearance is credible.
