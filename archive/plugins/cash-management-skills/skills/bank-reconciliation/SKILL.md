---
name: bank-reconciliation
description: >-
  Reconciles a bank statement to the ledger or system cash balance, matches transactions,
  classifies outstanding and in-transit items, and investigates breaks until the difference
  resolves to zero. Use when reconciling a bank account, chasing an unreconciled difference,
  reviewing someone's reconciliation, or setting up matching/tolerance rules. Triggers: bank
  reconciliation, recon, reconcile the bank, unreconciled, outstanding items, deposits in
  transit, outstanding checks, statement vs book, reconciling difference, break.
---

# Bank reconciliation

## When to use
- Reconciling a bank account's statement to the GL/subledger or a system cash balance for a period.
- Investigating an unreconciled difference or classifying outstanding / in-transit items.
- Reviewing a reconciliation someone else prepared, or designing matching/tolerance rules.
- Not for: GL balance-sheet account reconciliations (prepaids, accruals) → see
  `accounting-skills:account-reconciliations`. For detecting unusual items statistically → also
  use `machine-learning-skills:anomaly-detection`.

## Do it
1. **Frame the reconciliation.** State the two balances being tied and the as-of date/cutoff:
   the **bank** side (ending balance per the statement) and the **book** side (GL/system cash
   balance). Confirm both are the same account, same currency, same cutoff time.
2. **Assemble both sides to one schema.** Pull statement lines and book lines for the period and
   normalize each to: `date, amount, direction (debit/credit), reference, description, source`.
   If the statement is a bank file (BAI2 / MT940 / CAMT.053 / CSV), normalize it first — see
   `banking-skills:bank-statement-parsing`.
3. **Match in priority order.** Match one-to-one first (exact amount + date window + reference),
   then one-to-many and many-to-one (e.g. a deposit batch vs. individual receipts). Apply a
   **tolerance** only to one-to-one matches, and only if your policy allows it — see
   `references/matching-and-tolerance.md`.
4. **Classify every unmatched item** into exactly one bucket:
   - **Timing differences** (self-clearing): deposits in transit, outstanding/unpresented checks,
     payments in transit.
   - **Bank-only items** you must record: bank fees, interest, returned items, FX differences.
   - **True differences**: errors (yours or the bank's), duplicates, missing entries, possible fraud.
5. **Build the reconciliation to zero.** Start from the bank ending balance; add deposits in
   transit; subtract outstanding checks → **adjusted bank balance**. Start from the book balance;
   add/subtract bank-only items you now record → **adjusted book balance**. The two adjusted
   balances **must equal**. Any residual is an unexplained break — do not force or plug it.
6. **Age the open items and write the exceptions.** Produce the reconciliation schedule, an aging
   of open items (0–30 / 31–60 / 60+ days), and a one-line note per true difference with an owner
   and action. Flag anything stale (e.g. an outstanding check older than the stale-date policy).
7. **Record the correcting entries** for bank-only items and errors (fees, interest, NSF, your
   own keying errors) so next period's book balance is right. Bank errors are *not* booked — they
   stay as reconciling items until the bank corrects them.

## Why / learn
A bank reconciliation exists because two independent records of the same cash — yours and the
bank's — drift apart for two fundamentally different reasons, and the whole skill is telling them
apart. **Timing differences** are legitimate and self-correct: you recorded a deposit today, the
bank posts it tomorrow; the item will clear on its own, so you carry it, you don't fix it. **True
differences** never self-correct: an error, a duplicate, or fraud will sit there forever until
someone acts. The reason you *must* keep the two buckets separate (see Common mistakes) is that
netting them hides real problems behind normal timing noise — a $500 fraud looks like nothing next
to $50,000 of in-transit deposits. Reconciling *to zero* is the control: if the adjusted bank and
adjusted book balances agree, every dollar of difference is explained by a named item; a leftover
residual means something is still unknown, which is exactly the signal a reconciliation is meant to
raise. Thinking in terms of "bank truth vs. book truth, reconciled by explained differences" is the
mental model that transfers to every cash, clearing, and intercompany reconciliation you will do.

## Common mistakes
- Netting timing and true differences into one number → hides real breaks. Keep the buckets separate.
- Matching on amount alone → false matches. Match on amount **+** date window **+** reference.
- Plugging a residual to force zero → destroys the control. An unexplained difference is a finding.
- Booking bank *errors* as adjustments → overstates cash. Leave bank errors as reconciling items.
- Ignoring aging → stale outstanding checks and old in-transit items are often errors in disguise.
- Reconciling to the wrong balance (available vs. ledger/booked) → pick the balance your policy ties to.

## Tailor to your environment
Drop your real process into `references/your-environment.md` (kept out of git if it holds real
data — use `your-environment.private.md`): which balance you tie to (booked vs. available), your
cutoff convention, your statement format, your tolerance policy, your stale-check days, and the GL
accounts you post fees/interest/NSF to. This skill then maps its generic steps onto your specifics.
If you use Oracle Fusion Cash Management, its auto-reconciliation matching rules and tolerance
behavior are described in `references/matching-and-tolerance.md`, and you can report exceptions with
`oracle-otbi-skills:otbi-cash-management-reports`.

## References
- references/matching-and-tolerance.md — match types, tolerance rules, and Oracle Fusion specifics
- references/your-environment.md — your reconciliation process and formats (add when supplied)
