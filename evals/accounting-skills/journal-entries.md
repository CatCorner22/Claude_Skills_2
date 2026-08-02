# Evals — accounting-skills:journal-entries

## 1. Positive trigger (should load the skill)
> "We got June's cloud bill after close. Help me book an accrual for it and set up the reversing entry
> for July so we don't double-count when the invoice posts."

Expected: skill loads; classifies it as an accrual; builds a balanced entry (Dr expense / Cr accrued
liabilities) with a standalone memo; sets the reversing entry on July 1; explains why the reversal
prevents double-counting.

## 2. Near-miss (should NOT load this skill)
> "Reconcile our accrued liabilities GL account to the supporting accrual schedule for June and flag
> any unexplained items."

Expected: this is a balance-sheet account reconciliation, not the drafting/booking of an entry. The
`accounting-skills:account-reconciliations` skill should handle it. If journal-entries loads instead,
tighten the description and the "Not for" cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** identifies the entry type, puts each account on its correct normal balance, produces
  a balanced entry (debits = credits), writes a memo stating what/why/period/basis, and plans the reversal
  or amortization.
- **Teaches:** explains *why* accruals serve the matching principle and *why* the reversal offsets the later
  invoice — not just the mechanics of which line is a debit.
- **Safe:** never adds an unexplained plug line; respects preparer ≠ approver; posts to the intended open period.
