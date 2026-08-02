# Spreadsheet model structure (reference)

Conventions and patterns for auditable Excel / Google Sheets models.

## Contents
- Zone / sheet layout
- Formatting conventions
- Named ranges
- Check cells and control totals
- Sensitivity: data tables and scenarios
- Audit toolkit

## Zone / sheet layout
Separate the three concerns, by zone on a sheet or by dedicated sheets:
- **Inputs / assumptions** — every changeable number, each in its own labeled cell, with units and source.
- **Calculations** — the engine; references inputs and prior calcs only, no raw constants.
- **Outputs** — summary results, charts, KPIs; references calculations, contains no new logic.
Flow is one-directional: inputs → calcs → outputs. Add a **cover/README** sheet: purpose, owner,
version, date, key assumptions, and a change log.

## Formatting conventions
- **Input cells** in a distinct style (classic: blue font) so assumptions are visible at a glance.
- Calculated cells in black; links to other sheets sometimes green.
- Consistent number formats and units; show units in labels ($, %, days, 000s).
- One period per column, consistent across the row; freeze header rows/first column.

## Named ranges
- Name genuine inputs and key intermediates: `TaxRate`, `Price`, `Units`, `WACC`.
- `=Price*Units` reads like the logic; `=$B$4*$C$4` does not.
- Keep names meaningful and scoped; don't name every cell (noise). In Excel: Formulas → Name Manager;
  structured references for Tables (`=SUM(Sales[Amount])`).

## Check cells and control totals
Build tripwires that make silent errors loud:
- **Cross-foot:** sum of a row's parts = its total; sum of columns = grand total. Difference should be 0.
- **Balance identities:** assets = liabilities + equity; sources = uses; beginning + change = ending.
- **Reconciliations:** model output ties to a known external total.
- **Master flag:** one cell `=IF(AND(check1=0, check2=0, …), "OK", "ERROR")`, conditionally formatted
  red on ERROR, placed where you can't miss it.
- Use tolerances for float rounding: `=ABS(diff) < 0.01`.

## Sensitivity: data tables and scenarios
- **One-way data table:** vary a single input down a column, read one output across — shows the
  output's response to that driver.
- **Two-way data table:** vary one input down rows and another across columns (Excel: Data → What-If
  Analysis → Data Table).
- **Scenario toggle:** a `CHOOSE`/`INDEX` driven by a scenario selector switches whole input sets
  (Base/Upside/Downside) from the input zone — never by editing formulas.
- Goal Seek / Solver for "what input hits this target output". Always vary inputs, not formulas.

## Audit toolkit
- **Trace Precedents / Dependents** (Formulas tab) to follow the logic into and out of a cell.
- **Show Formulas** (Ctrl+`) or `FORMULATEXT()` to eyeball a row for an inconsistent cell.
- **Error Checking** and evaluate-formula to step through a complex cell.
- Check for **circular references** (status bar) and remove unless iterative calc is intended.
- Stress inputs to extremes and confirm outputs and check cells behave sensibly.
