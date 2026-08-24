# Reliability and Serviceability Plan - OpenQuad RaaS

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [PB-M] public benchmark/medium applicability or source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

**Table 1. Reliability and serviceability measures - Evidence: scenario targets [SA-L]; Confidence: low**

| Measure | Target | Trigger / action |
|---|---:|---|
| Fleet availability | >=95% | Weekly problem review below target |
| Mean time to diagnose eligible remote cases | <=4 business hours | Evidence-template or observability correction |
| Advance replacement shipped | >=95% within 48 hours | Increase pool or correct dispatch process |
| Repeat failure within 30 days | <=5% | Problem record and engineering corrective action |
| First-pass production yield | >=90% | Containment and process capability review |
| Golden-image reproducibility | 100% | Release hold |
| SBOM/license record completeness | 100% | Shipment hold |

The service team maintains serialized spare state, calibration currency, battery history, failure code, returned-unit quarantine, root cause, corrective action, and return-to-stock evidence.
