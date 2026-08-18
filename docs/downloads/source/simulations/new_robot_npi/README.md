# MuJoCo Demo — AD-01 Autonomous Tote Transfer Robot

AD-01 means Autonomous Delivery, product concept 01. It is the fictional product developed in Case 03, not a real vendor or commercial model. The product is a compact wheeled mobile manipulator designed to move one approved tote weighing no more than 15 kilograms along an 18-meter indoor route between two fixed stations.

The MuJoCo model contains six actuated degrees of freedom: planar X and Y travel, yaw, shoulder, elbow, and wrist. It shows the bounded product workflow used through customer discovery, Engineering Verification Test, Design Verification Test, Production Validation Test, first-customer deployment, and the release decision. The rendered clip is a product-workflow visualization, not proof of autonomous grasping, navigation safety, or production performance.

```bat
.venv\Scripts\python.exe simulations\new_robot_npi\run_demo.py --viewer
```
