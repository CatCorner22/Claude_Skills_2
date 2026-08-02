---
name: csv-and-flat-file-wrangling
description: >-
  Ingests real-world CSV and flat-file exports safely — detecting encodings and delimiters,
  surviving bank/ERP export quirks (BOMs, footers, quoted commas, leading-zero IDs, mixed date
  formats), validating the parsed schema, and merging files without silent row loss. Use when
  loading a CSV that parses wrong, combining exports from different systems, or hardening a
  recurring file feed. Triggers: csv parsing, delimiter, encoding error, utf-8 vs latin-1, BOM,
  pipe delimited, fixed width file, load csv pandas, merge csv files, bank export csv, leading
  zeros lost, csv broken columns.
---

# CSV and flat-file wrangling

## When to use
- Loading CSV/TSV/pipe-delimited/fixed-width exports from banks, ERPs, or vendors — especially
  when the parse comes out wrong (shifted columns, mojibake, lost zeros).
- Merging or appending multiple flat files into one dataset for analysis.
- Not for: deep cleaning after a correct parse (dedupe, outliers, imputation) → see
  `data-analytics-bi-skills:data-cleaning`. For statement-specific formats (BAI2, camt.053,
  MT940) → see `banking-skills:bank-statement-parsing`.

## Do it
1. **Look at the raw bytes before parsing.** `head -c 500 file.csv | xxd | head` (or open in a
   text editor showing invisibles). You're checking: encoding clues (a `EF BB BF` UTF-8 BOM;
   high bytes suggesting Latin-1/Windows-1252), the actual delimiter (comma, semicolon, pipe,
   tab), quoting style, line endings, and whether there are title/footer rows around the data.
2. **Parse explicitly — never rely on defaults for a recurring feed:**

```python
import pandas as pd
df = pd.read_csv(
    "export.csv",
    encoding="utf-8-sig",        # eats a BOM; try "cp1252" if accents garble
    sep=",",                     # set it; don't let a sniffer guess in production
    dtype={"account_id": "string", "invoice_no": "string"},  # IDs are text!
    parse_dates=["posting_date"], dayfirst=False,
    skiprows=0, skipfooter=0, engine="python",  # adjust for title/footer rows
    thousands=",",               # if amounts come as "1,234.56"
    na_values=["", "NULL", "N/A"],
)
```

   Fixed-width files → `pd.read_fwf` with explicit `colspecs` from the file spec.
3. **Validate the parse before using it.** Row count vs the source system's count; column count
   and names vs the expected schema; `df.dtypes` (amounts numeric, IDs still have their leading
   zeros, dates are datetimes not strings); min/max of dates and amounts as a sanity band; and
   a known total (sum of amounts) against a control figure when one exists.
4. **Fix quirks at the parse, not downstream.** Shifted columns usually mean unquoted delimiters
   in a text field (fix quoting/sep, or the export itself); `1.234,56` means European decimal
   convention (`decimal=","`, `thousands="."`); dates flipping month/day mid-file mean two
   source formats — parse with an explicit `format=` per slice and fail loudly on the rest.
   `references/flat-file-quirks.md` is the quirk-to-fix table.
5. **Merge without silent loss.** Appending files: assert identical schemas first, add a
   `source_file` column, then `pd.concat`. Joining: normalize keys (strip, case, zero-pad),
   then `df.merge(..., how="outer", indicator=True)` once and *look at* `_merge` counts before
   settling on the final join type — unmatched rows are findings, not noise.
6. **Harden the recurring feed.** Wrap the load in a function that runs the step-3 checks and
   raises on violation; log filename, row count, and totals per run. When the vendor changes the
   layout (they will), the load fails at the door instead of poisoning the analysis.

## Why / learn
A flat file has no schema — every load is an act of *interpretation*, and the parser will happily
misinterpret in silence: Latin-1 bytes read as UTF-8 become mojibake, an unquoted comma shifts
every column after it, and `read_csv`'s type inference turns account "00123" into the number 123.
The whole discipline is therefore to make interpretation explicit (encoding, delimiter, dtypes,
date formats are *declared*, not guessed) and then to *prove* the parse with counts and control
totals, exactly like reconciling a statement. The reason IDs are always strings is that identity
data has no arithmetic meaning — the moment it becomes a number, leading zeros, huge values
(scientific notation!), and checksums are corrupted. And the outer-join-with-indicator habit
exists because a join is a claim ("these keys correspond"); the `_merge` column is the audit of
that claim, and skipping it is how a thousand rows quietly vanish from a reconciliation.

## Common mistakes
- Letting pandas infer ID columns → leading zeros lost, long IDs in scientific notation; `dtype="string"` for identifiers.
- Guessing encoding until the error goes away → mojibake survives silently; inspect bytes, then declare.
- Ignoring the BOM → a phantom `\ufeff` in the first column name breaks every rename; `utf-8-sig`.
- Parsing European numbers as US → amounts off by orders of magnitude; set `decimal`/`thousands`.
- `how="inner"` as the default join → unmatched keys silently dropped; outer + `indicator=True` first, then decide.
- Skipping footer rows into the data → a "Total" row doubles your sum; `skipfooter`/filter it explicitly.
- No row-count/total check on a recurring feed → layout changes poison months of analysis before anyone notices.

## Tailor to your environment
Document each recurring feed in `references/your-environment.md` (real files in
`references/*.local.*`, git-ignored): source system, encoding, delimiter, schema, known quirks,
and the control totals you validate against. Sanitized structural examples only — **never real
bank or customer exports**.

## References
- references/flat-file-quirks.md — symptom → cause → fix table for encodings, delimiters, numbers, dates
- references/your-environment.md — your feeds, layouts, and validation contracts (fill in)
