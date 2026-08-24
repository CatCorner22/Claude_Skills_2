---
name: csv-and-flat-file-wrangling
description: >-
  Ingests real-world CSV and flat-file exports safely — inspecting raw bytes before parsing,
  detecting encodings and delimiters, declaring an explicit read_csv contract (encoding,
  separator, string-typed IDs, date formats, na_values) instead of trusting inference,
  surviving export quirks (BOMs, footer rows, quoted commas, European decimals, and the
  numeric-coercion hazard that strips leading zeros from join keys),
  validating every parse against row counts and control figures, and merging with an
  outer-join-plus-indicator audit so unmatched rows surface as findings instead of vanishing.
  Use when loading a CSV that parses wrong, combining exports from different systems, or
  hardening a recurring file feed to fail loudly on layout changes. Triggers: csv parsing, delimiter, encoding error, utf-8 vs latin-1, BOM, pipe
  delimited, fixed width file, load csv pandas, merge csv files, bank export csv, leading
  zeros lost, csv broken columns, mojibake, flat file feed.
metadata:
  version: "1.4.1"
---

# CSV and flat-file wrangling

## When to use
- Loading CSV/TSV/pipe-delimited/fixed-width exports from any upstream system — an ERP, a case
  or ticket system, a vendor portal, a bank — especially when the parse comes out wrong
  (shifted columns, mojibake, lost zeros).
- Merging or appending multiple flat files into one dataset for analysis.
- Not for: deep cleaning after a correct parse (dedupe, outliers, imputation) → see
  the archived `data-analytics-bi-skills:data-cleaning`. Statement-specific formats (BAI2, camt.053, MT940) are
  format-specific knowledge (a banking-domain topic this library does not carry; formerly at
  `archive/`), not general flat-file wrangling.
- Not for: sources that aren't flat files — a workbook (.xlsx) → openpyxl/pandas directly (the
  archived `data-tools-skills:excel-automation-python` carries the full recipes, restorable
  from `archive/`); a PDF report or statement → see
  `data-tools-skills:pdf-data-extraction`. Both hand their output back to this skill's typing
  discipline.

## Do it
1. **Look at the raw bytes before parsing.** `head -c 500 file.csv | xxd | head` — `xxd` ships
   with vim, so on a box without it use `head -c 500 file.csv | od -An -tx1z | head`; `od` is
   POSIX and always present, though the trailing `z` (the ASCII gutter beside the hex) is a GNU
   extension, so drop it to plain `-tx1` if a BSD/macOS `od` rejects the type string (or open
   the file in a text editor showing invisibles). You're checking:
   encoding clues (a `EF BB BF` UTF-8 BOM; high bytes suggesting Latin-1/Windows-1252), the
   actual delimiter (comma, semicolon, pipe, tab), quoting style, line endings, and whether
   there are title/footer rows around the data.
2. **Parse explicitly — never rely on defaults for a recurring feed:**

```python
import pandas as pd
df = pd.read_csv(
    "export.csv",
    encoding="utf-8-sig",        # eats a BOM; try "cp1252" if accents garble
    sep=",",                     # set it; don't let a sniffer guess in production
    dtype={"account_id": "string", "invoice_no": "string"},  # IDs are text!
    parse_dates=["posting_date"], dayfirst=False,
    skiprows=0, skipfooter=0,    # adjust for title/footer rows; leave the engine unset —
                                 # skipfooter>0 makes pandas fall back to its python engine
                                 # by itself, and pinning it costs ~6x on a large file
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
   `references/flat-file-quirks.md` is the symptom → cause → fix table, with a worked
   two-system merge example.
5. **Merge without silent loss.** Appending files: assert identical schemas first, add a
   `source_file` column, then `pd.concat`. Joining: normalize keys (strip, case, zero-pad),
   then `df.merge(..., how="outer", indicator=True)` once and *look at* `_merge` counts before
   settling on the final join type — unmatched rows are findings, not noise.
6. **Too big for pandas, or the job is really a join?** Point
   `data-tools-skills:duckdb-local-analytics` at the files and do it in SQL — the same
   declare-the-types discipline applies there (`types={'id':'VARCHAR'}`), because DuckDB's
   sniffer can mistype IDs exactly like pandas.
7. **Harden the recurring feed.** Wrap the load in a function that runs the step-3 checks and
   raises on violation; log filename, row count, and totals per run — structure the script per
   the archived `coding-agent-skills:python-for-analysts`. Keep the raw export pristine and separate from
   processed outputs per `data-tools-skills:data-file-hygiene`; when the vendor changes the
   layout (they will), the load fails at the door instead of poisoning the analysis.

## Why / learn
A flat file has no schema — every load is an act of *interpretation*, and the parser will happily
misinterpret in silence: Latin-1 bytes read as UTF-8 become mojibake, an unquoted comma shifts
every column after it, and `read_csv`'s type inference turns account "00123" into the number 123.
The numeric-coercion form of that hazard is the worst, because it corrupts *identity*: an ID
like `0006789599` round-tripped through numeric inference comes back as the integer `6789599`;
add one null to that column and it becomes the float `6789599.0`; and a 19-digit ID in that same
float column is written back out as `6.78959912345679e+18`. Every join against the original keys
goes quiet, and nothing errors — a known hazard class this library documents from hard
experience. The whole discipline is therefore to make interpretation
explicit (encoding, delimiter, dtypes, date formats are *declared*, not guessed) and then to
*prove* the parse with counts and control totals, exactly like reconciling a statement. The
reason IDs are always strings is that identity data has no arithmetic meaning — the moment it
becomes a number, leading zeros, huge values (scientific notation!), and checksums are
corrupted. And the outer-join-with-indicator habit exists because a join is a claim ("these
keys correspond"); the `_merge` column is the audit of that claim, and skipping it is how a
thousand rows quietly vanish from an analysis.

## Common mistakes
- Letting pandas infer ID columns → leading zeros lost, long IDs in scientific notation, join keys destroyed; `dtype="string"` for identifiers.
- Guessing encoding until the error goes away → mojibake survives silently; inspect bytes, then declare.
- Ignoring the BOM → an invisible marker rides on the first column name (`ï»¿account_id` once you fall back to `cp1252`, `\ufeffaccount_id` in readers that decode UTF-8 without stripping it, like the stdlib `csv` module) and every rename misses; declare `utf-8-sig` rather than relying on pandas, which happens to strip it for you.
- Parsing European numbers as US → amounts off by orders of magnitude; set `decimal`/`thousands`.
- `how="inner"` as the default join → unmatched keys silently dropped; outer + `indicator=True` first, then decide.
- Skipping footer rows into the data → a "Total" row doubles your sum; `skipfooter`/filter it explicitly.
- No row-count/total check on a recurring feed → layout changes poison months of analysis before anyone notices.

## Tailor to your environment
Wire in your current role here — this skill is domain-neutral and attaches to whatever feeds
you inherit wherever you work next: an analyst's system exports, an attorney's e-billing or
docket extracts, an ops manager's vendor files, a developer's log or usage dumps. Document
each recurring feed in `references/your-environment.md` (real files in
`references/*.local.*`, git-ignored): source system, encoding, delimiter, schema, known
quirks, and the control totals you validate against. Sanitized structural examples only —
**never real customer or account-bearing exports**.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/csv-and-flat-file-wrangling.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/flat-file-quirks.md — symptom → cause → fix tables for encodings, delimiters,
  numbers, dates, structure, and keys; the hardened-loader pattern; a worked two-system merge
- references/your-environment.md — your feeds, layouts, and validation contracts (fill in)
