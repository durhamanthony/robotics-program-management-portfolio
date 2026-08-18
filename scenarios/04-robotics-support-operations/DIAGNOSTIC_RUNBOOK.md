# Diagnostic and Troubleshooting Runbook

## First five actions

1. Confirm people/area safety and robot state. Do not restart or remotely move a robot without authorization and a clear area.
2. Identify customer, site, robot serial/model, installed configuration, software/firmware, mission, and exact time window.
3. Describe impact and expected/actual behavior; assign provisional severity.
4. Preserve evidence before changes: MCAP/logs, metrics, faults, relevant video/images under policy, and recent change history.
5. Choose the narrowest safe diagnostic branch and record every action.

## Diagnostic branches

| Symptom | Check | Tool/evidence | Safe escalation |
|---|---|---|---|
| Robot offline | Power, network, device identity, last heartbeat, site outage | Fleet platform, Grafana, edge mgmt, network logs | Field if power/hardware; IT if network; L3 if reproducible software |
| Mission failure | State transitions, localization, perception, planner, payload/environment | MCAP/Foxglove, event log, mission record | L3 with reproduction; ops if envelope violation |
| Joint/actuator fault | Fault code, temperature/current, calibration, load, recent maintenance | Time-series plots, manufacturer diagnostics | Safe stop; qualified field service; RMA/engineering |
| Sensor degradation | Health, obstruction/contamination, timestamps, calibration, environment | Foxglove, images, diagnostics | Suspend dependent mission; field clean/calibrate/replace |
| Battery/charging | State of charge/health, temperature, dock contact, charger/power | Fleet dashboard, charger logs, inspection | Recall/isolate per procedure; field/battery safety owner |
| Software/update issue | Version, rollout ring, signature, config, rollback status | Mender/balena, release record, logs | Freeze rollout, rollback under change authority, L3 defect |
| Repeated alert | Correlation, threshold, version/site concentration | Grafana/fleet analytics, problem record | Problem management and product action |

## Evidence bundle naming

`SITE_ROBOTID_YYYYMMDDThhmmssZ_CORRELATIONID` with manifest, checksums where required, collection method, access classification, retention, and links to case/work order/defect.

## Return to service

Authorized repair/change complete; configuration and serial updated; visual/mechanical inspection; calibration/diagnostic pass; safety-related checks by qualified owner; nominal and fault-recovery test; telemetry/alerts restored; area/customer notified; case evidence and knowledge updated.

