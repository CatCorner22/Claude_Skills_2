---
name: federal-billing-cash-management
description: >-
  Explains federal payment methods — Letter of Credit / Payment Management System drawdowns,
  advances, and reimbursement under §200.305 — and how each affects unbilled AR, billed AR,
  cash application, and aging in Oracle Fusion PPM + Receivables analysis: distinguishing draws
  from invoices, monitoring the expenditure-to-draw lag, overdraw debts (§200.346), SF-270-style
  documentation, and why federal write-offs can't hit the award. Use when analyzing
  unbilled/billed transitions, cash receipts from federal sponsors, federal AR aging, or
  drawdown-vs-invoicing questions. Triggers: LOC drawdown, letter of credit billing, PMS draw,
  payment management system, federal reimbursement, SF-270, expenditure to draw lag, federal
  advance payment, federal AR aging, drawdown vs invoice, overdraw, federal cash management.
---

# Federal billing and cash management

## When to use
- Analyzing sponsored-AR data with federal sponsors: separating draw-based awards from
  invoice-based awards, measuring the expenditure-to-cash cycle, and reading federal aging
  correctly.
- Explaining how LOC/PMS draws, advances, and reimbursement each work and what they do to
  unbilled/billed AR in Fusion.
- Not for: the general Uniform Guidance frame (thresholds, allowability) → see
  `sponsored-projects-ar-skills:uniform-guidance-federal-core`. For the generic pipeline
  mechanics → see `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`.

## Do it
1. **Identify each award's payment method before touching its AR data** — the same balance
   means different things under each:
   - **LOC / PMS drawdown** (common for large research awards — HHS's Payment Management
     System, agency LOC systems): the institution *draws* federal cash against reported
     expenditures. There is often **no customer invoice at all** — so "no invoices" is normal,
     and invoice-based aging is meaningless for these awards.
   - **Reimbursement** (§200.305's default when advance criteria aren't met): bill after
     spending (SF-270 or agency equivalent); payment is due **within 30 days of a proper
     request** absent agency reason — that 30-day clock is the correct aging yardstick.
   - **Advance**: permitted only when limited to **immediate cash needs**, with the time
     between receipt and disbursement **minimized** — advances create a liability-like
     position (federal cash held), the *opposite* of AR.
2. **Segment the Fusion data by method.** Draw-based awards: exclude from invoice metrics;
   their health metric is the **expenditure-to-draw lag** (PPM costs incurred vs cumulative
   draws). Reimbursement awards: standard invoice pipeline applies
   (`sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`), aged against the 30-day
   clock from a *proper* request. Mixed portfolios reported blind are the #1 federal-AR
   analysis error.
3. **Monitor the lag — it's the federal working-capital metric.** For cost-reimbursable
   federal awards, every day between expenditure (PPM cost collection / revenue recognition)
   and draw or billing is institutional cash lent to the government interest-free. Compute:
   cumulative allowable expenditures − cumulative draws/billings, by award, with the age of
   the undrawn balance. Timeliness runs both directions — see step 4.
4. **Respect the overdraw boundary (§200.346).** Drawing *ahead* of expenditures (beyond
   immediate-need advances) or drawing unallowable costs creates a **debt to the Federal
   Government**, often with interest. The target is a tight corridor: draw promptly for what
   you've spent, never for what you haven't. Excess federal cash held also triggers
   remittance-of-interest rules.
5. **Tie cash application back to the draw.** Draw receipts arrive as lump-sum federal cash,
   not invoice-matched payments — cash application needs the draw schedule (which awards, what
   amounts) to allocate correctly in Receivables/Cash Management. An "unapplied federal
   receipt" is usually an unallocated draw, not a mystery payment.
6. **Keep the documentation audit-ready.** Each draw/request is supported by the expenditure
   detail behind it (SF-270 or equivalent, system reports) under §200.302 standards and
   internal controls — the Single Audit tests exactly this linkage. A draw you can't tie to
   allowable expenditures is a finding waiting to be written.
7. **Handle non-payment the federal way.** A federal balance that won't collect is nearly
   always a *compliance* problem (improper request, unallowable costs, late filing, expired
   award) — fix the request, don't reserve it. **Bad debt can never be charged to the award
   (§200.426)**; a true loss lands on institutional funds, which is why prevention (timely,
   proper draws) is the whole game. `references/federal-payment-map.md` has the method
   comparison, lag worksheet, and the analysis checklist.

## Why / learn
Federal research cash is mostly a *pull* system, not a bill-and-wait system: under LOC/PMS the
institution reaches into a federal account for money it has already spent, which inverts almost
every commercial-AR instinct. There is no invoice to age, "collections" means drawing your own
entitlement promptly, and the counterparty risk is nearly zero while the *process* risk —
drawing late, drawing wrong, documenting badly — is everything. That's why the
expenditure-to-draw lag replaces DSO as the health metric, and why the corridor matters in
both directions: draw too slowly and you're financing the government (a pure working-capital
loss); draw too fast or too much and §200.346 converts the excess into a debt with interest.
Reimbursement awards look more commercial, but the 30-days-from-proper-request rule means aging
starts from a *compliant* request, not from any invoice you happen to send — an aged federal
receivable usually indicts the request, not the payer. And the bad-debt prohibition closes the
loop: since losses can't be pushed to the award, every dollar of federal AR risk must be
managed upstream in billing hygiene, which is exactly what the lag metric, the documentation
linkage, and the draw corridor operationalize.

## Common mistakes
- Running invoice aging on LOC/PMS awards → no invoices exist by design; use the expenditure-to-draw lag.
- Blending draw-based and reimbursement awards in one AR metric → segment by payment method first.
- Celebrating zero federal AR while the undrawn balance ages → the risk moved into the lag; measure it.
- Drawing ahead of expenditures "to be safe" → §200.346 debt + interest; the corridor runs both ways.
- Treating unapplied federal receipts as mysteries → they're unallocated draws; apply from the draw schedule.
- Aging reimbursement awards from invoice date regardless of request quality → the 30-day clock runs from a *proper* request.
- Reserving/writing off federal AR against the award → §200.426 prohibits it; fix the request, and true losses hit institutional funds.
- Draw support assembled at audit time → the SF-270-to-expenditure linkage is built at draw time or it's a finding.

## Tailor to your environment
Map your federal cash machinery in `references/your-environment.md` (award and draw specifics
in `your-environment.private.md`, git-ignored): which awards are LOC/PMS vs reimbursement vs
advance, draw cadence and who executes it, how draws are identified in Fusion data, your
normal lag benchmark, and the documentation package per draw. **Never commit award numbers,
draw amounts, or PMS credentials.**

## References
- references/federal-payment-map.md — method comparison, lag worksheet, cash-application and audit-defense checklists
- references/your-environment.md — your award methods, cadence, benchmarks (fill in)
