# Evals — cash-management-skills:intercompany-cash-netting

## 1. Positive trigger (should load the skill)
> "We have twelve subsidiaries paying each other gross every month across four currencies and it's
> costing a fortune in wire fees and FX. I want to set up a multilateral netting cycle through
> treasury and figure out whether an in-house bank makes sense."

Expected: skill loads; chooses multilateral netting through a netting center; sets an invoice-cutoff /
match / calc / advice / settlement calendar; quarantines disputes; nets FX exposure per currency
before converting the residual; and evaluates an in-house bank (POBO/COBO) and pooling against
tax/legal consequences.

## 2. Near-miss (should NOT load this skill)
> "What target balances and buffer should we hold at the group concentration account, and how should
> we sweep the operating accounts into it?"

Expected: this is target-balance, buffer, and sweep design — a liquidity-management task, not
intercompany settlement. The `cash-management-skills:liquidity-management` skill should handle it. If
this skill loads, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** picks bilateral vs. multilateral appropriately, sets a netting calendar with a
  single cutoff, quarantines disputed items, nets FX exposure before converting the residual, issues
  net advices with a confirm window, and reconciles the clearing account to zero.
- **Teaches:** explains *why* netting cuts transaction cost, float, and (especially) FX spread by
  converting only the net exposure, why disputes must be excluded, and how an in-house bank/POBO-COBO
  and pooling extend the same idea — not just the cycle steps.
- **Safe:** does not net disputed balances, does not convert FX after settling gross, and flags the
  tax/legal set-off consequences of pooling rather than treating sweeps as free.
