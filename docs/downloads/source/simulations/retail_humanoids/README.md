# MuJoCo Demo — Retail Backroom Inbound and Fulfillment

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This MuJoCo operations visualization mirrors the expanded Case 01 flow in one 40-second clip. The first model, documented in [`../retail_inbound/README.md`](../retail_inbound/README.md), begins with a loaded pallet visibly supported on a forklift inside a delivery truck. The robot-operated forklift backs the pallet into the center receiving zone, releases it, and returns into the truck. Two humanoids then stock ground and raised racks; the upper-route robot carries its carton up four visible, yellow-edged steps. The clip then cuts to this order-fulfillment model, where two robots pull requested cartons from different stock levels, place them on the courtesy drop-off table, and turn toward the shelves. A clearly human sales associate with a face, torso, connected upper arms, bending elbows, forearms, hands, and fingers reaches through the staffed service window, collects both packages, turns around, walks away, and disappears from view to complete the custody cycle.

The models demonstrate state ownership, forklift-to-humanoid work-zone separation, distinct item movements, stair-linked height changes, order-picking, courtesy drop-off, robot turn-away, human pickup, package removal, and deterministic route checks. Eight on-video stage labels make the sequence explicit. They do not claim that a commercial robot can autonomously perform these tasks, and they are not dynamics, grasp, collision-avoidance, forklift-control, stair-safety, or certified-control validation. [DC-L]

## Windows run

From the repository folder:

```bat
.venv\Scripts\python.exe simulations\retail_humanoids\run_demo.py --viewer --duration 36
```

The browser-playable portfolio video is composed from `../retail_inbound/retail_inbound.xml` and `retail.xml`. Motion is scripted for program-workflow communication and is not locomotion, grasp, forklift-control, or safety-performance validation.
