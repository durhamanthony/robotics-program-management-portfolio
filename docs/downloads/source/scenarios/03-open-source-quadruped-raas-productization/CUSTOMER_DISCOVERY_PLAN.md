# Customer Discovery Plan - Managed Research Quadrupeds

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Discovery objective

Determine whether customers value reproducibility and support enough to choose a term service over self-managed builds, and identify the narrow release that can be supported without absorbing arbitrary research forks.

## Interview and evidence plan

**Table 1. Discovery questions and decision evidence - Evidence: scenario plan [SA-L]; Confidence: see evidence key and row/source notes**

| Hypothesis | Question / observation | Evidence required | Decision |
|---|---|---|---|
| Build/calibration consumes material engineering time | Walk through the last robot build and recovery | Time records, defects, rework, and delays | Quantify addressable capacity |
| Configuration drift causes irreproducible experiments | Compare images, dependencies, and calibration files | Version manifests and failed reruns | Define supported baseline |
| Advance replacement has value | Review downtime and spare strategy | Downtime log and experiment schedule | Set swap entitlement |
| Security/procurement needs provenance | Observe review artifacts | SBOM, licenses, access, retention, and terms | Define release packet |
| Subscription can fit funding cycles | Test 12-, 24-, and 36-month terms | Budget authority and approval path | Set price/term gate |

The team must conduct at least 20 interviews across investigators, lab engineers, IT/security, procurement, and finance; observe five build/recovery workflows; and obtain nonbinding demand evidence before pilot authorization. Interview enthusiasm is not counted as contracted demand.
