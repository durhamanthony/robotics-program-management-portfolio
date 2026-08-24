# OpenQuad Managed Lab Product Brief and Product Requirements Document

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [PB-M] public benchmark/medium applicability or source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Product promise

Provide a reproducible two-robot research-lab capability with predictable monthly spend, maintained release images, traceable open-source provenance, remote diagnosis, and an advance-replacement path. The offer does not convert research hardware into an industrially certified robot.

## Users and jobs

**Table 1. Users and jobs to be done - Evidence: scenario discovery synthesis [SA-L]; Confidence: low**

| User | Job | Product response |
|---|---|---|
| Principal investigator | Start experiments without a semester-long build program | Calibrated units, onboarding, reference experiments, and release notes |
| Lab engineer | Reproduce a known configuration and recover faults safely | Versioned images, configuration manifest, diagnostics, and recovery runbook |
| Procurement / finance | Compare a term commitment with self-managed ownership | Transparent 36-month TCO, inclusions, exclusions, and exit terms |
| Security / IT | Know software components, access, data flow, and update ownership | SBOM, signed images, least privilege, retention choices, and audit records |
| Provider service owner | Maintain uptime without uncontrolled product variants | Configuration baseline, swap pool, serialized assets, and change gates |

## Release 1 requirements

**Table 2. Product requirements summary - Evidence: scenario requirements [SA-L]; confidence medium after stakeholder review**

| ID | Requirement | Release threshold | Verification |
|---|---|---|---|
| PRD-001 | Every shipped unit has a serialized configuration and build record | 100% | Record audit |
| PRD-002 | The golden software image installs reproducibly | 12 of 12 pilot units | Clean-image rebuild |
| PRD-003 | Hardware and software components have license/provenance records | 100% of shipped components | SBOM and notice audit |
| PRD-004 | Emergency stop and authorized recovery work in every defined test | 100% | Witnessed fault injection |
| PRD-005 | Scheduled fleet availability during pilot | At least 95% | Service telemetry |
| PRD-006 | Scheduled experiment completion during pilot | At least 97% | Mission/event records |
| PRD-007 | Provider can ship an advance replacement for an eligible failure | Within 48 hours for at least 95% | Service-case audit |
| PRD-008 | Customer data retention and export follow the executed order | 100% | Configuration and deletion test |
| PRD-009 | Unapproved forks cannot enter the supported release | Zero | Release-control audit |
| PRD-010 | Field updates are signed, staged, observable, and reversible | 100% of releases | Deployment and rollback test |

## Product principles

1. Preserve upstream notices and do not imply contributor endorsement.
2. Treat every dependency by its own license; do not infer that an entire stack is BSD-licensed.
3. Keep community reference, provider-maintained fork, customer configuration, and experimental code as separate controlled layers.
4. Sell service outcomes and support boundaries, not unsupported industrial autonomy claims.
