# Research and Assumptions - Open-Source Quadruped Productization

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [PB-M] public benchmark/medium applicability or source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Public anchors

**Table 1. Public source register - Evidence: public benchmarks [PB-H]/[PB-M]; Confidence: high/medium by row**

| Topic | Source | Portfolio use | Limitation |
|---|---|---|---|
| Open Dynamic Robot Initiative | https://open-dynamic-robot-initiative.github.io/ | Confirms open hardware/software objective and BSD 3-Clause statement | Does not approve this product or its commercial claims |
| Solo12 hardware | https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/quadruped_robot_12dof_v1/README.md | Confirms 12 active degrees of freedom and documented build components | Reference design, not a provider BOM or quote |
| Autonomy upgrade | https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/quadruped_robot_12dof_v1.1/README.md | Supports battery, wireless, e-stop, monitoring, and payload-interface feasibility screening | Prototype documentation; production verification still required |
| Solo low-level interface | https://github.com/open-dynamic-robot-initiative/solo | Confirms a BSD-3-Clause repository and low-level interface | Every transitive dependency needs its own review |
| Solo configuration files | https://github.com/open-dynamic-robot-initiative/robot_properties_solo | Confirms configuration resources and BSD-3-Clause repository | Does not establish provider configuration correctness |
| Master Board | https://github.com/open-dynamic-robot-initiative/master-board | Confirms board function and BSD-2-Clause repository | Hardware availability and lifecycle are [UPV] |
| Secure Software Development Framework | https://csrc.nist.gov/pubs/sp/800/218/final | Secure development and supplier communication structure | Guidance, not product certification |
| 2026 SBOM minimum elements | https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom | Release SBOM content baseline | Legal/security review still required |
| PAL Robotics Solo12 status | https://solo.pal-robotics.com/solo | Confirms commercial Solo12 sales are discontinued | Treats the reference as an obsolescence/supply-chain gate, not a purchasable product |
| Unitree Go2 EDU | https://www.unitree-robot.com/shop/products/unitree-go2 | Current $15,900 official research/developer quadruped comparator | Different platform and configuration; not a Solo12 quote or endorsed substitute [PB-M] |
| Glassdoor U.S. Robotics Software Engineer salary | https://www.glassdoor.com/Salaries/gyor-robotics-software-engineer-salary-SRCH_IL.0%2C4_KO5%2C31.htm | $154,709/year or $74/hour average, 435 salaries, as of May 2026 | Crowdsourced/model-based benchmark; not customer payroll or fully loaded labor [PB-M] |
| BLS Employer Costs for Employee Compensation | https://www.bls.gov/charts/employer-costs-for-employee-compensation/costs-by-industry.htm | March 2026 private-industry split: wages 69.9%, benefits 30.1% | Aggregate load factor; not company-specific [PB-H] |

Research checked 2026-08-24.

## Scenario assumptions

Six pilot sites, 12 robots, 60 days, 48-hour eligible advance replacement, 7.0 FTE-years, 50 configuration/calibration hours per robot, a $4,400 unit allowance, 36 service hours per robot-year, $600 annual cloud cost, a 12% spares/warranty reserve, $1,500 onboarding travel/materials, a $6,000 customer network allowance, 1,000 released customer hours per year, a 48-robot recovery cohort, and the resulting $2,400 subscription decision price are [SA-L]. Glassdoor, BLS, and Unitree provide anchors; they do not validate these quantities or conversion volume.

## Open unknowns

Supplier quotations, export/import treatment, battery transport, insurance, customer data terms, product liability, accessibility, independent safety review, component obsolescence, support demand, repair yield, warranty reserve, churn, collections, and actual conversion volume are [UPV] and must close before General Availability.
