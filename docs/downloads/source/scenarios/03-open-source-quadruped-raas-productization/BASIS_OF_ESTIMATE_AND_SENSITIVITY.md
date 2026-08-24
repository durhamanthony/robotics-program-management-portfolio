# Basis of Estimate and Sensitivity - OpenQuad RaaS

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Material inputs

**Table 1. Decision inputs and replacement evidence - Evidence and confidence shown per row**

| Input | Base | Evidence / confidence | Required replacement |
|---|---:|---|---|
| Open hardware/software and Solo12 reference | Available under published repository licenses | [PB-H] | Release-specific legal review and retained notices |
| Productization program | $2,400,000 | [SA-L] | Approved resource-loaded estimate and actuals |
| Build/calibration/delivery | $28,000 per robot | [SA-L] | Supplier quotes, routings, yield, freight, tax, and warranty reserve |
| Direct service/cloud reserve | $7,200 per robot-year | [SA-L] | Observed cases, cloud bills, spares consumption, and repair history |
| Subscription | $2,950 per robot-month | [SA-L] | Executed order and collection terms |
| Customer capacity | 1,200 hours per site-year | [SA-L] | Time study and approved work-redesign plan |
| Loaded capacity value | $78 per hour | [SA-L] | Customer payroll/contract ledger and Finance approval |

## Provider sensitivity

**Table 2. Provider 36-month sensitivity - Evidence: [DC-L] derived from [SA-L] inputs; Confidence: see evidence key and row/source notes**

| Case | Monthly price | Direct 3-year cost | Contribution including allocated onboarding | Units to recover $2.4M | Decision |
|---|---:|---:|---:|---:|---|
| Base | $2,950 | $49,600 | $58,600 | 41 | Conditional pass |
| Price -10% | $2,655 | $49,600 | $47,980 | 51 | Fails 48-unit cohort |
| Service cost +50% | $2,950 | $60,400 | $47,800 | 51 | Fails 48-unit cohort |
| Build cost +25% | $2,950 | $56,600 | $51,600 | 47 | Narrow pass before omitted costs |
| Price -10% and service +50% | $2,655 | $60,400 | $37,180 | 65 | Stop / redesign |

## Customer sensitivity

**Table 3. Customer two-robot value sensitivity - Evidence: [DC-L] derived from [SA-L] inputs; Confidence: see evidence key and row/source notes**

| Released hours per year | Loaded value/hour | Three-year gross capacity value | Net value vs. $236,400 TCO | Result |
|---:|---:|---:|---:|---|
| 1,200 | $78 | $280,800 | $44,400 | 18.8% ROI |
| 1,000 | $78 | $234,000 | ($2,400) | Fails |
| 900 | $78 | $210,600 | ($25,800) | Fails |
| 1,200 | $60 | $216,000 | ($20,400) | Fails |

The case is intentionally easy to fail. A correct calculation does not raise the confidence of its assumed inputs.
