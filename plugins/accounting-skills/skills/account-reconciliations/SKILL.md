---
name: account-reconciliations
description: >-
  Performs balance-sheet account reconciliations (not bank recs) — prepaids, accruals, fixed assets,
  intercompany, and other GL accounts — proving each balance against independent support with a supporting
  schedule, classified and aged reconciling items, roll-forwards, and risk-ranking. Use when reconciling a GL
  balance-sheet account, building a supporting schedule, or reviewing a reconciliation. Triggers: account
  reconciliation, balance sheet reconciliation, GL rec, reconciling items, supporting schedule, roll-forward,
  risk-ranking accounts, prepaid schedule, accrual reconciliation.
---

# Account reconciliations

## When to use
- Reconciling a GL **balance-sheet** account (prepaids, accruals, fixed assets, intercompany, other assets/liabilities).
- Building the supporting schedule that proves a balance, or classifying and aging reconciling items.
- Reviewing a reconciliation someone prepared, or risk-ranking accounts to set reconciliation frequency.
- Not for: reconciling a **bank statement** to book cash — that ties two records of the *same* cash, not a GL
  balance to independent support → see `cash-management-skills:bank-reconciliation`. For running the whole period
  close these recs sit inside → see `accounting-skills:month-end-close`.

## Do it
1. **State what the rec must prove.** A balance-sheet account rec asserts one thing: the GL balance is **real,
   correctly valued, and supported** by evidence outside the GL. Write down the account, the GL balance, and the
   as-of date before touching numbers.
2. **Build the supporting schedule (the independent side).** Assemble the detail that *should* equal the balance,
   from a source other than the GL — the prepaid amortization schedule, the accrual detail, the fixed-asset
   register, the intercompany confirmation, the loan amortization table. The schedule total is your proof of the
   balance. See `references/reconciliation-schedule.md`.
3. **Compare and isolate reconciling items.** Reconciling items = GL balance − supported balance. **Explain each
   item; never plug the difference.** An unexplained residual is a finding, not a rounding line.
4. **Classify every reconciling item.** Put each into exactly one bucket:
   - **Timing** — will self-clear next period (an accrual reversing, an in-transit item).
   - **Errors / misclassifications** — a correcting entry is required now.
   - **Unsupported / unknown** — no evidence yet; the highest-risk bucket and the one reviewers care about.
5. **Age the reconciling items.** Bucket open items by age (0–30 / 31–60 / 61–90 / 90+ days). Aging turns a static
   difference into a trend: an item that persists across periods is almost always an error or an unsupported
   balance masquerading as timing.
6. **Choose roll-forward vs. point-in-time.** For accounts that move by defined activity (fixed assets, prepaids,
   accruals, debt), reconcile as a **roll-forward**: opening balance + additions − reductions = closing balance,
   and tie the closing balance to the GL. For accounts that are just a list at a date (e.g. a deposits balance),
   a **point-in-time** schedule of the components is enough. Roll-forwards also prove the *activity*, not only the
   ending number.
7. **Risk-rank the account and set frequency.** Rate each account **high / medium / low** on size, volatility,
   estimation/judgment, and history of errors. High-risk accounts get a full rec every period with detailed
   support and independent review; low-risk, stable accounts can be reconciled less often or with lighter support.
8. **Apply preparer/reviewer controls and sign off.** Preparer ≠ reviewer. The reviewer checks that the support
   genuinely proves the balance, that items are classified and aged, and that action owners and dates exist for
   open items. Retain the rec, the schedule, and the support as the audit trail.

## Why / learn
A balance-sheet reconciliation is an **assurance** procedure: unlike a P&L account, which is a period's flow that
closes to zero, a balance-sheet account **carries forward**, so an error planted in it survives every future period
until someone proves the balance wrong. That is exactly what a rec does — it re-proves the balance from evidence
that does **not** come from the GL, because tying the GL to itself proves nothing. The independent support is the
whole point: if the prepaid balance equals the amortization schedule built from the underlying contracts, the
balance is real; if it does not, the gap is either explainable (timing) or a problem (error/unsupported), and the
rec's job is to force that distinction. **Unexplained reconciling items are findings, not noise** — plugging them
to make the rec tie destroys the only control the rec provides, the same way plugging a bank rec does. Aging is
what keeps timing honest: a genuine timing item clears; one that ages past a period or two was never timing. The
roll-forward earns its keep on activity-driven accounts because proving *opening + activity = closing* catches an
error in the movement that a point-in-time total would hide. And **risk-ranking is how finite review time is
spent well** — reconciling a volatile, judgment-heavy accrual with the same rigor as a stable clearing account
wastes effort where risk is low and starves it where risk is high. Under both US GAAP and IFRS the reconciliation
discipline is identical; the frameworks differ on how the *underlying balance* is measured, so reconcile to the
schedule your accounting policy produces.

## Common mistakes
- Reconciling the GL to the GL (e.g. to a trial-balance extract) → proves nothing. Support must be independent of the GL.
- Plugging the difference to make it tie → destroys the control. An unexplained item is a finding to investigate.
- Calling a persistent difference "timing" → real timing clears. If it ages past a period or two, it's an error/unsupported.
- Point-in-time schedule on an activity-driven account → hides errors in the movement. Roll it forward.
- Same rigor and frequency for every account → misallocated effort. Risk-rank and match frequency to risk.
- Preparer reviews their own rec → no independent check. Reviewer must be separate and actually test the support.
- Open items with no owner or due date → they never clear. Assign an action and a date to each.

## Tailor to your environment
Record your real reconciliation setup in `references/your-environment.md` (or `your-environment.private.md` if it
names real accounts/balances — that suffix is git-ignored, so raw data never gets committed). Capture which
accounts you reconcile and their risk rating and frequency, where each account's independent support comes from,
your reconciling-item aging thresholds and escalation rules, your preparer/reviewer assignments, and any
reconciliation tool you use. The generic steps then run against your actual accounts and support sources.

## References
- references/reconciliation-schedule.md — supporting-schedule and roll-forward templates, item classification, and the risk-ranking matrix
- references/your-environment.md — your accounts, support sources, aging thresholds, and reviewers (add when supplied)
