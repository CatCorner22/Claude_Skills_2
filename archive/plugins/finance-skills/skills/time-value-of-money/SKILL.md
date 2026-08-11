---
name: time-value-of-money
description: >-
  Applies present value, future value, discounting, and compounding to value cash flows over time,
  and computes annuities, perpetuities, NPV, and IRR — including IRR's known pitfalls (multiple or no
  solution, scale, and reinvestment assumptions). Use when valuing future cash flows, computing PV,
  FV, NPV, or IRR, choosing a discount rate, or comparing amounts that fall on different dates.
  Triggers: time value of money, present value, future value, discounting, compounding, NPV, IRR,
  annuity, perpetuity, discount rate, effective annual rate, EAR, opportunity cost of capital.
---

# Time value of money

## When to use
- Valuing a future cash flow or stream of cash flows at a point in time (PV or FV).
- Computing NPV or IRR, or choosing/justifying the discount rate to apply.
- Handling annuities, perpetuities, growing streams, or non-annual compounding.
- Not for: building a project's incremental after-tax cash flows and choosing between competing
  projects → see `finance-skills:capital-budgeting`. For investing surplus cash at money-market
  rates → see `finance-skills:short-term-investments`.

## Do it
1. **Lay the cash flows on a timeline.** Fix time 0 (the valuation date), the period length, and the
   sign of every flow (inflow +, outflow −). Timing errors, not formula errors, cause most mistakes.
2. **Pick the rate and match it to the period.** Use a periodic rate `r` consistent with the period
   length: a monthly stream uses a monthly rate. Convert a nominal annual rate `i` compounded `m`
   times per year to the periodic rate `i/m`. State *why* you chose the rate (opportunity cost).
3. **Discount or compound single sums.**
   - Future value: `FV = PV × (1 + r)^n`
   - Present value: `PV = FV / (1 + r)^n`
   - With `m` compounding periods per year over `n` years: `FV = PV × (1 + i/m)^(m·n)`.
   - Effective annual rate: `EAR = (1 + i/m)^m − 1`; continuous: `EAR = e^i − 1`, `FV = PV·e^(i·t)`.
4. **Use closed forms for level and growing streams** (see `references/formulas.md`):
   - Ordinary annuity PV: `C × [1 − (1 + r)^(−n)] / r`; FV: `C × [(1 + r)^n − 1] / r`.
   - Annuity due (payments at period start): multiply the ordinary result by `(1 + r)`.
   - Perpetuity: `C / r`; growing perpetuity: `C / (r − g)` with `r > g` (`C` is next period's flow).
5. **Compute NPV by discounting every dated flow to time 0 and summing:**
   `NPV = Σ_{t=0}^{n} CF_t / (1 + r)^t`. A positive NPV means the stream is worth more than its cost
   at rate `r`.
6. **Compute IRR as the rate that makes NPV zero** (`Σ CF_t / (1 + IRR)^t = 0`). Solve numerically.
   Before trusting it, run the pitfall checks in step 7.
7. **Screen IRR for its failure modes.** Count sign changes in the cash-flow sequence: more than one
   sign change can produce **multiple IRRs or none**. For ranking mutually exclusive or
   different-sized projects, **defer to NPV** — IRR ignores scale and assumes reinvestment at the IRR
   itself. If you need a rate that reinvests at the cost of capital, report MIRR instead.
8. **State the answer with its rate and date.** "PV = X at r%, as of <date>." A number without its
   discount rate and valuation date is not an answer.

## Why / learn
The whole subject rests on one fact: a dollar today is worth more than a dollar tomorrow because
today's dollar can be invested to earn a return. That return is the **discount rate** — the
opportunity cost of capital, the yield you forgo on an equal-risk alternative. Discounting is just
that fact run backward: dividing by `(1 + r)^n` restates a future dollar in today's dollars so cash
flows landing on different dates become **comparable on one scale**. Everything else is bookkeeping
on that idea. Compounding frequency matters because interest that is credited more often earns
interest sooner, so the *effective* rate rises with `m` — which is exactly why you compare
instruments on EAR, not on stated nominal rates. Annuity and perpetuity formulas are not new physics;
they are the geometric sum of the single-sum formula, worth memorizing only because level streams are
everywhere (loans, leases, coupons). NPV and IRR are two lenses on the same discounted stream: NPV
answers "how much value in today's dollars?" at a rate you choose, while IRR answers "what rate sets
that value to zero?" NPV is the more trustworthy lens because it is denominated in money and lets you
pick the rate; IRR is a single number that hides scale and silently assumes you can reinvest every
interim inflow at the IRR — rarely true. Higher risk means a higher discount rate, which means a
lower present value: risk and value pull in opposite directions through the rate.

## Common mistakes
- Mismatching rate and period (annual rate on monthly flows) → convert to a periodic rate first.
- Comparing a monthly-compounded rate to an annual one on stated terms → compare on EAR.
- Discounting an annuity **due** with the ordinary formula → multiply by `(1 + r)`.
- Trusting a single IRR when cash flows change sign more than once → check for multiple/no IRR.
- Ranking projects by IRR → IRR ignores size; use NPV for the decision.
- Growing-perpetuity formula with `g ≥ r` → the closed form breaks; the value is not finite.
- Quoting a PV without stating the discount rate and valuation date → the number is unusable.

## Tailor to your environment
Record your conventions in `references/your-environment.md` (or `your-environment.private.md`, which
is git-ignored, if it names real rates or deals — never commit real figures). Capture your default
discount rate or WACC and how it is set, your day-count/compounding convention, whether cash flows
are treated as period-end or period-start, and any house template for laying out NPV/IRR schedules.
The generic formulas then run against your standard assumptions.

## References
- references/formulas.md — the full formula set (single sums, annuities, growing streams, NPV/IRR) with worked notes
- references/your-environment.md — your discount rate, compounding convention, and cash-flow timing (add when supplied)
