# Observability and Data Plan — Robotics Support

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Evidence layers

**Table 1. Evidence layers — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Layer | Examples | Primary use |
|---|---|---|
| Robot/mission | State, mission, localization, component health, battery, safety state | Diagnose robot behavior and availability |
| High-fidelity event | MCAP/log window, sensor/joint/event timeline | Reproduce and correlate complex failures |
| Edge/site | Compute, storage, network, clock, certificates, services | Separate robot vs infrastructure causes |
| Fleet/service | Availability, mission success, version, alerts, interventions | Operations and reliability trends |
| Customer workflow | Throughput, patrols, acceptance/business outcome | Customer value and impact |

## Minimum event contract

`timestamp`, `robot_id`, `model`, `site_id`, `software_version`, `configuration_id`, `mission_id`, `operational_state`, `battery_pct`, `network`, `component`, `fault_code`, `severity`, `safety_state`, `location_or_zone`, `correlation_id`, and linked `support_case_id` when present.

## Alert design

Alert only when an actionable condition, owner and response exist. Define trigger, deduplication/suppression, severity, runbook, routing, maintenance mode, stale/no-data behavior, customer effect, and validation. Track precision, recall, alert-to-case conversion and repeated noise.

## Governance

Define ownership, purpose, minimization, consent/notice where applicable, retention, access, encryption, region, export, deletion, incident response and data quality. Use synthetic/redacted data in the public portfolio. Screenshots are supplementary; raw evidence and queries must be reproducible.
