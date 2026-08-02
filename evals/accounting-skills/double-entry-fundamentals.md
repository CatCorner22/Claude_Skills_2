# Evals — accounting-skills:double-entry-fundamentals

## 1. Positive trigger (should load the skill)
> "I'm booking a $10,000 equipment purchase we paid for in cash and I always get confused — which
> account is the debit and which is the credit, and how do I know it keeps the books in balance?"

Expected: skill loads; classifies both accounts (Equipment asset, Cash asset); applies normal balances
(debit the asset acquired, credit the asset given up); shows debits = credits; ties it back to the
accounting equation staying balanced; can post to T-accounts and confirm via a trial balance.

## 2. Near-miss (should NOT load this skill)
> "Draft the month-end accrual journal entry for June's unbilled cloud usage and set it to auto-reverse
> in July."

Expected: this is drafting a specific accrual/reversing entry, which is the `accounting-skills:journal-entries`
skill's job — not a from-scratch lesson in debit/credit mechanics. If double-entry-fundamentals loads
instead, tighten the description and the "Not for" cross-link. (The two are deliberately layered:
fundamentals teaches the rules; journal-entries applies them to real entry types.)

## 3. Quality rubric
A good response:
- **Does the task:** classifies each account by type, states its normal balance, picks the correct side for
  each line, produces a balanced entry (debits = credits), and can post to T-accounts / prove it on a trial balance.
- **Teaches:** explains *why* double-entry is self-checking — two equal, opposite sides keep A = L + E true — and
  that the normal-balance rules fall out of the equation, rather than just asserting which side to use.
- **Safe:** notes that a balanced trial balance is necessary but not sufficient (won't catch an omitted entry, a
  wrong-account posting, or offsetting errors); distinguishes an account's normal balance from a given
  transaction's direction; and flags that "debit/credit" on a bank statement is the opposite perspective.
