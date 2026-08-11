---
name: fusion-fbdi-data-loading
description: >-
  Loads data into Oracle Fusion Cloud with File-Based Data Import (FBDI) — picks the right import
  template, fills it without breaking its hidden formatting rules, generates and uploads the zip,
  runs the interface loader and the module import job, and works the error-correction loop until
  every row lands. Covers GL journal import (GL_INTERFACE) in depth. Use when bulk-loading
  journals, invoices, or other records into Fusion, or when an FBDI load errors out. Triggers:
  FBDI, file-based data import, journal import, GL_INTERFACE, import journals, load data into
  fusion, FBDI template, interface loader, ESS import job, correct import errors, bulk load
  fusion.
---

# Fusion FBDI data loading

## When to use
- Bulk-loading records into Oracle Fusion Cloud through File-Based Data Import: GL journals,
  AP invoices, AR transactions, suppliers, bank statements, and similar.
- Diagnosing an FBDI load where rows rejected, the loader errored, or the import job completed
  with errors.
- Not for: keying a handful of journal lines → see
  `oracle-fusion-finance-skills:fusion-gl-and-journals` (UI or ADFdi). For pulling data *out* of
  Fusion via REST → see `data-tools-skills:rest-api-data-pulls`.

## Do it
1. **Get the template for your exact release.** Download the FBDI template from Oracle's
   File-Based Data Import guide for your module and release (e.g. "Journal Import" for GL).
   Templates change between releases — a stale template is a classic silent killer.
2. **Fill only what the template allows.** Each template is an .xlsm workbook with an instructions
   sheet and one or more data sheets. Keep every column in place (don't insert, delete, or
   reorder), respect required columns (marked with an asterisk), use the demanded date format
   (typically YYYY/MM/DD), and enter lookup codes not display names (e.g. currency `USD`, the
   *code* for category/source). For journal import specifically, the sheet maps to
   **GL_INTERFACE**: ledger ID, accounting date, source, category, currency, segment values in
   separate columns, and entered debit/credit — `references/journal-import-map.md` has the column map.
3. **Generate the zip with the template's own button.** Use the **Generate CSV File** macro on the
   instructions sheet — it writes the CSVs in the exact layout and zips them. Hand-saving the
   sheet as CSV breaks encodings, headers, and file names the loader expects.
4. **Upload and load in two stages.** In Fusion: Tools → Scheduled Processes →
   **Load Interface File for Import** — pick the target import process (e.g. "Import Journals")
   and the uploaded zip (via File Import and Export → `fin/generalLedger/import` account, or
   attach directly). This stage only moves rows into the interface table.
5. **Run the module import job** (for GL, **Import Journals**; AP uses "Import Payables Invoices,"
   etc.) and read its output report. Rows either become real records or stay in the interface
   table flagged with error codes.
6. **Work the correction loop.** For journals, run/read the **Journal Import Execution Report**:
   each error code names the failing validation (invalid combination, closed period, unbalanced
   batch, bad currency/date). Fix in the spreadsheet and re-load, or use the **Correct Import
   Errors** ADFdi sheet to patch interface rows in place. Before re-loading a fresh file, **delete
   the failed interface rows** (Delete Journal Import Data for the failed request) so you don't
   double-load.
7. **Verify like an accountant.** Row counts in = journals/invoices created + rejected; batch
   totals match the source file; spot-check one loaded record in the UI; and confirm the batch
   posted (journal import can post automatically or leave batches unposted for review).

## Why / learn
FBDI is a *staged* pipeline, and every mystery disappears once you see the three hops: file →
interface table → real record. The loader stage only checks file mechanics (layout, encoding,
names) — which is why the template's macro matters — while the import stage runs the same business
validations the UI would (combinations, periods, balancing). So a "load succeeded but nothing
imported" is not a contradiction: rows are parked in the interface table with error flags, waiting
for you. The whole discipline of FBDI — never touch template structure, codes not names, generate
don't hand-save — exists because the CSV contract between file and interface table is positional
and unforgiving, while everything after the interface table is ordinary Fusion validation you
already know from manual entry. Treat the execution report as the primary interface: it is the one
place Oracle tells you exactly which gate each row failed.

## Common mistakes
- Editing template structure (inserting/reordering columns) → loader misreads every row; refill a clean template.
- Hand-saving CSVs instead of the Generate CSV macro → wrong headers/encoding; always use the macro.
- Display names instead of lookup codes (source/category/currency) → rows reject; use codes.
- Running only "Load Interface File for Import" and stopping → data sits in the interface table; run the module import job too.
- Re-loading a fixed file without deleting failed interface rows → duplicates; purge failed rows first.
- Wrong or stale template release → subtle column mismatches; re-download for your release/module.
- Ignoring the execution report and re-trying blind → the report names the exact failing validation per row.

## Tailor to your environment
Keep your load specifics in `references/your-environment.md` (raw files and real values in
`your-environment.private.md`, git-ignored): which FBDI templates you use, your ledger IDs,
journal sources/categories reserved for loads, the UCM upload account, and who owns error
correction. Commit only sanitized structural examples — **never a real load file**.

## References
- references/journal-import-map.md — GL_INTERFACE column map, required fields, and common error codes
- references/your-environment.md — your templates, ledger IDs, sources, and upload paths (fill in)
