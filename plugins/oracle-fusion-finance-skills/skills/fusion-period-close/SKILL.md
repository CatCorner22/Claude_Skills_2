---
name: fusion-period-close
description: >-
  Drives period close in Oracle Fusion Cloud — the subledger-to-GL close sequence (AP, AR, FA,
  projects, then GL), period statuses per module, exception sweeps (unaccounted transactions,
  stuck interface rows), subledger-to-GL reconciliation, and the Close Monitor/close calendar.
  Use when closing a period in Fusion, deciding the close order, chasing why a period won't
  close, or reconciling a subledger to its GL control account at close. Triggers: period close
  fusion, close the period, period status, can't close period, close AP period, sweep
  unaccounted, subledger close, close monitor, period end fusion, exceptions preventing close.
---

# Fusion period close

## When to use
- Running or sequencing month-end/period close across Fusion subledgers and GL, or unblocking a
  module period that refuses to close.
- Reconciling subledgers (AP, AR) to their GL control accounts at close, or standing up a close
  calendar/Close Monitor discipline.
- Not for: the accounting content of close (accruals, estimates, checklist design) → see
  `accounting-skills:month-end-close`. For the AR aging tie-out detail → see
  `oracle-fusion-finance-skills:fusion-ar-and-collections`.

## Do it
1. **Sequence subledgers before GL — always.** The dependency order is: transactional modules
   finish → their accounting transfers to GL → GL closes. A practical order: AP (and payments) →
   AR (and receipts) → fixed assets (depreciation) → projects/inventory where used → tax → GL.
   Cash Management reconciliation (see
   `oracle-fusion-finance-skills:fusion-cash-management-module`) ties out alongside.
2. **Use period statuses as the control they are.** Each module has its own period status
   (Open / Closed; GL adds **Never Opened, Future Enterable, Permanently Closed**). Closing a
   module period is the assertion "no more transactions here this period." Close subledger
   periods first so nothing new can arrive while GL finalizes; reopen deliberately and rarely —
   every reopen is a control exception worth logging.
3. **Sweep exceptions before attempting the close.** A module period close is blocked (or made
   dishonest) by: **unaccounted transactions** (run Create Accounting final; review the
   exceptions report), **incomplete/unvalidated documents** (AP invoices needing revalidation,
   incomplete AR transactions), and **stuck interface rows** (AutoInvoice, journal import,
   statement loads). Each module has an exception report — run it, fix or sweep to next period
   per policy, and only then close. `references/close-sequence.md` maps blockers by module.
4. **Transfer and post everything to GL.** Create Accounting (final, with transfer) per
   subledger, then confirm no untransferred SLA accounting and no unposted journals in GL for
   the period. The GL period can't honestly close with journals sitting unposted.
5. **Reconcile subledger to GL control accounts.** AP trial balance = AP liability control
   account; AR aging = AR control account. Differences come from manual journals booked straight
   to control accounts (prevent via account rules), unposted/untransferred activity, or cutoff
   items. Name every dollar before signing the reconciliation.
6. **Close GL and revalue/translate if multicurrency.** Run revaluation of foreign-currency
   balances and translation for reporting currencies per policy, then close the GL period.
   Open the next period(s) — including Future Enterable where the flow needs it.
7. **Run the close on a calendar with owners.** Day -2 to Day +5 task list: each task has a
   module, an owner, a dependency, and evidence. Fusion's **Close Monitor / close checklist**
   tooling (or your own tracker) makes status visible; the discipline (see
   `accounting-skills:month-end-close`) matters more than the tool.

## Why / learn
Close order isn't tradition — it's data dependency. GL is downstream of every subledger, so a GL
"close" done while AP is still accounting invoices is a statement built on moving sand; the
period-status ladder exists to freeze upstream layers one at a time so the downstream snapshot
means something. The exception sweeps are the honest version of "we're done": an unaccounted
transaction is a business event with no accounting yet, and closing around it doesn't make it
disappear — it makes next month's open items and this month's statements disagree. Control-account
reconciliation is the proof of the whole structure: the subledger is the detail, the GL account
is the summary, and if they differ, either activity didn't flow (mechanical) or someone wrote
directly on the summary (control failure). That's also why "reopen the period" should feel
expensive: each reopen invalidates the frozen snapshot everyone downstream — consolidation, FP&A,
audit — already consumed.

## Common mistakes
- Closing GL while subledgers are open → late entries force reopens; close subledgers first.
- Closing around unaccounted transactions → this month closes, next month inherits the mess; sweep first.
- Manual journals directly to AP/AR control accounts → permanent recon noise; restrict via account rules.
- Ignoring interface tables at close → stuck AutoInvoice/journal-import rows are unrecorded activity; clear or document them.
- Treating Permanently Closed casually → it's irreversible; use plain Closed until audit sign-off.
- No owner per close task → "everyone's" task closes late; one name per task on the calendar.
- Skipping revaluation/translation in multicurrency ledgers → FX sits wrong in equity/income; run per policy before close.

## Tailor to your environment
Keep your close design in `references/your-environment.md` (entity-level specifics in
`your-environment.private.md`, git-ignored): module close order and target days, period-status
owners per module, exception reports you run, control accounts and who reconciles each, and
your reopen policy. Commit structure, not real balances.

## References
- references/close-sequence.md — per-module blockers, sweep jobs, and a day-by-day close skeleton
- references/your-environment.md — your close calendar, owners, control accounts (fill in)
