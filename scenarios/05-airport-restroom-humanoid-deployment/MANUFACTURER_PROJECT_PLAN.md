# Manufacturer Project Manager Plan

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Accountable outcome

Release and support a traceable pilot configuration that can execute the four-room routine scope, produce verification evidence, and fail safely. The release is limited to the pilot; it is not General Availability.

## Product baseline

- Two serialized humanoid robots and two chargers.
- Approved cleaning-tool and supply interfaces.
- Locked chemical/material compatibility list.
- Restroom mapping and fixture approach parameters.
- Local safe-state behavior for network, occupancy, energy, thermal, leak, and contact faults.
- Telemetry bundle for mission, configuration, fault, intervention, and inspection correlation.

## Verification plan

**Table 1. Verification plan — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Area | Evidence | Release threshold | Result |
|---|---|---:|---:|
| Repeated task sequence | 500 laboratory cycles | At least 97% completion | 491 of 500 or 98.2% |
| Tool retention | 200 attach/use/release cycles | Zero uncontrolled releases | 0 |
| Fixture contact | Force-limited approach tests | All within approved envelope | 120 of 120 |
| Chemical compatibility | Coupons and 30-day exposure | No unsafe degradation | Pass with approved products only |
| Safe state | 40 injected faults | 40 of 40 stop/recover as specified | 40 of 40 |
| Serviceability | Replaceable-unit drill | Median repair within 45 minutes | 38 minutes |

## Defect and release control

Every defect links to configuration, evidence, severity, workaround, correction, regression result, and release decision. A mirror-wiping path defect found in pilot week 22 was corrected in the pilot branch, regression-tested for 50 cycles, approved by change control, and released to both serialized robots in week 23.

## Closeout

The manufacturer accepted the v4.4 pilot baseline for the four mapped rooms. General Availability remained blocked by broader chemical compatibility, additional fixture families, long-duration reliability, production cost, and second-source evidence.
