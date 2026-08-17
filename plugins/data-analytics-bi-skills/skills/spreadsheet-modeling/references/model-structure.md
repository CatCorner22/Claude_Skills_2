# Spreadsheet model structure (reference)

Conventions and patterns for auditable Excel / Google Sheets models. Method lineage: the
published structured-modeling conventions (the FAST standard — flexible, appropriate,
structured, transparent — and its relatives), motivated by the spreadsheet-error field-audit
record collected by EuSpRIG. Claims marked [snippet-only] were cross-checked via web-search
snippets rather than the primary papers.

## Contents
- [Why structure: the error record](#why-structure-the-error-record)
- [Zone / sheet layout](#zone--sheet-layout)
- [Formatting conventions](#formatting-conventions)
- [Named ranges](#named-ranges)
- [Check cells and control totals](#check-cells-and-control-totals)
- [Sensitivity: data tables and scenarios](#sensitivity-data-tables-and-scenarios)
- [Audit toolkit](#audit-toolkit)
- [Worked example — a 12-month staffing-and-cost model](#worked-example--a-12-month-staffing-and-cost-model)
- [Model review checklist](#model-review-checklist)
- [Sources and attribution notes](#sources-and-attribution-notes)

## Why structure: the error record

The case for these conventions is empirical, not aesthetic. Panko's synthesis of the
spreadsheet-error research (the literature EuSpRIG curates) reports [snippet-only]:
- **94% of 88 operational spreadsheets audited contained at least one error**; recent field
  audits generally found errors in at least 86% of spreadsheets examined.
- The **average cell error rate ran about 5%** across 13 studies (1995–2004) — rare per
  cell, but a model has thousands of cells, so at least one wrong bottom-line value becomes
  very likely as models grow.

Two consequences drive everything below. First, errors are invisible by default — a wrong
constant produces a clean-looking number — so the design goal is to make errors *visible*
(consistent rows, check cells) and *localized* (single-source inputs). Second, since the
per-cell rate is roughly constant, fewer distinct formulas mean fewer chances to be wrong:
one formula filled across a row is one opportunity for error, not twelve.

## Zone / sheet layout
Separate the three concerns, by zone on a sheet or by dedicated sheets:
- **Inputs / assumptions** — every changeable number, each in its own labeled cell, with units and source.
- **Calculations** — the engine; references inputs and prior calcs only, no raw constants.
- **Outputs** — summary results, charts, KPIs; references calculations, contains no new logic.

Flow is one-directional: inputs → calcs → outputs. A calculation never reaches "forward"
into outputs, and outputs never compute anything new — when an output needs a number the
calcs don't produce, the fix is a new calc row, not a formula on the output sheet.

Add a **cover/README** sheet: purpose, owner, version, date, key assumptions, and a change
log. If raw data feeds the model (an extract, an export), land it on a marked **data** sheet
as values — cleaned first (`data-analytics-bi-skills:data-cleaning`) — and reference it from
calcs; never paste raw data into the middle of logic.

## Formatting conventions
- **Input cells** in a distinct style (classic: blue font) so assumptions are visible at a glance.
- Calculated cells in black; links to other sheets sometimes green.
- Consistent number formats and units; show units in labels ($, %, days, 000s).
- One period per column, consistent across the row; freeze header rows/first column.
- One column per period means **column = time**; never mix "Jan, Feb, Mar, Total, Apr" — put
  totals in their own clearly separated column or a summary block.

## Named ranges
- Name genuine inputs and key intermediates: `TaxRate`, `Price`, `Units`, `WACC`.
- `=Price*Units` reads like the logic; `=$B$4*$C$4` does not.
- Keep names meaningful and scoped; don't name every cell (noise). In Excel: Formulas → Name Manager;
  structured references for Tables (`=SUM(Sales[Amount])`).
- Audit tip: paste a list of all names (Formulas → Use in Formula → Paste Names) onto the
  cover sheet so reviewers can see the model's vocabulary in one place.

## Check cells and control totals
Build tripwires that make silent errors loud:
- **Cross-foot:** sum of a row's parts = its total; sum of columns = grand total. Difference should be 0.
- **Balance identities:** assets = liabilities + equity; sources = uses; beginning + change = ending.
- **Reconciliations:** model output ties to a known external total.
- **Sanity bounds:** rates between 0 and 1; headcounts non-negative; percentages sum to 100.
- **Master flag:** one cell `=IF(AND(check1=0, check2=0, …), "OK", "ERROR")`, conditionally formatted
  red on ERROR, placed on the cover sheet and beside the headline output.
- Use tolerances for float rounding: `=ABS(diff) < 0.01`.

A check cell asserts an identity that holds *whatever the inputs are*. If a check only holds
for today's inputs, it is not a check — it is a snapshot that will cry wolf on the first
what-if run.

## Sensitivity: data tables and scenarios
- **One-way data table:** vary a single input down a column, read one output across — shows the
  output's response to that driver.
- **Two-way data table:** vary one input down rows and another across columns (Excel: Data → What-If
  Analysis → Data Table).
- **Scenario toggle:** a `CHOOSE`/`INDEX` driven by a scenario selector switches whole input sets
  (Base/Upside/Downside) from the input zone — never by editing formulas.
- Goal Seek / Solver for "what input hits this target output". Always vary inputs, not formulas.
- Read the result for **leverage**: the two or three inputs that move the output most are
  where estimation effort and review scrutiny belong; the rest can stay rough.

## Audit toolkit
- **Trace Precedents / Dependents** (Formulas tab) to follow the logic into and out of a cell.
- **Show Formulas** (Ctrl+`) or `FORMULATEXT()` to eyeball a row for an inconsistent cell.
- **Error Checking** and evaluate-formula to step through a complex cell.
- Check for **circular references** (status bar) and remove unless iterative calc is intended.
- Stress inputs to extremes and confirm outputs and check cells behave sensibly; then
  gut-check the headline number — sign, magnitude, units, and a rough independent
  re-derivation (`math-foundations-skills:number-sense-and-estimation`).
- Google Sheets equivalents: named ranges (Data → Named ranges), `FORMULATEXT`, and
  conditional formatting all exist; data tables don't — emulate with a small scenario grid
  or an Apps Script.

## Worked example — a 12-month staffing-and-cost model

Domain-neutral on purpose: "billable work" below is any effort sold or recovered — an
analyst team's projects, a law firm's matters, an ops group's chargebacks, a consultancy's
engagements. **All numbers are illustrative.**

**Purpose (cover sheet).** Decide whether hiring two more staff in April is affordable if
utilization lands anywhere between 55% and 75%.

**Inputs sheet** (blue cells, each with source and units):

| Name | Value | Units | Source |
|---|---|---|---|
| `Headcount_Start` | 8 | people | org chart, as-of Jan |
| `Hires_New` | 2 | people | proposal under test |
| `Hire_Month` | 4 | month index | proposal under test (April) |
| `Salary_Annual` | 90,000 | $/person/yr | HR band midpoint |
| `Overhead_Rate` | 30% | of salary | finance standard |
| `Bill_Rate` | 120 | $/hr | current rate card |
| `Hours_Per_Month` | 160 | hr/person/mo | org standard workable month |
| `Util_Base` | 65% | % of `Hours_Per_Month` | trailing 6-mo actual |

**Calculations sheet** — one row per line item, one column per month, every row filled
across unchanged:
- `Headcount`: Jan–Mar `=Headcount_Start`; Apr+ `=Headcount_Start+Hires_New` — via a
  start-month flag row (`=IF(month>=Hire_Month,1,0)`) so the formula is still identical
  across columns.
- `Cost`: `=Headcount * Salary_Annual/12 * (1+Overhead_Rate)`.
- `Billable_Hours`: `=Headcount * Hours_Per_Month * Util_Base`.
- `Revenue`: `=Billable_Hours * Bill_Rate`.
- `Margin`: `=Revenue - Cost`.

**Checks** (beside the calcs, rolled into the master flag):
- Cross-foot: sum of monthly margins = annual revenue − annual cost (must be 0 difference).
- Sanity: `Util_Base` between 0 and 1; headcount integer and ≥ 0.
- Reconciliation: Jan cost ties to the payroll actual for January (external anchor).

One of these defenses earns its keep immediately — but be precise about which. A first
draft typed April's headcount as `=Headcount_Start+2` (hardcoded 2), so when `Hires_New`
was later changed to 3, every April-onward number was silently wrong. The **consistency
scan** is what catches it: the row is no longer identical across columns, and `FORMULATEXT`
shows the odd cell. The cross-foot cannot fire on this — Σ(monthly margins) ≡ annual
revenue − annual cost is an algebraic identity that holds for *every* input set, hardcode
included, so that flag stays green no matter what the rows contain; its job is catching
broken aggregation (a roll-up range that dropped a month), not wrong logic. A model that is
internally coherent but wrong is what the **external reconciliation** exists for — numbers
that tie to nothing outside the model can agree with each other forever.

**Outputs sheet.** Headline: annual margin under Base. Below it, a **two-way data table**:
`Util_Base` 45–75% down the rows, `Hires_New` 0/1/2/3 across the columns, annual margin in
the body. The answer to the actual question is read straight off the table: margin stays
positive down to ~51% utilization — per-person breakeven is monthly cost ÷ monthly capacity
revenue = (90,000/12 × 1.30) ÷ (160 × 120) = 9,750 / 19,200 = 50.8%, and because both sides
scale with headcount it holds at any hire count. On leverage, run the numbers before naming
the driver: a 15% salary move is ≈ $1,460/person/month (0.15 × 9,750) against ≈ $960 for a
5-point utilization drop (0.05 × 160 × 120) — salary is the larger lever here, even though
only utilization carries real month-to-month uncertainty. A scenario toggle
(Base/Upside/Downside) switches the full input set for the narrative cases.

## Model review checklist
Reviewing an inherited workbook, in order:
1. Cover sheet: purpose, owner, version — or reconstruct one first.
2. Map the zones: can you point at inputs, calcs, outputs? If not, color the inputs now.
3. `FORMULATEXT` / Show Formulas scan: any row whose formula changes mid-row?
4. Hardcode hunt: constants inside formulas (search for `*0.`, `+1`, digits in formula view).
5. Check cells: do any exist? Do they still tie? Add cross-foots before changing anything.
6. Circulars: status bar clean?
7. Stress: push each key input to an extreme; watch outputs and checks respond.
8. Only then: make the requested change, and leave the model with more checks than you found.

## Sources and attribution notes
- Panko, R., "What We Know About Spreadsheet Errors" and the follow-up literature he and
  EuSpRIG collect — 94%-of-88 field-audit figure, ~5% average cell error rate, ≥86% in
  later field audits [snippet-only].
- EuSpRIG (European Spreadsheet Risks Interest Group) — curates the error research and the
  public horror-stories list of documented spreadsheet incidents.
- FAST Standard — a published structured-modeling convention (flexible, appropriate,
  structured, transparent); the zone separation and consistent-formula rules here follow its
  spirit without adopting its full rulebook.
- Attribution note: the often-quoted "88% (or 90%) of all spreadsheets contain errors" is a
  compression of study-specific figures that vary with audit method and sample — quote the
  specific audit result, not a universal law.
