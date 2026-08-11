# Evals — banking-skills:bank-account-structure

## 1. Positive trigger (should load the skill)
> "We have 40 bank accounts across five entities and cash is scattered everywhere. Help me design a
> concentration structure with ZBA sweeps and rationalize the account count."

Expected: skill loads; inventories the estate; groups accounts by purpose/currency; designs a
concentration/header hierarchy with ZBA or target-balance sweeps; addresses physical vs notional
pooling and the intercompany-loan implication; proposes a rationalization plan and BAM/mandate hygiene.

## 2. Near-miss (should NOT load this skill)
> "What minimum operating balance should we target in the main account before we sweep excess to the
> money market fund?"

Expected: setting the target/minimum balance *level* is a liquidity-management decision, not a
structure-design one — `cash-management-skills:liquidity-management` should handle it. This skill
covers the sweep *mechanism*, not the target level. If it loads, tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** separates collection/disbursement/special-purpose accounts, builds a header +
  sub-account hierarchy, chooses ZBA vs target-balance per account, and gives a rationalization list.
- **Teaches:** explains *why* concentration cuts idle cash and fees, the difference between ZBA and
  target-balance sweeps, and the physical-vs-notional pooling trade-off (intercompany loans vs legal
  enforceability).
- **Safe:** flags that physical sweeps across entities create intercompany loans to document/price,
  and that notional pooling is restricted in some jurisdictions — confirm for the bank/region.
