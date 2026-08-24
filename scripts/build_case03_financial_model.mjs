import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = process.env.PORTFOLIO_ROOT
  ? path.resolve(process.env.PORTFOLIO_ROOT)
  : path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const outPath = path.join(root, "scenarios", "03-open-source-quadruped-raas-productization", "OPENQUAD_RAAS_FINANCIAL_MODEL.xlsx");
const previewDir = path.join(root, "qa", "xlsx", "case03-financial-model");
await fs.mkdir(path.dirname(outPath), { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const wb = Workbook.create();
const COLORS = {
  navy: "#0B2545",
  teal: "#087F6B",
  blue: "#2E74B5",
  pale: "#E8EEF5",
  cyan: "#DDF4F0",
  white: "#FFFFFF",
  ink: "#17212B",
  muted: "#5B6670",
  green: "#E6F4EA",
  amber: "#FFF0CE",
  red: "#FCE8E6",
  border: "#CBD5E1",
};
const evidenceKey = "PB-H = public benchmark/high; PB-M = public benchmark/medium; SA-L = scenario assumption/low; DC-M/DC-L = derived calculation inheriting its weakest material input; UPV = pending validation.";

function colName(n) {
  let s = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    s = String.fromCharCode(65 + r) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function title(sheet, endCol, text) {
  const end = colName(endCol);
  sheet.getRange(`A1:${end}1`).merge();
  sheet.getRange("A1").values = [[text]];
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
    font: { italic: true, color: COLORS.muted, size: 9 },
    rowHeight: 28,
    wrapText: true,
    verticalAlignment: "center",
  };
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(4);
}

function table(sheet, { titleText, headers, rows, tableName, widths, numberFormats = {} }) {
  title(sheet, headers.length, titleText);
  const end = colName(headers.length);
  sheet.getRange(`A4:${end}4`).values = [headers];
  sheet.getRange(`A4:${end}4`).format = {
    fill: COLORS.blue,
    font: { bold: true, color: COLORS.white, size: 10 },
    rowHeight: 30,
    wrapText: true,
    verticalAlignment: "center",
  };
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
  const object = sheet.tables.add(`A4:${end}${4 + rows.length}`, true, tableName);
  object.style = "TableStyleMedium2";
  object.showBandedRows = true;
  widths.forEach((width, i) => { sheet.getRange(`${colName(i + 1)}:${colName(i + 1)}`).format.columnWidth = width; });
  Object.entries(numberFormats).forEach(([range, format]) => { sheet.getRange(range).format.numberFormat = format; });
}

const executive = wb.worksheets.add("Executive");
const assumptions = wb.worksheets.add("Assumptions");
const program = wb.worksheets.add("Program_Budget");
const unit = wb.worksheets.add("Unit_Economics");
const customer = wb.worksheets.add("Customer_Value");
const providerSensitivity = wb.worksheets.add("Provider_Sensitivity");
const customerSensitivity = wb.worksheets.add("Customer_Sensitivity");
const sources = wb.worksheets.add("Sources");
const checks = wb.worksheets.add("Checks");

table(assumptions, {
  titleText: "Table 1. Case 03 financial assumptions and evidence — Confidence shown by row",
  headers: ["ID", "Input", "Value", "Unit", "Evidence", "Confidence", "Source / validation"],
  rows: [
    ["ASM-001", "Glassdoor U.S. Robotics Software Engineer annual salary", 154709, "USD/year", "PB-M", "Medium", "Glassdoor; May 2026; 435 salaries"],
    ["ASM-002", "Glassdoor U.S. Robotics Software Engineer hourly salary", 74, "USD/hour", "PB-M", "Medium", "Glassdoor; May 2026; not fully loaded"],
    ["ASM-003", "BLS private-industry wage share", 0.699, "share of compensation", "PB-H", "High", "BLS ECEC; March 2026"],
    ["ASM-004", "BLS private-industry benefits share", 0.301, "share of compensation", "PB-H", "High", "BLS ECEC; March 2026"],
    ["ASM-005", "Loaded annual planning labor cost", null, "USD/FTE-year", "DC-M", "Medium", "Annual salary / BLS wage share"],
    ["ASM-006", "Productization staffing", 7, "FTE-years", "SA-L", "Low", "Replace with approved resource plan"],
    ["ASM-007", "Unitree Go2 EDU list-price comparator", 15900, "USD/unit", "PB-M", "Medium", "Official Unitree store; different platform"],
    ["ASM-008", "Configuration/calibration labor", 50, "hours/unit", "SA-L", "Low", "Replace with routing and time study"],
    ["ASM-009", "Battery, e-stop, network, spares, delivery allowance", 4400, "USD/unit", "SA-L", "Low", "Replace with binding BOM and freight"],
    ["ASM-010", "Direct service labor", 36, "hours/unit-year", "SA-L", "Low", "Replace with service-case history"],
    ["ASM-011", "Cloud and telemetry", 600, "USD/unit-year", "SA-L", "Low", "Replace with cloud bills"],
    ["ASM-012", "Spares/warranty reserve", 0.12, "share of build cost", "SA-L", "Low", "Replace with reliability and warranty actuals"],
    ["ASM-013", "Onboarding labor", 40, "hours/site", "SA-L", "Low", "Replace with delivery time study"],
    ["ASM-014", "Onboarding travel/materials", 1500, "USD/site", "SA-L", "Low", "Replace with actual travel and materials"],
    ["ASM-015", "Onboarding customer price", 6000, "USD/site", "SA-L", "Low", "Replace with executed order"],
    ["ASM-016", "Subscription term", 36, "months", "SA-L", "Low", "Replace with executed order"],
    ["ASM-017", "Recovery cohort", 48, "robots", "SA-L", "Low", "Planning target, not forecast"],
    ["ASM-018", "Customer lab size", 2, "robots/site", "SA-L", "Low", "Replace with customer configuration"],
    ["ASM-019", "Released customer capacity", 1000, "hours/site-year", "SA-L", "Low", "Replace with time study"],
    ["ASM-020", "Customer network allowance", 6000, "USD/site", "SA-L", "Low", "Replace with site quote"],
    ["ASM-021", "Customer ROI gate", 0.15, "three-year ROI", "SA-L", "Low", "Replace with customer hurdle rate"],
    ["ASM-022", "Pilot units", 12, "robots", "SA-L", "Low", "Fictional pilot scope"],
    ["ASM-023", "Fixtures and laboratory equipment", 120000, "USD", "SA-L", "Low", "Replace with binding quotes"],
    ["ASM-024", "External safety, legal, and insurance", 150000, "USD", "SA-L", "Low", "Replace with binding proposals"],
    ["ASM-025", "Cloud, data, and pilot operations", 72000, "USD", "SA-L", "Low", "Replace with approved operating plan"],
    ["ASM-026", "Management reserve", 0.10, "share of subtotal", "SA-L", "Low", "Replace with approved risk reserve"],
    ["ASM-027", "Program/product/systems staffing", 1.5, "FTE-years", "SA-L", "Low", "Approved resource plan"],
    ["ASM-028", "Hardware/reliability/safety staffing", 1.5, "FTE-years", "SA-L", "Low", "Approved resource plan"],
    ["ASM-029", "Software/security/release staffing", 2, "FTE-years", "SA-L", "Low", "Approved resource plan"],
    ["ASM-030", "Manufacturing/quality staffing", 1, "FTE-years", "SA-L", "Low", "Approved resource plan"],
    ["ASM-031", "Service/customer-operations staffing", 1, "FTE-years", "SA-L", "Low", "Approved resource plan"],
  ],
  tableName: "Case03Assumptions",
  widths: [14, 42, 18, 20, 14, 14, 44],
  numberFormats: { "C5:C35": "0.00", "C5:C6": "$#,##0.00", "C11:C11": "$#,##0", "C27:C29": "$#,##0", "C7:C8": "0.0%", "C16:C16": "0.0%", "C25:C25": "0.0%", "C30:C30": "0.0%" },
});
assumptions.getRange("C9").formulas = [["=C5/C7"]];
assumptions.getRange("C9").format.numberFormat = "$#,##0";

table(program, {
  titleText: "Table 1. Productization budget — Evidence: [PB-M]/[PB-H]/[SA-L]/[DC-L]; Confidence: low overall",
  headers: ["Cost category", "Basis", "Amount", "Evidence", "Confidence", "Replacement evidence"],
  rows: [
    ["Program, product, systems, compliance labor", "1.5 FTE-years x loaded planning cost", null, "DC-L", "Low", "Approved staffing and payroll"],
    ["Hardware, reliability, and safety labor", "1.5 FTE-years x loaded planning cost", null, "DC-L", "Low", "Approved staffing and payroll"],
    ["Software, security, and release labor", "2.0 FTE-years x loaded planning cost", null, "DC-L", "Low", "Approved staffing and payroll"],
    ["Manufacturing and quality labor", "1.0 FTE-year x loaded planning cost", null, "DC-L", "Low", "Approved staffing and payroll"],
    ["Service and customer operations labor", "1.0 FTE-year x loaded planning cost", null, "DC-L", "Low", "Approved staffing and payroll"],
    ["Twelve pilot units", "Pilot units x modeled unit direct cost", null, "DC-L", "Low", "Binding BOM, routing, yield, freight"],
    ["Fixtures and laboratory equipment", "Scenario allowance", null, "SA-L", "Low", "Binding quotes"],
    ["External safety, legal, and insurance", "Scenario allowance", null, "SA-L", "Low", "Binding proposals"],
    ["Cloud, data, and pilot operations", "Scenario allowance", null, "SA-L", "Low", "Approved operating plan"],
    ["Subtotal", "Sum before reserve", null, "DC-L", "Low", "Reconciled estimate"],
    ["Management reserve", "10% of subtotal", null, "DC-L", "Low", "Sponsor-approved risk reserve"],
    ["Total productization investment", "Subtotal + reserve", null, "DC-L", "Low", "Approved authorization and actuals"],
  ],
  tableName: "ProgramBudget",
  widths: [38, 38, 20, 14, 14, 42],
  numberFormats: { "C5:C16": "$#,##0.00;[Red]-$#,##0.00" },
});
program.getRange("C5:C9").formulas = [
  ["=Assumptions!C31*Assumptions!C9"],
  ["=Assumptions!C32*Assumptions!C9"],
  ["=Assumptions!C33*Assumptions!C9"],
  ["=Assumptions!C34*Assumptions!C9"],
  ["=Assumptions!C35*Assumptions!C9"],
];
program.getRange("C10:C16").formulas = [
  ["=Assumptions!C26*Unit_Economics!C8"],
  ["=Assumptions!C27"],
  ["=Assumptions!C28"],
  ["=Assumptions!C29"],
  ["=SUM(C5:C13)"],
  ["=C14*Assumptions!C30"],
  ["=C14+C15"],
];
program.getRange("A14:F16").format = { fill: COLORS.pale, font: { bold: true, color: COLORS.navy } };

table(unit, {
  titleText: "Table 1. Provider unit economics over 36 months — Confidence: low overall",
  headers: ["Item", "Formula basis", "Amount", "Evidence", "Confidence", "Replacement evidence"],
  rows: [
    ["Research-quadruped comparator", "Official Unitree Go2 EDU list price", null, "PB-M", "Medium", "Product-specific binding quote"],
    ["Configuration/calibration labor", "50 hours x Glassdoor $74/hour", null, "DC-L", "Low", "Routing and payroll actuals"],
    ["Battery, e-stop, network, spares, delivery allowance", "Scenario allowance", null, "SA-L", "Low", "Binding BOM and freight"],
    ["Build, calibration, and delivery", "Comparator + labor + allowance", null, "DC-L", "Low", "Audited unit cost"],
    ["Direct service labor", "36 hours/year x $74 x 3 years", null, "DC-L", "Low", "Service history and payroll"],
    ["Cloud and telemetry", "$600/year x 3 years", null, "DC-L", "Low", "Cloud bills"],
    ["Spares/warranty reserve", "12% x build cost", null, "DC-L", "Low", "Warranty actuals"],
    ["Total direct 36-month cost", "Build + service + cloud + reserve", null, "DC-L", "Low", "Audited service cost"],
    ["Onboarding delivery cost", "40 hours x $74 + $1,500", null, "DC-L", "Low", "Delivery actuals"],
    ["Onboarding contribution per robot", "($6,000 price - cost) / 2 robots", null, "DC-L", "Low", "Executed order and actual cost"],
    ["Unrounded monthly price floor", "Recover program across 48 robots", null, "DC-L", "Low", "Executed terms and audited costs"],
    ["Monthly decision price", "Nearest $100 above modeled floor", null, "DC-L", "Low", "Approved price book"],
    ["Subscription revenue per robot", "Monthly price x 36", null, "DC-L", "Low", "Executed order"],
    ["Contribution before onboarding", "Revenue - direct cost", null, "DC-L", "Low", "Collected revenue and audited costs"],
    ["Total contribution per robot", "Contribution + onboarding allocation", null, "DC-L", "Low", "Collected revenue and audited costs"],
    ["Robots to recover investment", "Investment / contribution, rounded up", null, "DC-L", "Low", "Contracted units and actual contribution"],
    ["48-robot cohort contribution", "Contribution x 48", null, "DC-L", "Low", "Collected cohort contribution"],
    ["Cohort buffer before omitted costs", "Cohort contribution - investment", null, "DC-L", "Low", "Full income statement"],
  ],
  tableName: "UnitEconomics",
  widths: [38, 40, 20, 14, 14, 42],
  numberFormats: { "C5:C22": "$#,##0.00;[Red]-$#,##0.00", "C20:C20": "0" },
});
unit.getRange("C5:C22").formulas = [
  ["=Assumptions!C11"],
  ["=Assumptions!C12*Assumptions!C6"],
  ["=Assumptions!C13"],
  ["=SUM(C5:C7)"],
  ["=Assumptions!C14*Assumptions!C6*3"],
  ["=Assumptions!C15*3"],
  ["=C8*Assumptions!C16"],
  ["=SUM(C8:C11)"],
  ["=Assumptions!C17*Assumptions!C6+Assumptions!C18"],
  ["=(Assumptions!C19-C13)/Assumptions!C22"],
  ["=(Program_Budget!C16/Assumptions!C21+C12-C14)/Assumptions!C20"],
  ["=ROUND(C15/100,0)*100"],
  ["=C16*Assumptions!C20"],
  ["=C17-C12"],
  ["=C18+C14"],
  ["=CEILING(Program_Budget!C16/C19,1)"],
  ["=C19*Assumptions!C21"],
  ["=C21-Program_Budget!C16"],
];
unit.getRange("A15:F22").format = { fill: COLORS.pale, font: { bold: true, color: COLORS.navy } };

table(customer, {
  titleText: "Table 1. Customer two-robot value screen over 36 months — Confidence: low overall",
  headers: ["Item", "Formula basis", "Amount", "Evidence", "Confidence", "Decision meaning"],
  rows: [
    ["Onboarding", "One site", null, "SA-L", "Low", "Replace with executed order"],
    ["Subscription", "2 robots x monthly price x 36", null, "DC-L", "Low", "Replace with executed order"],
    ["Lab network allowance", "Scenario allowance", null, "SA-L", "Low", "Replace with site quote"],
    ["Three-year TCO", "Onboarding + subscription + network", null, "DC-L", "Low", "Customer cost screen"],
    ["Capacity value", "1,000 hours/year x Glassdoor $74/hour x 3", null, "DC-L", "Low", "Capacity, not automatic cash savings"],
    ["Net capacity value", "Capacity value - TCO", null, "DC-L", "Low", "Must be converted to realized savings"],
    ["Three-year ROI", "Net value / TCO", null, "DC-L", "Low", "Base case passes 15% gate"],
    ["Break-even released hours/year", "TCO / ($74 x 3)", null, "DC-L", "Low", "Round up to 833 hours"],
    ["Maximum monthly price at 15% ROI", "Capacity/(1+gate), less onboarding/network, divided by robot-months", null, "DC-L", "Low", "Price ceiling at base utilization"],
  ],
  tableName: "CustomerValue",
  widths: [38, 46, 20, 14, 14, 42],
  numberFormats: { "C5:C10": "$#,##0.00;[Red]-$#,##0.00", "C11:C11": "0.0%", "C12:C12": "0.00", "C13:C13": "$#,##0.00" },
});
customer.getRange("C5:C13").formulas = [
  ["=Assumptions!C19"],
  ["=Assumptions!C22*Unit_Economics!C16*Assumptions!C20"],
  ["=Assumptions!C24"],
  ["=SUM(C5:C7)"],
  ["=Assumptions!C23*Assumptions!C6*3"],
  ["=C9-C8"],
  ["=C10/C8"],
  ["=C8/(Assumptions!C6*3)"],
  ["=((C9/(1+Assumptions!C25))-C5-C7)/(Assumptions!C22*Assumptions!C20)"],
];
customer.getRange("A8:F13").format = { fill: COLORS.pale, font: { bold: true, color: COLORS.navy } };

table(providerSensitivity, {
  titleText: "Table 1. Provider sensitivity — Evidence: formula-derived from mixed inputs; Confidence: low",
  headers: ["Case", "Monthly price", "Build multiplier", "Service multiplier", "Direct 3-year cost", "Contribution", "Units to recover", "Decision"],
  rows: [
    ["Base", null, 1, 1, null, null, null, "Conditional pass at 48 units"],
    ["Price -10%", null, 1, 1, null, null, null, "Fails 48-unit cohort"],
    ["Service cost +50%", null, 1, 1.5, null, null, null, "Fails 48-unit cohort"],
    ["Build cost +25%", null, 1.25, 1, null, null, null, "Fails 48-unit cohort"],
    ["Price -10% and service +50%", null, 1, 1.5, null, null, null, "Stop / redesign"],
  ],
  tableName: "ProviderSensitivity",
  widths: [34, 18, 18, 18, 20, 20, 18, 28],
  numberFormats: { "B5:B9": "$#,##0", "C5:D9": "0.00x", "E5:F9": "$#,##0", "G5:G9": "0" },
});
providerSensitivity.getRange("B5:B9").formulas = [
  ["=Unit_Economics!C16"],
  ["=Unit_Economics!C16*0.9"],
  ["=Unit_Economics!C16"],
  ["=Unit_Economics!C16"],
  ["=Unit_Economics!C16*0.9"],
];
for (let row = 5; row <= 9; row += 1) {
  providerSensitivity.getRange(`E${row}`).formulas = [[`=Unit_Economics!C8*C${row}+SUM(Unit_Economics!C9:C11)*D${row}`]];
  providerSensitivity.getRange(`F${row}`).formulas = [[`=B${row}*Assumptions!C20-E${row}+Unit_Economics!C14`]];
  providerSensitivity.getRange(`G${row}`).formulas = [[`=CEILING(Program_Budget!C16/F${row},1)`]];
}

table(customerSensitivity, {
  titleText: "Table 1. Customer value sensitivity — Evidence: formula-derived from [PB-M]/[SA-L]; Confidence: low",
  headers: ["Released hours/year", "Salary value/hour", "Three-year capacity value", "Net value vs. TCO", "ROI", "15% gate"],
  rows: [
    [1200, 74, null, null, null, "Pass"],
    [1000, 74, null, null, null, "Pass"],
    [900, 74, null, null, null, "Below gate"],
    [800, 74, null, null, null, "Fail"],
    [1000, 60, null, null, null, "Fail"],
  ],
  tableName: "CustomerSensitivity",
  widths: [24, 22, 28, 24, 16, 18],
  numberFormats: { "A5:A9": "0", "B5:B9": "$#,##0", "C5:D9": "$#,##0;[Red]-$#,##0", "E5:E9": "0.0%" },
});
for (let row = 5; row <= 9; row += 1) {
  customerSensitivity.getRange(`C${row}`).formulas = [[`=A${row}*B${row}*3`]];
  customerSensitivity.getRange(`D${row}`).formulas = [[`=C${row}-Customer_Value!C8`]];
  customerSensitivity.getRange(`E${row}`).formulas = [[`=D${row}/Customer_Value!C8`]];
}
customerSensitivity.getRange("F5:F6").format = { fill: COLORS.green, font: { bold: true, color: COLORS.teal } };
customerSensitivity.getRange("F7").format = { fill: COLORS.amber, font: { bold: true, color: "#7A5A00" } };
customerSensitivity.getRange("F8:F9").format = { fill: COLORS.red, font: { bold: true, color: "#9B1C1C" } };

table(sources, {
  titleText: "Table 1. Public source register — Research checked 2026-08-24",
  headers: ["Source", "URL", "Dated fact used", "Evidence", "Confidence", "Limitation"],
  rows: [
    ["Glassdoor U.S. Robotics Software Engineer salary", "https://www.glassdoor.com/Salaries/gyor-robotics-software-engineer-salary-SRCH_IL.0%2C4_KO5%2C31.htm", "$154,709/year or $74/hour; 435 salaries; May 2026", "PB-M", "Medium", "Crowdsourced/model-based; not customer payroll or loaded cost"],
    ["BLS Employer Costs for Employee Compensation", "https://www.bls.gov/charts/employer-costs-for-employee-compensation/costs-by-industry.htm", "Private-industry wages 69.9% and benefits 30.1%; March 2026", "PB-H", "High", "Aggregate factor, not company-specific"],
    ["Unitree Go2 EDU official store", "https://www.unitree-robot.com/shop/products/unitree-go2", "$15,900 research/developer configuration", "PB-M", "Medium", "Different platform; not a Solo12 quote"],
    ["Open Dynamic Robot Initiative", "https://open-dynamic-robot-initiative.github.io/", "Open hardware/software objective and BSD 3-Clause statement", "PB-H", "High", "Does not endorse the fictional product"],
    ["Solo12 hardware repository", "https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/quadruped_robot_12dof_v1/README.md", "12 active degrees of freedom and documented components", "PB-H", "High", "Reference design, not product BOM"],
    ["PAL Robotics Solo12 status", "https://solo.pal-robotics.com/solo", "Solo12 sales discontinued", "PB-H", "High", "Creates supply-chain/obsolescence gate"],
    ["NIST Secure Software Development Framework", "https://csrc.nist.gov/pubs/sp/800/218/final", "Secure development control structure", "PB-H", "High", "Guidance, not certification"],
  ],
  tableName: "Case03Sources",
  widths: [36, 72, 46, 14, 14, 48],
});

table(checks, {
  titleText: "Table 1. Formula and reconciliation checks — All rows must pass before release",
  headers: ["Check", "Calculated", "Expected", "Variance", "Status"],
  rows: [
    ["Program investment", null, 2397233.62, null, null],
    ["Build/calibration/delivery", null, 24000, null, null],
    ["Direct service/cloud/reserve", null, 12672, null, null],
    ["Monthly decision price", null, 2400, null, null],
    ["Robots to recover investment", null, 48, null, null],
    ["Customer three-year TCO", null, 184800, null, null],
    ["Customer ROI", null, 0.2012987013, null, null],
  ],
  tableName: "Case03Checks",
  widths: [38, 22, 22, 20, 16],
  numberFormats: { "B5:D10": "$#,##0.00;[Red]-$#,##0.00", "B11:D11": "0.0000%" },
});
checks.getRange("B5:B11").formulas = [
  ["=Program_Budget!C16"],
  ["=Unit_Economics!C8"],
  ["=SUM(Unit_Economics!C9:C11)"],
  ["=Unit_Economics!C16"],
  ["=Unit_Economics!C20"],
  ["=Customer_Value!C8"],
  ["=Customer_Value!C11"],
];
for (let row = 5; row <= 11; row += 1) {
  checks.getRange(`D${row}`).formulas = [[`=B${row}-C${row}`]];
  checks.getRange(`E${row}`).formulas = [[`=IF(ABS(D${row})<0.01,"PASS","FAIL")`]];
}
checks.getRange("E5:E11").format = { fill: COLORS.green, font: { bold: true, color: COLORS.teal } };

table(executive, {
  titleText: "Table 1. OpenQuad RaaS decision economics — Formula-linked executive view",
  headers: ["Metric", "Value", "Evidence", "Confidence", "Plain-English meaning"],
  rows: [
    ["Productization investment", null, "DC-L", "Low", "Seven FTE-years plus pilot units, external work, operating allowances, and 10% reserve"],
    ["Monthly decision price per robot", null, "DC-L", "Low", "Rounded price needed to recover the program across the assumed 48-robot cohort"],
    ["Provider recovery gate", null, "DC-L", "Low", "Minimum subscribing robots at the modeled contribution"],
    ["Two-robot customer three-year TCO", null, "DC-L", "Low", "Onboarding, subscription, and network allowance"],
    ["Three-year customer capacity value", null, "DC-L", "Low", "1,000 released hours/year valued at Glassdoor's $74/hour salary benchmark"],
    ["Customer net capacity value", null, "DC-L", "Low", "Capacity value less TCO; not automatic cash savings"],
    ["Customer ROI", null, "DC-L", "Low", "Passes the fictional 15% gate only at the base utilization"],
    ["Break-even released hours/year", null, "DC-L", "Low", "Round up to 833 hours; below this, modeled net value is negative"],
  ],
  tableName: "Case03Executive",
  widths: [38, 24, 16, 16, 68],
  numberFormats: { "B5:B6": "$#,##0.00", "B7:B7": "0", "B8:B10": "$#,##0.00", "B11:B11": "0.0%", "B12:B12": "0.00" },
});
executive.getRange("B5:B12").formulas = [
  ["=Program_Budget!C16"],
  ["=Unit_Economics!C16"],
  ["=Unit_Economics!C20"],
  ["=Customer_Value!C8"],
  ["=Customer_Value!C9"],
  ["=Customer_Value!C10"],
  ["=Customer_Value!C11"],
  ["=Customer_Value!C12"],
];
executive.getRange("A14:E14").merge();
executive.getRange("A14").values = [["Decision rule: proceed only when 48 signed units at or above $2,384.57/month, customer time studies, audited costs, supported supply, and independent compliance evidence all close. Glassdoor salary is a planning benchmark—not a customer actual."]];
executive.getRange("A14:E14").format = { fill: COLORS.amber, font: { bold: true, color: "#7A5A00" }, rowHeight: 48, wrapText: true, verticalAlignment: "center" };

for (const sheetName of ["Executive", "Assumptions", "Program_Budget", "Unit_Economics", "Customer_Value", "Provider_Sensitivity", "Customer_Sensitivity", "Sources", "Checks"]) {
  const preview = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName}.png`), new Uint8Array(await preview.arrayBuffer()));
}
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outPath);
try {
  await fs.rename(`${outPath}.inspect.ndjson`, path.join(previewDir, "OPENQUAD_RAAS_FINANCIAL_MODEL.inspect.ndjson"));
} catch (error) {
  if (error.code !== "ENOENT") throw error;
}
console.log(`Built ${path.relative(root, outPath)}`);
