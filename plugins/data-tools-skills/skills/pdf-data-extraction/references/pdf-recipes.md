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
| Table aligned by whitespace, no borders | camelot `flavor="stream"`, or `"network"`/`"ml"` when stream plateaus, or pdfplumber text strategy |
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
tables[0].parsing_report   # accuracy/whitespace/confidence — low accuracy = wrong flavor/areas
```

## OCR pipeline for scanned PDFs
```bash
ocrmypdf --deskew --rotate-pages input.pdf ocr.pdf   # adds a text layer via Tesseract
```
Then extract as native. Expect: 0/O, 1/l/I, 5/S confusions in amounts — the balance check is
mandatory, and a human review threshold for low-confidence pages is reasonable policy.

## Bank-statement pattern
1. Crop to the transaction table region per page (headers/footers/marketing out).
2. Extract rows; keep section headings (Deposits / Withdrawals / Fees) as a `section` column,
   listing them exactly as this document prints them.
3. Stitch continuation lines: a row with empty date and amount is description overflow —
   append to previous row's description, skipping blank spacer rows and refusing (loudly) to
   stitch one that arrives before the first transaction.
4. Normalize amounts (strip currency symbols/commas; parens or trailing minus → negative;
   debit/credit columns → one signed column with the sign convention documented).
5. Assert: opening + sum(credits) − sum(debits) = closing (per the statement's own figures).

All five steps in one pass — repeated headers dropped, section headings captured, continuation
lines stitched, parens/trailing-minus negatives signed, and the statement's own arithmetic used
as the assertion:

```python
import pdfplumber, pandas as pd, re

HDR = ("Date", "Description", "Amount")
# The exact headings *this* statement prints — copy them off the document, don't recall
# them. A heading you leave out (banks write "Electronic Withdrawals", "Deposits and
# Other Credits") is invisible to the balance check below, because it only reads
# amounts: the heading gets stitched onto the previous row's description and every
# row after it keeps the stale `section`. The stitch log at the end is how you see that.
SECTIONS = {"Deposits", "Withdrawals", "Fees"}

def amount(s):            # "(750.25)" -> -750.25 ; "1,200.00-" -> -1200.0 ;
                          # "-750.25" -> -750.25 ; "" -> None
    s = (s or "").replace(",", "").replace("$", "").strip()
    if not s:
        return None
    # Leading "-" must be tested here: the re.sub below strips every "-", so a plain
    # negative would otherwise come back positive — a sign inversion that reconciles.
    neg = (s.startswith("(") and s.endswith(")")) or s.startswith("-") or s.endswith("-")
    return (-1.0 if neg else 1.0) * float(re.sub(r"[()\-]", "", s))

rows, section, stitched, orphans = [], None, [], []
with pdfplumber.open("statement.pdf") as pdf:
    for page in pdf.pages:
        for tbl in page.extract_tables():
            for r in tbl:
                date, desc, amt = [(x or "").strip() for x in r[:3]]
                if (date, desc, amt) == HDR:              # repeated page header
                    continue
                if not date and not amt:
                    if not desc:
                        continue                          # blank spacer row
                    if desc in SECTIONS:
                        section = desc                    # section heading, not a row
                    elif rows:
                        rows[-1]["description"] += " " + desc  # continuation line
                        stitched.append(desc)
                    else:
                        orphans.append(desc)              # nothing to attach it to
                else:
                    rows.append({"section": section, "date": date,
                                 "description": desc, "amount": amount(amt)})

# A dateless line before the first transaction means the crop or the heading list is
# wrong, not that the statement has data there — say so instead of raising IndexError
# on `rows[-1]` (a blank spacer row or an unlisted heading at the top does exactly that).
assert not orphans, f"dateless text before the first transaction: {orphans}"
if stitched:                  # read this once per layout before freezing the recipe
    print("stitched as continuations (a heading in this list is a missing SECTIONS entry):")
    for line in stitched:
        print("   ", line)

df = pd.DataFrame(rows)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

OPENING, CLOSING = 1000.00, 2835.25       # read off the statement itself, not computed
assert abs(OPENING + df["amount"].sum() - CLOSING) < 0.005, \
    f"balance check failed: {OPENING + df['amount'].sum():.2f} != {CLOSING:.2f}"
```

On a two-page statement whose rows are +2,500.00, +110.50, −750.25, −25.00, this yields four
typed rows carrying their section, and `1,000.00 + 1,835.25 = 2,835.25` passes. Every failure
of that assertion is a dropped, doubled, or mis-signed row — find it before shipping the table.
Note the reach of the check, though: only amounts enter the arithmetic, so a wrong `section`
label or a heading absorbed into a description passes it untouched. That is what the stitch log
is for — it is the only signal that the `SECTIONS` list doesn't match the document.

## Invoice pattern
1. Header fields by regex on text: invoice number, dates, PO number, supplier
   (`re.search(r"Invoice\s*(?:No|#)\s*[:.]?\s*(\S+)", text, re.I)` — the `re.I` is not
   optional: `INVOICE NO:` in all caps is the common case and the pattern misses it without).
2. Line-item table by the table tools above.
3. Assert: sum(line totals) = subtotal; subtotal + tax = total. Route failures to a human.
4. Per-supplier recipes: invoices are template-stable per sender — key the recipe on supplier.
