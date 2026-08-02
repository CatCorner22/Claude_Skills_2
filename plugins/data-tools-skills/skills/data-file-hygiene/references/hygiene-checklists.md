# Data-file hygiene checklists (reference)

## Contents
- Sanitization scrub by file type
- Sensitive-data classes
- Project folder checklist
- Archive / retirement checklist

## Sanitization scrub by file type

### Excel (.xlsx)
- [ ] Replace identifiers in *all* sheets — including hidden sheets (`unhide all` first)
- [ ] Delete or refresh pivot caches (a pivot remembers source rows even after deletion) —
      safest: paste sanitized values into a fresh workbook
- [ ] Check defined names, header/footer, and comments/notes for names and account numbers
- [ ] File → Info → Inspect Document (Document Inspector) for metadata, hidden rows/columns,
      personal info
- [ ] Break external links (they leak source paths and can pull real data on open)
- [ ] Re-save under a sanitized name (the filename itself may name a client)

### CSV / flat files
- [ ] Scrub identifier columns with consistent, shape-preserving fakes
- [ ] Check free-text columns (descriptions, memos) — names and account numbers hide there
- [ ] Confirm no real values survive in the header row or a trailing footer
- [ ] Regenerate rather than hand-edit when the file came from a script

### PDFs
- [ ] Real redaction tools only (black-box drawing over text leaves the text selectable)
- [ ] Check document properties/metadata (author, title) 
- [ ] For statements/invoices: prefer recreating a synthetic example over redacting a real one

### Code / notebooks
- [ ] No credentials, hostnames, or tokens in code, comments, or notebook *output cells*
- [ ] Clear notebook outputs before committing (outputs embed the data they displayed)
- [ ] Connection strings via environment variables; `.env` files git-ignored

## Sensitive-data classes (default; align to your policy)
| Class | Examples | Handling |
|---|---|---|
| Credentials | passwords, tokens, keys | Never in files at all — secrets manager/env vars |
| Direct identifiers | account numbers, IBANs, tax IDs, names + contact | Sanitize before any sharing |
| Quasi-identifiers | customer + amount + date combinations | Sanitize or aggregate; combinations re-identify |
| Business-confidential | balances, margins, forecasts | Share on need-to-know channels only |
| Structural | column layouts, formats, code | Shareable once scrubbed of the above |

## Project folder checklist
- [ ] `raw/` present, untouched, source noted in README (system, date, who pulled it)
- [ ] `scripts/` regenerate everything in `processed/` and `output/`
- [ ] README says: purpose, data sources, how to rerun, owner
- [ ] Naming: `<dataset>_<scope>_<date>[_vN].<ext>`, ISO dates, no spaces
- [ ] Sensitive files only in paths your `.gitignore` (or equivalent) excludes

## Archive / retirement checklist
- [ ] Deliverables archived *with* the exact inputs and script versions that produced them
- [ ] Raw retained/deleted per retention policy (note the policy applied)
- [ ] Regenerable intermediates deleted
- [ ] Archive README: what this was, final state, where the evidence lives
