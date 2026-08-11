# Fusion close sequence: blockers and skeleton (reference)

## Contents
- Per-module close blockers and sweeps
- Day-by-day close skeleton
- Reopen policy

## Per-module close blockers and sweeps
| Module | Must be true to close | Typical blockers | Sweep/fix |
|---|---|---|---|
| AP | All invoices validated + accounted; payments accounted | Invoices needing revalidation; unaccounted payments; incomplete PPRs | Validate batch; Create Accounting final; complete or cancel in-flight PPRs; "Complete/sweep" unaccounted to next period per policy |
| AR | Transactions complete + accounted; receipts applied/accounted; AutoInvoice clear | Incomplete transactions; stuck AutoInvoice lines; unaccounted receipts | Work AutoInvoice exceptions; Create Accounting final; complete or delete incomplete transactions |
| FA | Depreciation run; additions/retirements accounted | Unposted mass additions; depreciation not run | Post/clear mass additions; run depreciation; Create Accounting |
| CE | Statements loaded and reconciled through period end | Missing statements; unreconciled lines; missing external transactions | Load statements; triage unmatched; create external transactions |
| Tax | Tax accounted with the transactions | Usually rides AP/AR closes | — |
| GL | All subledgers transferred; no unposted journals; recons done | Untransferred SLA accounting; unposted batches; journal import rows in interface | Transfer to GL; post or delete batches; clear/delete interface rows |

## Day-by-day close skeleton
- **Day -2/-1:** cutoff comms; pre-close sweeps (validate AP, AutoInvoice exceptions, mass
  additions); confirm statement feeds current.
- **Day 1:** AP close (validate, account, close period); AR close (complete, account, close);
  start FA depreciation.
- **Day 2:** FA close; CE reconciliation tie-out; all Create Accounting final + transfer;
  post all GL journals; accruals and standard entries.
- **Day 3:** subledger-to-GL control account reconciliations (AP trial balance vs control;
  AR aging vs control); revaluation and translation; close GL period; open next periods.
- **Day 4/5:** reporting, flux/variance review, sign-offs, file evidence.
Compress once stable — the order is the invariant, the days are ambition.

## Reopen policy
- Reopen requires: named approver, reason logged, and a re-run of everything invalidated
  (transfers, recons, reports) — which is why the bar is high.
- Prefer booking in the current open period with disclosure over reopening, unless materiality
  or compliance forces the reopen.
- Permanently Closed only after audit sign-off for the year; it cannot be undone.
