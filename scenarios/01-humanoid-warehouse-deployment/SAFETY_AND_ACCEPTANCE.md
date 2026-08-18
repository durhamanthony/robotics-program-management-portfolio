# Safety and Acceptance Plan

## Safety boundary

The program manager coordinates evidence, owners, gates, and closure. Qualified robot-safety, EHS, engineering, and customer authorities determine applicable standards, perform/approve the risk assessment, validate safety functions, and accept residual risk.

## Hazard themes

Collision/crushing; unstable robot/fall; dropped or ejected cartons; sharp/leaking/hazardous contents; pinch points; trailer/dock gap and uneven surfaces; battery/electrical/thermal hazards; unexpected startup; manual recovery/lifting; forklift/pedestrian interaction; loss of perception/localization/network; unsafe remote command; cybersecurity compromise.

## Acceptance suite

The table below is the Site Acceptance Test (SAT) baseline.

| Test ID | Requirement | Method | Threshold/evidence |
|---|---|---|---|
| SAT-001 | Identity/configuration | Inspect/query | Five serials and approved versions match register |
| SAT-010 | Emergency stop/protective response | Qualified validation | All mandatory functions pass; zero open critical safety findings |
| SAT-020 | Nominal carton handling | Test | At least 225 cartons/hour for two consecutive hours at the approved 2-15 kilogram mix and at least 98% success |
| SAT-030 | Unsupported carton | Test | Safe reject/escalation; no uncontrolled attempt |
| SAT-040 | Dropped carton | Test | Safe stop/recovery workflow and event evidence |
| SAT-050 | Network loss | Test | Enters defined safe state; local safety unaffected |
| SAT-060 | Warehouse Management System/conveyor loss | Test | 10 of 10 approved normal and failure cases enter the defined controlled pause and recovery path |
| SAT-070 | Low battery | Test | Mission completion/abort rule and safe dock behavior |
| SAT-080 | Multi-robot concurrency | Soak | Zero lane/exclusion-zone violations and at least 225 cartons/hour for two hours |
| SAT-090 | Support path | Drill | Three injected alerts meet the 15-minute Severity-1 acknowledgement target with complete evidence |
| SAT-100 | Return to service | Drill | Authorized checklist completed after simulated repair |

## Evidence package

Signed test records, configuration/version export, photos/layout, training evidence, telemetry/MCAP links, defect disposition, risk register and residual-risk acceptance, cutover approval, support drill, and customer acceptance certificate.
