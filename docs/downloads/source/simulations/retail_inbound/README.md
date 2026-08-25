# Retail Backroom Inbound Receiving — MuJoCo Story Segment

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This model is the inbound half of the Case 01 retail operations story. A full pallet begins visibly supported on the forks inside an open-backed delivery truck. A robot-operated forklift backs the loaded pallet down the ramp, places it in the center receiving zone, and returns into the truck before the humanoid work area is released. One humanoid carries a carton to a ground-level rack. A second humanoid carries a carton up four visible, yellow-edged steps and places it on the raised storage rack.

The browser video then cuts to the order-fulfillment model: robots pull requested merchandise from the storage area, place it on the courtesy drop-off table, and turn toward the shelves. A human associate reaches through the service window with connected, bending arms, removes both packages, turns around, walks away, and disappears from view.

The movement is scripted for workflow communication. It does not validate autonomous unloading, forklift controls, grasp reliability, collision avoidance, stair safety, or any commercial robot's production capability. [DC-L]

## Deterministic checks

`retail_inbound_sequence.py` verifies that the loaded pallet starts on the forks inside the truck, the forklift moves it to the center receiving zone and returns into the truck, the two cartons end on their intended racks, the upper-route height matches each physical tread, and the two humanoid centerlines remain separated.
