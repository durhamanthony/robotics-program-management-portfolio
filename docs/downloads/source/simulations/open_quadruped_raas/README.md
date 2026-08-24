# MuJoCo Demo - Open-Source Quadruped RaaS Validation Cell

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This generic MuJoCo operations visualization supports Case 03, the productization of an open research quadruped into a supervised-laboratory Robotics-as-a-Service offer. The lab cell contains serialized intake, calibration, functional-test, fault-evidence, replacement-pool, and ready-to-ship stations.

The geometry is intentionally generic. It is not an Open Dynamic Robot Initiative Solo12 model, a vendor digital twin, a locomotion controller, a safety case, or evidence of commercial performance. The purpose is to make the program workflow visible: a controlled source and configuration become a calibrated unit, a fault produces traceable evidence, a replacement rotates into service, and the verified unit returns to the supported pool.

## Run on Windows

From the repository root:

```bat
.venv\Scripts\python.exe simulations\open_quadruped_raas\run_demo.py --viewer --duration 36
```

The headless mode completes without real-time waiting and writes `open_quadruped_raas_telemetry.csv` plus a JSON summary into `outputs/`.
