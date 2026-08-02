# Evals — data-analytics-bi-skills:spreadsheet-modeling

## 1. Positive trigger (should load the skill)
> "I'm building a 3-year revenue model in Excel and I keep hardcoding growth rates into the formulas.
> How should I structure it so it's clean and I can run sensitivity on the growth assumption?"

Expected: skill loads; separates inputs/calculations/outputs; moves the growth rate to a named input
cell referenced everywhere; enforces one-formula-per-row; adds check cells; and sets up a data-table
sensitivity on the growth driver.

## 2. Near-miss (should NOT load this skill)
> "What method should I use to forecast next quarter's operating cash flow — direct or indirect — and
> how do I handle seasonality in the drivers?"

Expected: this is forecasting methodology, not spreadsheet construction — the
`cash-management-skills:cash-forecasting` skill should handle it. If this modeling skill loads as
primary, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** separates inputs/calcs/outputs, replaces hardcoded constants with referenced
  input cells (named ranges), keeps one consistent formula per row, adds check cells/control totals,
  and builds a data-table or scenario sensitivity.
- **Teaches:** explains *why* auditability is the point — how structure prevents silent errors and
  why sensitivity reveals which assumptions actually drive the answer.
- **Safe:** warns against overtyping formulas with values, hardcoding, and unintended circular
  references; recommends documentation and an audit pass.
