# Evals — finance-skills:financial-ratios

## 1. Positive trigger (should load the skill)
> "Here are our income statement and balance sheet. Our ROE jumped from 12% to 19% this year — is
> that good, and what's actually driving it? Also check whether we're still onside our interest
> coverage covenant of 3.0x."

Expected: skill loads; computes ROE and interest coverage on the right (average) bases; runs a DuPont
decomposition to attribute the ROE rise to margin, turnover, or leverage; flags that a leverage-driven
ROE gain cuts both ways; and interprets the coverage ratio against the 3.0x covenant rather than in
isolation.

## 2. Near-miss (should NOT load this skill)
> "Can you build the income statement and balance sheet from this trial balance and make sure they
> tie?"

Expected: this is preparing the underlying statements, not analyzing ratios from them — the
`accounting-skills:financial-statements` skill should handle it. If financial-ratios loads as primary,
tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** computes the requested ratios with correct formulas and average balances, and
  decomposes ROE via DuPont to locate the driver.
- **Teaches:** stresses that ratios are diagnostics meaningful only against a benchmark or trend, and
  that identical ROE can be assembled very differently (operations vs leverage).
- **Safe:** does not cheer a leverage-driven ROE uncritically, defines "debt" when computing leverage,
  and notes distortions (one-time items, near-zero denominators, industry structure) before concluding.
