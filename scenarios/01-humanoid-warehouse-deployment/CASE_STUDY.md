# Case Study 1 — Five Humanoids for Pallet Building and Truck Loading

## Scenario

A robotics vendor has sold five humanoid robots to a distribution warehouse. Each robot works in a marked lane, stops before a powered conveyor, receives one approved carton, carries it to a floor pallet, and contributes to a seven-carton stack. A robot-operated forklift then moves the loaded pallet into the open back of an outbound truck. The robots pause while a replacement pallet is placed. The program manager owns delivery from signed order through customer acceptance and the end of hypercare.

## Outcome

Deploy the five-robot cell for two shifts at one site. The controlled pilot must move at least 225 approved cartons per hour for two consecutive hours, complete at least 98 of every 100 pick-carry-place attempts without manual recovery, and require no more than two human interventions per 100 cartons. Expansion is not approved unless the financial model also shows a five-year simple payback using finance-approved labor-capacity value.

## Success measures

| Measure | Acceptance threshold |
|---|---:|
| Safety validation | 100% mandatory tests passed; no open critical safety findings |
| Mission success | >= 98% during acceptance window within agreed carton envelope |
| Throughput | At least 225 cartons/hour for two consecutive hours using the acceptance carton mix |
| Damage/mis-sort | No more than 0.5% damaged or misplaced cartons during the acceptance run |
| Fleet availability | >= 95% during two-week hypercare, excluding approved windows |
| Human intervention | No more than 2 interventions per 100 cartons |
| Support readiness | Portal, telemetry, severity routing, on-call, spares, and remote access tested |
| Training | 100% designated operators/support staff pass role assessment |

## Program phases

1. Contract and SOW (Statement of Work) acceptance crosswalk.
2. Use-case validation and carton/conveyor/pallet/truck-process data collection.
3. Site survey, safety concept, material-flow and integration design.
4. Configuration/build, integration, simulation, FAT (Factory Acceptance Test), and support preparation.
5. Site readiness and pre-ship go/no-go.
6. Delivery, installation, calibration, SAT (Site Acceptance Test), safety validation, and UAT (User Acceptance Testing).
7. Controlled pilot by lane/shift, production cutover, and hypercare.
8. Handoff, benefits review, and expansion decision.

## Workstreams

- Program governance and customer management
- Robot hardware, end effector, firmware/software, and configuration
- Warehouse process, material flow, pallet/forklift/truck interface, and conveyor/WMS (Warehouse Management System) integration
- Safety/EHS (Environment, Health, and Safety) and human factors
- Site/facilities, power, charging, network, and physical controls
- Data, cybersecurity, privacy, telemetry, and dashboards
- Training, change management, labor/operational readiness
- Support, field service, spares, warranty, RMA (Return Material Authorization), and hypercare

## Critical scenario decisions

- How are robot lanes separated from the conveyor, pallet exchange, forklift travel, and human recovery zones?
- What carton dimensions, weights, materials, damage states, and stack patterns are supported?
- How are unknown, damaged, leaking, unstable, or prohibited items rejected?
- What creates and ends a robot mission, and what happens when WMS/conveyor/network is unavailable?
- How are dropped cartons, unstable pallet stacks, forklift conflicts, truck availability, lighting, dust, and wet floors handled?
- What is the safe state after localization, perception, grasp, power, or communications failure?
- Which intervention requires a protective stop versus energy isolation and qualified service?

## Financial decision tied to the scenario

The baseline uses 18,750 annual manual handling hours and a public labor-cost benchmark of $36.27 per hour. Retaining one cell attendant per shift leaves 15,000 hours that could become capacity value. The full value is $544,050 per year, but it may be counted only when finance approves an overtime reduction, avoided temporary-labor expense, or documented redeployment plan. With a $1.346 million installed cost and $176,000 recurring annual cost, at least $445,200 in annual gross benefit is required for a five-year simple payback. The detailed calculation and conservative case are in [Business Case and TCO](BUSINESS_CASE_AND_TCO.md).
