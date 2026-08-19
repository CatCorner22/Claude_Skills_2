---
name: excel-automation-python
description: >-
  Reads, writes, and formats real Excel workbooks with Python — pandas read_excel/to_excel for
  data in and out, openpyxl for the document layer (formulas as strings, number formats,
  widths, freeze panes, styling), xlsxwriter for write-only speed, and the template-workbook
  pattern where styling lives in a human-maintained file and the script only moves numbers —
  so recurring spreadsheet deliverables become a verified script instead of hand work. Reads
  defensively (shifted headers, merged cells, numbers-as-text, leading-zero loss on IDs, stale
  formula caches) and verifies output totals against the source. Use when automating an Excel
  report, converting data to a formatted .xlsx, reading a messy workbook into a DataFrame, or
  deciding between pandas and openpyxl. Triggers: excel automation, openpyxl, write xlsx, read
  excel python, pandas to_excel, format excel with python, excel report script, xlsxwriter,
  automate spreadsheet, excel formulas python, excel template python, ExcelWriter.
metadata:
  version: "1.2.1"
---

# Excel automation with Python

## When to use
- Producing a formatted .xlsx deliverable from data with a script (recurring reports, extracts,
  summary workbooks), or reading real-world workbooks into pandas.
- Deciding the tool split: pandas vs openpyxl vs xlsxwriter vs a document-generation skill.
- Not for: the model *design* living in the workbook → see
  `data-analytics-bi-skills:spreadsheet-modeling`. Source data trapped in a PDF → see
  `data-tools-skills:pdf-data-extraction`. If you have Anthropic's official `xlsx` skill
  installed (from the `anthropics/skills` marketplace), prefer it for polished one-off document
  creation; use this skill when you're building your *own* repeatable script.
- Not for: a substantial multi-file automation build where the *process* (scoping, phasing,
  audit) is the hard part → see `coding-agent-skills:script-wizard`; this skill supplies the
  Excel layer inside it.

## Do it
1. **Pick the layer by the job.** Data in/out → **pandas** (`read_excel`, `to_excel`). Formatting,
   formulas, multiple sheets, widths, freeze panes → **openpyxl** (or xlsxwriter for write-only
   speed). The standard pattern is both: pandas writes the data, openpyxl polishes the workbook.
   Set the project up to run the same way twice — venv, pinned installs
   (`pip install pandas openpyxl`), script structure — per
   `coding-agent-skills:python-for-analysts`.
2. **Read defensively.** Real workbooks hide traps: header rows that start at row 3
   (`header=2`), merged cells (unmerge or expect NaNs), numbers stored as text
   (`pd.to_numeric(..., errors="coerce")` and count the coerced), dates as serials or strings,
   multiple sheets (`sheet_name=None` returns a dict). Type identifiers as strings
   (`dtype={"account_id": str}`) — a float round-trip strips leading zeros and corrupts join
   keys, a known data-integrity hazard class. For .xlsx, if the cell holds the *number* 4217
   under a `000000` display format, the zeros are already gone and `dtype=str` returns
   `"4217"`; the repair is at the export (emit text) or a zero-pad to the width the spec
   documents, never a width inferred from the data. Print `df.dtypes` and `df.head()` before trusting
   anything. The same discipline governs flat files — see
   `data-tools-skills:csv-and-flat-file-wrangling` when the source is CSV, not .xlsx.
3. **Write the data with pandas, then format with openpyxl:**

```python
import pandas as pd
with pd.ExcelWriter("report.xlsx", engine="openpyxl") as xw:
    summary.to_excel(xw, sheet_name="Summary", index=False)
    detail.to_excel(xw, sheet_name="Detail", index=False)
    ws = xw.sheets["Summary"]
    for col in ws.columns:  # width ≈ longest value
        w = max(len(str(c.value or "")) for c in col) + 2
        ws.column_dimensions[col[0].column_letter].width = min(w, 40)
    for cell in ws["B"][1:]:
        cell.number_format = "#,##0.00"
    ws.freeze_panes = "A2"
```

4. **Write formulas as strings** (`ws["B10"] = "=SUM(B2:B9)"`) when the workbook must stay live
   for users; compute in pandas when the numbers should be frozen facts. Know that openpyxl
   doesn't *evaluate* formulas — reading a formula cell back gives the formula (or the cached
   value with `data_only=True`, which is stale if the file wasn't saved by Excel since the data
   changed).
5. **Keep templates and data separate for recurring reports.** Load a styled template workbook
   (`openpyxl.load_workbook("template.xlsx")`), write fresh data into named ranges/known cells,
   save under a dated name. Styling lives in the template where a human maintains it; the script
   only moves numbers. Follow `data-tools-skills:data-file-hygiene` for the file side: dated
   immutable output names, raw/processed/output separation, and sanitizing anything you share.
   `references/excel-recipes.md` has the patterns (tables, charts, conditional formats,
   protected sheets) and a worked end-to-end example.
6. **When the data outgrows the workbook, don't fight it in openpyxl.** Aggregate first —
   `data-tools-skills:duckdb-local-analytics` queries .xlsx/CSV/Parquet directly with SQL — and
   write only the summarized result into the formatted deliverable.
7. **Verify the output like a deliverable:** open it (or re-read it with pandas) and check row
   counts, a couple of totals against the source, number formats on money columns, and that
   nothing landed as text. A report script without a check step just automates mistakes faster.

## Why / learn
Excel automation goes wrong when people treat a workbook like a CSV with decoration. A workbook
is a *document* — formats, formulas, merged regions, and stale cached values are part of its
truth — so the robust pattern is a clean split: pandas owns rectangular data (it is fast and
type-aware, and its `ExcelWriter` gives openpyxl a workbook to polish), openpyxl owns the
document layer (it edits the file's XML directly, which is why it can style anything but
evaluates nothing). Once you internalize "openpyxl never computes," the two classic bugs —
reading yesterday's cached formula values, and expecting a written formula to have a value
before Excel opens the file — stop being surprises. The template pattern is the same idea at
project scale: humans are better at maintaining *look*, scripts are better at moving *numbers*,
so let each own their layer and the report survives both a rebrand and a data change. And the
verification step is what makes automation trustworthy rather than merely fast — a script that
proves its totals against the source earns the right to replace hand work.

## Common mistakes
- `df = pd.read_excel(f)` and trusting it → check dtypes; numbers-as-text and shifted headers are the norm in the wild.
- Letting ID columns become floats on a read/resave round-trip → leading zeros stripped, join keys destroyed; type identifiers as strings end to end.
- Reading formula cells and expecting numbers → openpyxl returns the formula; `data_only=True` returns a possibly stale cache.
- Styling cell-by-cell for thousands of rows in Python → slow and unmaintainable; use a template workbook or column-level formats.
- Overwriting the one styled workbook the team loves → template + dated output files; never write over the template.
- Forgetting `index=False` in `to_excel` → a mystery unnamed first column in every deliverable.
- Skipping the verification step → automated wrong numbers look more credible than manual ones; check totals against source.

## Tailor to your environment
Wire in your current role here — this skill is domain-neutral and attaches to whatever
recurring workbooks you own wherever you work next: an analyst's monthly report, an attorney's
matter or billing summary, an ops manager's staffing workbook, a developer's release metrics.
Note your recurring workbooks in `references/your-environment.md` (real files under
`references/*.local.*`, git-ignored): which reports are scripted, their templates, sheet/column
contracts, and house number formats. Commit structure and sanitized examples only — **never a
real report with live figures**.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/excel-automation-python.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/excel-recipes.md — layer choice, defensive reading, tables, charts, conditional
  formatting, protection, performance, verification harness, and a worked end-to-end example
- references/your-environment.md — your scripted reports, templates, and format standards (fill in)
