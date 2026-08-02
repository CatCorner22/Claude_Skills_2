# Close checklist template (reference)

A checklist template organized by **business day (WD)** offset. WD1 = first business day of the new month.
Adjust offsets to your target close length. Every task needs an **owner**, a **reviewer**, and its
**dependencies**. Copy this into `references/your-environment.md` and fill in names, systems, and thresholds.

## Contents
- Pre-close (WD-2 to WD-1)
- Subledger close (WD1)
- GL close and accruals (WD1–WD2)
- Reconciliations (WD2–WD3)
- Intercompany & consolidation (WD3–WD4)
- Review, flux & lock (WD4–WD5)

## Pre-close (WD-2 to WD-1)
| Task | Owner | Reviewer | Depends on |
|---|---|---|---|
| Confirm close calendar published, owners notified | | | |
| Chase open POs / uninvoiced receipts list for accruals | | | |
| Confirm bank feeds / statements available | | | |

## Subledger close (WD1)
| Task | Owner | Reviewer | Depends on |
|---|---|---|---|
| Close AP (freeze invoice entry) | | | |
| Close AR / billing | | | |
| Run payroll accrual / post payroll | | | |
| Close inventory / cost | | | |
| Run depreciation, close fixed assets | | | |

## GL close and accruals (WD1–WD2)
| Task | Owner | Reviewer | Depends on |
|---|---|---|---|
| Post standard/recurring entries (depreciation, amortization, allocations) | | | Subledgers closed |
| Post accruals (uninvoiced expense, accrued revenue) | | | Cutoff list |
| Post/amortize deferrals (prepaids, deferred revenue) | | | |
| Confirm prior-period accruals reversed | | | |

## Reconciliations (WD2–WD3)
| Task | Owner | Reviewer | Depends on |
|---|---|---|---|
| Bank reconciliations (cash-management-skills:bank-reconciliation) | | | Bank statements |
| Subledger-to-GL tie-outs (AP, AR, FA, inventory control accounts) | | | Subledgers closed |
| Balance-sheet account recs, risk-ranked (accounting-skills:account-reconciliations) | | | Entries posted |
| Clearing / suspense accounts cleared to zero | | | |

## Intercompany & consolidation (WD3–WD4)
| Task | Owner | Reviewer | Depends on |
|---|---|---|---|
| Confirm intercompany balances mirror & agree | | | IC entries posted |
| Resolve intercompany out-of-balances | | | |
| Run consolidation / eliminations | | | Entities closed |
| FX translation (if multi-currency) | | | Rates loaded |

## Review, flux & lock (WD4–WD5)
| Task | Owner | Reviewer | Depends on |
|---|---|---|---|
| Flux/variance analysis vs prior, budget, forecast (above threshold) | | | TB final |
| Controller / management review & sign-off | | | Flux done |
| Hard close: lock period, restrict posting | | | Sign-off |
| Archive close binder (checklist, recs, support) | | | Period locked |
