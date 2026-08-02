# Evals — banking-skills:bank-fee-analysis

## 1. Positive trigger (should load the skill)
> "Here's our account analysis statement. Fees jumped this quarter. Can you break down the charges,
> tell me how the earnings credit is offsetting them, and where we can push back?"

Expected: skill loads; reads the balance summary and investable balance; computes the earnings credit
(investable balance × ECR × day-count) vs total charges; decodes service lines as volume × unit price
mapped to AFP codes; identifies the biggest drivers and negotiation levers; tests the balance-vs-fee
trade-off (ECR vs investment yield).

## 2. Near-miss (should NOT load this skill)
> "We have $3M of surplus cash this month — should we put it in a money market fund or a T-bill ladder?"

Expected: this is an investment/liquidity decision, handled by
`cash-management-skills:liquidity-management` (or a short-term investing skill), not a fee analysis.
Fee analysis only informs the ECR side of the trade-off. If it loads, tighten the "Not for" line.

## 3. Quality rubric
A good response:
- **Does the task:** reads the statement structure, computes the earnings credit and net settlement,
  decomposes charges into volume × unit price mapped to AFP codes, trends them, and lists negotiation
  levers targeting the biggest dollars.
- **Teaches:** explains that the ECR is a notional fee-offset (not interest paid), computed on the
  investable balance, and why the pay-with-fees-vs-balances choice hinges on ECR vs investment yield.
- **Safe:** doesn't treat the earnings credit as income; computes on investable (not ledger) balance;
  says to confirm reserve factor, day count, and carry-forward rules for the specific bank.
