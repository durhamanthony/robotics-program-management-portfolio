# Phase 2 24-Hour Operating Plan

## Service objective

Provide scheduled restroom service across a continuously operating terminal without claiming that either robot works continuously. Two robots are staggered so charging, maintenance, and exception recovery do not remove all fleet capacity at once.

## Daily demand model

| Service class | Rooms | Frequency | Standard time | Daily hours |
|---|---:|---:|---:|---:|
| Short service visit | 12 | 8 per room | 10 minutes | 16 |
| Deep clean | 12 | 2 per room | 30 minutes | 12 |
| **Total productive fleet time** |  |  |  | **28** |

Short visits cover approved fixture touch-up, dispensers, visible litter, waste-bin status, and inspection evidence. Deep cleans cover the full approved fixture and floor sequence. Prohibited contamination always transfers to trained human responders.

## Staggered coverage

| Window | Robot A | Robot B | Operations control |
|---|---|---|---|
| 00:00–06:00 | Deep cleans and low-demand rooms | Charge, maintenance, then short visits | Duty supervisor releases rooms |
| 06:00–12:00 | Short visits and replenishment | Short visits, charge as scheduled | Passenger peaks drive closure timing |
| 12:00–18:00 | Charge, inspection support, then short visits | Short visits and approved deep cleans | Dispatch adjusts to flight bank |
| 18:00–24:00 | Short visits and deep cleans | Charge, maintenance, then service | Overnight reset and evidence review |

The table is an operating pattern, not a minute-by-minute dispatch plan. The fleet scheduler must preserve 28 productive hours while respecting charger state, room availability, travel, preventive maintenance, and safe-stop recovery.

## Human authority retained

- Verify the room is closed and empty before release.
- Select and control chemicals and Safety Data Sheets.
- Respond to sharps, blood, vomit, unknown substances, smoke, standing water, or aggressive behavior.
- Inspect work, order corrective cleaning, and reopen the room.
- Refill locked consumables and approve recipe or route changes.
- Take over when remote recovery fails or a robot blocks an egress path.

## Performance dashboard

| Measure | Conditional threshold | Evidence |
|---|---:|---|
| Productive fleet utilization | At least 28 hours/day | Dispatch and mission logs |
| Scheduled availability | At least 85% | Robot-ready hours ÷ scheduled hours |
| Mission completion | At least 95% | Completed ÷ released missions |
| First-pass inspection | At least 90% | Custodial checklist sample |
| Supply accuracy | At least 98% | Requested versus delivered quantity |
| Uncontrolled public entry | 0 | Entry-control and incident record |
| Prohibited-condition contact | 0 | Exception and safe-stop record |

## Approved adjacency backlog

Restroom cleaning remains the anchor workload. If the 12-room schedule has unused capacity, the change-control board may test supply-cart loading and delivery, paper and soap replenishment, waste movement, spill-response support, facilities inspection, lost-item transfer, overnight concession supply movement, and nontechnical condition reporting. Each task requires its own route, payload, safety, privacy, acceptance, and economic review.

