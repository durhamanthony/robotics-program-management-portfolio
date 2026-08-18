# Business Case — AD-01 Mobile Manipulator Through First Sale

## Decision

Fund an 18-month, **$10.975 million** New Product Introduction (NPI) program in tranches to build and deliver the first AD-01: a compact mobile manipulator that transfers one approved tote type, up to 15 kilograms, over an 18-meter indoor route between two fixed stations.

Do not authorize the first-customer shipment until the product demonstrates at least 40 completed transfers per hour, 98% mission success, no more than three human interventions per 100 missions, at least 95% scheduled availability, safe behavior under mandatory faults, production first-pass yield of at least 90%, and Cost of Goods Sold (COGS) at or below $150,000.

## First-customer workflow and value

The customer operates two material-handler positions per shift, two shifts per day, 7.5 productive hours per shift, 250 days per year. AD-01 does not remove human exception ownership; the model retains the equivalent of 0.5 handler per shift for replenishment, recovery, and adjacent work.

The $36.27 hourly labor-cost anchor comes from the March 2026 U.S. Bureau of Labor Statistics (BLS) private-industry production, transportation, and material-moving occupational group: $24.74 wages plus $11.53 in employer-paid benefits. It is a planning anchor, not a customer quote.

| Customer calculation | Formula | Annual value |
|---|---:|---:|
| Current handling cost | 2 handlers × 2 shifts × 7.5 hours × 250 days × $36.27 | $272,025 |
| Retained supervision/recovery | 0.5 handler × 2 shifts × 7.5 hours × 250 days × $36.27 | ($68,006) |
| Gross capacity value | $272,025 − $68,006 | **$204,019** |
| Annual software/service | Scenario offer | ($36,000) |
| Net annual customer benefit | $204,019 − $36,000 | **$168,019** |

At a $285,000 unit price plus $45,000 installation and training, the customer’s $330,000 initial outlay has a 1.96-year simple payback. Five-year Total Cost of Ownership (TCO) is $510,000; five-year net benefit is $510,094; and five-year Net Present Value (NPV) at 8% is $340,850. The model gives no credit for injury avoidance, overtime, or downstream throughput.

## Company investment and unit economics

| Item | Amount | Basis |
|---|---:|---|
| 20-person average cross-functional team for 18 months | $4,875,000 | $162,500 average annual loaded cost including benefits, contractor premium, and management allocation |
| Prototypes, tooling, fixtures, and test equipment | $2,300,000 | Engineering Verification Test, Design Verification Test, and Production Validation Test builds |
| Pilot parts and supplier qualification | $900,000 | Pilot material, alternates, and qualification |
| Safety, cybersecurity, legal, and external testing | $600,000 | Quote-required planning allowance |
| First-customer deployment and hypercare | $350,000 | One controlled installation, training, spares, and field coverage |
| Cloud, laboratory, and data systems | $450,000 | 18-month planning allowance |
| Commercial, contract, and launch readiness | $300,000 | Offer, demonstration, contract, and launch material |
| Management reserve | $1,200,000 | Sponsor-controlled unknowns |
| **Total NPI investment** | **$10,975,000** | Before production working capital and corporate overhead |

The team-cost assumption is checked against public BLS medians for engineering managers, mechanical engineers, electrical/electronics engineers, industrial engineers, software developers, and project-management specialists. The model deliberately uses a higher blended loaded figure than salary because a startup program also carries benefits, payroll burden, contractors, recruiting, equipment, and management allocation. Finance must replace it with actual payroll and contractor rates.

At a $285,000 selling price and $150,000 COGS, unit contribution before sales, support, warranty, corporate overhead, working capital, tax, and financing is $135,000. Recovering the $10.975 million development investment therefore requires approximately **82 units** ($10,975,000 ÷ $135,000, rounded up). This is a program-screening threshold, not a forecast of demand.

## Funding gates

| Gate | Release condition | Funding decision |
|---|---|---|
| Discovery | Twelve observed workflows; at least four qualified design partners; customer baseline and willingness-to-pay evidence | Release concept funding |
| Concept | 15-kilogram payload and 18-meter route feasibility; preliminary hazards; target cost and supplier plan | Release Engineering Verification Test funding |
| Engineering Verification Test (EVT) | Core mobility, grasp, transfer, safe-state, telemetry, and charging functions demonstrated; top five technical risks reduced | Release Design Verification Test tooling |
| Design Verification Test (DVT) | Requirements matrix passed; 98% mission success over 2,000 representative cycles; COGS forecast at or below $165,000 | Release Production Validation Test build |
| Production Validation Test (PVT) | Ten units on intended process; at least 90% first-pass yield; final assembly/test at or below 40 labor hours; COGS at or below $150,000 | Authorize first-customer unit |
| First customer | Thirty-day acceptance window meets mission, availability, intervention, support, and value thresholds | Decide General Availability (GA), narrow scope, or stop |

## Stop or pivot conditions

- Fewer than four qualified customers confirm the same narrow workflow and economic range.
- The product cannot safely handle the 15-kilogram tote or mandatory fault cases.
- DVT mission success remains below 98% after the approved correction period.
- Forecast COGS remains above $165,000 at the DVT gate or above $150,000 at PVT.
- PVT first-pass yield is below 90% or final assembly/test exceeds 40 labor hours without an approved recovery plan.
- The first customer requires custom engineering that changes the common product baseline.
- The commercial forecast cannot support the 82-unit development break-even threshold within the approved planning horizon.

## Research anchors

- [BLS employer compensation by occupational group, March 2026](https://www.bls.gov/charts/employer-costs-for-employee-compensation/costs-by-occupational-group.htm)
- [BLS architectural and engineering managers](https://www.bls.gov/ooh/management/architectural-and-engineering-managers.htm)
- [BLS mechanical engineers](https://www.bls.gov/ooh/architecture-and-engineering/mechanical-engineers.htm)
- [BLS electrical and electronics engineers](https://www.bls.gov/ooh/architecture-and-engineering/electrical-and-electronics-engineers.htm)
- [BLS industrial engineers](https://www.bls.gov/ooh/architecture-and-engineering/industrial-engineers.htm)
- [BLS software developers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)
- [BLS business career options, including project-management specialists](https://www.bls.gov/careeroutlook/2025/article/business-career-options.htm)
- [OSHA robot-system standards and consensus-standard references](https://www.osha.gov/robotics/standards)
- [NIOSH Revised Lifting Equation](https://www.cdc.gov/niosh/ergonomics/about/rnle.html)

Research checked August 16, 2026. See [Research and Assumptions](RESEARCH_AND_ASSUMPTIONS.md) for the evidence hierarchy and replacement rules.
