# Excel automation recipes (openpyxl / pandas)

## Contents
- Excel tables and autofilter
- Charts
- Conditional formatting
- Sheet protection
- Performance
- Reading landmines checklist

## Excel tables and autofilter
```python
from openpyxl.worksheet.table import Table, TableStyleInfo
tab = Table(displayName="Detail", ref=f"A1:F{ws.max_row}")
tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
ws.add_table(tab)          # gives users sorting/filtering and structured refs
# or minimal: ws.auto_filter.ref = ws.dimensions
```

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
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule
ws.conditional_formatting.add("D2:D500",
    CellIsRule(operator="lessThan", formula=["0"], font=Font(color="9C0006")))
ws.conditional_formatting.add("E2:E500",
    ColorScaleRule(start_type="min", start_color="FFF8696B",
                   end_type="max", end_color="FF63BE7B"))
```

## Sheet protection
```python
ws.protection.sheet = True
for cell in ws["B2":"B100"]:            # unlock input cells only
    for c in cell: c.protection = Protection(locked=False)
```
Protection is a guardrail against accidents, not security — the file format doesn't encrypt
cell locks.

## Performance
- Writing: `xlsxwriter` engine is faster for large write-only files
  (`pd.ExcelWriter(f, engine="xlsxwriter")`); openpyxl `write_only=True` mode streams rows.
- Reading: `read_only=True` for huge files; read only needed columns with `usecols`.
- Never style per-cell in a loop over 100k cells; apply formats per column or via the template.

## Reading landmines checklist
- [ ] Header row correct (`header=`), no title rows swallowed
- [ ] `df.dtypes` sane — money numeric, dates datetime, IDs as *strings* (leading zeros!)
- [ ] Merged cells produced NaNs where you expected values (`ffill` deliberately if so)
- [ ] Hidden sheets/rows accounted for (`wb.sheetnames`, row visibility if it matters)
- [ ] Trailing whitespace in keys stripped before any merge
- [ ] Row count matches the source system's count
