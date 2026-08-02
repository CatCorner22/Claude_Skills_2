# Evals — oracle-fusion-finance-skills:fusion-gl-and-journals

## 1. Positive trigger (should load the skill)
> "I entered a journal in Fusion GL yesterday and it still shows Unposted — the error says
> something about a cross-validation rule. How do I fix it and get it posted?"

Expected: skill loads; checks period status and reads the CVR message as the control it is;
guides fixing the *combination* rather than hunting for another screen; walks status
Unposted → approval → Posted; explains the three gates (valid combination, balanced by
balancing segment, open period).

## 2. Near-miss (should NOT load this skill)
> "What's the right debit and credit for recording an accrued expense at month end?"

Expected: pure double-entry logic — `accounting-skills:journal-entries` should handle it. If
this skill loads instead, tighten the description toward Fusion mechanics.

## 3. Quality rubric
A good response:
- **Does the task:** diagnoses the specific blocker (period, combination/CVR, balance,
  approval) from the status and message, and gets the journal posted or routed correctly.
- **Teaches:** the ledger 4-C model, segment/value-set/CVR structure, why intercompany
  balancing lines auto-generate, and why every posting failure maps to one of three gates.
- **Safe:** doesn't advise deleting auto-generated balancing lines, bypassing approval, or
  working around a CVR instead of fixing the combination or requesting a rule review.
