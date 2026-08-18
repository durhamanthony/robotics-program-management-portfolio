# Business Case and TCO (Total Cost of Ownership) — Warehouse Truck Loading

## Decision

Complete the contracted controlled pilot. Authorize two-shift production use only if the pilot passes the safety and operating tests below **and** Finance validates at least **$445,200 of annual gross capacity value**. That is the minimum annual value required for a five-year simple payback on the $1.346 million installed cost and $176,000 annual recurring cost used in this scenario.

If Finance can monetize only 60% of the available labor hours, the five-year case loses $594,000 before discounting. In that case, do not expand the deployment; renegotiate the commercial model, add a higher-value shift/use case, or stop after contractual obligations are met.

## Operating baseline

| Input | Scenario value | Basis |
|---|---:|---|
| Conveyor lanes / humanoids | 5 / 5 | Signed-order scenario input |
| Manual handlers per shift before deployment | 5 | One handler assigned to each lane |
| Shifts / productive hours / operating days | 2 / 7.5 / 250 | Customer time-study input to validate |
| Annual manual handling hours | 18,750 | 5 × 2 × 7.5 × 250 |
| Retained cell attendants | 1 per shift | Human recovery, pallet exchange, and safe restart remain staffed |
| Annual retained-attendant hours | 3,750 | 1 × 2 × 7.5 × 250 |
| Hours available for approved capacity value | 15,000 | 18,750 − 3,750 |
| Loaded labor benchmark | $36.27/hour | March 2026 BLS production/transportation/material-moving compensation components |
| Full annual capacity value | $544,050 | 15,000 × $36.27 |

BLS is the U.S. Bureau of Labor Statistics. The labor benchmark is a public planning anchor, not the customer's payroll. Finance must replace it with the customer's actual wage, benefits, overtime, temporary-labor invoices, and approved workforce plan.

## Five-year cost model

Detailed line items are in [BUDGET.csv](BUDGET.csv).

| Cost | Calculation | Amount |
|---|---:|---:|
| One-time installed cost | Equipment, integration, site, logistics, training, contingency, reserve | $1,346,000 |
| Annual recurring cost | Software/support/spares plus contingency | $176,000 |
| Five-year recurring cost | $176,000 × 5 | $880,000 |
| Five-year TCO (Total Cost of Ownership) | $1,346,000 + $880,000 | **$2,226,000** |

The five-robot purchase price is a scenario contract input because commercially deployed humanoid pricing is not publicly quoted. Every non-public line is labeled quote-required in the budget and must be replaced during procurement.

## Base and conservative results

| Result | Base case: 100% approved capacity value | Conservative case: 60% approved capacity value |
|---|---:|---:|
| Annual gross benefit | $544,050 | $326,430 |
| Less annual recurring cost | ($176,000) | ($176,000) |
| Annual net benefit | $368,050 | $150,430 |
| Simple payback | 3.66 years | 8.95 years |
| Five-year net benefit | $494,250 | ($593,850) |
| Five-year ROI (Return on Investment) | 22.2% | Negative |
| Five-year NPV (Net Present Value) at 8% | $123,517 | ($745,377) |

No injury reduction, damage reduction, tax credit, depreciation benefit, or avoided incident cost is included. Those items require customer evidence and Finance approval.

## Pilot acceptance tied to the operating scenario

1. Five marked robot lanes remain clear of the conveyor, pallet exchange, forklift, and human recovery zones.
2. The cell sustains at least 225 cartons/hour for two consecutive hours across the approved 2–15 kilogram carton mix.
3. At least 98% of pick-carry-place attempts complete without manual recovery; no more than 2 interventions occur per 100 cartons.
4. Damage or wrong-placement rate is no more than 0.5% during the witnessed run.
5. Each seven-carton demonstration stack triggers a controlled robot pause, forklift pickup, truck entry, empty-forklift return, replacement-pallet placement, and authorized restart.
6. FAT (Factory Acceptance Test), SAT (Site Acceptance Test), and UAT (User Acceptance Testing) mandatory tests pass with no open critical safety finding.
7. Support can trace a robot event through telemetry, case creation, escalation, field action, and authorized return to service.

The MuJoCo animation compresses time and uses seven cartons so a viewer can see one complete flow. Production pallet patterns and cycle times come from the customer's approved SKU (Stock Keeping Unit) and pallet specification; they are not inferred from animation speed.

## Research anchors

- [BLS May 2025 wage overview](https://www.bls.gov/oes/2025/may/largest2.htm): laborers and freight, stock, and material movers averaged $42,260 annually.
- [BLS March 2026 compensation by occupational group](https://www.bls.gov/charts/employer-costs-for-employee-compensation/costs-by-occupational-group.htm): production, transportation, and material-moving compensation components total $36.27 per hour.
- [OSHA warehousing hazards and solutions](https://www.osha.gov/warehousing/hazards-solutions): repetitive lifting, lowering, bending, pushing, pulling, and awkward posture are warehouse musculoskeletal risk factors.
- [NIOSH Revised Lifting Equation](https://www.cdc.gov/niosh/ergonomics/about/rnle.html): object weight, reach, height, travel distance, asymmetry, frequency, duration, and coupling are required lifting-risk inputs.
- [OSHA robotics standards](https://www.osha.gov/robotics/standards): robot-system integration requires task-based risk assessment and safeguarding; cited standards are guidance and are not themselves OSHA regulations.

Research checked August 16, 2026. See [Research and Assumptions](RESEARCH_AND_ASSUMPTIONS.md) for source classification and replacement rules.
