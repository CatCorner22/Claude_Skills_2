---
name: debt-facilities-and-covenants
description: >-
  Manages corporate debt facilities day to day — revolver draws and paydowns, term loan
  amortization, interest calculations (SOFR + spread, day-count conventions), availability and
  borrowing-base tracking, and the covenant compliance cycle: computing leverage/coverage ratios
  exactly as the credit agreement defines them and producing the compliance certificate. Use when
  drawing or repaying a facility, verifying an interest charge, computing covenants, preparing a
  compliance certificate, or assessing headroom. Triggers: revolver draw, credit facility,
  term loan, covenant, leverage ratio, interest coverage, compliance certificate, borrowing base,
  facility availability, SOFR interest, debt covenant headroom, paydown.
---

# Debt facilities and covenant compliance

## When to use
- Operating a revolver or term loan: sizing and executing draws/paydowns, forecasting and
  verifying interest, tracking availability and fees.
- Running the covenant cycle: computing defined ratios, checking headroom, preparing the
  quarterly compliance certificate, or evaluating a potential breach.
- Not for: deciding whether/how much to borrow strategically (capital structure) → see
  `finance-skills:capital-budgeting` and `finance-skills:working-capital-management`. For
  where borrowed cash goes day-to-day → see `cash-management-skills:cash-positioning`.

## Do it
1. **Anchor every number in the credit agreement, not in GAAP.** Pull the definitions section
   first: "EBITDA," "Indebtedness," "Fixed Charges" are *defined terms* with agreement-specific
   add-backs and exclusions that rarely match the financial statements. Every covenant
   calculation starts by restating your GAAP numbers into the agreement's definitions.
2. **Know the facility mechanics you're operating.**
   - **Revolver:** borrow/repay at will up to the commitment; availability = commitment − drawn
     − letters of credit outstanding (− borrowing-base shortfall if asset-based). Costs: drawn
     interest + **unused/commitment fee** on the undrawn portion + LC fees.
   - **Term loan:** funded once, repays on an amortization schedule (often with a bullet);
     prepayments may carry premiums or be applied against future amortization.
   - Draws follow the notice mechanics (notice period, minimum amounts, interest-period
     selection); missing a notice cutoff is a real operational failure.
3. **Compute interest exactly.** Interest = principal × (benchmark + spread) × day-count.
   Confirm: the benchmark (term SOFR vs daily simple/compounded SOFR + any credit spread
   adjustment), the **spread from the pricing grid** (it often steps with the leverage ratio),
   and the **day-count convention** (Actual/360 inflates the effective rate vs Actual/365 —
   agreements specify which). Verify bank interest charges rather than booking them blind;
   `references/facility-calcs.md` has worked examples.
4. **Run the covenant calc as a repeatable worksheet.** For each covenant (typically net
   leverage = Net Debt / EBITDA-as-defined; interest or fixed-charge coverage = EBITDA / interest
   or fixed charges; sometimes minimum liquidity): map every input line to its source
   (statements → adjustments per definitions), compute at the required frequency (usually
   trailing-twelve-months, quarterly), and show the required level vs actual vs **headroom** in
   both ratio terms and dollars ("EBITDA can fall $X before breach").
5. **Forecast covenants before they bite.** Run the same worksheet on forecast financials
   (see `cash-management-skills:cash-forecasting` for the cash side) each quarter — a breach you
   see two quarters out is a conversation with the bank; a surprise breach is a default. Watch
   for **springing covenants** (tested only above a draw threshold) and cure rights.
6. **Produce the compliance certificate.** Use the agreement's exhibit form: officer
   certification, covenant calcs with the defined-term build shown, and any required schedules.
   File by the deadline (usually 45–60 days after quarter end, with financials). Keep the
   workpaper tying every certificate number to the statements — auditors and the bank both ask.
7. **If a breach is possible:** quantify it, check cure provisions (equity cure, netting more
   cash) and grace periods, and escalate early — waivers are cheapest when requested before the
   test date, not after.

## Why / learn
A credit agreement is a private contract that borrows accounting words and redefines them, so
the cardinal skill is *reading covenant math as contract math*. Lenders define EBITDA with
add-backs (and caps on them) because they're underwriting repayment capacity, not reported
earnings; they choose Actual/360 because it quietly yields ~1.4% more interest per year than the
words suggest; they put the spread on a leverage grid so pricing self-adjusts to risk. Every one
of those choices is rational from the lender's seat, and reading them that way tells you where
to be careful. Headroom-in-dollars is the single most useful transform — a ratio of 3.2x vs a
4.0x max means nothing to an operator until it becomes "EBITDA can drop $18M before we breach,"
which is a number a forecast can monitor. And the reason covenant forecasting matters more than
covenant reporting is asymmetry: a foreseen breach is negotiable (waiver, amendment, cure), while
a reported breach can cross-default other debt. The compliance certificate is where all of it
becomes an officer's signed representation — which is why the workpaper behind it must trace.

## Common mistakes
- Computing covenants from GAAP figures without the agreement's definitions → wrong by
  construction; restate through the defined terms every time.
- Ignoring the pricing grid → interest verified against last quarter's spread; re-check the
  grid tier after each covenant calc.
- Actual/360 treated as Actual/365 → interest checks "fail" by a consistent ~1.4%; match the convention.
- Reporting the ratio without dollar headroom → no one can act on 3.2x; translate to dollars of cushion.
- Forgetting LCs in availability → the revolver has less room than commitment − drawn.
- Testing covenants only when the certificate is due → forecast them; surprises are defaults.
- Missing draw-notice mechanics → funding arrives late; calendar the notice cutoffs.

## Tailor to your environment
Put your facility's real terms in `references/your-environment.md` (the agreement itself and any
sensitive terms in `your-environment.private.md`, git-ignored): commitments, maturity, benchmark
and spread grid, day-count, covenant definitions and levels, test frequency, certificate
deadlines, and notice mechanics. **Never commit the credit agreement or actual covenant results.**

## References
- references/facility-calcs.md — worked interest calcs, availability, and a covenant worksheet skeleton
- references/your-environment.md — your facilities, definitions, levels, and deadlines (fill in)
