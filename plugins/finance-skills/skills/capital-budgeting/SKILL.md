---
name: capital-budgeting
description: >-
  Evaluates capital projects with NPV, IRR, payback, discounted payback, and the profitability index,
  built on incremental after-tax free cash flows, and explains which rule governs when they conflict
  and why NPV is primary. Use when evaluating an investment or capital project, a buy-versus-build or
  equipment-replacement decision, or when ranking competing or mutually exclusive projects under a
  budget. Triggers: capital budgeting, project evaluation, NPV, IRR, payback period, discounted
  payback, profitability index, incremental cash flow, hurdle rate, mutually exclusive projects,
  capital rationing.
---

# Capital budgeting

## When to use
- Deciding whether to undertake a capital project or investment given its cash flows.
- Ranking competing or mutually exclusive projects, or allocating a limited capital budget.
- Building the incremental after-tax cash flows a project decision rests on, and testing sensitivity.
- Not for: the underlying PV/FV/IRR mechanics in isolation, or choosing a discount rate → see
  `finance-skills:time-value-of-money`. For placing surplus cash in money-market instruments → see
  `finance-skills:short-term-investments`.

## Do it
1. **Build incremental after-tax free cash flows — the foundation.** Count only cash flows that change
   *because of* the project (see `references/cash-flow-model.md`):
   - **Include:** incremental revenues and costs, the depreciation **tax shield**, changes in net
     working capital, after-tax salvage, and opportunity costs of resources the project consumes.
   - **Exclude:** sunk costs (already spent, irrecoverable), non-incremental allocated overhead, and
     financing costs (interest/dividends — those live in the discount rate, not the cash flows).
2. **Lay out the three phases:**
   - Initial outlay (t=0): `capex + ΔNWC` (less any after-tax salvage of an asset being replaced).
   - Operating cash flow (each year): `(Revenue − Costs − Depreciation) × (1 − Tax) + Depreciation`
     — equivalently `EBIT×(1 − Tax) + Depreciation`, or `(Revenue − Costs)×(1 − Tax) + Depreciation×Tax`.
   - Terminal cash flow (final year): after-tax salvage `= Salvage − Tax×(Salvage − Book value)`, plus
     recovery of the net working capital invested.
3. **Discount at the project's cost of capital** and compute the metrics:
   - `NPV = Σ CF_t / (1 + r)^t` — accept if `NPV > 0`.
   - `IRR`: the rate where NPV = 0 — accept if `IRR > r` for conventional cash flows.
   - `Payback`: years to recover the outlay from undiscounted cash flows.
   - `Discounted payback`: same, but from discounted cash flows.
   - `Profitability index (PI) = PV of future cash flows / initial outlay = 1 + NPV/outlay` — accept if `PI > 1`.
4. **Apply the decision rule, and know which one wins when they conflict.** For a single conventional
   project the rules agree. They diverge on **mutually exclusive** or **different-sized/timed** projects
   and on unconventional cash flows: in every such case **NPV governs**. IRR can rank wrongly on scale
   and timing and may have multiple or no solution; payback ignores time value and everything after
   payback; PI is for capital rationing, not head-to-head choice.
5. **Handle rationing and mutual exclusivity explicitly.** Under a hard capital budget, rank by **PI**
   to get the most NPV per dollar of scarce capital. For mutually exclusive projects, pick the highest
   **NPV** (not IRR); if lives differ, compare on equal lives (equivalent annual annuity).
6. **Run sensitivity and scenario analysis.** Flex the key drivers — price, volume, unit cost, discount
   rate, salvage — and find the break-even on each. Report what the decision hinges on, not a single
   point estimate. A positive NPV that flips negative on a small price move is a different recommendation
   than a robust one.
7. **Present the decision.** Show the cash-flow build, all metrics, the governing rule, and the
   sensitivity — with a clear accept/reject or ranking and the assumptions it depends on.

## Why / learn
Every capital-budgeting rule is trying to answer one question — *does this project create value?* — and
**NPV answers it directly**: it is the sum of the project's cash flows discounted at the opportunity
cost of capital, expressed in today's money, so a positive NPV means the project is worth more than it
costs and adds exactly that many dollars of value. That is why NPV is the primary rule and the tiebreaker
whenever the others disagree. The others are useful supplements with known blind spots. IRR restates the
same discounted cash flows as a single percentage, which is intuitive and communicates well — but a
percentage is blind to **scale** (50% on a small project can create less value than 15% on a large one),
can rank projects opposite to NPV when timing differs, and can be multiple-valued or undefined when cash
flows change sign more than once. Payback is really a **liquidity/risk** screen — how fast do we get our
money back — not a value measure; it ignores the time value of money and everything after the cutoff, so
it can reject a highly valuable long-dated project. Discounted payback fixes the time-value flaw but
still ignores post-cutoff cash flows. The profitability index earns its place in **capital rationing**:
when capital is scarce, ranking by NPV per dollar invested squeezes the most value from a fixed budget.
The deepest habit is the one before any metric: the analysis is only as honest as the **incremental
cash flows**. Sunk costs are gone and must not sway a forward-looking decision; financing costs belong
in the discount rate, not the flows (double-counting them otherwise); and opportunity costs and working-
capital swings are real cash the naïve model forgets. Get the incremental cash flows right, discount at
the right rate, decide on NPV, and use the rest as commentary.

## Common mistakes
- Including sunk costs → they are irrecoverable and irrelevant to a forward-looking decision. Exclude them.
- Subtracting interest/financing from the cash flows → it is already in the discount rate; that double-counts.
- Forgetting the depreciation tax shield or working-capital changes → both are real incremental cash.
- Ranking mutually exclusive projects by IRR → IRR ignores scale/timing; choose the higher NPV.
- Trusting one IRR when cash flows change sign more than once → multiple or no IRR; fall back to NPV.
- Deciding on payback alone → ignores time value and all cash flows after the cutoff.
- Comparing different-life projects on raw NPV → equalize lives (equivalent annual annuity) first.
- Reporting a single-point NPV with no sensitivity → a fragile positive NPV is not the same recommendation.

## Tailor to your environment
Record your setup in `references/your-environment.md` (or `your-environment.private.md`, git-ignored, if
it names real projects or figures — never commit real data). Capture your hurdle rate/WACC and how it is
set, your tax rate and depreciation method, your capital-budget limit and approval thresholds, your
standard cash-flow template and horizon, and which metrics your approvals require. The generic process
then runs against your assumptions.

## References
- references/cash-flow-model.md — the incremental after-tax cash-flow build, the three phases, and worked decision-rule notes
- references/your-environment.md — your hurdle rate, tax/depreciation, budget limits, and approval metrics (add when supplied)
