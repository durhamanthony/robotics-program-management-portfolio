# Basis of Estimate and Sensitivity — Robotics Support Operations

## Planning basis

This model sizes a support organization for a fictional installed base of 250 robots across 60 customer sites. It is an operating-model estimate, not a vendor quotation or claim about an existing fleet.

| Input | Base value | Evidence class | Required replacement evidence |
|---|---:|---|---|
| Installed base | 250 robots / 60 sites | Fictional portfolio baseline | Installed-product register and signed deployment forecast |
| Customer-created cases | 0.35 per robot per month | Fictional demand rate | At least 90 days of normalized case history |
| Actionable telemetry incidents | 0.20 per robot per month | Fictional demand rate | Alert precision, suppression, and human-action data |
| Planned maintenance visits | 25 per month | Fictional operating input | Maintenance plan and regional route forecast |
| Changes and deployments | 20 per month | Fictional operating input | Release and deployment calendar |
| Fifteen-person team | $1,950,000 loaded annual cost | Fictional role-based allowance | Human Resources rates, contractor bids, geographic mix, and on-call terms |
| Platforms, telemetry, remote access, and storage | Scenario allowances | Quote required | Named editions, users, assets, retention, data volume, egress, implementation, and support terms |

## Workload and capacity math

- Customer cases = 250 × 0.35 = **87.5**, rounded to 88 per month.
- Actionable telemetry incidents = 250 × 0.20 = **50 per month**.
- Planned work = 88 cases + 50 telemetry incidents + 25 maintenance visits + 20 changes/deployments = **183 work items per month**.
- Three Level 1 agents provide about **300 net case-hours per month** in the model.
- Four Level 2 engineers provide about **400 net diagnostic hours per month**.
- Four field technicians provide a planning capacity of **32 two-day visits per month** before regional travel constraints.

The staffing plan triggers review when usable capacity exceeds 75% for six consecutive weeks, response targets are missed twice in a rolling month, or a critical skill/on-call rotation cannot be covered by two people.

## Cost reconciliation

- Year-one base = **$3,950,000**.
- Management reserve = **$718,000**.
- Year-one authorized exposure = $3,950,000 + $718,000 = **$4,668,000**.
- Year-two steady-state run rate = **$2,970,000**.
- Three-year Total Cost of Ownership (TCO), assuming the year-two run rate repeats in year three and the full reserve is consumed, = $4,668,000 + 2 × $2,970,000 = **$10,608,000**.

## Sensitivity

| Change | Operating effect | Financial treatment |
|---|---|---|
| Case and actionable-alert rates are 25% higher | About 218 monthly work items before planned-project changes | Recalculate touch time and Level 1/Level 2 capacity before hiring |
| Field demand rises from 25 to 35 two-day visits per month | Exceeds the four-technician planning capacity | Add regional contractor or headcount after travel analysis |
| Vendor platform quotes are 20% higher than allowances | Increase affected tooling lines, implementation, reserve, and recurring run rate | Sponsor reauthorization required |
| Telemetry precision reduces actionable alerts by 40% | About 30 rather than 50 telemetry incidents per month | Reallocate engineering time; do not book savings until sustained for 90 days |

## Decision rule

The operating model can close only when the installed-product baseline, intake and severity process, safe remote-access controls, on-call model, field coverage, parts/Return Material Authorization (RMA), continuity test, service dashboards, and product escalation path are accepted. Budget approval remains conditional on vendor quotes and a 90-day workload calibration.
