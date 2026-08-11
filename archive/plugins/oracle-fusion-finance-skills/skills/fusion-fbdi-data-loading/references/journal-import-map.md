# GL journal import (GL_INTERFACE) column map and errors (reference)

Directional map for the Journal Import FBDI template. **Always confirm against the template for
your release** — columns shift between releases.

## Contents
- Key columns
- Import job parameters
- Common error codes
- Correction options

## Key columns
| Template column | What it is | Notes |
|---|---|---|
| Status | Load status marker | Template sets `NEW`; leave it |
| Ledger ID | Target ledger's numeric ID | Look it up (Manage Primary Ledgers or an OTBI query); not the name |
| Effective Date of Transaction | Accounting date | Template date format (YYYY/MM/DD); must fall in an open or future-enterable period |
| Journal Source | Source *code* | Use a code reserved for imports (not "Manual"); source controls approval/AutoPost behavior |
| Journal Category | Category *code* | e.g. `Accrual`, `Adjustment` — the code, not display name |
| Currency Code | Entered currency | ISO code, e.g. `USD` |
| Segment1..SegmentN | COA segment values, one per column | Order = your chart's segment order; all segments filled |
| Entered Debit / Entered Credit | Line amounts | One side per line; batch must balance by balancing segment |
| Converted Debit/Credit | Accounted amounts | Only for user-rate conversions; usually blank with a rate type |
| Currency Conversion Rate / Type / Date | FX conversion | Rate type code (e.g. `Corporate`) or explicit user rate |
| Batch Name / Journal Entry Name | Grouping names | Make them traceable to the source file |
| Line Description | Line text | What the reviewer will read — write it for them |
| Reference columns (1–10) | Batch/journal/line references | Useful for drill-back to the source system |

## Import job parameters
- **Load Interface File for Import** → Import Process: *Import Journals*; Data File: your zip.
- **Import Journals** → Ledger, Source; options include Post Journals (auto-post after import)
  and Create Summary Journals (collapse to one line per account — keep detail for audit unless
  volume forces summarization).

## Common error codes (Journal Import Execution Report)
| Code family | Meaning | Fix |
|---|---|---|
| EU02 / invalid period | Accounting date not in an open/future-enterable period | Open the period or change the date |
| EF01–EF05 (flexfield) | Invalid segment value or combination, or CVR failure | Correct segment values; validate the combination manually in the UI |
| EC01–EC12 (currency) | Bad currency code, missing/invalid rate or rate date | Fix the code, rate type, or supply the rate |
| EB (balance) | Batch or journal out of balance by balancing segment | Correct amounts; check suspense settings |
| EL (ledger) | Ledger ID wrong or user lacks access | Verify the numeric ledger ID and data access set |
| ES (source/category) | Source or category code not defined | Use defined codes; check Manage Journal Sources/Categories |

## Correction options
1. **Fix the file** and re-load — first run *Delete Journal Import Data* for the failed request so
   interface rows don't duplicate.
2. **Correct Import Errors** ADFdi workbook — edit failed interface rows in place, re-import.
3. For systemic errors (a bad mapping in the source extract), fix upstream and regenerate; don't
   hand-patch hundreds of rows.
