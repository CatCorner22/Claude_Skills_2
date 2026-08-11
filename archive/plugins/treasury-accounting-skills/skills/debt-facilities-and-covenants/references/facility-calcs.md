# Facility calculations (reference)

Directional examples — always compute from your own agreement's definitions and conventions.

## Contents
- Interest calculation walkthrough
- Availability and fees
- Covenant worksheet skeleton
- Headroom translation

## Interest calculation walkthrough
Draw: $25,000,000 · Term SOFR (1-month) = 4.30% · spread = 2.25% (grid tier for leverage 2.5–3.0x)
· day-count Actual/360 · interest period 30 days.

```
Interest = 25,000,000 × (0.0430 + 0.0225) × 30/360 = 25,000,000 × 0.0655 × 0.08333 = $136,458.33
```
- Actual/365 on the same facts: $134,589.04 — the 360 denominator adds ~1.39%/yr of effective cost.
- Daily-compounded SOFR facilities accrue day by day; verify against the bank's accrual schedule,
  not a single-period formula.
- Rate floors: many agreements floor the benchmark (e.g. 0%); irrelevant until it isn't.

## Availability and fees
```
Availability = Commitment − Drawn − LCs outstanding [− Borrowing-base shortfall]
Example: 100M − 40M − 7.5M = 52.5M available
Unused fee  = (Commitment − Drawn) × unused fee rate × days/360    (LCs may or may not count as usage for the fee — check)
LC fee      = LC face × LC fee rate (≈ drawn spread) + fronting fee
```
Asset-based (ABL) facilities: availability caps at the **borrowing base**
(eligible AR × advance rate + eligible inventory × advance rate − reserves), reported on a
borrowing-base certificate (often monthly, weekly when tight).

## Covenant worksheet skeleton
One tab per covenant; every line sourced. Example: Net Leverage ≤ 4.00x, TTM basis.

| Line | Source | Amount |
|---|---|---|
| Net income (TTM) | Income statement | ... |
| + Interest expense | IS | ... |
| + Taxes | IS | ... |
| + D&A | Cash flow stmt | ... |
| + Permitted add-backs (per definition, with caps) | Agreement §1.01 + support | ... |
| **= EBITDA (as defined)** | | ... |
| Total debt (as defined — check what counts: LCs? leases? earnouts?) | BS + agreement | ... |
| − Unrestricted cash (netting often capped) | BS + agreement | ... |
| **= Net debt** | | ... |
| **Net leverage** | Net debt / EBITDA | ...x |
| Required | Agreement | ≤ 4.00x |
| Headroom (ratio) | | ... |
| Headroom ($ EBITDA) | Net debt / 4.00 − EBITDA, sign-flipped | ... |

Repeat the identical worksheet on forecast financials each quarter for the next 4 test dates.

## Headroom translation
- EBITDA cushion: `EBITDA_actual − NetDebt / MaxLeverage`
- Debt capacity: `MaxLeverage × EBITDA − NetDebt`
Report both — one says how much performance can slip, the other how much more you can borrow.
