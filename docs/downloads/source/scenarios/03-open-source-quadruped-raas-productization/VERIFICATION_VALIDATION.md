# Verification and Validation - OpenQuad RaaS

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [PB-M] public benchmark/medium applicability or source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Evidence strategy

Verification proves the product was built to its controlled requirements. Validation proves the supported service solves the disclosed customer problem within the laboratory envelope.

**Table 1. Release verification and pilot validation - Evidence: scenario plan/results [SA-L]; Confidence: low**

| Layer | Test | Threshold | Fictional closeout |
|---|---|---|---|
| Build | Clean rebuild from pinned source and artifacts | 12 of 12 units | Pass |
| Compliance | Component, license, hash, notice, and relationship completeness | 100% | Pass |
| Safety | E-stop, battery fault, comms loss, recovery authorization | 100% witnessed | Pass |
| Configuration | Serial, hardware revision, calibration, image, customer assignment | 100% | Pass |
| Reliability | 500-hour mixed lab endurance across pilot fleet | No unresolved critical failure | Pass after fan-duct correction |
| Service | Eligible advance replacement | At least 95% within 48 hours | 7 of 7 pass |
| Availability | Entitled scheduled time | At least 95% | 95.6% |
| Customer workflow | Scheduled experiment completion | At least 97% | 97.8% |
| Release | Signed update and rollback | 12 of 12 units | Pass |

MuJoCo validates only that the portfolio's generic demonstration model compiles and its scripted states render. It does not validate Solo12 dynamics, product safety, control quality, or commercial performance.
