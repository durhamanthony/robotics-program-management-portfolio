# Retail Backroom Inbound Receiving — MuJoCo Story Segment

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This model is the inbound half of the Case 01 retail operations story. A full pallet begins inside an open-backed delivery truck. A robot-operated forklift backs down the ramp, places the pallet in the receiving zone, and clears the humanoid work area. One humanoid carries a carton to a ground-level rack. A second humanoid carries a carton up four visible, yellow-edged steps and places it on the raised storage rack.

The browser video then cuts to the existing order-fulfillment model: robots pull requested merchandise from the storage area and place it on the courtesy drop-off table for a sales associate.

The movement is scripted for workflow communication. It does not validate autonomous unloading, forklift controls, grasp reliability, collision avoidance, stair safety, or any commercial robot's production capability. [DC-L]

## Deterministic checks

`retail_inbound_sequence.py` verifies that the pallet starts inside the truck, the forklift moves it out to receiving, the two cartons end on their intended racks, the upper-route height matches each physical tread, and the two humanoid centerlines remain separated.
