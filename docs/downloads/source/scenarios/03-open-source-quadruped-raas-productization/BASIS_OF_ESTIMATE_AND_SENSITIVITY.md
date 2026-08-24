# Basis of Estimate and Sensitivity - OpenQuad RaaS

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [PB-M] public benchmark/medium applicability or source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Material inputs

**Table 1. Decision inputs and replacement evidence - Evidence and confidence shown per row**

| Input | Base | Evidence / confidence | Required replacement |
|---|---:|---|---|
| Open hardware/software and Solo12 reference | Available under published repository licenses | [PB-H] | Release-specific legal review and retained notices |
| Glassdoor U.S. Robotics Software Engineer | $154,709/year or $74/hour; May 2026 | [PB-M] | Customer payroll/contract ledger and Finance approval |
| BLS private-industry compensation split | Wages 69.9%; benefits 30.1%; March 2026 | [PB-H] | Company-specific benefit and payroll burden |
| Loaded planning labor cost | $154,709 / 69.9% = $221,329 per FTE-year | [DC-M] | Approved employer labor model |
| Productization program | $2,397,234 rounded | [DC-L] from 7.0 FTE-years and [SA-L] allowances | Approved resource-loaded estimate and actuals |
| Unitree Go2 EDU list price comparator | $15,900 | [PB-M] | Product-specific binding BOM and supplier quote |
| Build/calibration/delivery | $24,000 per robot | [DC-L] | Supplier quotes, routings, yield, freight, tax, and warranty reserve |
| Direct 36-month service/cloud reserve | $12,672 per robot | [DC-L] | Observed cases, cloud bills, spares consumption, and repair history |
| Subscription decision price | $2,400 per robot-month | [DC-L] from 48-unit recovery target | Executed order and collection terms |
| Customer capacity | 1,000 hours per site-year | [SA-L] | Time study and approved work-redesign plan |
| Customer capacity value | $74 per hour | [PB-M] Glassdoor salary rate, not loaded cost | Customer payroll/contract ledger and Finance approval |

## Provider sensitivity

**Table 2. Provider 36-month sensitivity - Evidence: [DC-L] derived from mixed inputs; Confidence: low overall**

| Case | Monthly price | Direct 3-year cost | Contribution including allocated onboarding | Units to recover $2.397M | Decision |
|---|---:|---:|---:|---:|---|
| Base | $2,400 | $36,672 | $50,498 | 48 | Conditional pass; $26,670 cohort buffer |
| Price -10% | $2,160 | $36,672 | $41,858 | 58 | Fails 48-unit cohort |
| Service cost +50% | $2,400 | $43,008 | $44,162 | 55 | Fails 48-unit cohort |
| Build cost +25% | $2,400 | $42,672 | $44,498 | 54 | Fails 48-unit cohort |
| Price -10% and service +50% | $2,160 | $43,008 | $35,522 | 68 | Stop / redesign |

## Customer sensitivity

**Table 3. Customer two-robot value sensitivity - Evidence: [DC-L] from [PB-M]/[SA-L] inputs; Confidence: low overall**

| Released hours per year | Salary value/hour | Three-year gross capacity value | Net value vs. $184,800 TCO | Result |
|---:|---:|---:|---:|---|
| 1,200 | $74 | $266,400 | $81,600 | 44.2% ROI |
| 1,000 | $74 | $222,000 | $37,200 | 20.1% ROI; passes 15% gate |
| 900 | $74 | $199,800 | $15,000 | 8.1% ROI; below gate |
| 800 | $74 | $177,600 | ($7,200) | Fails |
| 1,000 | $60 | $180,000 | ($4,800) | Fails |

The case is intentionally easy to fail. A correct calculation does not raise the confidence of its assumed inputs.
