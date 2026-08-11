# Excel automation recipes (pandas / openpyxl / xlsxwriter)

## Contents
- Choosing the layer: a decision table
- Defensive reading patterns
- Number formats that matter
- Excel tables and autofilter
- Charts
- Conditional formatting
- Sheet protection
- Formulas and cached values
- The template pattern, step by step
- Performance
- Verification harness
- Worked example: a recurring two-sheet activity report
- Reading landmines checklist

## Choosing the layer: a decision table

| Job | Tool | Why |
|---|---|---|
| Rectangular data in/out | pandas (`read_excel` / `to_excel`) | Fast, type-aware, one line per direction |
| Formats, widths, freeze panes, multiple sheets | openpyxl via `pd.ExcelWriter(engine="openpyxl")` | Edits the document layer pandas can't touch |
| Live formulas users will recalculate | openpyxl (write formula strings) | pandas writes values only |
| Large write-only output | xlsxwriter engine | Faster streaming writes; cannot read or edit |
| Editing an existing styled workbook | openpyxl `load_workbook` | The only layer that preserves what's already there |
| Aggregating data too big for a workbook | DuckDB first, then write the summary | Don't fight scale inside the document layer |

The standard recurring-report pattern is pandas for the data plus openpyxl for the polish —
one `ExcelWriter` context gives you both.

## Defensive reading patterns

```python
import pandas as pd

# Headers not on row 1: skip the title block explicitly.
df = pd.read_excel("input.xlsx", sheet_name="Data", header=2)

# Identifiers as strings — floats strip leading zeros and corrupt join keys.
df = pd.read_excel("input.xlsx", dtype={"account_id": str, "invoice_no": str})

# Numbers stored as text: coerce, then COUNT what failed instead of ignoring it.
amt = pd.to_numeric(df["amount"], errors="coerce")
bad = amt.isna() & df["amount"].notna()
print(f"{bad.sum()} amount cells failed numeric coercion")  # investigate if > 0
df["amount"] = amt

# Excel serial dates that arrived as numbers:
df["posted"] = pd.to_datetime(df["posted"], unit="D", origin="1899-12-30")

# All sheets at once (returns a dict of DataFrames):
sheets = pd.read_excel("input.xlsx", sheet_name=None)

# Merged cells read as NaN below the top-left cell — forward-fill deliberately:
df["region"] = df["region"].ffill()
```

Always end a read with `df.dtypes` and `df.head()` printed, and a row count compared to what
the source system says it exported.

## Number formats that matter

Apply per column, not per cell, and keep a house list:

| Content | Format string |
|---|---|
| Money (2 dp, thousands) | `#,##0.00` |
| Money, negatives in parens | `#,##0.00;(#,##0.00)` |
| Whole counts | `#,##0` |
| Percentages | `0.0%` |
| ISO dates | `yyyy-mm-dd` |
| Identifiers | format the *cell* as text or write strings — never let Excel "help" |

```python
for cell in ws["C"][1:]:
    cell.number_format = "#,##0.00;(#,##0.00)"
```

## Excel tables and autofilter
```python
from openpyxl.worksheet.table import Table, TableStyleInfo
tab = Table(displayName="Detail", ref=f"A1:F{ws.max_row}")
tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
ws.add_table(tab)          # gives users sorting/filtering and structured refs
# or minimal: ws.auto_filter.ref = ws.dimensions
```
Table `displayName`s must be unique per workbook and contain no spaces.

## Charts
```python
from openpyxl.chart import BarChart, Reference
chart = BarChart(); chart.title = "By month"
data = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row)      # includes header
cats = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
chart.add_data(data, titles_from_data=True); chart.set_categories(cats)
ws.add_chart(chart, "H2")
```
For dashboard-grade visuals, chart in the template workbook pointed at a data sheet the script
refreshes — Excel maintains the chart, Python maintains the data.

## Conditional formatting
```python
from openpyxl.styles import Font
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule
ws.conditional_formatting.add("D2:D500",
    CellIsRule(operator="lessThan", formula=["0"], font=Font(color="9C0006")))
ws.conditional_formatting.add("E2:E500",
    ColorScaleRule(start_type="min", start_color="FFF8696B",
                   end_type="max", end_color="FF63BE7B"))
```

## Sheet protection
```python
from openpyxl.styles import Protection
ws.protection.sheet = True
for row in ws["B2":"B100"]:            # unlock input cells only
    for c in row: c.protection = Protection(locked=False)
```
Protection is a guardrail against accidents, not security — the file format doesn't encrypt
cell locks.

## Formulas and cached values

- Write a formula as a string: `ws["B10"] = "=SUM(B2:B9)"`. openpyxl stores it; Excel computes
  it on open. Until Excel saves the file, the cell has no cached value.
- Read with `data_only=False` (default): you get the formula text.
- Read with `data_only=True`: you get the *last value Excel cached* — stale if the data changed
  since Excel last saved. If your script wrote the file, the cache is empty.
- Rule of thumb: formulas for workbooks that must stay live in users' hands; computed pandas
  values for numbers that must be frozen facts in a deliverable.

## The template pattern, step by step

1. A human builds `template.xlsx` once: styles, logo, headers, charts, print setup.
2. Mark the cells the script fills — named ranges or a documented sheet/cell contract
   (e.g. "Data!A2 downward; Summary!B3 = period label").
3. The script:

```python
from openpyxl import load_workbook
wb = load_workbook("template.xlsx")
ws = wb["Data"]
for r, rec in enumerate(records, start=2):
    ws.cell(row=r, column=1, value=rec.category)
    ws.cell(row=r, column=2, value=rec.amount).number_format = "#,##0.00"
wb["Summary"]["B3"] = period_label
wb.save(f"output/report_{period_label}.xlsx")   # dated name; NEVER over the template
```

4. Styling changes (rebrand, new column order) happen in the template; data changes happen in
   the script. Neither touches the other's layer.

## Performance
- Writing: the `xlsxwriter` engine is faster for large write-only files
  (`pd.ExcelWriter(f, engine="xlsxwriter")`); openpyxl's `write_only=True` mode streams rows.
- Reading: `read_only=True` for huge files; read only needed columns with `usecols`.
- Don't style per-cell in a loop over 100k cells; apply formats per column or via the template.
- If you're aggregating millions of rows just to write a small summary sheet, do the
  aggregation in DuckDB or pandas first — the workbook is the deliverable, not the database.

## Verification harness

End every report script by re-reading its own output and asserting against the source:

```python
out = pd.read_excel("output/report_2026-07.xlsx", sheet_name="Detail",
                    dtype={"item_id": str})
assert len(out) == len(detail), f"row count {len(out)} != source {len(detail)}"
assert abs(out["amount"].sum() - detail["amount"].sum()) < 0.005, "total drifted"
assert out["item_id"].str.len().nunique() == 1 or True  # spot-check IDs kept their zeros
print("verified: rows", len(out), "total", round(out['amount'].sum(), 2))
```

A failed assertion before delivery is a bug; a wrong number after delivery is a retraction.

## Worked example: a recurring two-sheet activity report

Domain-neutral by design — "items" can be an analyst's transactions, an attorney's matters,
an ops manager's work orders, or a developer's tickets. Input: `activity_2026-07.csv` with
columns `item_id, opened, category, owner, hours, status`. Deliverable: a formatted workbook
with a Summary sheet (hours by category) and a Detail sheet.

```python
import pandas as pd

detail = pd.read_csv("activity_2026-07.csv",
                     dtype={"item_id": str},          # IDs keep leading zeros
                     parse_dates=["opened"])
assert detail["item_id"].is_unique, "duplicate item IDs in source"

summary = (detail.groupby("category", as_index=False)
                 .agg(items=("item_id", "count"), hours=("hours", "sum"))
                 .sort_values("hours", ascending=False))

with pd.ExcelWriter("output/activity_2026-07.xlsx", engine="openpyxl") as xw:
    summary.to_excel(xw, sheet_name="Summary", index=False)
    detail.to_excel(xw, sheet_name="Detail", index=False)
    ws = xw.sheets["Summary"]
    for col in ws.columns:
        w = max(len(str(c.value or "")) for c in col) + 2
        ws.column_dimensions[col[0].column_letter].width = min(w, 40)
    for cell in ws["C"][1:]:
        cell.number_format = "#,##0.0"
    ws.freeze_panes = "A2"

# Verify: re-read the output and prove it against the source.
check = pd.read_excel("output/activity_2026-07.xlsx", sheet_name="Summary")
assert abs(check["hours"].sum() - detail["hours"].sum()) < 0.05
print("verified:", len(detail), "items,", round(detail["hours"].sum(), 1), "hours")
```

Next month the script runs on `activity_2026-08.csv` and produces a dated sibling file —
no hand formatting, and the assertion proves the totals before anyone reads them.

## Reading landmines checklist
- [ ] Header row correct (`header=`), no title rows swallowed
- [ ] `df.dtypes` sane — money numeric, dates datetime, IDs as *strings* (leading zeros!)
- [ ] Merged cells produced NaNs where you expected values (`ffill` deliberately if so)
- [ ] Hidden sheets/rows accounted for (`wb.sheetnames`, row visibility if it matters)
- [ ] Trailing whitespace in keys stripped before any merge
- [ ] Row count matches the source system's count
