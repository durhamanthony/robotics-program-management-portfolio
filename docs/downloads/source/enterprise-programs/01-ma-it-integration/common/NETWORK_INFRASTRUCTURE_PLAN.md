# M&A Network and Infrastructure Integration Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Create secure, observable connectivity without introducing route, DNS, segmentation, or perimeter failures.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Discovery | Three sites, two cloud environments, four overlapping subnets identified | Network Lead | Validated L2/L3, WAN, DNS, DHCP, firewall, Wi-Fi, VoIP inventory |
| Interconnect | Redundant IPsec/IKE site-to-site tunnels with restricted routes | Network Architect | Tunnel, failover, latency, throughput tests |
| Collision remediation | NAT/renumber plan for four conflicts; no overlapping routes advertised | Network Lead | Approved address plan |
| Segmentation | Default deny; user, server, management, guest, voice, and migration zones | Security | Firewall rule review |
| Observability | Flow, DNS, firewall, VPN, and availability telemetry routed to Company ABC | Network Operations | Dashboard and alert test |

## Execution sequence

1. Discover topology, circuits, public IPs, routes, subnets, VLANs, DNS zones/forwarders, firewalls, Wi-Fi, voice, certificates, and cloud gateways.
2. Classify required flows by application, source, destination, port/protocol, data class, owner, duration, and removal date.
3. Resolve address collisions before route exchange; validate forward and reverse DNS and split-horizon behavior.
4. Build redundant tunnels and deny-by-default rules in a non-production path; enable monitoring before traffic.
5. Pilot business flows, failure/failback, bandwidth, packet loss, name resolution, and security detections.
6. Enable production by site; reconcile rules and routes; remove temporary migration access after acceptance.

## Acceptance evidence

- [ ] Zero unresolved overlapping routes at go/no-go; all four collision plans are tested.
- [ ] Tier 0/Tier 1 flows pass functional, failover, logging, and owner acceptance tests.
- [ ] Every temporary firewall rule has an owner, ticket, purpose, expiry, and removal evidence.
- [ ] Network Operations accepts diagrams, configurations, monitoring, backup, vendor, and incident procedures.

## Exception, rollback, and escalation

Immediately withdraw new routes and disable the affected tunnel/rule set for asymmetric routing, unapproved lateral movement, unresolved DNS corruption, or Sev 1 performance impact. Restore the prior path, keep evidence, and reconvene the technical design authority. Rollback checkpoints are defined per site and per rule group—not as one all-or-nothing instruction.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `topology / circuit inventory`
- `IP address and collision plan`
- `required flow matrix`
- `DNS/DHCP design`
- `segmentation`
- `firewall rules and expiry`
- `VPN/SD-WAN design`
- `monitoring`
- `test scripts`
- `rollback and operations acceptance`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
