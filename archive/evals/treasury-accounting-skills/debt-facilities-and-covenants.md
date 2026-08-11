# Evals — treasury-accounting-skills:debt-facilities-and-covenants

## 1. Positive trigger (should load the skill)
> "Our Q2 compliance certificate is due — compute the net leverage covenant, check the headroom,
> and verify the bank's interest charge on the $25M revolver draw looks right."

Expected: skill loads; restates GAAP figures through the credit agreement's defined terms (not
straight off the statements); checks the pricing-grid tier and day-count (Actual/360) on the
interest verification; reports headroom in dollars of EBITDA, not just the ratio; produces the
certificate on the agreement's exhibit form with a traced workpaper.

## 2. Near-miss (should NOT load this skill)
> "Should we finance this equipment purchase with debt or use cash — walk me through the NPV of
> the options."

Expected: capital budgeting / financing decision — `finance-skills:capital-budgeting` should
handle it. If this skill loads, tighten the description toward facility operations and covenant
mechanics.

## 3. Quality rubric
A good response:
- **Does the task:** correct covenant calc via defined terms, headroom in both ratio and
  dollars, verified interest with the right benchmark/spread/day-count, certificate prepared.
- **Teaches:** why agreement definitions diverge from GAAP (lender's seat), Actual/360's real
  cost, the pricing grid's self-adjustment, and why forecasting covenants beats reporting them.
- **Safe:** never computes covenants from raw GAAP, flags potential breaches early toward
  waiver conversations, and keeps real facility terms out of committed files.
