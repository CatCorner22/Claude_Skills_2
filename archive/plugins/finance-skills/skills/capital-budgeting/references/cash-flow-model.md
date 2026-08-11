# Incremental cash-flow model and decision rules (reference)

## Contents
- What counts as incremental
- The three cash-flow phases
- Decision metrics and rules
- When the rules conflict
- Sensitivity

## What counts as incremental
Include only cash flows that change *because of* the project:
- **Include:** incremental revenues and operating costs; the **depreciation tax shield**
  (`Depreciation × Tax`); changes in **net working capital**; after-tax **salvage**; **opportunity
  costs** (e.g. the market rent of a building the project occupies); positive/negative **side effects**
  on other products (cannibalization is a real incremental loss).
- **Exclude:** **sunk costs** (already incurred, non-recoverable — e.g. a completed feasibility study);
  **allocated overhead** that would exist anyway; **financing costs** (interest, dividends) — these are
  captured in the discount rate, so putting them in the cash flows double-counts them.

## The three cash-flow phases
1. **Initial outlay (t = 0):**
   `−(capex + installation) − ΔNWC (+ after-tax salvage of any asset replaced)`.
   Working capital invested at the start is a cash outflow now and is recovered at the end.
2. **Operating cash flow (each year t):**
   `OCF = (Revenue − Costs − Depreciation) × (1 − Tax) + Depreciation`
   Equivalent forms (all identical):
   - `OCF = EBIT × (1 − Tax) + Depreciation`
   - `OCF = (Revenue − Costs) × (1 − Tax) + Depreciation × Tax`  ← the "tax-shield" form
   Depreciation is a non-cash expense added back; its only cash effect is the tax it saves.
3. **Terminal cash flow (final year, in addition to that year's OCF):**
   `After-tax salvage + recovery of NWC`, where
   `After-tax salvage = Salvage − Tax × (Salvage − Book value)`.
   If salvage exceeds book value the excess is taxed; if below, it generates a tax saving.

## Decision metrics and rules
| Metric | Formula | Accept if | Blind spot |
|---|---|---|---|
| NPV | `Σ CF_t / (1 + r)^t` | `NPV > 0` | none material — the value measure |
| IRR | rate where `NPV = 0` | `IRR > r` (conventional flows) | scale, timing, multiple/no IRR |
| Payback | years to recover outlay (undiscounted) | `< policy cutoff` | ignores time value & post-cutoff flows |
| Discounted payback | years to recover using discounted flows | `< policy cutoff` | ignores post-cutoff flows |
| Profitability index | `PV of future flows / outlay = 1 + NPV/outlay` | `PI > 1` | a ratio; not for head-to-head choice |

## When the rules conflict
- **Single conventional project:** NPV > 0 ⇔ IRR > r ⇔ PI > 1. All agree; use any.
- **Mutually exclusive projects:** choose the highest **NPV**. IRR can favor a smaller project with a
  higher percentage but less total value (scale), or rank opposite to NPV when cash-flow **timing**
  differs (the crossover rate is where their NPV profiles intersect).
- **Unconventional cash flows (more than one sign change):** IRR may be multiple-valued or undefined —
  rely on NPV (or MIRR for a single, reinvestment-honest rate).
- **Capital rationing (hard budget):** rank by **PI** to maximize NPV per dollar of scarce capital, then
  select down the ranking until the budget is exhausted.
- **Different project lives:** raw NPV favors the longer project unfairly — compare using the
  **equivalent annual annuity** (annualize each project's NPV over its life) or a common replacement horizon.

NPV is primary because it measures value created in currency and assumes reinvestment at the cost of
capital; the others are supplements with the blind spots above.

## Sensitivity
Flex one driver at a time (price, volume, unit cost, discount rate, salvage) to find each break-even,
then run a few coherent scenarios (base / downside / upside). Report what the decision hinges on: a
positive NPV that turns negative on a small adverse move in a key driver is a materially weaker
recommendation than a robust one.
