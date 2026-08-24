# Open-Source Compliance and SBOM Plan

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Control objective

Ship a reproducible commercial service while preserving every applicable copyright notice, license condition, source/binary redistribution obligation, security record, and non-endorsement boundary. "Open source" is not treated as a single license or as permission to ignore third-party dependencies.

## Release controls

**Table 1. Open-source release controls - Evidence: control design [SA-L], source statements [PB-H]; Confidence: see evidence key and row/source notes**

| Control | Owner | Gate evidence |
|---|---|---|
| Approved component and license inventory | Product Security | SBOM, component hash, version, supplier, license, relationship, and generation context |
| Copyright and notice preservation | Legal / Release Manager | Binary notice bundle and source-offer decision where applicable |
| Upstream-to-fork traceability | Software Lead | Upstream commit, provider patch set, customer configuration, and signed release tag |
| Dependency exception | Architecture Review Board | Written disposition before merge or shipment |
| Vulnerability intake and response | Product Security | Advisory intake, severity, affected releases, mitigation, and customer notice |
| Reproducible build | Release Engineering | Clean build from pinned sources and retained artifacts |
| No endorsement claim | Product / Legal | Approved name, attribution, and marketing review |

## Minimum release packet

Each release contains the signed image, hardware/configuration manifest, SBOM, license and notice bundle, build provenance, known issues, security fixes, calibration version, rollback target, test result, change approval, and customer-facing release note. CISA's 2026 SBOM minimum-elements publication and NIST Secure Software Development Framework are planning references, not certifications.
