# Research and Assumptions - Open-Source Quadruped Productization

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Public anchors

**Table 1. Public source register - Evidence: public benchmarks [PB-H] unless noted; Confidence: see evidence key and row/source notes**

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

Research checked 2026-08-23.

## Scenario assumptions

Six pilot sites, 12 robots, 60 days, 48-hour eligible advance replacement, $2.4 million development, $28,000 direct unit cost, $7,200 annual direct service cost, $2,950 monthly subscription, $12,000 site onboarding, 1,200 customer hours released per year, and $78 loaded capacity value are all [SA-L]. None is a vendor quote, customer actual, or market forecast.

## Open unknowns

Supplier quotations, export/import treatment, battery transport, insurance, customer data terms, product liability, accessibility, independent safety review, component obsolescence, support demand, repair yield, warranty reserve, churn, collections, and actual conversion volume are [UPV] and must close before General Availability.
