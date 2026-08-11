# Your reconciliation-design environment (sanitized template)

Fill in structural facts. Anything sensitive (account numbers, real statement data) belongs
in `your-environment.private.md`, which is git-ignored.

- **Accounts and formats:** <account (structural name) → BAI2 / CAMT.053 / MT940>
- **References your banks actually populate:** <which record/field carries receipt
  numbers, check numbers, merchant IDs, terminal IDs — per bank>
- **Settlement patterns in play:** <card processors and their fee handling, lockbox,
  sweeps/ZBA, payroll>
- **Current match rates by account:** <baseline numbers — tuning needs a before>
- **Rule sets and sequence:** <rule set → rules in order, type, keys, tolerances>
- **TCRs in force and why:** <each TCR and the bank-originated justification>
- **Clearing account map:** <cash / cash clearing accounts by account-use>
