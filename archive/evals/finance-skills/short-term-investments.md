# Evals — finance-skills:short-term-investments

## 1. Positive trigger (should load the skill)
> "We're sitting on about 8M of surplus cash we won't need for a couple of months. Where should we put
> it — I'm looking at a 90-day T-bill quoted at a 4.8% discount versus a 90-day CD at 4.95%. Which
> actually yields more, and how should we spread it out?"

Expected: skill loads; segments the cash by horizon; ranks options by Safety-Liquidity-Yield; converts
the T-bill's discount yield to a bond-equivalent yield before comparing it to the CD; recommends a
maturity ladder; and frames the decision against an investment policy rather than picking the top yield.

## 2. Near-miss (should NOT load this skill)
> "How large a cash buffer should we hold, and how much revolver capacity do we need to cover a bad
> quarter?"

Expected: this is sizing overall liquidity and structuring facilities, not selecting money-market
instruments — the `cash-management-skills:liquidity-management` skill should handle it. If
short-term-investments loads as primary, tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** segments cash, matches instruments to horizons, converts the T-bill and CD to a
  common (bond-equivalent) yield basis, and proposes a ladder plus policy limits.
- **Teaches:** leads with SLY — Safety, then Liquidity, then Yield — and explains that this is operating
  cash, so principal and access outrank return; also *why* discount yield understates the true return.
- **Safe:** does not pick the highest headline yield, does not treat prime MMFs as risk-free cash, and
  invokes an investment policy statement and per-issuer concentration limits as the control.
