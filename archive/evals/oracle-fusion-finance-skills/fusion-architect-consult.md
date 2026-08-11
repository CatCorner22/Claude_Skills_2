# Evals — oracle-fusion-finance-skills:fusion-architect-consult

## 1. Positive trigger (should load the skill)
> "Our BAI2 statements from Bank X load but the 88 continuation lines aren't parsing into
> the reference field, so auto-reconciliation misses half the wires. How do I fix the
> parsing rule configuration?"

Expected: skill loads; packages context (bank, format, the failing segment detail, existing
rule sets from the environment files) and delegates to the
`fusion-treasury-architect` subagent; the answer comes back configuration-specific (parsing
rule setup with segment/string-matching logic, FSM task names, navigation) with the
downstream reconciliation impact stated; validation-in-sandbox advised before production.

## 2. Near-miss (should NOT load this skill)
> "Walk me through reconciling this month's bank statement and classifying the unmatched
> lines."

Expected: process teaching — `oracle-fusion-finance-skills:fusion-cash-management-module`
(module operation) or `cash-management-skills:bank-reconciliation` (method). If this skill
loads, sharpen the configure-vs-operate split.

## 3. Quality rubric
A good response:
- **Does the task:** context packaged before delegation, architect consulted, answer relayed
  with FSM tasks/navigation/parameters and the structured troubleshooting format for errors.
- **Teaches:** the operate-vs-configure seam, why configuration questions suit an
  interrogating persona over static docs, and configuration-as-production-state (sandbox
  first, no undo).
- **Safe:** read-only advisor, no straight-to-production changes, integration ripple
  checked, environment-specific learnings routed back into your-environment files.
