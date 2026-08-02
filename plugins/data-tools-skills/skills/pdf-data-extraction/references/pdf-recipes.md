# PDF extraction recipes (reference)

## Contents
- Tool cheat sheet
- pdfplumber settings that matter
- camelot settings that matter
- OCR pipeline for scanned PDFs
- Bank-statement pattern
- Invoice pattern

## Tool cheat sheet
| Situation | Tool/mode |
|---|---|
| Table with drawn cell borders | camelot `flavor="lattice"` |
| Table aligned by whitespace, no borders | camelot `flavor="stream"` or pdfplumber text strategy |
| Odd layouts, need coordinates/control | pdfplumber |
| Key-value fields (invoice no, dates, totals) | pdfplumber `extract_text()` + regex |
| Scanned/image pages | `ocrmypdf` first, then any of the above |
| Just need raw text fast | `pdfplumber` or `pypdf` text extraction |

## pdfplumber settings that matter
```python
table_settings = {
    "vertical_strategy": "lines",     # "lines" if ruled, "text" if alignment-based
    "horizontal_strategy": "lines",
    "snap_tolerance": 3,              # merge nearly-aligned edges
    "join_tolerance": 3,
    "text_x_tolerance": 2,            # word grouping; raise if letters split
}
page.crop((x0, top, x1, bottom)).extract_table(table_settings)  # crop to the table's bbox
```
- Debug visually: `page.to_image().debug_tablefinder(table_settings).save("dbg.png")` shows the
  detected grid — the fastest way to see *why* columns merged.
- Explicit column boundaries when detection fails:
  `"vertical_strategy": "explicit", "explicit_vertical_lines": [x0, x1, x2, ...]`.

## camelot settings that matter
```python
import camelot
tables = camelot.read_pdf("doc.pdf", pages="1-end", flavor="stream",
                          table_areas=["50,700,550,80"],   # x1,y1,x2,y2 (PDF coords)
                          columns=["90,180,320,420,500"])  # explicit column x-positions
tables[0].parsing_report   # accuracy/whitespace metrics — low accuracy = wrong flavor/areas
```

## OCR pipeline for scanned PDFs
```bash
ocrmypdf --deskew --rotate-pages input.pdf ocr.pdf   # adds a text layer via Tesseract
```
Then extract as native. Expect: 0/O, 1/l/I, 5/S confusions in amounts — the balance check is
mandatory, and a human review threshold for low-confidence pages is reasonable policy.

## Bank-statement pattern
1. Crop to the transaction table region per page (headers/footers/marketing out).
2. Extract rows; keep section headings (Deposits / Withdrawals / Fees) as a `section` column.
3. Stitch continuation lines: a row with empty date and amount is description overflow —
   append to previous row's description.
4. Normalize amounts (strip currency symbols/commas; parens or trailing minus → negative;
   debit/credit columns → one signed column with the sign convention documented).
5. Assert: opening + sum(credits) − sum(debits) = closing (per the statement's own figures).

## Invoice pattern
1. Header fields by regex on text: invoice number, dates, PO number, supplier
   (`r"Invoice\s*(?:No|#)\s*[:.]?\s*(\S+)"` style — anchor per supplier layout).
2. Line-item table by the table tools above.
3. Assert: sum(line totals) = subtotal; subtotal + tax = total. Route failures to a human.
4. Per-supplier recipes: invoices are template-stable per sender — key the recipe on supplier.
