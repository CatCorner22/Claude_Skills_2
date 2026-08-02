---
name: month-end-close
description: >-
  Runs a structured month-end close — cutoff, accruals, subledger-to-GL tie-outs, reconciliations,
  intercompany, and flux/variance review — tracked on a close checklist with owners and a close calendar.
  Use when closing the books, building a close calendar or checklist, sequencing close tasks, or reviewing
  close status. Triggers: month-end close, period close, period end, close checklist, close calendar, cutoff,
  flux analysis, variance review, soft close, hard close.
---

# Month-end close

## When to use
- Closing the books for a period, or building/updating the close calendar and checklist.
- Sequencing close tasks, assigning owners, or reviewing where the close stands and what is blocking it.
- Performing cutoff, accrual, subledger-to-GL, intercompany, or flux/variance steps as part of a close.
- Not for: reconciling one specific balance-sheet account in depth → see `accounting-skills:account-reconciliations`.
  For a bank statement vs. book cash rec → see `cash-management-skills:bank-reconciliation`. To standardize and
  improve the close process itself → see `continuous-improvement-skills:standard-work`.

## Do it
1. **Publish the close calendar with owners.** Lay tasks on business-day offsets (WD-1, WD1, WD2 …) with an
   **owner and a reviewer** for each, and map dependencies (subledgers close before the GL ties out; recons
   follow the entries they depend on). The calendar is the plan; the checklist is how you track it — see
   `references/close-checklist.md`.
2. **Enforce cutoff and completeness.** Freeze the subledgers (AP, AR, payroll, inventory, fixed assets) and
   confirm every transaction is in the **right period**: goods/services received by period-end are recorded
   even if uninvoiced; nothing from the next period has leaked in. Cutoff answers *right period*; completeness
   answers *is everything captured*. Together they are the foundation everything else rests on.
3. **Book accruals and deferrals.** Record earned/incurred amounts not yet invoiced (accruals) and amortize
   or defer amounts already paid (deferrals). Flag accruals to reverse next period. Mechanics and reversals
   live in `accounting-skills:journal-entries`.
4. **Tie subledgers to the GL.** For each subledger, reconcile its ending balance to the GL control account
   (AP subledger = AP control; AR subledger = AR control; FA register = fixed-asset accounts). A difference
   here means an entry bypassed the subledger or a posting failed — resolve it before moving on.
5. **Reconcile the balance sheet.** Reconcile balance-sheet accounts to independent support, prioritizing by
   risk. This is its own discipline — see `accounting-skills:account-reconciliations`. Clearing and suspense
   accounts should clear to zero.
6. **Settle and tie out intercompany.** Confirm intercompany balances **mirror** across entities and agree,
   then eliminate on consolidation. Chase any intercompany out-of-balance to its source — a one-sided IC entry
   is the usual culprit — before you consolidate.
7. **Run flux / variance analysis.** Compare actuals to prior period, budget, and forecast at the account or
   line level. **Explain every movement above your materiality threshold** with a real business reason, not a
   restatement of the number. Flux review is the last net that catches a missed accrual or a miscoding that
   every earlier tie-out passed.
8. **Decide soft vs. hard close and lock the period.** A **soft close** produces preliminary numbers with some
   estimates open; a **hard close** finalizes and locks the period from further posting. Get sign-off, lock the
   period, and archive the checklist, recs, and support as the audit trail.

## Why / learn
A close is a controlled hand-off: it turns a month of transactions into financial statements someone will rely
on, so its whole job is to make those numbers **complete, in the right period, and explained**. **Cutoff and
completeness come first because they are unrecoverable later** — if a period-end expense was never captured or a
next-month sale slipped in, no downstream reconciliation creates the missing amount or removes the stray one; it
just ties out to the wrong total. Everything after cutoff is a *check* on numbers that must already be right. The
sequence is dependency-driven for the same reason: subledgers close before you tie them to the GL, and accounts
are reconciled after the entries that populate them, because a check is only meaningful once its inputs are final.
**Flux analysis is the close's reasonableness test** — tie-outs prove the numbers are *internally consistent*, but
only comparing the P&L and balance sheet against expectations catches a figure that is consistent yet *wrong* (a
doubled accrual reconciles perfectly to its own — wrong — schedule). The soft/hard distinction manages the tension
between speed and finality: report early on estimates, then lock once support is complete, so you neither delay the
business nor leave the books open to change after people have acted on them. These close mechanics are framework-
neutral — US GAAP and IFRS differ on *measurement and disclosure*, not on the discipline of cutoff, tie-outs, and
review — so the process transfers across both.

## Common mistakes
- Treating cutoff as a formality → a missed period-end accrual can't be recovered by any later step. Get cutoff right first.
- No owner or reviewer per task → tasks stall and no one is accountable. Assign both on the calendar.
- Ignoring subledger-to-GL differences → an entry bypassed the subledger; the control account is wrong. Tie out every one.
- Flux commentary that restates the number ("expense up 12%") → not an explanation. Give the business reason.
- Consolidating with an intercompany out-of-balance → it won't eliminate. Fix the one-sided IC entry first.
- Leaving clearing/suspense accounts non-zero at close → they accumulate silently. Clear and reconcile them.
- Locking (hard close) before recons and flux are reviewed → you finalize errors. Review, then lock.

## Tailor to your environment
Put your real close in `references/your-environment.md` (or `your-environment.private.md` if it names real entities
or systems — that suffix is git-ignored). Capture your business-day calendar and target close days, task owners and
reviewers, your subledgers and their control accounts, your materiality threshold for flux, your intercompany and
consolidation setup, and where you archive the close binder. The generic checklist then becomes *your* checklist.

## References
- references/close-checklist.md — a business-day close checklist template (tasks, owners, dependencies, WD offsets)
- references/your-environment.md — your close calendar, subledgers, thresholds, and systems (add when supplied)
