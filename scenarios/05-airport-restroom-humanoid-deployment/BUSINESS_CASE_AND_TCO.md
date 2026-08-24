# Business Case and Total Cost of Ownership

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Decision being made

Should the airport accept the two-robot, four-restroom pilot, and should it authorize expansion?

These are two separate decisions. Pilot acceptance is based on delivered scope and evidence. Expansion requires a defensible operating and financial case.

## Evidence status

Airport operating patterns, labor references, and cited safety or cleaning guidance are **public benchmarks**. Task timing informed by published material is a **research-based estimate**. Equipment, integration, support, oversight, workload, and fictional pilot-result inputs are **scenario assumptions**. Total Cost of Ownership, capacity value, and economic gaps are **derived calculations**. Actual restroom demand, task time, customer labor cost, vendor pricing, service terms, performance, and conversion of released capacity into avoided expense are **unknown / pending validation**.

## Pilot authorization

**Table 1. Pilot authorization — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Cost group | Planning amount |
|---|---:|
| Two humanoid robots and chargers | $500,000 |
| Manufacturer application engineering | $220,000 |
| Seller/integrator configuration and commissioning | $310,000 |
| Airport site, network, cybersecurity, and entry controls | $145,000 |
| Independent safety and acceptance | $120,000 |
| Training and operational change | $70,000 |
| Pilot support, spares, and consumables | $110,000 |
| Integrated program management | $155,000 |
| Direct-cost base | $1,630,000 |
| Uncertainty allowance — 15% | $244,500 |
| **Pilot authorization** | **$1,874,500** |

## Five-year planning Total Cost of Ownership

The authorization includes equipment, deployment, and the initial pilot-support period. The steady-state planning run rate after pilot is $315,000 per year: $120,000 support/software, $60,000 maintenance/spares, $25,000 incremental consumables, $90,000 airport oversight/quality, and $20,000 network/data.

Five-year Total Cost of Ownership = USD 1,874,500 + (4 × USD 315,000) = **USD 3,134,500**.

## Benefit model

The pilot baseline contains 4 restrooms × 3 routine missions per day × 0.50 observed labor-hour per mission × 365 days = 2,190 annual labor-hours. At the fictional airport's USD 31.50 loaded rate, that is **USD 68,985 of annual task capacity**.

The May 2025 U.S. Bureau of Labor Statistics national mean wage for janitors and cleaners is USD 18.64 per hour. The fictional USD 31.50 loaded airport rate is 1.69 times that public wage benchmark and is assumed to include benefits, shift differential, supervision, insurance, and contractor overhead. It must be replaced with the airport's payroll or custodial-contract ledger.

This is not booked savings. Custodians remain responsible for inspection, exception response, corrective cleaning, supplies, and reopening. No position is eliminated in this scenario.

## Decision outcome

- Pilot deliverables: accept.
- Controlled 60-day evidence extension: accept within the existing four-room scope.
- Airport-wide rollout: do not authorize.
- Reason: the pilot established technical and operating evidence, but $68,985 annualized capacity value does not support a $3,134,500 five-year Total Cost of Ownership.

## Separate Phase 2 recommendation

Do not scale the pilot's capital-purchase design. Evaluate a separate 12-restroom Robotics-as-a-Service (RaaS) operating model documented in `PHASE_2_RAAS_EXPANSION_BUSINESS_CASE.md`.

That design schedules 28 productive fleet-hours per day across two robots. At the same USD 31.50 loaded task rate, it creates USD 321,930 of annual capacity value. With a USD 6,000 per-robot monthly subscription, USD 150,000 of integration, and USD 80,000 per year of retained human support, five-year Total Cost of Ownership is USD 1,270,000. The resulting planning net benefit is USD 339,650 and Return on Investment (ROI) is 26.7%.

The same case has approximately USD 241,006 of five-year Net Present Value at 8% and 1.53-year simple payback on integration. It breaks even at 22.1 productive fleet-hours per day; at 22 hours the five-year net benefit is negative USD 5,275. At the public USD 18.64 mean wage, even 28 productive hours per day would not cover the modeled USD 224,000 annual recurring cost.

The Phase 2 result is **Conditional Green**, not authorized work. It depends on verified utilization, binding quotations, and a subscription no higher than USD 6,595 per robot per month to preserve a 20% five-year customer ROI.

## Conditions to reopen expansion

1. Binding equipment, integration, support, and infrastructure quotations.
2. Observed workload by room, time of day, service type, and exception class.
3. Measured passenger-service value, closure time, quality consistency, exposure reduction, and response performance.
4. A fleet and staffing model that preserves specialist response and human inspection.
5. Sensitivity that remains acceptable under lower utilization, higher support cost, and replacement-part delay.
6. Airport, workforce, safety, cybersecurity, privacy, finance, and procurement approval.
