# Evals — data-tools-skills:excel-automation-python

## 1. Positive trigger (should load the skill)
> "Every month I paste this CSV into a formatted Excel report by hand — two sheets, money
> formats, a totals row. Can you script it in Python?"

Expected: skill loads; pandas writes the data, openpyxl formats (number formats, widths, freeze
panes) or a template workbook carries the styling; formulas-vs-computed-values decided
deliberately; output verified against source totals.

## 2. Near-miss (should NOT load this skill)
> "Help me structure this 13-week cash forecast model — assumptions tab, drivers, and scenario
> toggles."

Expected: model *design* — `data-analytics-bi-skills:spreadsheet-modeling`. If this skill loads,
tighten the automation/scripting framing.

## 3. Quality rubric
A good response:
- **Does the task:** produces a working script (pandas + openpyxl), correct formats on money
  columns, `index=False`, and a verification step (row counts/totals re-read from the output).
- **Teaches:** the data-layer vs document-layer split, why openpyxl never evaluates formulas
  (stale `data_only` caches), and the template-plus-data pattern for recurring reports.
- **Safe:** never overwrites the template; warns about numbers-as-text and dtype checks when
  reading; keeps real report figures out of committed examples.
