---
name: pdf-data-extraction
description: >-
  Extracts tables and text from PDFs into usable data — choosing between pdfplumber and camelot
  by PDF type, detecting scanned-vs-native pages, handling multi-page tables, bank-statement and
  invoice layouts, and validating extracted numbers against the document's own totals. Use when
  pulling transactions from a PDF bank statement, tabling data out of a PDF report or invoice,
  or when a PDF extraction comes out scrambled. Triggers: extract pdf table, pdf to excel,
  pdfplumber, camelot, parse bank statement pdf, pdf invoice data, scanned pdf, OCR pdf,
  pdf text extraction, table extraction python.
---

# PDF data extraction

## When to use
- Turning PDF bank statements, invoices, or report tables into DataFrames/CSV/Excel.
- Debugging an extraction that merges columns, drops rows, or returns empty text.
- Not for: understanding statement *formats* like BAI2/camt.053 (those are data files, not PDFs)
  → see `banking-skills:bank-statement-parsing`. For cleaning after a good extraction → see
  `data-analytics-bi-skills:data-cleaning`. If you have Anthropic's official `pdf` skill (from
  `anthropics/skills`), prefer it for creating/filling PDFs; this skill is about getting *data
  out*.

## Do it
1. **Classify the PDF first — it decides everything.** Open a page and try to select text. Text
   selects → **native** PDF (text layer exists; pdfplumber/camelot will work). Nothing selects →
   **scanned image** (you need OCR — `ocrmypdf` adds a text layer, then proceed as native; accept
   that OCR of numbers demands verification). Programmatic check: `page.extract_text()`
   returning nothing ≈ scanned.
2. **Pick the tool by table style.**
   - **pdfplumber** — the general workhorse: text with positions, and table extraction driven by
     ruling lines or alignment. Best when you need control or the layout is odd.
   - **camelot** — table-specialist with two modes: `lattice` (tables with drawn cell borders)
     and `stream` (whitespace-aligned tables, no borders). Quick win when the table is clean.
   - Text-only needs (paragraphs, key-value fields on invoices) → pdfplumber `extract_text()`
     plus targeted regex.
3. **Extract, then look at what you got:**

```python
import pdfplumber
with pdfplumber.open("statement.pdf") as pdf:
    rows = []
    for page in pdf.pages:
        for t in page.extract_tables():
            rows += t
# Inspect: how many rows? do columns line up? where did headers repeat?
```

   If columns merge or split, tune `table_settings` (strategy `"lines"` vs `"text"`, snap/join
   tolerances) or crop to the table's bbox first — `references/pdf-recipes.md` has the settings
   that matter and per-layout patterns.
4. **Handle document structure explicitly.** Multi-page tables re-print headers (drop repeated
   header rows); statements interleave section headers ("Deposits", "Withdrawals") — capture
   them as a column, not noise; multi-line descriptions belong to the row above (stitch by
   detecting rows whose date/amount cells are empty).
5. **Type the result like a flat file.** Amounts arrive as strings with currency symbols, commas,
   parentheses-negatives, or trailing minus — normalize deliberately; dates per the document's
   locale; IDs as strings. (Same landmines as
   `data-tools-skills:csv-and-flat-file-wrangling` — reuse that discipline.)
6. **Validate against the document itself.** Statements and invoices carry their own controls:
   opening balance + credits − debits = closing balance; line items sum to the invoice total;
   page counts of transactions match a stated count when present. An extraction that doesn't
   reproduce the document's own totals is wrong somewhere — find the dropped or doubled rows.
7. **For a recurring document, freeze the recipe.** Lock the per-layout settings (bbox, strategy,
   column positions, header patterns) in a script keyed to the document type; when the bank
   redesigns the statement, the totals check fails loudly and you re-tune once.

## Why / learn
A PDF is a *page-description* format: it says "draw these characters at these coordinates," and
any table you see is an optical illusion assembled by your eye. Extraction is therefore geometry
reconstruction — grouping characters into words, words into columns, rows out of vertical
positions — which is why tools differ by *what geometric evidence they use* (camelot-lattice
trusts drawn lines, stream and pdfplumber's text strategy trust alignment) and why the right
tool is a property of the document, not of taste. It's also why extraction is inherently
fragile: a slightly shifted column or a wrapped description changes the geometry, not the data.
The antidote is the document's own arithmetic — statements and invoices are self-checking
documents, and using their internal totals as an assertion converts "looks right" into "proves
right." OCR adds one more layer of the same lesson: it *guesses* characters from pixels, so its
numbers are hypotheses until a control total confirms them.

## Common mistakes
- Running table extraction on a scanned PDF and getting nothing → check for a text layer first; OCR, then extract.
- One tool for every PDF → match tool/mode to the table's geometry (borders → lattice; alignment → stream/pdfplumber).
- Ignoring repeated page headers in multi-page tables → phantom rows corrupt sums; drop them by pattern.
- Letting multi-line descriptions become separate rows → stitch rows with empty date/amount cells to the row above.
- Trusting extracted amounts without the balance check → dropped/doubled rows are the norm, not the exception.
- Parsing `(1,234.56)` or `1.234,56` naively → normalize accounting negatives and locale decimals deliberately.
- Re-tuning by hand every month → freeze a per-layout recipe with a totals assertion; re-tune only when it fails.

## Tailor to your environment
Catalog your recurring PDFs in `references/your-environment.md` (real documents in
`references/*.local.*`, git-ignored): document type, native or scanned, the tool/settings recipe
that works, and the internal totals used for validation. **Never commit real statements or
invoices.**

## References
- references/pdf-recipes.md — pdfplumber/camelot settings, OCR pipeline, statement/invoice layout patterns
- references/your-environment.md — your document types and frozen extraction recipes (fill in)
