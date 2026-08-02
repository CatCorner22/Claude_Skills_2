# Evals — data-tools-skills:pdf-data-extraction

## 1. Positive trigger (should load the skill)
> "Pull the transactions out of these PDF bank statements into a spreadsheet — my first attempt
> merged the date and description columns and the totals don't match the statement."

Expected: skill loads; classifies native vs scanned first; picks tool by table geometry;
tunes settings/bbox or explicit columns; stitches continuation lines and drops repeated
headers; validates with opening + credits − debits = closing.

## 2. Near-miss (should NOT load this skill)
> "What do the type codes in this BAI2 statement file mean and how do I map them?"

Expected: statement *data-format* knowledge — `banking-skills:bank-statement-parsing`. If this
skill loads, sharpen the PDF-specific framing.

## 3. Quality rubric
A good response:
- **Does the task:** correct extraction with a per-layout recipe (tool, mode, settings), typed
  amounts/dates, and the document's own totals reproduced as the acceptance test.
- **Teaches:** PDFs as page descriptions (tables are geometry reconstruction), why tool choice
  is a property of the document, and why OCR output is hypothesis until a control total confirms.
- **Safe:** never trusts extracted numbers without the balance check; recommends freezing a
  recipe with a totals assertion for recurring documents; no real statements in committed files.
