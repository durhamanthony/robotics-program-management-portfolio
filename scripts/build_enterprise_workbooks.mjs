import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = process.env.PORTFOLIO_ROOT
  ? path.resolve(process.env.PORTFOLIO_ROOT)
  : path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const qaRoot = path.join(root, "qa", "xlsx-enterprise");
await fs.mkdir(qaRoot, { recursive: true });

const C = {
  navy: "#07352B", blue: "#17627D", teal: "#12A594", pale: "#E8F3F5",
  white: "#FFFFFF", ink: "#17212B", muted: "#5B6670", border: "#CBD5E1",
  green: "#E6F4EA", amber: "#FFF0CE", red: "#FCE8E6",
};
const truth = "Experience-informed fictional Company ABC/XYZ case. Scenario quantities, dates, costs, and results are assumptions; replace with approved source records before use.";

function colName(n) {
  let s = "";
  while (n) { const r = (n - 1) % 26; s = String.fromCharCode(65 + r) + s; n = Math.floor((n - 1) / 26); }
  return s;
}

function title(sheet, columns, text) {
  const end = colName(columns);
  sheet.getRange(`A1:${end}1`).merge();
  sheet.getRange("A1").values = [[text]];
  sheet.getRange(`A1:${end}1`).format = { fill: C.navy, font: { bold: true, color: C.white, size: 15 }, rowHeight: 30, verticalAlignment: "center" };
  sheet.getRange(`A2:${end}2`).merge();
  sheet.getRange("A2").values = [[truth]];
  sheet.getRange(`A2:${end}2`).format = { fill: C.pale, font: { color: C.muted, italic: true, size: 9 }, wrapText: true, rowHeight: 30 };
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(4);
}

function addTable(wb, spec) {
  const sheet = wb.worksheets.add(spec.name);
  title(sheet, spec.headers.length, spec.title);
  const end = colName(spec.headers.length);
  sheet.getRange(`A4:${end}4`).values = [spec.headers];
  sheet.getRange(`A4:${end}4`).format = { fill: C.blue, font: { bold: true, color: C.white, size: 9 }, wrapText: true, rowHeight: 28 };
  if (spec.rows.length) {
    sheet.getRange(`A5:${end}${4 + spec.rows.length}`).values = spec.rows;
    sheet.getRange(`A5:${end}${4 + spec.rows.length}`).format = { font: { color: C.ink, size: 9 }, wrapText: true, verticalAlignment: "top", borders: { insideHorizontal: { style: "thin", color: C.border }, insideVertical: { style: "thin", color: C.border }, bottom: { style: "thin", color: C.border } } };
    const tbl = sheet.tables.add(`A4:${end}${4 + spec.rows.length}`, true, spec.tableName);
    tbl.style = "TableStyleMedium2";
    tbl.showBandedRows = true;
  }
  (spec.widths || []).forEach((w, i) => { sheet.getRange(`${colName(i + 1)}:${colName(i + 1)}`).format.columnWidth = w; });
  for (const [range, fmt] of Object.entries(spec.numberFormats || {})) sheet.getRange(range).format.numberFormat = fmt;
  for (const v of spec.validations || []) sheet.getRange(v.range).dataValidation = { rule: { type: "list", values: v.values } };
  return sheet;
}

function kpiBlock(sheet, range, labels, formulas, formats = []) {
  const [left, right] = range.split(":");
  sheet.getRange(`${left}:${right}`).format = { fill: C.white, borders: { insideHorizontal: { style: "thin", color: C.border }, insideVertical: { style: "thin", color: C.border }, bottom: { style: "thin", color: C.border } } };
  const startCol = left.match(/[A-Z]+/)[0];
  const startRow = Number(left.match(/\d+/)[0]);
  const valueCol = colName(startCol.charCodeAt(0) - 64 + 1);
  sheet.getRange(`${startCol}${startRow}:${startCol}${startRow + labels.length - 1}`).values = labels.map(v => [v]);
  sheet.getRange(`${valueCol}${startRow}:${valueCol}${startRow + formulas.length - 1}`).formulas = formulas.map(v => [v]);
  formats.forEach((f, i) => { if (f) sheet.getRange(`${valueCol}${startRow + i}`).format.numberFormat = f; });
}

function dashboard(wb, spec) {
  const s = wb.worksheets.add(spec.name);
  title(s, 12, spec.title);
  s.freezePanes.freezeRows(3);
  s.getRange("A4:B4").values = [[spec.kpiTitle, "VALUE"]];
  s.getRange("D4:E4").values = [["CONTROL", "VALUE"]];
  for (const r of ["A4:B4", "D4:E4"]) s.getRange(r).format = { fill: C.blue, font: { bold: true, color: C.white } };
  kpiBlock(s, "A5:B8", spec.kpis.slice(0, 4).map(x => x[0]), spec.kpis.slice(0, 4).map(x => x[1]), spec.kpis.slice(0, 4).map(x => x[2]));
  kpiBlock(s, "D5:E8", spec.kpis.slice(4, 8).map(x => x[0]), spec.kpis.slice(4, 8).map(x => x[1]), spec.kpis.slice(4, 8).map(x => x[2]));
  s.getRange("A10:H10").merge();
  s.getRange("A10").values = [[spec.decision]];
  s.getRange("A10:H10").format = { fill: C.amber, font: { bold: true, color: C.navy }, wrapText: true, rowHeight: 34 };
  s.getRange("A12:H12").values = [["Dimension", "Current evidence", "Threshold", "State", "Owner", "Decision / action", "Source", "Confidence"]];
  s.getRange("A13:H16").values = spec.controls;
  s.getRange("A12:H16").format = { wrapText: true, font: { size: 9, color: C.ink }, borders: { insideHorizontal: { style: "thin", color: C.border }, insideVertical: { style: "thin", color: C.border }, bottom: { style: "thin", color: C.border } } };
  s.getRange("A12:H12").format = { fill: C.blue, font: { bold: true, color: C.white, size: 9 }, wrapText: true };
  const dt = s.tables.add("A12:H16", true, spec.tableName); dt.style = "TableStyleMedium2";
  s.getRange("J4:K4").values = [[spec.chartHeaders[0], spec.chartHeaders[1]]];
  s.getRange("J5:J9").values = spec.chartLabels.slice(0, 5).map(x => [x]);
  s.getRange("K5:K9").formulas = spec.chartFormulas.slice(0, 5).map(x => [x]);
  const chart = s.charts.add("bar", s.getRange("J4:K9"));
  chart.title = spec.chartTitle; chart.hasLegend = false; chart.setPosition("A18", "H33");
  s.getRange("A:A").format.columnWidth = 23; s.getRange("B:B").format.columnWidth = 17;
  s.getRange("C:C").format.columnWidth = 22; s.getRange("D:D").format.columnWidth = 17;
  s.getRange("E:E").format.columnWidth = 19; s.getRange("F:F").format.columnWidth = 27;
  s.getRange("G:G").format.columnWidth = 22; s.getRange("H:H").format.columnWidth = 15;
  s.getRange("J:K").format.columnWidth = 16;
  return s;
}

async function renderAndSave(wb, outPath, qaDir) {
  await fs.mkdir(path.dirname(outPath), { recursive: true });
  await fs.mkdir(qaDir, { recursive: true });
  const names = wb.worksheets.items.map(s => s.name);
  for (const sheetName of names) {
    const png = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
    await fs.writeFile(path.join(qaDir, `${sheetName.replaceAll("/", "-")}.png`), new Uint8Array(await png.arrayBuffer()));
  }
  const file = await SpreadsheetFile.exportXlsx(wb); await file.save(outPath);
  try { await fs.rename(`${outPath}.inspect.ndjson`, path.join(qaDir, `${path.basename(outPath)}.inspect.ndjson`)); } catch (e) { if (e.code !== "ENOENT") throw e; }
}

function buildMa() {
  const wb = Workbook.create();
  addTable(wb, { name: "Instructions", title: "M&A integration workbook instructions", headers: ["Step", "Action", "Control", "Evidence"], rows: [
    [1, "Replace scenario assumptions with authorized deal records.", "Do not type over dashboard formulas.", "Signed charter and source exports"],
    [2, "Reconcile roster, identity, device, app, content, contract, and site denominators.", "Unknown or unowned exceptions block affected release.", "Dated reconciliation package"],
    [3, "Update registers first; dashboards summarize them.", "A tool success message is not acceptance.", "Counts, samples, permissions, workflows"],
    [4, "Export a dated decision pack at each gate or Sprint review.", "Human approvers retain decision authority.", "Signed decision log"],
  ], widths: [8, 44, 42, 38], tableName: "MaInstructions" });
  addTable(wb, { name: "Assumptions", title: "Scenario assumptions and truth boundary", headers: ["ID", "Variable", "Value", "Unit", "Class", "Validation", "Owner", "State"], rows: [
    ["MA-A-001", "Workers", 680, "people", "Scenario assumption", "Reconcile HR rosters at T-10/T-3/T-0", "HR/Identity Lead", "Modeled"],
    ["MA-A-002", "Endpoints", 745, "devices", "Scenario assumption", "Reconcile MDM/CMDB/procurement", "Endpoint Lead", "Modeled"],
    ["MA-A-003", "Applications", 142, "apps", "Scenario assumption", "SSO/finance/CASB/interviews", "App Lead", "Modeled"],
    ["MA-A-004", "Authorized budget", 1860000, "USD", "Scenario assumption", "Finance-approved baseline", "Finance Lead", "Modeled"],
  ], widths: [14, 25, 15, 14, 22, 45, 20, 15], numberFormats: { "C8": "$#,##0" }, tableName: "MaAssumptions" });
  addTable(wb, { name: "RAID", title: "M&A RAID and decision register", headers: ["ID", "Type", "Statement", "P", "I", "Score", "Response", "Owner", "Due", "Status", "Trigger"], rows: [
    ["MA-R-001", "Risk", "Identity duplicates or stale contractors create access failures.", 4, 5, 20, "T-10/T-3/T-0 reconcile; disable destinations until release.", "Identity Lead", "2026-09-04", "Open", "Mismatch >1%"],
    ["MA-R-002", "Risk", "Overlapping subnets disrupt routing or DNS.", 3, 5, 15, "NAT/renumber; isolate; validate route withdrawal.", "Network Lead", "2026-09-11", "Watching", "Unresolved collision"],
    ["MA-R-003", "Risk", "Collaboration permissions, holds, or integrations differ.", 3, 5, 15, "Identity-first mapping; legal review; pilot and reconcile.", "Collab Lead", "2026-09-18", "Open", "Variance <99.5%"],
    ["MA-I-004", "Issue", "Fifteen Day 1 readiness exceptions remain.", 3, 5, 15, "Named workaround, owner, expiry, and daily burn-down.", "Day 1 Lead", "2026-09-28", "Open", "Exception unowned"],
  ], widths: [14, 13, 42, 8, 8, 10, 42, 20, 15, 15, 30], validations: [{ range: "J5:J100", values: ["Open", "Watching", "Closed"] }], tableName: "MaRaid" });
  addTable(wb, { name: "Day1", title: "Day 1 worker readiness by cohort", headers: ["Cohort", "Population", "Fully ready", "Authentication", "Exceptions", "Owner", "Evidence", "State"], rows: [
    ["HQ Site A", 280, 272, 276, 8, "Site Lead A", "Roster/device/access/support", "Conditional"],
    ["Office Site B", 190, 186, 188, 4, "Site Lead B", "Roster/device/access/support", "Conditional"],
    ["Office Site C", 110, 107, 110, 3, "Site Lead C", "Roster/device/access/support", "Conditional"],
    ["Remote", 100, 100, 100, 0, "Remote Lead", "Courier/virtual support", "Ready"],
    ["Total", 680, 665, 674, 15, "Day 1 Lead", "Formula check", "Conditional"],
  ], widths: [20, 14, 16, 17, 14, 20, 34, 16], tableName: "MaDay1" });
  addTable(wb, { name: "Applications", title: "Application rationalization decisions", headers: ["App", "Tier", "Users", "Company ABC", "Company XYZ", "Disposition", "Owner", "Contract action", "Exit evidence", "State"], rows: [
    ["Identity directory", 0, 680, "Target", "Source", "Migrate/converge", "Identity Lead", "Retain bridge temporarily", "Roster/access/log tests", "In progress"],
    ["Productivity suite", 0, 610, "Google Workspace", "Google Workspace", "Cross-domain migrate", "Collab Lead", "Consolidate licensing", "Count/sample/permission acceptance", "Pilot"],
    ["Messaging", 1, 520, "Slack Enterprise", "Slack", "Consolidate", "Collab Lead", "Retire source contract", "Channel/history/app acceptance", "Pilot"],
    ["Work management", 1, 280, "Asana", "Asana", "Migrate projects", "Business Apps", "Consolidate", "Project/task/field reconciliation", "Planned"],
    ["Engineering work", 0, 190, "Jira", "Jira", "Migrate after defect fix", "Engineering Apps", "Consolidate", "Group/workflow regression", "Hold"],
  ], widths: [24, 9, 12, 22, 22, 24, 20, 25, 38, 16], tableName: "MaApps" });
  addTable(wb, { name: "Migration Validation", title: "Collaboration and data migration validation", headers: ["Platform", "Cohort", "Source objects", "Target objects", "Reconciled %", "Permissions", "Integrations", "Business test", "Decision", "Evidence owner"], rows: [
    ["Google Workspace", "Pilot", 125000, 124625, 0.997, "Pass", "Pass", "Pass", "Accept pilot", "Collab Lead"],
    ["Slack", "Pilot", 286, 284, 0.993, "Pass", "2 defects", "Conditional", "Hold affected channels", "Collab Lead"],
    ["Asana", "Pilot", 8200, 8175, 0.997, "Pass", "Pass", "Pass", "Accept pilot", "Business Apps"],
    ["Jira", "Pilot", 6400, 6320, 0.988, "Group variance", "Automation defect", "Fail", "Hold production", "Engineering Apps"],
  ], widths: [22, 16, 17, 17, 17, 16, 20, 18, 25, 20], numberFormats: { "E5:E8": "0.0%" }, tableName: "MaValidation" });
  addTable(wb, { name: "Budget", title: "M&A cost baseline and forecast", headers: ["Control account", "Baseline", "Forecast", "Actual to date", "ETC", "Variance", "Owner", "Evidence"], rows: [
    ["Day 1 / endpoints", 420000, 398000, 205000, 193000, null, "Day 1 Lead", "PO/invoice/forecast"],
    ["Network / infrastructure", 365000, 354000, 144000, 210000, null, "Network Lead", "PO/invoice/forecast"],
    ["Collaboration migration", 510000, 498000, 221000, 277000, null, "Collab Lead", "Vendor SOW + forecast"],
    ["Application rationalization", 280000, 267000, 94000, 173000, null, "App Lead", "Work packages"],
    ["Change / support / reserve", 285000, 265000, 101000, 164000, null, "Program Lead", "Labor/reserve log"],
  ], widths: [28, 18, 18, 18, 18, 18, 20, 34], numberFormats: { "B5:F9": "$#,##0;[Red]-$#,##0" }, tableName: "MaBudget" });
  const b = wb.worksheets.getItem("Budget"); b.getRange("F5").formulas = [["=B5-C5"]]; b.getRange("F5:F9").fillDown();
  addTable(wb, { name: "Sources", title: "Primary-source research register", headers: ["Publisher", "Source", "URL", "Use", "Accessed", "Authority"], rows: [
    ["PMI", "PMBOK Guide Eighth Edition", "https://www.pmi.org/standards/pmbok", "Principles, domains, tailoring", "2026-08-25", "Primary"],
    ["PMI", "Process Groups: A Practice Guide", "https://www.pmi.org/standards/process-groups", "Predictive lifecycle", "2026-08-25", "Primary"],
    ["PMI", "Agile Practice Guide", "https://www.pmi.org/standards/agile", "Adaptive delivery", "2026-08-25", "Primary"],
    ["NIST", "Cybersecurity Framework 2.0", "https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20", "Security outcomes", "2026-08-25", "Primary"],
    ["Microsoft", "Multi-tenant M&A scenarios", "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/multi-tenant/scenarios", "Tenant integration", "2026-08-25", "Primary"],
    ["Google", "Google Workspace migration", "https://workspace.google.com/solutions/migration/", "Workspace planning", "2026-08-25", "Primary"],
    ["Slack", "Migrate workspaces", "https://slack.com/help/articles/115002532808-Migrate-workspaces-to-an-Enterprise-organization", "Workspace consolidation", "2026-08-25", "Primary"],
  ], widths: [18, 36, 66, 34, 15, 15], tableName: "MaSources" });
  addTable(wb, { name: "Template Blank", title: "Reusable blank register", headers: ["ID", "Item", "Owner", "Due", "State", "Acceptance", "Evidence", "Decision", "Notes"], rows: [["[ENTER]", "[ENTER]", "[ENTER]", "[ENTER]", "[ENTER]", "[ENTER]", "[LINK]", "[ENTER]", "[ENTER]"]], widths: [14, 35, 20, 15, 15, 35, 28, 25, 35], tableName: "MaBlank" });
  dashboard(wb, { name: "Agile Dashboard", title: "M&A IT Integration — Agile Dashboard", kpiTitle: "OUTCOME", tableName: "MaAgileControls",
    kpis: [["Day 1 ready", "=Day1!C9/Day1!B9", "0.0%"], ["Authentication", "=Day1!D9/Day1!B9", "0.0%"], ["Open RAID", "=COUNTIF(RAID!J5:J100,\"Open\")", "0"], ["Held apps", "=COUNTIF(Applications!J5:J100,\"Hold\")", "0"], ["Pilot reconciliation", "=AVERAGE('Migration Validation'!E5:E8)", "0.0%"], ["Forecast", "=SUM(Budget!C5:C9)", "$#,##0"], ["Forecast variance", "=SUM(Budget!F5:F9)", "$#,##0"], ["Sprints", "=10", "0"],
    ], decision: "Decision: keep Jira production cohort on hold; continue accepted Google Workspace and Asana increments; close all 15 Day 1 exceptions with named expiry.", controls: [["Day 1", "665/680 ready", ">=99% or owned workaround", "Conditional", "Day 1 Lead", "Daily exception burn-down", "Day1", "Scenario"], ["Identity", "674/680 authenticated", ">=99%", "Pass", "Identity Lead", "Monitor temporary bridge expiry", "Day1", "Scenario"], ["Migration", "Jira workflow failed", ">=99.5% plus workflow pass", "Hold", "App Lead", "Fix group/automation mapping", "Migration Validation", "Scenario"], ["Finance", "$1.782M forecast", "Within $1.86M", "Favorable", "Finance Lead", "Protect quality gates", "Budget", "Scenario"]], chartHeaders: ["Cohort", "Ready"], chartLabels: ["HQ A", "Site B", "Site C", "Remote", "Total"], chartFormulas: ["=Day1!C5", "=Day1!C6", "=Day1!C7", "=Day1!C8", "=Day1!C9"], chartTitle: "Day 1 fully ready by cohort" });
  dashboard(wb, { name: "Predictive Dashboard", title: "M&A IT Integration — Predictive / Waterfall Dashboard", kpiTitle: "BASELINE", tableName: "MaPredControls",
    kpis: [["SPI", "=0.97", "0.00"], ["CPI", "=1.02", "0.00"], ["Forecast", "=SUM(Budget!C5:C9)", "$#,##0"], ["VAC", "=SUM(Budget!F5:F9)", "$#,##0"], ["Open RAID", "=COUNTIF(RAID!J5:J100,\"Open\")", "0"], ["Held apps", "=COUNTIF(Applications!J5:J100,\"Hold\")", "0"], ["Gate week", "=12", "0"], ["Completion week", "=24", "0"],
    ], decision: "Decision: approve conditional Gate 4 only for accepted migration packages; Jira work package remains held under integrated change and quality control.", controls: [["Scope", "142 apps discovered", "100% owner/disposition", "Watch", "App Lead", "Resolve five Tier 2 owners", "Applications", "Scenario"], ["Schedule", "SPI 0.97", ">=0.95", "Watch", "Program Lead", "Protect critical path", "IMS", "Scenario"], ["Quality", "Jira pilot failed", "Workflow regression pass", "Hold", "Quality Lead", "Correct and retest", "Migration Validation", "Scenario"], ["Cost", "CPI 1.02", ">=0.95", "Favorable", "Finance Lead", "Maintain reserve", "Budget", "Scenario"]], chartHeaders: ["Account", "Forecast"], chartLabels: ["Day 1", "Network", "Collab", "Apps", "Change"], chartFormulas: ["=Budget!C5", "=Budget!C6", "=Budget!C7", "=Budget!C8", "=Budget!C9"], chartTitle: "Forecast by control account" });
  return wb;
}

function buildHardware() {
  const wb = Workbook.create();
  addTable(wb, { name: "Instructions", title: "Hardware refresh workbook instructions", headers: ["Step", "Action", "Control", "Evidence"], rows: [
    [1, "Replace Company ABC assumptions with authorized device, user, site, and financial records.", "Keep one serial-level source of truth.", "CMDB/MDM/procurement/HR exports"],
    [2, "Update inventory, wave, data, security, return, and sanitization registers.", "A handed-out device is not Done.", "User/task/security/asset acceptance"],
    [3, "Use method dashboards for delivery control; use Portfolio Summary for governance.", "No competing denominators or shadow plans.", "Dated reconciliation pack"],
    [4, "Quarantine missing serial, hold release, or sanitization evidence.", "Invoice alone never closes custody.", "Chain-of-custody record"],
  ], widths: [8, 48, 42, 40], tableName: "HwInstructions" });
  addTable(wb, { name: "RAID", title: "Hardware refresh RAID register", headers: ["ID", "Type", "Statement", "P", "I", "Score", "Response", "Owner", "Due", "Status", "Trigger"], rows: [
    ["HW-R-003", "Risk", "Critical app, driver, VPN, or peripheral failure.", 4, 4, 16, "Persona pilot, versioned package, fallback.", "App Lead", "2026-09-11", "Open", "Tier 0/1 test fails"],
    ["HW-R-002", "Risk", "Local or application data is not protected.", 3, 5, 15, "Precheck, KFM/backup, validation, sanitization hold.", "Data Lead", "2026-09-18", "Open", "Unknown local data"],
    ["HW-I-005", "Issue", "Sixteen accessibility, leave, app, or logistics exceptions remain.", 3, 5, 15, "Owner, new date, workaround, specialized capacity.", "Wave Lead", "2026-10-16", "Open", "Exception unowned"],
    ["HW-R-004", "Risk", "Custody or sanitization evidence gap.", 2, 5, 10, "Scan custody, secure storage, validate, quarantine.", "Asset Lead", "2026-10-23", "Watching", "Unknown serial"],
  ], widths: [14, 13, 42, 8, 8, 10, 42, 20, 15, 15, 30], tableName: "HwRaid" });
  addTable(wb, { name: "Inventory", title: "Serial-level device inventory and disposition", headers: ["Asset ID", "Device type", "Site", "Persona", "Old serial", "New serial", "Assigned user", "Build", "Wave", "State", "Final disposition"], rows: [
    ["ABC-0001", "Laptop", "Site A", "Standard", "OLD-0001", "NEW-0001", "Worker 001", "W11.2", "Pilot", "Accepted", "Return received"],
    ["ABC-0002", "Laptop", "Site A", "Developer", "OLD-0002", "NEW-0002", "Worker 002", "W11.2-DEV", "Site A", "Accepted", "Return received"],
    ["ABC-0003", "Desktop", "Site B", "Specialized", "OLD-0003", "NEW-0003", "Worker 003", "W11.2-SP", "Site B", "Exception", "Pending"],
    ["ABC-0004", "Phone", "Remote", "Mobile", "OLD-0004", "NEW-0004", "Worker 004", "MDM-4.2", "Remote/all", "Accepted", "Carrier return"],
  ], widths: [16, 17, 16, 20, 18, 18, 20, 17, 16, 16, 22], tableName: "HwInventory" });
  addTable(wb, { name: "App Readiness", title: "Application and persona readiness", headers: ["App", "Tier", "Persona", "Packaging", "License", "Task test", "Fallback", "Owner", "State", "Evidence"], rows: [
    ["Identity/VPN", 0, "All", "Versioned", "Ready", "Pass", "Old device", "Identity Lead", "Ready", "Pilot report"],
    ["ERP client", 0, "Finance", "Versioned", "Ready", "Pass", "VDI", "App Lead", "Ready", "Task test"],
    ["CAD suite", 1, "Engineering", "Versioned", "Ready", "Conditional", "Old workstation", "App Lead", "Watch", "Peripheral defect"],
    ["Accessibility tools", 0, "Accessibility", "Specialized", "Ready", "Pass", "Named support", "Accessibility Lead", "Ready", "User acceptance"],
  ], widths: [24, 10, 20, 18, 16, 18, 22, 20, 16, 34], tableName: "HwApps" });
  addTable(wb, { name: "Deployment Waves", title: "Deployment waves and outcome measures", headers: ["Wave", "Planned", "Deployed", "FTR", "Data validated", "24h compliant", "Returns", "Exceptions", "State", "Owner"], rows: [
    ["Pilot", 20, 20, 19, 20, 20, 20, 0, "Closed", "Pilot Lead"],
    ["Site A", 95, 94, 92, 94, 93, 92, 1, "Hypercare", "Site A Lead"],
    ["Site B", 90, 87, 85, 86, 86, 84, 3, "Hypercare", "Site B Lead"],
    ["Site C", 75, 71, 69, 71, 70, 68, 4, "Deploying", "Site C Lead"],
    ["Remote/all", 80, 72, 71, 71, 70, 70, 8, "Deploying", "Remote Lead"],
    ["Total", 360, 344, 336, 342, 339, 334, 16, "Conditional", "Program Lead"],
  ], widths: [18, 14, 14, 14, 18, 18, 15, 16, 16, 20], tableName: "HwWaves" });
  addTable(wb, { name: "Data Validation", title: "User data protection and acceptance", headers: ["Wave", "Users", "Precheck pass", "Backup/sync pass", "Post-check pass", "Exceptions", "Hold release", "Owner", "Evidence"], rows: [
    ["Pilot", 20, 20, 20, 20, 0, "Yes", "Data Lead", "Count/sample/task acceptance"],
    ["Site A", 94, 94, 94, 94, 0, "Yes", "Data Lead", "Count/sample/task acceptance"],
    ["Site B", 87, 87, 86, 86, 1, "Yes", "Data Lead", "One owned exception"],
    ["Site C", 71, 71, 71, 71, 0, "Yes", "Data Lead", "Count/sample/task acceptance"],
    ["Remote/all", 72, 72, 71, 71, 1, "Yes", "Data Lead", "One owned exception"],
  ], widths: [18, 13, 18, 20, 18, 16, 16, 20, 38], tableName: "HwData" });
  addTable(wb, { name: "Sanitization", title: "Old-asset custody and sanitization evidence", headers: ["Custody ID", "Old serial", "User", "Received", "Hold release", "Method/program", "Validation", "Certificate", "Final disposition", "State"], rows: [
    ["CUST-0001", "OLD-0001", "Worker 001", "2026-09-04", "Approved", "ABC approved clear", "Pass", "CERT-0001", "Reuse", "Closed"],
    ["CUST-0002", "OLD-0002", "Worker 002", "2026-09-11", "Approved", "ABC approved clear", "Pass", "CERT-0002", "Recycle", "Closed"],
    ["CUST-0003", "OLD-0003", "Worker 003", "Pending", "Not released", "Pending", "Pending", "Pending", "Quarantine", "Open"],
    ["CUST-0004", "OLD-0004", "Worker 004", "2026-10-02", "Approved", "Carrier program", "Pass", "CARR-0004", "Carrier return", "Closed"],
  ], widths: [18, 18, 20, 16, 18, 24, 16, 18, 20, 16], tableName: "HwSanitize" });
  addTable(wb, { name: "Exceptions", title: "Deployment exception register", headers: ["ID", "User/cohort", "Category", "Statement", "Workaround", "Owner", "New date", "Age days", "State", "Final disposition"], rows: [
    ["EX-001", "Site A / Worker 095", "Leave", "User unavailable at wave date.", "Old device remains compliant", "Site A Lead", "2026-10-09", 6, "Owned", "Reschedule"],
    ["EX-002", "Site B / Finance", "Application", "ERP plug-in requires vendor fix.", "Approved VDI", "App Lead", "2026-10-16", 9, "Owned", "Retest"],
    ["EX-003", "Remote / Worker 344", "Logistics", "Return kit delayed.", "Courier escalation", "Asset Lead", "2026-10-23", 11, "Owned", "Recover asset"],
    ["EX-004", "Site C / Worker 301", "Accessibility", "Specialized peripheral pending.", "Retain old setup", "Accessibility Lead", "2026-10-30", 7, "Owned", "Specialized deployment"],
  ], widths: [14, 24, 18, 38, 34, 20, 15, 14, 16, 26], tableName: "HwExceptions" });
  addTable(wb, { name: "Budget", title: "Hardware refresh cost baseline and forecast", headers: ["Control account", "Baseline", "Forecast", "Actual", "ETC", "Variance", "Owner", "Evidence"], rows: [
    ["Devices/accessories", 468000, 451000, 442000, 9000, null, "Procurement Lead", "PO/receipt/invoice"],
    ["Shipping/logistics", 74000, 69000, 55000, 14000, null, "Logistics Lead", "Carrier invoices"],
    ["Staging/deployment labor", 126000, 121400, 87000, 34400, null, "Deployment Lead", "Time/vendor records"],
    ["Support/hypercare", 59000, 55000, 31000, 24000, null, "Service Lead", "Labor/queue forecast"],
    ["Sanitization/retirement", 37000, 34000, 17000, 17000, null, "Asset Lead", "Vendor/certificate records"],
    ["Change/reserve", 28000, 18000, 7000, 11000, null, "Program Lead", "Change/reserve log"],
  ], widths: [30, 18, 18, 18, 18, 18, 20, 34], numberFormats: { "B5:F10": "$#,##0;[Red]-$#,##0" }, tableName: "HwBudget" });
  const b = wb.worksheets.getItem("Budget"); b.getRange("F5").formulas = [["=B5-C5"]]; b.getRange("F5:F10").fillDown();
  addTable(wb, { name: "Sources", title: "Primary-source research register", headers: ["Publisher", "Source", "URL", "Use", "Accessed", "Authority"], rows: [
    ["PMI", "PMBOK Guide Eighth Edition", "https://www.pmi.org/standards/pmbok", "Principles, domains, tailoring", "2026-08-25", "Primary"],
    ["PMI", "Process Groups", "https://www.pmi.org/standards/process-groups", "Predictive lifecycle", "2026-08-25", "Primary"],
    ["Scrum Guides", "Scrum Guide", "https://scrumguides.org/scrum-guide.html", "Scrum accountabilities/events/artifacts", "2026-08-25", "Primary"],
    ["Kanban Guides", "Kanban Guide", "https://kanbanguides.org/the-kanban-guide/", "Workflow, WIP, SLE, flow metrics", "2026-08-25", "Primary"],
    ["NIST", "SP 800-88 Rev. 2", "https://csrc.nist.gov/pubs/sp/800/88/r2/final", "Sanitization program", "2026-08-25", "Primary"],
    ["Microsoft", "Windows Autopilot overview", "https://learn.microsoft.com/en-us/autopilot/overview", "Provisioning", "2026-08-25", "Primary"],
    ["Microsoft", "Intune compliance", "https://learn.microsoft.com/en-us/intune/device-security/compliance/overview", "Compliance validation", "2026-08-25", "Primary"],
  ], widths: [18, 38, 66, 38, 15, 15], tableName: "HwSources" });
  addTable(wb, { name: "Template Blank", title: "Reusable blank control register", headers: ["ID", "Item", "Owner", "Due", "State", "Acceptance", "Evidence", "Decision", "Notes"], rows: [["[ENTER]", "[ENTER]", "[ENTER]", "[ENTER]", "[ENTER]", "[ENTER]", "[LINK]", "[ENTER]", "[ENTER]"]], widths: [14, 35, 20, 15, 15, 35, 28, 25, 35], tableName: "HwBlank" });

  const methodSpecs = [
    ["Kanban Dashboard", "Hardware Refresh — Kanban Dashboard", "FLOW", "HwKanbanControls", [["Deployed", "='Deployment Waves'!C10", "0"], ["Throughput/week", "=42", "0"], ["Median cycle days", "=3.4", "0.0"], ["P85 days", "=6.2", "0.0"], ["Exceptions", "='Deployment Waves'!H10", "0"], ["Open RAID", "=COUNTIF(RAID!J5:J100,\"Open\")", "0"], ["FTR", "='Deployment Waves'!D10/'Deployment Waves'!C10", "0.0%"], ["Returns", "='Deployment Waves'!G10/'Deployment Waves'!C10", "0.0%"]], "Decision: stop starting remote work when exception/return lanes exceed WIP; swarm the oldest item at 75% of SLE."],
    ["Scrum Dashboard", "Hardware Refresh — Scrum Dashboard", "INCREMENT", "HwScrumControls", [["Accepted", "='Deployment Waves'!C10", "0"], ["PBIs remaining", "='Deployment Waves'!B10-'Deployment Waves'!C10", "0"], ["Sprint", "=9", "0"], ["FTR", "='Deployment Waves'!D10/'Deployment Waves'!C10", "0.0%"], ["Data pass", "='Deployment Waves'!E10/'Deployment Waves'!C10", "0.0%"], ["Compliance", "='Deployment Waves'!F10/'Deployment Waves'!C10", "0.0%"], ["Returns", "='Deployment Waves'!G10/'Deployment Waves'!C10", "0.0%"], ["Open RAID", "=COUNTIF(RAID!J5:J100,\"Open\")", "0"]], "Decision: only security/data/asset-accepted cohorts count in the Increment; incomplete work returns to the Product Backlog."],
    ["Predictive Dashboard", "Hardware Refresh — Predictive / Waterfall Dashboard", "BASELINE", "HwPredControls", [["SPI", "=0.97", "0.00"], ["CPI", "=1.03", "0.00"], ["Forecast", "=SUM(Budget!C5:C10)", "$#,##0"], ["VAC", "=SUM(Budget!F5:F10)", "$#,##0"], ["Deployed", "='Deployment Waves'!C10", "0"], ["Exceptions", "='Deployment Waves'!H10", "0"], ["Week", "=16", "0"], ["Finish week", "=18", "0"]], "Decision: maintain Week 18 baseline; control exception scope under rolling-wave work packages without weakening gate evidence."],
    ["Hybrid Dashboard", "Hardware Refresh — Hybrid Dashboard", "INTEGRATED", "HwHybridControls", [["Deployed", "='Deployment Waves'!C10", "0"], ["FTR", "='Deployment Waves'!D10/'Deployment Waves'!C10", "0.0%"], ["Data pass", "='Deployment Waves'!E10/'Deployment Waves'!C10", "0.0%"], ["Compliance", "='Deployment Waves'!F10/'Deployment Waves'!C10", "0.0%"], ["Returns", "='Deployment Waves'!G10/'Deployment Waves'!C10", "0.0%"], ["Exceptions", "='Deployment Waves'!H10", "0"], ["Forecast", "=SUM(Budget!C5:C10)", "$#,##0"], ["VAC", "=SUM(Budget!F5:F10)", "$#,##0"]], "Recommended: fixed budget/security/site gates plus pull-based staging, rolling-wave deployment, and a dedicated exception lane."],
  ];
  for (const [name, dashTitle, kpiTitle, tableName, kpis, decision] of methodSpecs) dashboard(wb, { name, title: dashTitle, kpiTitle, tableName, kpis, decision, controls: [["User outcome", "344/360 deployed", "360 final dispositions", "Conditional", "Wave Lead", "Own every remaining exception", "Deployment Waves", "Scenario"], ["Quality", "97.7% FTR", ">=97%", "Pass", "Quality Lead", "Correct recurring defects", "Deployment Waves", "Scenario"], ["Security/data", "98.5% / 99.4%", ">=98% / 99%", "Pass", "Security/Data", "Close five compliance and two data exceptions", "Deployment Waves", "Scenario"], ["Asset", "97.1% returns", "100% final disposition", "Watch", "Asset Lead", "Recover/quarantine open assets", "Sanitization", "Scenario"]], chartHeaders: ["Wave", "Deployed"], chartLabels: ["Pilot", "Site A", "Site B", "Site C", "Remote"], chartFormulas: ["='Deployment Waves'!C5", "='Deployment Waves'!C6", "='Deployment Waves'!C7", "='Deployment Waves'!C8", "='Deployment Waves'!C9"], chartTitle: "Devices deployed by wave" });
  dashboard(wb, { name: "Portfolio Summary", title: "Hardware Refresh — Portfolio Summary", kpiTitle: "OUTCOME", tableName: "HwPortfolioControls", kpis: [["Planned", "='Deployment Waves'!B10", "0"], ["Deployed", "='Deployment Waves'!C10", "0"], ["FTR", "='Deployment Waves'!D10/'Deployment Waves'!C10", "0.0%"], ["Data validated", "='Deployment Waves'!E10/'Deployment Waves'!C10", "0.0%"], ["24h compliant", "='Deployment Waves'!F10/'Deployment Waves'!C10", "0.0%"], ["Returns", "='Deployment Waves'!G10/'Deployment Waves'!C10", "0.0%"], ["Forecast", "=SUM(Budget!C5:C10)", "$#,##0"], ["Variance", "=SUM(Budget!F5:F10)", "$#,##0"]], decision: "Portfolio decision: Hybrid is the modeled best fit; close only after 360/360 new and old asset dispositions reconcile.", controls: [["Scope", "344/360 deployed", "360 final dispositions", "Conditional", "Program Lead", "Close 16 exceptions", "Deployment Waves", "Scenario"], ["Quality", "97.7% FTR", ">=97%", "Pass", "Quality Lead", "Monitor repeat defects", "Deployment Waves", "Scenario"], ["Security/data", "Pass with owned gaps", "No unowned gap", "Conditional", "Security/Data", "Close remediation evidence", "Data Validation", "Scenario"], ["Finance", "$748.4K forecast", "Within $792K", "Favorable", "Finance Lead", "Reconcile credits/reserve", "Budget", "Scenario"]], chartHeaders: ["Account", "Forecast"], chartLabels: ["Devices", "Logistics", "Labor", "Support", "Retirement"], chartFormulas: ["=Budget!C5", "=Budget!C6", "=Budget!C7", "=Budget!C8", "=Budget!C9"], chartTitle: "Forecast by control account" });
  return wb;
}

const maOut = path.join(root, "enterprise-programs", "01-ma-it-integration", "M_AND_A_INTEGRATION_CONTROL_WORKBOOK.xlsx");
const hwOut = path.join(root, "enterprise-programs", "02-hardware-refresh", "HARDWARE_REFRESH_CONTROL_WORKBOOK.xlsx");
await renderAndSave(buildMa(), maOut, path.join(qaRoot, "ma"));
await renderAndSave(buildHardware(), hwOut, path.join(qaRoot, "hardware"));
console.log(`Built ${path.relative(root, maOut)}`);
console.log(`Built ${path.relative(root, hwOut)}`);
