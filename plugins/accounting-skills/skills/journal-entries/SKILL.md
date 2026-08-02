---
name: journal-entries
description: >-
  Drafts and reviews journal entries — standard, accrual, deferral, reversing, reclassifying,
  and adjusting — keeping debits equal to credits and every line on its correct normal balance,
  with a clear memo and support. Use when creating, booking, or reviewing a journal entry, recording
  an accrual or deferral, or setting up a reversing entry. Triggers: journal entry, JE, book an entry,
  accrual, deferral, reversing entry, reclass, reclassifying entry, adjusting entry, debit and credit,
  top-side entry.
---

# Journal entries

## When to use
- Drafting or booking a journal entry: standard, accrual, deferral, reversing, reclass, or adjusting.
- Recording a period-end accrual or deferral, or the reversing entry that later clears it.
- Reviewing or approving a JE someone prepared — checking balance, accounts, normal balances, memo, support.
- Not for: learning debit/credit mechanics from scratch → see `accounting-skills:double-entry-fundamentals`.
  For where an entry lands across the account structure → see `accounting-skills:chart-of-accounts-design`.
  For running the whole period close → see `accounting-skills:month-end-close`.

## Do it
1. **Classify the entry and its purpose.** Name the type and why it exists this period:
   - *Standard* — records an actual transaction (invoice, payment, payroll).
   - *Accrual* — records revenue earned / expense incurred but not yet invoiced or paid.
   - *Deferral* — pushes cash already received/paid out to future periods (deferred revenue, prepaid).
   - *Reversing* — auto-clears a prior accrual/deferral on day one of the next period.
   - *Reclass* — moves a balance from one account to another to correct classification.
   - *Adjusting* — period-end entry (accrual, deferral, depreciation, estimate) to state the period correctly.
2. **Identify each account and its normal balance.** Assets and expenses are **debit-normal**; liabilities,
   equity, and revenue are **credit-normal**. Contra accounts flip (accumulated depreciation is a
   credit-normal contra-asset). Debit the account you are increasing if it is debit-normal; credit it if it
   is credit-normal. See `references/normal-balances.md`.
3. **Build the lines so total debits = total credits.** Every entry has ≥2 lines and must balance to the
   cent. If it does not balance, it will not post — do not plug a rounding line without explaining it.
4. **Write a memo that stands alone.** State *what, why, period, and basis of the amount* so a reviewer or
   auditor needs no verbal context (e.g. "Accrue June AWS usage per usage report; invoice expected mid-July").
   Attach or reference the support (calculation, contract, report) behind every estimate.
5. **Set the posting date and accounting period deliberately.** The date drives which period the entry hits;
   confirm the period is open and is the one you intend (cutoff matters — see `accounting-skills:month-end-close`).
6. **Plan the unwind for accruals and deferrals.** For an accrual, mark it to **reverse** next period so the
   real invoice posts normally without double-counting. For a deferral, schedule the **amortization** that
   moves it from the balance sheet to the P&L over the benefit period.
7. **Route for review and preserve the audit trail.** Preparer ≠ approver. Keep who prepared/approved, when,
   the support, and any edit history. Flag manual **top-side** entries (booked directly at the GL, bypassing
   a subledger) — they carry the most risk and deserve the closest review.

## Why / learn
Double-entry works because every transaction has two sides: a source and a use, a giver and a receiver. The
normal-balance rules fall straight out of the accounting equation — Assets = Liabilities + Equity, extended by
Revenue − Expenses. Debits raise the left side (assets, expenses); credits raise the right side (liabilities,
equity, revenue). Keeping debits equal to credits is simply keeping that equation true, which is why an entry
that does not balance is meaningless, not merely inconvenient. **Accruals and deferrals exist to serve the
matching principle**: revenue is recognized when earned and expense when incurred, regardless of when cash
moves. An accrual pulls an earned/incurred amount *into* the period that has not hit cash yet; a deferral
pushes an already-paid amount *out* to the periods that will consume it. That is what makes the P&L reflect
the period's real economic activity rather than its cash timing. **Reversing entries** are the clean-up for
accruals: booking the mirror image on the first day of the next period lets the actual invoice post the normal
way — its debit to expense is offset by the reversal's credit, so the cost is never counted twice. A **reclass**
never changes total debits and credits; it just relocates a balance to the right account, which is why it is
the safe fix for a misclassification and why it can leave net income unchanged even as it moves cost between
departments. The mechanics here are identical under US GAAP and IFRS — reversing entries in particular are a
bookkeeping convenience, not a standard requirement — so the mental model transfers across frameworks.

## Common mistakes
- Entry does not balance, so a plug line is added silently → the plug hides an error. Find the real second side.
- Booking to cash in an adjusting entry → most adjusting entries (accrual/deferral/depreciation) never touch cash.
- Accruing but forgetting to reverse → next period double-counts when the invoice arrives. Mark accruals to reverse.
- A one-line memo like "true-up" → useless to a reviewer. State what, why, period, and how the amount was derived.
- Debiting a credit-normal account to "increase" it (or vice versa) → check the account type before choosing a side.
- Preparer approves their own entry → breaks segregation of duties. Route to an independent approver.
- Posting to a closed or wrong period → the entry lands in the wrong month. Confirm the open period and the date.

## Tailor to your environment
Record your real conventions in `references/your-environment.md` (or `your-environment.private.md` if it names
real accounts — that suffix is git-ignored, so raw data never gets committed). Capture your ERP/GL, your JE
number and memo conventions, approval thresholds and who approves at each level, which accruals reverse
automatically, your standard recurring entries, and the account numbers you post common accruals and deferrals
to. The generic steps above then map onto your specific accounts and workflow.

## References
- references/normal-balances.md — account types, normal balances, contra accounts, and worked entry examples
- references/your-environment.md — your ERP, JE conventions, approval thresholds, and standard entries (add when supplied)
