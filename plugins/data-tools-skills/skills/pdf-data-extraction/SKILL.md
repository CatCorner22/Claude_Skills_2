---
name: pdf-data-extraction
description: >-
  Extracts tables and text from PDFs into usable data — choosing between pdfplumber and camelot
  by PDF type, detecting scanned-vs-native pages, handling multi-page tables, bank-statement and
  invoice layouts, and validating extracted numbers against the document's own totals. Delivers
  a typed table (DataFrame/CSV/Excel) that reproduces the document's control totals, plus a
  frozen per-layout recipe for recurring documents. Use when
  pulling transactions from a PDF bank statement, tabling data out of a PDF report or invoice,
  or when a PDF extraction comes out scrambled. Triggers: extract pdf table, pdf to excel,
  pdfplumber, camelot, parse bank statement pdf, pdf invoice data, scanned pdf, OCR pdf,
  pdf text extraction, table extraction python.
metadata:
  version: "1.4.0"
---

# PDF data extraction

## When to use
- Turning PDF bank statements, invoices, or report tables into DataFrames/CSV/Excel.
- Debugging an extraction that merges columns, drops rows, or returns empty text.
- Not for: understanding statement *formats* like BAI2/camt.053 — those are data files, not PDFs
  — format-specific banking knowledge this library does not carry. For cleaning
  after a good extraction → see
  `data-analytics-bi-skills:data-cleaning`. If you have Anthropic's official `pdf` skill (from
  `anthropics/skills`), prefer it for creating/filling PDFs; this skill is about getting *data
  out*.

## Do it
1. **Classify the PDF first — it decides everything.** Open a page and try to select text. Text
   selects → **native** PDF (text layer exists; pdfplumber/camelot will work). Nothing selects →
   **scanned image** (you need OCR — `ocrmypdf` adds a text layer, then proceed as native; accept
   that OCR of numbers demands verification). Programmatic check:
   `not page.extract_text().strip()` ≈ scanned — pdfplumber returns an empty *string*, not
   `None`, so an `is None` test never fires.
2. **Pick the tool by table style.**
   - **pdfplumber** — the general workhorse: text with positions, and table extraction driven by
     ruling lines or alignment. Best when you need control or the layout is odd.
   - **camelot** — table-specialist, selected by `flavor=`. `lattice` (the default) reads drawn
     cell borders; `stream` reads whitespace alignment. Camelot 2.x adds `network` (borderless
     tables via text-edge connectivity), `hybrid`, `ml` (a table-structure model, needs
     `pip install 'camelot-py[ml]'`), and `auto` (per-page detection) — try those when
     `stream` plateaus on a borderless table. Quick win when the table is clean.
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
   them as a column, not noise, matching the wording the document actually prints rather than
   a remembered list; multi-line descriptions belong to the row above (stitch by detecting rows
   whose date/amount cells are empty, and log what you stitched — a heading you failed to
   recognize lands in that log rather than corrupting a description in silence).
5. **Type the result like a flat file.** Amounts arrive as strings with currency symbols, commas,
   parentheses-negatives, or trailing minus — normalize deliberately; dates per the document's
   locale; IDs as strings. (Same landmines as
   `data-tools-skills:csv-and-flat-file-wrangling` — reuse that discipline.)
6. **Validate against the document itself.** Statements and invoices carry their own controls:
   opening balance + credits − debits = closing balance; line items sum to the invoice total;
   page counts of transactions match a stated count when present. An extraction that doesn't
   reproduce the document's own totals is wrong somewhere — find the dropped or doubled rows.
   The assistant extracts and runs these checks; the human adjudicates OCR-uncertain digits the
   totals cannot confirm and owns the decision to rely on the output.
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
right" for the quantities that enter the sum. Know the edge of that proof: labels, sections, and
description text never touch the arithmetic, so a balance check that passes says nothing about
them, and they need their own eyes-on pass when you first freeze a layout. OCR adds one more
layer of the same lesson: it *guesses* characters from pixels, so its numbers are hypotheses
until a control total confirms them.

## Common mistakes
- Running table extraction on a scanned PDF and getting nothing → check for a text layer first; OCR, then extract.
- One tool for every PDF → match tool/mode to the table's geometry (borders → lattice; alignment → stream/pdfplumber).
- Ignoring repeated page headers in multi-page tables → phantom rows corrupt sums; drop them by pattern.
- Letting multi-line descriptions become separate rows → stitch rows with empty date/amount cells to the row above, and guard the first one: with nothing above it, `rows[-1]` raises.
- Trusting extracted amounts without the balance check → dropped/doubled rows are the norm, not the exception.
- Parsing `(1,234.56)` or `1.234,56` naively → normalize accounting negatives and locale decimals deliberately.
- Re-tuning by hand every month → freeze a per-layout recipe with a totals assertion; re-tune only when it fails.

## Tailor to your environment
Catalog your recurring PDFs in `references/your-environment.md` (real documents in
`references/*.local.*`, git-ignored): document type, native or scanned, the tool/settings recipe
that works, and the internal totals used for validation. **Never commit real statements or
invoices.**

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/pdf-data-extraction.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/pdf-recipes.md — pdfplumber/camelot settings, OCR pipeline, statement/invoice layout patterns
- references/your-environment.md — your document types and frozen extraction recipes (fill in)
