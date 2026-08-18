# Cybersecurity and Data Governance

## Minimum control domains

- Asset identity and inventory for robots, compute, sensors, chargers, gateways, and service tools.
- Unique human and machine identities; least privilege; MFA for administrative/remote access.
- Network segmentation, approved ports/protocols, encryption in transit, and certificate/key lifecycle.
- Signed/approved software and configuration releases with rollback and audit records.
- Vulnerability intake, severity, remediation targets, compensating controls, and disclosure process.
- Secure remote diagnostics with customer authorization, session logging, time limits, and emergency revocation.
- Telemetry classification, minimization, retention, access, export, deletion, and customer ownership.
- Privacy review for cameras, audio, location, people detection, license plates, and other identifiable data.
- Incident response, evidence preservation, customer notification, and recovery testing.
- Supplier/subprocessor review and contractual flow-down.

## Required artifacts

Asset/data-flow diagram; threat model; security requirements; access matrix; remote-access SOP; vulnerability register; patch plan; logging/monitoring plan; incident playbook; backup/restore test; privacy impact assessment where applicable; customer security acceptance.

## Deployment gate questions

1. Can every deployed device and privileged identity be identified and revoked?
2. Is production separated from engineering/test access?
3. Can the customer see and approve remote sessions?
4. Are data types, destinations, retention, and support use documented?
5. Can a vulnerable release be contained, rolled back, and proven corrected?
6. Are logs time-synchronized and sufficient for safety, service, and security investigations?

## Public portfolio boundary

Only fictional network values and sanitized telemetry appear publicly. Credentials, customer/site identifiers, serial numbers, exact vulnerabilities, proprietary architecture, and unrestricted raw imagery are excluded.
