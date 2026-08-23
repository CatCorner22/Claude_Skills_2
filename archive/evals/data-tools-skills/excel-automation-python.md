# Evals — data-tools-skills:excel-automation-python

## 1. Positive trigger (should load the skill)
> "Every month I paste this CSV into a formatted Excel report by hand — two sheets, money
> formats, a totals row. Can you script it in Python?"

Expected: skill loads; pandas writes the data, openpyxl formats (number formats, widths, freeze
panes) or a template workbook carries the styling; IDs typed as strings; formulas-vs-computed-
values decided deliberately; output re-read and verified against source totals.

## 2. Near-miss (should NOT load this skill)
> "Help me structure this 13-week forecast model — assumptions tab, drivers, and scenario
> toggles."

Expected: model *design* — `data-analytics-bi-skills:spreadsheet-modeling`. If this skill loads,
tighten the automation/scripting framing.

## 2b. Near-miss (upstream-source guard)
> "This vendor export CSV loads with garbled characters and the columns shift on some rows —
> fix the load."

Expected: flat-file ingestion — `data-tools-skills:csv-and-flat-file-wrangling`. This skill is
about the .xlsx document layer, not parsing flat files; if it loads here, the boundary between
the two needs sharpening.

## 3. Quality rubric
A good response:
- **Does the task:** produces a working script (pandas + openpyxl), correct formats on money
  columns, `index=False`, IDs as strings, and a verification step (row counts/totals re-read
  from the output).
- **Teaches:** the data-layer vs document-layer split, why openpyxl never evaluates formulas
  (stale `data_only` caches), and the template-plus-data pattern for recurring reports.
- **Routes:** hands model design to `data-analytics-bi-skills:spreadsheet-modeling`, oversized
  aggregation to `data-tools-skills:duckdb-local-analytics`, file naming/sanitization to
  `data-tools-skills:data-file-hygiene`, and project setup to
  `coding-agent-skills:python-for-analysts` where those seams appear.
- **Safe:** never overwrites the template; warns about numbers-as-text, leading-zero loss on ID
  columns, and dtype checks when reading; keeps real report figures out of committed examples.
