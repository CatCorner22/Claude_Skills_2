# Evals — data-analytics-bi-skills:spreadsheet-modeling

## 1. Positive trigger (should load the skill)
> "I'm building a 3-year revenue model in Excel and I keep hardcoding growth rates into the formulas.
> How should I structure it so it's clean and I can run sensitivity on the growth assumption?"

Expected: skill loads; separates inputs/calculations/outputs with one-directional flow; moves
the growth rate to a named input cell referenced everywhere; enforces one-formula-per-row;
adds check cells rolled into a master OK/ERROR flag; and sets up a data-table sensitivity on
the growth driver.

## 2. Near-miss (should NOT load this skill)
> "What method should I use to forecast next quarter's operating cash flow — direct or indirect — and
> how do I handle seasonality in the drivers?"

Expected: this is forecasting methodology, not spreadsheet construction — the statistical side
(seasonality, model choice, validation) belongs to `machine-learning-skills:time-series-forecasting`;
the direct-vs-indirect treasury framing has no active owner. If this modeling skill loads as
primary, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** separates inputs/calcs/outputs, replaces hardcoded constants with referenced
  input cells (named ranges), keeps one consistent formula per row, adds check cells/control totals
  with a master flag, and builds a data-table or scenario sensitivity.
- **Teaches:** explains *why* auditability is the point — grounds it in the documented
  spreadsheet-error field-audit record (EuSpRIG/Panko: errors are the norm in unaudited
  models) without inflating it into a universal "90% of all spreadsheets" law — and why
  sensitivity reveals which assumptions actually drive the answer.
- **Safe:** warns against overtyping formulas with values, hardcoding, and unintended circular
  references; recommends documentation and an audit pass with a final gut-check of the
  headline number (sign, magnitude, units — `math-foundations-skills:number-sense-and-estimation`);
  points recurring hand-rebuilt workbooks toward
  `data-tools-skills:excel-automation-python` rather than more manual tabs.
