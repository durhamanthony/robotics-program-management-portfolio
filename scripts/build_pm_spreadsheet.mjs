import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = process.env.PORTFOLIO_ROOT
  ? path.resolve(process.env.PORTFOLIO_ROOT)
  : path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const outPath = path.join(root, "pm-operating-system", "excel", "ROBOTICS_PM_OPERATING_SYSTEM.xlsx");
const previewDir = path.join(root, "qa", "xlsx");
await fs.mkdir(path.dirname(outPath), { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const wb = Workbook.create();
const COLORS = {
  navy: "#0B2545",
  blue: "#2E74B5",
  teal: "#087F6B",
  cyan: "#DDF4F0",
  pale: "#E8EEF5",
  white: "#FFFFFF",
  ink: "#17212B",
  muted: "#5B6670",
  amber: "#FFF0CE",
  red: "#FCE8E6",
  green: "#E6F4EA",
  border: "#CBD5E1",
};
const evidenceKey = "Evidence-confidence key: PB-H = public benchmark/high; RBE-M = range estimate/medium; SA-L = scenario assumption/low; DC-L = derived calculation/low; UPV = unverified production value.";

function colName(n) {
  let s = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    s = String.fromCharCode(65 + r) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function styleTitle(sheet, endCol, title) {
  const end = colName(endCol);
  sheet.getRange(`A1:${end}1`).merge();
  sheet.getRange("A1").values = [[title]];
  sheet.getRange(`A1:${end}1`).format = {
    fill: COLORS.navy,
    font: { bold: true, color: COLORS.white, size: 16 },
    rowHeight: 30,
    verticalAlignment: "center",
  };
  sheet.getRange(`A2:${end}2`).merge();
  sheet.getRange("A2").values = [[evidenceKey]];
  sheet.getRange(`A2:${end}2`).format = {
    fill: COLORS.cyan,
    font: { color: COLORS.muted, italic: true, size: 9 },
    wrapText: true,
    rowHeight: 28,
    verticalAlignment: "center",
  };
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(4);
}

function addTableSheet({ name, title, headers, rows, widths = [], tableName, numberFormats = {}, validations = [], conditional = [] }) {
  const sheet = wb.worksheets.add(name);
  styleTitle(sheet, headers.length, title);
  const end = colName(headers.length);
  sheet.getRange(`A4:${end}4`).values = [headers];
  sheet.getRange(`A4:${end}4`).format = {
    fill: COLORS.blue,
    font: { bold: true, color: COLORS.white, size: 10 },
    wrapText: true,
    verticalAlignment: "center",
    rowHeight: 30,
    borders: { bottom: { style: "medium", color: COLORS.navy } },
  };
  if (rows.length) {
    sheet.getRange(`A5:${end}${4 + rows.length}`).values = rows;
    sheet.getRange(`A5:${end}${4 + rows.length}`).format = {
      font: { color: COLORS.ink, size: 9 },
      wrapText: true,
      verticalAlignment: "top",
      borders: {
        insideHorizontal: { style: "thin", color: COLORS.border },
        insideVertical: { style: "thin", color: COLORS.border },
        bottom: { style: "thin", color: COLORS.border },
      },
    };
    const table = sheet.tables.add(`A4:${end}${4 + rows.length}`, true, tableName);
    table.style = "TableStyleMedium2";
    table.showBandedRows = true;
  }
  widths.forEach((width, i) => { sheet.getRange(`${colName(i + 1)}:${colName(i + 1)}`).format.columnWidth = width; });
  Object.entries(numberFormats).forEach(([range, format]) => { sheet.getRange(range).format.numberFormat = format; });
  validations.forEach(({ range, values }) => { sheet.getRange(range).dataValidation = { rule: { type: "list", values } }; });
  conditional.forEach(({ range, text, fill, color }) => {
    sheet.getRange(range).conditionalFormats.add("containsText", { text, format: { fill, font: { bold: true, color } } });
  });
  return sheet;
}

// Create all worksheets before cross-sheet formulas.
const dashboard = wb.worksheets.add("Dashboard");
const instructions = wb.worksheets.add("Instructions");
const assumptions = wb.worksheets.add("Assumptions");
const portfolio = wb.worksheets.add("Portfolio");
const schedule = wb.worksheets.add("Schedule");
const raid = wb.worksheets.add("RAID");
const requirements = wb.worksheets.add("Requirements");
const budget = wb.worksheets.add("Budget_TCO");
const benefits = wb.worksheets.add("Benefits");
const evidence = wb.worksheets.add("Evidence");
const stakeholders = wb.worksheets.add("Stakeholders");
const vendors = wb.worksheets.add("Vendors");
const gateLog = wb.worksheets.add("Gate_Log");

function populateTableSheet(sheet, { title, headers, rows, tableName, widths, numberFormats = {}, validations = [], conditional = [] }) {
  styleTitle(sheet, headers.length, title);
  const end = colName(headers.length);
  sheet.getRange(`A4:${end}4`).values = [headers];
  sheet.getRange(`A4:${end}4`).format = { fill: COLORS.blue, font: { bold: true, color: COLORS.white, size: 10 }, wrapText: true, verticalAlignment: "center", rowHeight: 30 };
  sheet.getRange(`A5:${end}${4 + rows.length}`).values = rows;
  sheet.getRange(`A5:${end}${4 + rows.length}`).format = { font: { color: COLORS.ink, size: 9 }, wrapText: true, verticalAlignment: "top", borders: { insideHorizontal: { style: "thin", color: COLORS.border }, insideVertical: { style: "thin", color: COLORS.border }, bottom: { style: "thin", color: COLORS.border } } };
  const table = sheet.tables.add(`A4:${end}${4 + rows.length}`, true, tableName);
  table.style = "TableStyleMedium2";
  table.showBandedRows = true;
  widths.forEach((width, i) => { sheet.getRange(`${colName(i + 1)}:${colName(i + 1)}`).format.columnWidth = width; });
  Object.entries(numberFormats).forEach(([range, format]) => { sheet.getRange(range).format.numberFormat = format; });
  validations.forEach(({ range, values }) => { sheet.getRange(range).dataValidation = { rule: { type: "list", values } }; });
  conditional.forEach(({ range, text, fill, color }) => sheet.getRange(range).conditionalFormats.add("containsText", { text, format: { fill, font: { bold: true, color } } }));
}

populateTableSheet(instructions, {
  title: "Table 1. Workbook instructions — Evidence: operating pattern [SA-L]; Confidence: low",
  headers: ["Step", "Action", "Control", "Owner / evidence"],
  rows: [
    [1, "Copy this workbook into a controlled program folder and assign a program owner.", "Do not use the example values as commitments.", "Named program owner [UPV]"],
    [2, "Replace every example row and [ENTER] field with approved project records.", "Preserve identifiers across all sheets.", "Source-system exports [UPV]"],
    [3, "Update source registers first; dashboard formulas summarize them.", "Never type over dashboard formulas.", "Weekly reconciliation [UPV]"],
    [4, "Attach source location, evidence class, and confidence to material facts.", "UPV blocks a release or financial commitment.", "Evidence owner [UPV]"],
    [5, "Export a dated evidence pack at each gate.", "Human approvers retain all decision authority.", "Signed gate log [UPV]"],
  ], tableName: "InstructionsTable", widths: [8, 42, 38, 28]
});

populateTableSheet(assumptions, {
  title: "Table 1. Assumptions and source controls — Evidence: example entries [SA-L/RBE-M]; Confidence: low/medium",
  headers: ["Assumption ID", "Variable", "Value", "Unit", "Evidence class", "Confidence", "Source / validation", "Owner", "Review date", "State"],
  rows: [
    ["ASM-001", "Discount rate", 0.08, "annual", "SA-L", "Low", "Replace with finance-approved hurdle rate", "Finance Lead", "2026-09-04", "Open"],
    ["ASM-002", "Robot useful life", 5, "years", "RBE-M", "Medium", "Validate with supplier warranty and reliability data", "Service Lead", "2026-09-18", "Open"],
    ["ASM-003", "Productive utilization", 1200, "hours/year", "SA-L", "Low", "Validate with pilot telemetry and approved task taxonomy", "Operations Lead", "2026-11-13", "Open"],
  ], tableName: "AssumptionsTable", widths: [14, 24, 12, 14, 16, 14, 42, 18, 15, 14], numberFormats: { "C5:C7": "0.00" }, validations: [{ range: "J5:J100", values: ["Open", "Validated", "Retired"] }]
});

populateTableSheet(portfolio, {
  title: "Table 1. Robotics case portfolio — Evidence: fictional cases [SA-L/DC-L]; Confidence: low",
  headers: ["Case ID", "Case", "Lifecycle", "Investment", "NPV / contribution", "Economic gate", "Status", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["CASE-01", "Retail backroom humanoid pilot", "Deployment", 672000, -221990, "Pilot accepted; scale held", "Complete", "SA-L/DC-L", "Low", "Case 01 business case and signed-pilot placeholders"],
    ["CASE-02", "Quadruped night security", "Deployment", 527000, 174099, "Break-even labor rate $33.98/hour", "Complete", "PB-H/SA-L/DC-L", "Low", "BLS wage benchmark plus disclosed assumptions"],
    ["CASE-03", "Open-source quadruped RaaS", "Productization", 2400000, 412800, "41 robots recover productization authorization", "Conditional", "SA-L/DC-L", "Low", "Case 03 unit economics and open-source gates"],
    ["CASE-04", "Robotics support operations", "Service", 678000, 255600, "250 robots / 60 sites service baseline", "Complete", "SA-L/DC-L", "Low", "Synthetic data workflow and operating model"],
    ["CASE-05", "Airport restroom humanoid pilot", "Deployment", 515000, 241006, "22.1 productive fleet hours/day", "Conditional", "PB-H/SA-L/DC-L", "Low", "BLS wage benchmark plus disclosed assumptions"],
  ], tableName: "PortfolioTable", widths: [12, 30, 18, 18, 22, 34, 16, 20, 14, 42], numberFormats: { "D5:E9": "$#,##0;[Red]-$#,##0" }, validations: [{ range: "G5:G100", values: ["Planned", "Conditional", "Complete", "Hold"] }], conditional: [{ range: "G5:G100", text: "Hold", fill: COLORS.red, color: "#9B1C1C" }, { range: "G5:G100", text: "Complete", fill: COLORS.green, color: COLORS.teal }]
});

populateTableSheet(schedule, {
  title: "Table 1. Integrated master schedule — Evidence: illustrative baseline [SA-L]; Confidence: low",
  headers: ["Activity ID", "Workstream", "Activity", "Owner", "Start", "Finish", "Predecessor", "Gate", "% complete", "Status", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["IMS-010", "Program", "Charter and outcome baseline", "Program Lead", "2026-08-31", "2026-09-04", "", "G0", 0, "Not started", "SA-L", "Low", "Replace with approved schedule"],
    ["IMS-020", "Safety", "Hazard analysis and thresholds", "Safety Lead", "2026-09-07", "2026-09-18", "IMS-010", "G1", 0, "Not started", "SA-L", "Low", "Signed safety plan required"],
    ["IMS-030", "Site", "Network, facilities, and workflow readiness", "Site Lead", "2026-09-14", "2026-10-02", "IMS-010", "G2", 0, "Not started", "SA-L", "Low", "Signed readiness checklist required"],
    ["IMS-040", "Acceptance", "FAT, SAT, and UAT execution", "Test Lead", "2026-10-05", "2026-10-16", "IMS-020; IMS-030", "G3", 0, "Not started", "SA-L", "Low", "Signed test evidence required"],
    ["IMS-050", "Operate", "Launch, hypercare, and benefits baseline", "Operations Lead", "2026-10-19", "2026-11-13", "IMS-040", "G4", 0, "Not started", "SA-L", "Low", "Operational evidence required"],
  ], tableName: "ScheduleTable", widths: [13, 18, 36, 18, 14, 14, 20, 10, 13, 16, 16, 14, 36], numberFormats: { "I5:I9": "0%" }, validations: [{ range: "J5:J100", values: ["Not started", "In progress", "Blocked", "Complete"] }], conditional: [{ range: "J5:J100", text: "Blocked", fill: COLORS.red, color: "#9B1C1C" }, { range: "J5:J100", text: "Complete", fill: COLORS.green, color: COLORS.teal }]
});

populateTableSheet(raid, {
  title: "Table 1. RAID register — Evidence: example entries [SA-L/RBE-M]; Confidence: low/medium",
  headers: ["RAID ID", "Type", "Statement", "Probability", "Impact", "Score", "Response", "Owner", "Due", "Status", "Trigger", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["R-001", "Risk", "Unvalidated stop-distance performance may block site acceptance", 3, 5, 15, "Run controlled-zone tests; hold release pending signed evidence", "Safety Lead", "2026-10-02", "Open", "Missed stop or incomplete record", "SA-L", "Low", "Approved hazard analysis and test report required"],
    ["A-001", "Assumption", "Customer network supports approved telemetry path", 3, 4, 12, "Validate ports, identity, retention, and fail-safe behavior", "IT Lead", "2026-09-18", "Open", "Security review or connectivity test fails", "SA-L", "Low", "Approved network design required"],
    ["D-001", "Dependency", "Supplier ships service spares before readiness gate", 2, 4, 8, "Track confirmed date and qualify alternate source", "Supply Lead", "2026-09-25", "Open", "Arrival crosses gate date", "RBE-M", "Medium", "Confirmed shipment record required"],
  ], tableName: "RaidTable", widths: [12, 14, 42, 12, 10, 10, 42, 18, 14, 14, 34, 16, 14, 38], validations: [{ range: "B5:B100", values: ["Risk", "Assumption", "Issue", "Dependency"] }, { range: "J5:J100", values: ["Open", "Watching", "Closed"] }], conditional: [{ range: "F5:F100", text: "15", fill: COLORS.red, color: "#9B1C1C" }, { range: "J5:J100", text: "Closed", fill: COLORS.green, color: COLORS.teal }]
});

populateTableSheet(requirements, {
  title: "Table 1. Requirements traceability — Evidence: example requirements [SA-L/UPV]; Confidence: low/unverified",
  headers: ["Requirement ID", "Requirement", "Method", "Test case", "Threshold", "Result", "Status", "Evidence location", "Owner", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["REQ-SAF-001", "Controlled safe state after loss of approved communications", "Test", "SAT-SAF-01", "10/10 trials within approved envelope", "TBD", "Not run", "[ATTACH]", "Safety Lead", "SA-L", "Low", "Threshold and result require signed evidence"],
    ["REQ-OPS-001", "Correlate mission to robot, software, and evidence bundle", "Demonstration", "SAT-OPS-03", "10/10 sampled missions complete", "TBD", "Not run", "[ATTACH]", "Operations Lead", "SA-L", "Low", "Replace with exported evidence"],
    ["REQ-CYB-001", "Approved identity, least privilege, logging, and revocation", "Inspection", "SAT-CYB-02", "All controls present; no critical exception", "TBD", "Not run", "[ATTACH]", "Security Lead", "PB-H", "High", "Validate against approved policy and logs"],
  ], tableName: "RequirementsTable", widths: [16, 42, 18, 18, 32, 14, 14, 24, 18, 16, 14, 38], validations: [{ range: "G5:G100", values: ["Not run", "Passed", "Failed", "Blocked", "Waived"] }], conditional: [{ range: "G5:G100", text: "Failed", fill: COLORS.red, color: "#9B1C1C" }, { range: "G5:G100", text: "Passed", fill: COLORS.green, color: COLORS.teal }]
});

populateTableSheet(budget, {
  title: "Table 1. Budget and TCO — Evidence: range estimates and assumptions [RBE-M/SA-L/DC-L]; Confidence: low/medium",
  headers: ["Cost ID", "Category", "Item", "Quantity", "Unit cost", "Total cost", "Timing", "Owner", "Actual / forecast", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["CAP-001", "Capital", "Robot and approved accessories", 2, 150000, null, "Year 0", "Finance Lead", "Forecast", "RBE-M", "Medium", "Competitive supplier quote required"],
    ["IMP-001", "Implementation", "Integration, safety, training, and launch", 1, 95000, null, "Year 0", "Program Lead", "Forecast", "SA-L", "Low", "Work-breakdown estimate required"],
    ["OPE-001", "Operating", "Support, cloud, connectivity, spares, and field service", 3, 42000, null, "Years 1-3", "Service Lead", "Forecast", "RBE-M", "Medium", "Contract and baseline required"],
    ["CON-001", "Contingency", "Risk reserve", 1, 47400, null, "Year 0", "Program Lead", "Forecast", "DC-L", "Low", "12% of capital + implementation; recalculate"],
  ], tableName: "BudgetTable", widths: [13, 18, 38, 12, 17, 18, 16, 18, 18, 16, 14, 40], numberFormats: { "E5:F8": "$#,##0;[Red]-$#,##0" }, validations: [{ range: "I5:I100", values: ["Forecast", "Actual"] }]
});
budget.getRange("F5").formulas = [["=D5*E5"]];
budget.getRange("F5:F8").fillDown();

populateTableSheet(benefits, {
  title: "Table 1. Benefits register — Evidence: example targets [SA-L/PB-H]; Confidence: low/high",
  headers: ["Benefit ID", "Outcome", "Metric", "Baseline", "Target", "Measurement method", "Frequency", "Owner", "Start", "Status", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["BEN-001", "Recover productive capacity", "Qualified productive hours/week", 0, 40, "Approved taxonomy and sampled telemetry", "Weekly", "Operations Lead", "2026-10-19", "Planned", "SA-L", "Low", "Signed baseline and telemetry required"],
    ["BEN-002", "Improve service reliability", "Mission success rate", "TBD", "95%", "Eligible completed / eligible attempted", "Weekly", "Service Lead", "2026-10-19", "Planned", "SA-L", "Low", "Customer definition and target required"],
    ["BEN-003", "Reduce safety exposure", "Recordable robot-caused safety events", "TBD", 0, "Approved safety incident register", "Monthly", "Safety Lead", "2026-10-19", "Planned", "PB-H", "High", "Zero critical-event threshold; baseline required"],
  ], tableName: "BenefitsTable", widths: [14, 30, 32, 14, 14, 40, 14, 18, 14, 14, 16, 14, 38], validations: [{ range: "J5:J100", values: ["Planned", "Measuring", "Realized", "Stopped"] }]
});

populateTableSheet(evidence, {
  title: "Table 1. Evidence register — Evidence: release controls [UPV/RBE-M]; Confidence: unverified/medium",
  headers: ["Evidence ID", "Claim / control", "Evidence type", "Location", "Record owner", "Approver", "Review date", "Approval state", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["EVD-001", "Safety thresholds approved", "Signed hazard and acceptance plan", "[ATTACH]", "Safety Lead", "Executive Sponsor", "2026-09-18", "Pending", "UPV", "Unverified", "Block gate until signed"],
    ["EVD-002", "Budget reflects current supplier and labor inputs", "Quote and rate package", "[ATTACH]", "Finance Lead", "Executive Sponsor", "2026-09-25", "Pending", "RBE-M", "Medium", "Replace estimates with dated evidence"],
    ["EVD-003", "Tests satisfy release requirements", "Signed RTM and test report", "[ATTACH]", "Test Lead", "Customer Owner", "2026-10-16", "Pending", "UPV", "Unverified", "Each passed row needs traceable evidence"],
  ], tableName: "EvidenceTable", widths: [14, 36, 30, 20, 18, 18, 14, 16, 16, 14, 36], validations: [{ range: "H5:H100", values: ["Pending", "Approved", "Rejected", "Expired"] }], conditional: [{ range: "H5:H100", text: "Pending", fill: COLORS.amber, color: "#7A5A00" }, { range: "H5:H100", text: "Approved", fill: COLORS.green, color: COLORS.teal }]
});

populateTableSheet(stakeholders, {
  title: "Table 1. Stakeholder and communications plan — Evidence: recommended pattern [SA-L]; Confidence: low",
  headers: ["Stakeholder", "Role", "Influence", "Impact", "Decision right", "Information need", "Channel / cadence", "Owner", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["Executive sponsor", "Investment owner", "High", "High", "Approves budget, scope, and residual risk", "Outcome, exception, decision", "Steering / biweekly", "Program Lead", "SA-L", "Low", "Replace with signed governance plan"],
    ["Safety lead", "Safety authority", "High", "High", "Sets stop/restart and acceptance controls", "Hazards, tests, incidents", "Gate review / as needed", "Program Lead", "SA-L", "Low", "Replace with approved RACI"],
    ["Site operators", "Daily users", "Medium", "High", "Accept workflow and handoff", "Training, exceptions, changes", "Daily huddle / weekly review", "Change Lead", "SA-L", "Low", "Validate through discovery and UAT"],
  ], tableName: "StakeholdersTable", widths: [22, 22, 13, 13, 34, 30, 26, 18, 16, 14, 36]
});

populateTableSheet(vendors, {
  title: "Table 1. Vendor readiness and commercial controls — Evidence: example controls [SA-L/RBE-M]; Confidence: low/medium",
  headers: ["Vendor / item", "Control area", "Requirement", "Evidence due", "Owner", "Status", "Commercial exposure", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["Robot supplier", "Configuration", "Serialized BOM, firmware, calibration, and release note", "2026-09-25", "Supply Lead", "Open", "Shipment blocked", "RBE-M", "Medium", "Approved supplier package required"],
    ["Cloud / connectivity", "Security", "Data flow, identity, retention, logging, and exit plan", "2026-09-18", "Security Lead", "Open", "Production access blocked", "SA-L", "Low", "Security approval required"],
    ["Field service", "Support", "Coverage, spares, response, escalation, and reporting", "2026-10-02", "Service Lead", "Open", "Launch blocked", "RBE-M", "Medium", "Executed service agreement required"],
  ], tableName: "VendorsTable", widths: [24, 20, 42, 16, 18, 14, 24, 16, 14, 40], validations: [{ range: "F5:F100", values: ["Open", "Conditional", "Ready", "Rejected"] }]
});

populateTableSheet(gateLog, {
  title: "Table 1. Stage-gate decision log — Evidence: example gate sequence [SA-L/UPV]; Confidence: low/unverified",
  headers: ["Gate", "Decision date", "Decision", "Decision owner", "Criteria summary", "Conditions", "Closure due", "Evidence package", "Evidence class", "Confidence", "Source / validation"],
  rows: [
    ["G0 Charter", "2026-09-04", "Pending", "Executive Sponsor", "Outcome, scope, roles, and funding", "[ENTER]", "2026-09-04", "[ATTACH]", "UPV", "Unverified", "Signed decision required"],
    ["G1 Design", "2026-09-18", "Pending", "Executive Sponsor", "Requirements, hazards, architecture, and estimate", "[ENTER]", "2026-09-25", "[ATTACH]", "UPV", "Unverified", "Signed decision required"],
    ["G2 Ready", "2026-10-02", "Pending", "Executive Sponsor", "Site, service, security, supplier, and test readiness", "[ENTER]", "2026-10-05", "[ATTACH]", "UPV", "Unverified", "Signed decision required"],
    ["G3 Accept", "2026-10-16", "Pending", "Customer Owner", "FAT/SAT/UAT result and residual risk", "[ENTER]", "2026-10-19", "[ATTACH]", "UPV", "Unverified", "Signed decision required"],
    ["G4 Scale", "2026-11-13", "Pending", "Executive Sponsor", "Reliability, benefit, TCO, support, and adoption", "[ENTER]", "2026-11-20", "[ATTACH]", "UPV", "Unverified", "Signed decision required"],
  ], tableName: "GateLogTable", widths: [16, 16, 16, 20, 42, 28, 16, 20, 16, 14, 36], validations: [{ range: "C5:C100", values: ["Pending", "Go", "Conditional go", "Hold"] }], conditional: [{ range: "C5:C100", text: "Hold", fill: COLORS.red, color: "#9B1C1C" }, { range: "C5:C100", text: "Go", fill: COLORS.green, color: COLORS.teal }]
});

// Dashboard: linked formulas, a visible data table title, and a formula-backed chart.
styleTitle(dashboard, 12, "Robotics PM Operating System — Integrated Dashboard");
dashboard.freezePanes.freezeRows(3);
dashboard.getRange("A4:B4").values = [["PROGRAM CONTROL", "VALUE"]];
dashboard.getRange("D4:E4").values = [["ASSURANCE", "VALUE"]];
dashboard.getRange("G4:H4").values = [["FINANCE / BENEFIT", "VALUE"]];
for (const range of ["A4:B4", "D4:E4", "G4:H4"]) dashboard.getRange(range).format = { fill: COLORS.blue, font: { bold: true, color: COLORS.white } };
dashboard.getRange("A5:A8").values = [["Portfolio cases"], ["Open RAID items"], ["Blocked schedule items"], ["Pending gates"]];
dashboard.getRange("B5:B8").formulas = [["=COUNTA(Portfolio!A5:A9)"], ["=COUNTIF(RAID!J5:J100,\"Open\")"], ["=COUNTIF(Schedule!J5:J100,\"Blocked\")"], ["=COUNTIF(Gate_Log!C5:C100,\"Pending\")"]];
dashboard.getRange("D5:D8").values = [["Pending evidence"], ["Passed requirements"], ["Failed requirements"], ["Unverified evidence"]];
dashboard.getRange("E5:E8").formulas = [["=COUNTIF(Evidence!H5:H100,\"Pending\")"], ["=COUNTIF(Requirements!G5:G100,\"Passed\")"], ["=COUNTIF(Requirements!G5:G100,\"Failed\")"], ["=COUNTIF(Evidence!J5:J100,\"Unverified\")"]];
dashboard.getRange("G5:G8").values = [["Illustrative TCO"], ["Portfolio investment"], ["Positive NPV / contribution"], ["Benefit records"]];
dashboard.getRange("H5:H8").formulas = [["=SUM(Budget_TCO!F5:F8)"], ["=SUM(Portfolio!D5:D9)"], ["=SUMIF(Portfolio!E5:E9,\">0\",Portfolio!E5:E9)"], ["=COUNTA(Benefits!A5:A100)"]];
dashboard.getRange("A5:H8").format = { fill: COLORS.white, font: { color: COLORS.ink, size: 10 }, borders: { insideHorizontal: { style: "thin", color: COLORS.border }, insideVertical: { style: "thin", color: COLORS.border }, bottom: { style: "thin", color: COLORS.border } } };
dashboard.getRange("B5:B8").format.numberFormat = "0";
dashboard.getRange("E5:E8").format.numberFormat = "0";
dashboard.getRange("H5:H7").format.numberFormat = "$#,##0;[Red]-$#,##0";
dashboard.getRange("H8").format.numberFormat = "0";
dashboard.getRange("A10:H10").merge();
dashboard.getRange("A10").values = [["Table 1. Executive control summary — Evidence: linked source-register formulas [DC-L]; Confidence: low until source records are approved"]];
dashboard.getRange("A10:H10").format = { fill: COLORS.pale, font: { bold: true, color: COLORS.navy }, wrapText: true, rowHeight: 28 };
dashboard.getRange("A11:H11").values = [["Domain", "Current state", "Decision rule", "Owner", "Evidence source", "Evidence class", "Confidence", "Next review"]];
dashboard.getRange("A12:H16").values = [
  ["Program", "Conditional", "No critical dependency may cross a gate unresolved", "Program Lead", "Schedule + RAID", "DC-L", "Low", "Weekly"],
  ["Safety", "Pending evidence", "No release without signed acceptance", "Safety Lead", "Requirements + Evidence", "UPV", "Unverified", "Per gate"],
  ["Finance", "Illustrative", "Reconcile quotes, TCO, benefit, and sensitivity", "Finance Lead", "Budget_TCO + Assumptions", "RBE-M/DC-L", "Low", "Monthly"],
  ["Service", "Design baseline", "Support, spares, telemetry, and rollback ready", "Service Lead", "Evidence + Vendors", "SA-L", "Low", "Weekly"],
  ["Customer", "Acceptance pending", "Signed UAT and limitation acknowledgement", "Customer Owner", "Requirements + Gate_Log", "UPV", "Unverified", "Per gate"],
];
dashboard.getRange("A11:H16").format = { wrapText: true, font: { size: 9, color: COLORS.ink }, borders: { insideHorizontal: { style: "thin", color: COLORS.border }, insideVertical: { style: "thin", color: COLORS.border }, bottom: { style: "thin", color: COLORS.border } } };
dashboard.getRange("A11:H11").format = { fill: COLORS.blue, font: { bold: true, color: COLORS.white, size: 9 }, wrapText: true };
const dashboardTable = dashboard.tables.add("A11:H16", true, "DashboardControlTable");
dashboardTable.style = "TableStyleMedium2";
dashboard.getRange("J4:K4").values = [["Case", "Investment"]];
dashboard.getRange("J5:J9").formulas = [["=Portfolio!A5"], ["=Portfolio!A6"], ["=Portfolio!A7"], ["=Portfolio!A8"], ["=Portfolio!A9"]];
dashboard.getRange("K5:K9").formulas = [["=Portfolio!D5"], ["=Portfolio!D6"], ["=Portfolio!D7"], ["=Portfolio!D8"], ["=Portfolio!D9"]];
const chart = dashboard.charts.add("bar", dashboard.getRange("J4:K9"));
chart.title = "Illustrative investment by case";
chart.hasLegend = false;
chart.yAxis = { numberFormatCode: "$#,##0" };
chart.setPosition("A18", "H34");
dashboard.getRange("A:A").format.columnWidth = 24;
dashboard.getRange("B:B").format.columnWidth = 16;
dashboard.getRange("C:C").format.columnWidth = 22;
dashboard.getRange("D:D").format.columnWidth = 22;
dashboard.getRange("E:E").format.columnWidth = 28;
dashboard.getRange("F:F").format.columnWidth = 18;
dashboard.getRange("G:G").format.columnWidth = 24;
dashboard.getRange("H:H").format.columnWidth = 18;
dashboard.getRange("J:K").format.columnWidth = 14;

// Render every sheet for visual QA, then export the workbook.
for (const sheetName of ["Dashboard", "Instructions", "Assumptions", "Portfolio", "Schedule", "RAID", "Requirements", "Budget_TCO", "Benefits", "Evidence", "Stakeholders", "Vendors", "Gate_Log"]) {
  const preview = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName}.png`), new Uint8Array(await preview.arrayBuffer()));
}
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outPath);
try {
  await fs.rename(`${outPath}.inspect.ndjson`, path.join(previewDir, "ROBOTICS_PM_OPERATING_SYSTEM.inspect.ndjson"));
} catch (error) {
  if (error.code !== "ENOENT") throw error;
}
console.log(`Built ${path.relative(root, outPath)}`);
