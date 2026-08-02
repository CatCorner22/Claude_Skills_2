# Evals — treasury-accounting-skills:investment-policy-compliance

## 1. Positive trigger (should load the skill)
> "We're sitting on $80M of excess cash — draft an investment policy with limits, and set up a
> monthly check that proves our holdings stay inside it."

Expected: skill loads; opens with the safety-liquidity-yield objectives clause; tiers the
portfolio to the cash forecast; permitted-instruments table with hard rating/maturity/
concentration edges plus a named prohibited list; entity-level counterparty limits; monthly
compliance check from custody data with documented all-clears and an exception process.

## 2. Near-miss (should NOT load this skill)
> "Explain how T-bills, commercial paper, and money market funds work and what they yield."

Expected: instrument mechanics — `finance-skills:short-term-investments`. If this skill loads,
tighten the policy/compliance framing.

## 3. Quality rubric
A good response:
- **Does the task:** complete IPS skeleton with calibrated limits, tiering tied to the
  forecast, and a runnable compliance worksheet with an exception log.
- **Teaches:** the policy as pre-commitment against yield creep, entity-level aggregation
  (deposits + CDs + CP + derivative MTM per bank group), and checker-vs-doer independence via
  custody data.
- **Safe:** doesn't stretch credit/maturity for yield, doesn't auto-sell on downgrades without
  assessment, documents clean checks, and keeps real holdings out of committed files.
