# Evals — public-sector-treasury-skills:public-funds-investing

## 1. Positive trigger (should load the skill)
> "Fall tuition just landed and we're holding about $30M at our bank, way over the insured
> limit. The CFO wants to pick up some yield. What are we actually allowed to invest in,
> and how do we make sure the deposits are protected in the meantime?"

Expected: skill loads; starts from the legal chain of authority (state statute → board
policy → delegation) and says to pull the current statute text; frames
safety-liquidity-yield as binding, not preference; addresses collateralization of the
uninsured balance (pledged securities at the statutory margin with independent custody, or
the state collateral pool); positions LGIP/permitted instruments as the yield answer inside
the legal boundary; notes deposit-spike monitoring.

## 2. Near-miss (should NOT load this skill)
> "Explain how Treasury bills and commercial paper work and how to compare their yields on
> a bond-equivalent basis."

Expected: generic instrument mechanics and yield math —
`finance-skills:short-term-investments` should handle it. (Similarly, "draft our company's
corporate IPS and run the monthly holdings check" belongs to
`treasury-accounting-skills:investment-policy-compliance`.) If this skill loads on the
instrument-mechanics prompt, tighten the description.

## 3. Quality rubric
A good response:
- **Does the task:** establishes the authority chain; treats the permitted list as a closed
  set (not listed = not legal); gives concrete collateralization steps (margin, independent
  custodian or state pool, monitoring vs balances); covers DVP/third-party custody; ties the
  outcome into board reporting.
- **Teaches:** explains *why* the hierarchy is law for public money, why collateral must be
  independently held (reachability in a bank failure), and why statutes are closed sets
  (written from historical failures) — the structure, not just the checklist.
- **Safe:** never invents or hard-codes statute citations, margin percentages, or program
  rules from memory — consistently says to confirm the current state statute/program text
  (Tennessee used only as example framing); flags bond proceeds as a special regime
  (indenture + arbitrage, involve bond counsel); keeps balances/exposures out of committed
  files.
