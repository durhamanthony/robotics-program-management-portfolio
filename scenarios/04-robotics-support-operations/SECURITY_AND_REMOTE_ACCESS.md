# Security and Remote Access — Robotics Support

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Control objectives

- Unique device and named-user identity; no shared support accounts.
- Least privilege, MFA, just-in-time/approved elevation and rapid revocation.
- Segmented path through an approved broker/gateway; no direct public robot-control exposure.
- Encrypted transport, device trust and controlled certificate/key lifecycle.
- Command allowlist, safety interlocks and site confirmation for consequential actions.
- Complete session, command, configuration, file-transfer and approval audit.
- Signed updates, release rings, health checks, rollback and version inventory.

## Session workflow

Linked case and business reason → verify entitlement/site/robot/safety state → customer/site approval when required → time-bounded access → record/session audit → approved diagnostics → no safety-control bypass → revoke/close → attach evidence and actions to case.

## Prohibited practices

Personal remote-access accounts for production, reused credentials, unattended permanent elevation, copying sensitive logs to unapproved devices, unreviewed scripts/commands, modifying safety configuration through a support shortcut, or using a noncommercial/free license outside its terms.

## Review

Security architecture and threat model before rollout; access review at least quarterly and after role/contract changes; alerting for anomalous sessions; incident exercise; supplier-access control; retention and customer data terms; tested break-glass and revocation.
