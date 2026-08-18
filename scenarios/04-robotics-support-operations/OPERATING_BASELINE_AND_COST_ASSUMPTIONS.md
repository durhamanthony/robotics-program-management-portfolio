# Operating Baseline and Cost Assumptions — Robotics Support

## Installed base and workload

The planning baseline is 250 robots across 60 customer sites, with humanoid and quadruped products, business-hours customer intake, and 24-hour on-call coverage for safety and Severity-1 incidents.

| Monthly demand input | Calculation | Volume |
|---|---:|---:|
| Customer-created cases | 250 robots × 0.35 cases per robot | 88 |
| Actionable telemetry incidents | 250 robots × 0.20 incidents per robot | 50 |
| Planned maintenance visits | Scenario input | 25 |
| Deployments, updates, and site changes | Scenario input | 20 |
| **Total planned work items** | Rounded sum | **183/month** |

The organization must replace these inputs with at least 90 days of actual cases, telemetry precision, maintenance plans, release schedules, travel time, case handling time, severity mix, and service contracts. Telemetry events that do not require human action are not counted as cases.

## Launch staffing and loaded annual planning cost

| Function | People | Loaded annual cost per person | Annual cost |
|---|---:|---:|---:|
| Service owner/program manager | 1 | $180,000 | $180,000 |
| Level 1 customer support | 3 | $85,000 | $255,000 |
| Level 2 robotics support | 4 | $150,000 | $600,000 |
| Field service | 4 | $130,000 | $520,000 |
| Reliability/problem engineer | 1 | $155,000 | $155,000 |
| Knowledge/tools/data analyst | 1 | $125,000 | $125,000 |
| Parts/Return Material Authorization coordinator | 1 | $100,000 | $100,000 |
| On-call, overtime, and surge allowance | — | — | $15,000 |
| **Initial staffing** | **15** |  | **$1,950,000** |

Loaded cost means salary or contractor fee plus the scenario allowance for benefits, payroll burden, on-call, and management allocation. It is not a wage claim. Human Resources and Finance must replace it with named-role compensation and contractor quotes.

## Capacity checks

- Three Level 1 agents provide about 300 net case-hours per month after meetings, training, and non-case work. At 30 minutes per intake/case-administration touch, that is roughly 600 touches per month, leaving room for updates and launch spikes.
- Four Level 2 engineers provide about 400 net diagnostic hours per month. At two hours per escalated case, they can cover roughly 200 escalations per month before field/project work; sustained utilization above 75% triggers hiring or scope review.
- Four field technicians can support approximately 32 two-day visits per month before travel constraints. A 13-week regional forecast and contractor coverage determine whether that is sufficient.
- Add coverage when the forecast exceeds 75% of usable capacity for six consecutive weeks, two people cannot cover a critical skill/on-call rotation, or contracted response is missed twice in a rolling month.

## Cost result

The first-year base program is $3.950 million plus $718,000 reserve, or $4.668 million authorized exposure. The steady-state year-two run rate is $2.970 million. Three-year Total Cost of Ownership (TCO), assuming the year-two run rate repeats in year three and the full reserve is consumed, is **$10.608 million**.

See [BUDGET.csv](BUDGET.csv) for line items and [Tool Selection and Cost Model](TOOL_SELECTION_AND_COST.md) for the stack. Every platform amount remains quote-required and must account for robot count, users, sites, storage, data egress, integration, implementation, support, and contract term.
