# Evals — oracle-fusion-finance-skills:fusion-cash-management-module

## 1. Positive trigger (should load the skill)
> "We just onboarded a new bank sending camt.053 files into Fusion, and half the statement lines
> aren't auto-reconciling. How do I get the match rate up?"

Expected: skill loads; checks transaction-code mapping for the new bank's codes; reviews rule-set
order (strictest first) and tolerances; classifies the unmatched (missing system transaction /
mangled reference / splits needing many-to-one rules / true exceptions); warns that raising the
match rate with loose rules risks false matches.

## 2. Near-miss (should NOT load this skill)
> "Explain how to classify outstanding checks vs deposits in transit when my reconciliation
> doesn't tie."

Expected: reconciliation *method* — `cash-management-skills:bank-reconciliation`. If this skill
loads, tighten the module/config framing in the description.

## 3. Quality rubric
A good response:
- **Does the task:** diagnoses unmatched lines by cause, fixes mapping/rules deliberately, and
  ties bank balance = module reconciled position = GL cash at the end.
- **Teaches:** the matching-machine model (statement vs subledgers), why rule order and
  tolerances trade off false matches vs manual work, and what external transactions are for.
- **Safe:** doesn't recommend loose amount-only rules first, permanent rules for one-off events,
  or external transactions for items a subledger will also book; keeps account numbers/IBANs
  out of committed examples.
