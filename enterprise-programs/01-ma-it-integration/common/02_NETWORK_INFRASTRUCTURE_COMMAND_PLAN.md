# Network & Infrastructure Integration — Command Plan

> **Portfolio truth boundary:** Company ABC and Company XYZ are fictional placeholders. Inventory, counts, progress and results are scenario assumptions with low confidence pending discovery and signed test evidence.

## Executive intent

Connect the two companies safely enough to enable approved business flows while keeping untrusted, conflicting, or unassessed environments isolated. “Infrastructure” includes networks, data centers, servers and virtual machines, storage, databases, backup, cloud services, DNS/DHCP/IPAM, Wi‑Fi, VoIP, observability, certificates, service accounts and disaster recovery.

## Scenario checkpoint

| Control | Modeled checkpoint | Acceptance evidence | Status |
|---|---:|---|---|
| Sites securely interconnected | 2 / 3 | Dual-path reachability, monitoring and failover test | Amber |
| Subnet collisions resolved | 4 / 4 | Approved IPAM/NAT/renumber record and route test | Green |
| Tier 0/1 application flows passed | 94 / 97 | Source/destination/port test tied to business owner | Amber |
| Servers/VMs classified | 186 / 214 | Owner, criticality, dependency, backup, disposition | Amber |
| Cloud environments inventoried | 2 / 2 | Account/subscription/project inventory and owner | Green |
| Critical restore tests passed | 11 / 12 | Restore evidence within RTO/RPO | Amber |
| Critical network integrations tested | 16 / 18 | Jira, Slack and monitoring integrations pending | Amber |

## Discovery and target-state controls

Build a current-state inventory covering sites, circuits, carriers, routers, firewalls, SD‑WAN edges, wireless controllers/APs, SSIDs, NAC/802.1X, switches, VLANs, subnets, IPAM, DNS zones/forwarders, DHCP, proxies, load balancers, VPNs, public IPs, certificates, VoIP/PSTN/SBCs, E911, data-center racks, hypervisors, servers, storage, databases, backup, monitoring and cloud resources. Link every item to an owner, location, business service, lifecycle state, contract and disposition.

The architecture decision record selects **coexist, migrate, consolidate, retire or replace** for each domain. Default posture is deny-by-default and least privilege. Cross-entity traffic is enabled only from an approved flow matrix after asset, vulnerability, identity and logging prerequisites are met.

## Network integration runbook

1. Freeze authoritative topology and IP address data; identify overlapping routes and unknown networks.
2. Approve target routing, segmentation, NAT/renumber strategy, DNS trust/forwarding, firewall zones and rollback.
3. Establish redundant IPsec/IKE or SD‑WAN paths with separate failure domains where practical.
4. Apply explicit firewall rules from a business-flow matrix; time-box temporary rules.
5. Validate routing, MTU, latency, packet loss, DNS, NTP, proxy, identity, application flows and monitoring.
6. Test path failover and route withdrawal. Record before/after configurations and restore points.
7. Move sites in controlled waves; maintain command bridge, telemetry, incident thresholds and rollback authority.
8. Standardize hardware, Wi‑Fi and telephony only after coverage, compatibility and business testing.
9. Remove temporary NAT, tunnels, rules, DNS forwarding and admin accounts after convergence approval.

## Server, data-center and compute plan

For every physical server, VM, appliance, database and storage service, record OS/version, CPU/memory/storage, hypervisor/cluster, IP/DNS, owner, application dependencies, identity/service accounts, data classification, criticality, monitoring, patch/vulnerability state, backup policy, last restore test, RTO/RPO, HA/DR design, license/support end, certificate/secrets, CMDB record and target disposition.

Migration waves use discovery → dependency confirmation → remediation → replication/backup → rehearsal → change approval → cutover → functional/performance/security validation → rollback window → decommission certificate. No server is retired until the business owner, application owner, security, backup and CMDB/asset owners sign the evidence.

## Cloud services integration

Inventory AWS accounts, Azure tenants/subscriptions, Google Cloud organizations/folders/projects, SaaS control planes, regions, data residency, connectivity, identity federation, privileged roles, service principals, keys/secrets, KMS, certificates, policies, logs, SIEM feeds, backups, budgets, reservations/commitments, tags, support plans, marketplace contracts and external sharing.

Decide account-by-account whether to isolate, federate, transfer, rebuild, migrate or retire. Align landing zones, guardrails, centralized logging, vulnerability management, network hubs, DNS, identity, backup, incident response, cost allocation and policy-as-code. Test business workloads against security, reliability, performance, operational excellence, cost and sustainability criteria; keep coexistence where transfer risk exceeds value.

## Wi‑Fi, SD‑WAN and VoIP

- **Wi‑Fi:** site survey, RF/capacity baseline, approved AP/controller versions, target SSIDs, 802.1X/NAC, guest isolation, certificates, roaming, warehouse/special-device testing and monitoring.
- **SD‑WAN:** carrier/circuit inventory, overlay design, segmentation, application policy, QoS, HA, orchestrator access, telemetry, failover and hardware lifecycle.
- **VoIP:** DID inventory, carrier porting, SBC/call-manager compatibility, E911/location records, emergency calling, contact-center/call queues, voicemail, recording/retention, QoS, softphones, analog/special devices and rollback.

## Go/no-go and rollback

Go only with signed topology/flow changes, approved security controls, validated monitoring, current backups/config exports, available carrier/vendor support, application-owner test scripts, incident bridge and explicit rollback trigger. Roll back for uncontrolled security exposure, routing instability, critical flow failure, material performance degradation, loss of monitoring, E911 impact or restore failure.

## Reusable template fields

**Sites/data centers/clouds in scope:** [list]  
**Critical services and RTO/RPO:** [list]  
**Subnet collision strategy:** [NAT/renumber/other]  
**Interconnect pattern:** [IPsec/SD‑WAN/private circuit]  
**Flow approval authority:** [role]  
**Server/cloud disposition options:** [list]  
**Wi‑Fi/VoIP target standards:** [details]  
**Test plan and thresholds:** [details]  
**Rollback triggers/steps:** [details]  
**Decommission evidence:** [details]  
