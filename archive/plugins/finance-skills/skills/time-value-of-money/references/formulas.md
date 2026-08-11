# Time-value formulas (reference)

Notation: `PV` present value, `FV` future value, `C` periodic cash flow, `r` periodic discount rate
(as a decimal), `n` number of periods, `i` nominal annual rate, `m` compounding periods per year,
`g` periodic growth rate, `e` Euler's number. Keep `r` and the period on the same footing.

## Single sums
- Future value: `FV = PV × (1 + r)^n`
- Present value: `PV = FV / (1 + r)^n` = `FV × (1 + r)^(−n)`
- Sub-annual compounding over `n` years: `FV = PV × (1 + i/m)^(m·n)`
- Effective annual rate (EAR): `EAR = (1 + i/m)^m − 1`
- Continuous compounding: `FV = PV × e^(i·t)`; `EAR = e^i − 1`
- Solve for rate: `r = (FV / PV)^(1/n) − 1`; for periods: `n = ln(FV/PV) / ln(1 + r)`

## Level annuities (equal payments `C`)
- Ordinary annuity (payments at period **end**):
  - PV = `C × [1 − (1 + r)^(−n)] / r`
  - FV = `C × [(1 + r)^n − 1] / r`
- Annuity **due** (payments at period **start**): multiply either ordinary result by `(1 + r)`.
- Loan/mortgage payment (amortizing): `C = PV × r / [1 − (1 + r)^(−n)]`.

## Perpetuities and growing streams
- Level perpetuity: `PV = C / r`
- Growing perpetuity: `PV = C / (r − g)`, valid only when `r > g`; `C` is the flow one period out.
- Growing annuity (n periods): `PV = C/(r − g) × [1 − ((1 + g)/(1 + r))^n]`, `r ≠ g`.

## NPV and IRR
- Net present value: `NPV = Σ_{t=0}^{n} CF_t / (1 + r)^t`. Time-0 flow `CF_0` is usually the outlay (−).
- Decision rule (standalone project): accept if `NPV > 0`.
- Internal rate of return: the `IRR` solving `Σ_{t=0}^{n} CF_t / (1 + IRR)^t = 0`. No closed form for
  `n > 4` in general — solve numerically (bisection or Newton) or with a spreadsheet's `IRR`/`XIRR`.
- Modified IRR (MIRR): compounds inflows forward at the reinvestment/finance rate and discounts
  outflows back, then takes the single rate linking them — removes IRR's reinvestment distortion.

## IRR pitfalls (why NPV is the tiebreaker)
- **Multiple IRRs / no IRR:** by Descartes' rule of signs, each sign change in the cash-flow sequence
  can add a root. Conventional flows (one sign change: outflow then inflows) have one IRR; two or more
  sign changes can yield several IRRs or none real.
- **Scale:** IRR is a percentage and blind to size. A 50% return on 1,000 creates less value than a
  15% return on 1,000,000. NPV, in currency, is not fooled.
- **Timing / ranking mutually exclusive projects:** IRR can rank two projects opposite to NPV when
  their cash-flow timing differs. The crossover rate is where their NPV profiles intersect; below it
  NPV and IRR can disagree. Use NPV.
- **Reinvestment assumption:** IRR implicitly reinvests interim inflows at the IRR; MIRR fixes this by
  reinvesting at an explicit rate.

## Choosing the discount rate
- The rate is the opportunity cost of capital for cash flows of that risk: what an equal-risk
  alternative yields. For firm-wide, average-risk projects this is typically the WACC.
- Match the rate's risk to the cash flow's risk — do not discount a risky stream at a risk-free rate.
- Real vs nominal: discount **nominal** cash flows at a **nominal** rate and **real** cash flows at a
  **real** rate; never mix. Fisher: `(1 + nominal) = (1 + real)(1 + inflation)`.
