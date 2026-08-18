# MuJoCo Support Lab — Robotics Field-Service Bay

The MuJoCo scene places a faulted quadruped in a field-service bay with a technician, diagnostic laptop, spare module, fault and case lights, and a verification zone. The rendered clip shows physical intake, diagnosis, repair staging, verification, and return to service.

The companion Python lab turns synthetic robot telemetry into a deduplicated case register, severity classification, assignment path, and operational scorecard. Together they demonstrate the physical and information handoffs in Case 04, not remote control of a real fleet.

```bat
.venv\Scripts\python.exe simulations\support_lab\triage.py
```
