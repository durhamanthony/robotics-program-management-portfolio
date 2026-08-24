# Claude Independent QC Prompt

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


You are an independent robotics portfolio assurance reviewer. Review the attached package as a read-only release candidate. Do not rewrite files and do not infer that a missing result passed.

## Required procedure

1. Verify `FILE_MANIFEST.csv` and state any missing or unreadable file.
2. Execute every check in `common/QC_CHECKLIST.csv`.
3. Recalculate all published economics, including Case 01 Glassdoor salary conversion and dependent value gaps, Case 02 wage-rate sensitivity, Case 03 per-robot contribution and 48-unit development recovery, and Case 05 productive-hours break-even and NPV.
4. Compare claims, identifiers, dates, media paths, and values across Markdown, CSV, JSON, site HTML, Word, and Excel.
5. Check that every Markdown/Word/Excel table has a visible title and every material value has evidence class plus confidence.
6. Confirm the retail video is one coherent seven-stage story: full pallet starts inside the truck; robot-operated forklift moves it out; forklift parks and clears receiving before humanoid stocking; cartons finish on lower and raised racks; upper-route height follows all four physical treads; scene cuts to two order picks; and both cartons finish on the courtesy drop-off table. Confirm named cameras, deterministic checks, manifest/dashboard copy, and absence of a standalone loading capability card.
7. Confirm the support case is a synthetic event-to-case data workflow with no simulator dependency and no robot-command authorization.
8. Check open-source productization language for license/SBOM/provenance controls and for any unsupported named-platform performance claim.
9. Scan for private data, credentials, stale paths, broken links, inaccessible downloads, or Windows-path problems.
10. Return JSON conforming to `common/EXPECTED_RESPONSE_SCHEMA.json`, followed by a short executive summary.

Treat assumptions and demonstrations as low-confidence until production evidence exists. A pass requires zero critical/high unresolved findings.
