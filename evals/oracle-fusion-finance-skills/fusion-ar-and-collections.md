# Evals — oracle-fusion-finance-skills:fusion-ar-and-collections

## 1. Positive trigger (should load the skill)
> "Our unapplied receipts balance in Fusion Receivables keeps growing — lockbox runs daily but
> lots of cash isn't landing on invoices. How do I work this down?"

Expected: skill loads; explains unapplied vs on-account as visible parking lots; triages by
pattern (missing remittance, short-pay/dispute, duplicate/prepayment); reviews AutoMatch rule
thresholds; sets a weekly queue discipline and ties to the aging/collections impact.

## 2. Near-miss (should NOT load this skill)
> "Reconcile yesterday's bank statement — the deposits don't match what the ledger shows."

Expected: bank-side reconciliation — `cash-management-skills:bank-reconciliation` (method) or
the Fusion CE module skill. If this skill loads, sharpen the AR-side framing.

## 3. Quality rubric
A good response:
- **Does the task:** classifies and resolves the unapplied queue, fixes the upstream cause
  (remittance channels, AutoMatch tuning), and reconciles AR aging to the control account.
- **Teaches:** the transactions-vs-receipts model, why corrections are credit memos/adjustments
  (audit trail) not edits, and how disputes keep dunning credible.
- **Safe:** never recommends editing completed transactions, applying newest-first for
  convenience, or dunning disputed items; keeps customer data out of committed examples.
