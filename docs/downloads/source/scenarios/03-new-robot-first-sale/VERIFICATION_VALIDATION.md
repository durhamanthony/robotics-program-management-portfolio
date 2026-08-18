# Verification and Validation Strategy

## Verification asks: did we build the specified product?

Requirements trace to analysis, inspection, test, or demonstration at component, subsystem, integrated robot, and production-unit levels.

## Validation asks: does the product solve the customer workflow in its real context?

Use representative payloads, people, layouts, shifts, lighting, network conditions, exception frequency, and maintenance/support workflows—not only a polished nominal demo.

## Test program

| Level | Examples | Gate/evidence |
|---|---|---|
| Component | actuator, sensor, battery, compute, gripper | Characterization and supplier qualification |
| Subsystem | arm, mobile base, perception, power, charging | Interface/performance/fault tests |
| Integrated Engineering Verification Test (EVT) | Nominal mission and highest-risk interactions | Feasibility and risk-retirement report |
| Design Verification Test (DVT) | 2,000-cycle mission mix, rate, safety, reliability, environmental, security, and service tests | Completed traceability and design-verification report |
| Production Validation Test (PVT) | Ten-unit build, yield, labor, calibration, end-of-line test, and packaging | Process validation and pilot-build report |
| First site | Commissioning, Site Acceptance Test (SAT), User Acceptance Testing (UAT), 30-day soak, and support drill | Customer acceptance package |

## Defect priority

Priority 0 (P0) is stop-ship, safety, or security; Priority 1 (P1) blocks acceptance or the core mission; Priority 2 (P2) is degraded with an approved workaround; Priority 3 (P3) is minor, cosmetic, or documentation-only. Every waiver records customer, product, and safety impact, owner, expiration, and permanent action.

## Portfolio MuJoCo evidence

The `new_robot_npi` demo verifies that the simplified AD-01 MuJoCo XML model loads, actuators respond, joint limits are respected, a repeatable motion sequence completes, simulated telemetry is produced, and an injected stop creates an auditable result.
