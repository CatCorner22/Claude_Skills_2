---
name: accruals-and-prepaids
description: >-
  Builds and maintains accrual and prepaid processes that survive audit — identifying what needs
  accruing at cutoff, estimating defensibly when invoices haven't arrived, running amortization
  schedules for prepaids, reversing correctly, true-ing up estimates against actuals, and testing
  cutoff so expenses land in the right period. Use when booking month-end accruals, setting up or
  amortizing a prepaid, investigating an expense that hit the wrong period, reviewing accrual
  completeness, or measuring estimate accuracy. Triggers: accrual, accrue, prepaid, accrued
  expense, cutoff, amortization schedule, reversing entry, true-up, accrual completeness,
  expense in wrong period, unbilled, month-end accruals.
---

# Accruals, prepaids, and cutoff

## When to use
- Preparing month-end accruals: finding what's incurred-but-uninvoiced, estimating it, booking
  and reversing it, and true-ing up when actuals arrive.
- Managing prepaids: capitalizing, amortizing on schedule, and keeping the balance reconciled.
- Diagnosing cutoff problems — expenses or revenue landing in the wrong period.
- Not for: journal mechanics (debits/credits, entry format) → see
  `accounting-skills:journal-entries`. For the overall close sequence these tasks live in →
  see `accounting-skills:month-end-close`.

## Do it
1. **Work from a completeness driver list, not memory.** Accrual completeness comes from
   sources that *know about obligations before invoices exist*: open POs with receipts not yet
   invoiced, recurring vendor calendar (rent, utilities, SaaS — what's normally invoiced but
   hasn't arrived?), payroll cutoff (days worked past the last payroll), legal/professional
   engagement letters, commissions and bonus plans, interest on debt
   (`treasury-accounting-skills:debt-facilities-and-covenants` for the calc), and
   post-period invoices reviewed for prior-period service dates. Keep the list as a standing
   checklist; every close, walk it.
2. **Estimate with a documented basis.** Best evidence first: contract or PO price → vendor
   confirmation → run-rate (last 3 invoices) → budget as last resort. Write the basis on the
   accrual workpaper ("3-month average of vendor X, $42k ± seasonal") — an accrual without a
   basis is a plug, and auditors treat it accordingly. Match precision to materiality: a $2k
   utilities accrual can be run-rate; a $2M construction accrual needs the project manager's
   percent-complete.
3. **Book as auto-reversing, then let the invoice settle the score.** Accrue Dr expense /
   Cr accrued liabilities, flagged to reverse on day 1 of the next period. The arriving invoice
   books normally; reversal + invoice nets to the estimate error, which lands in the new
   period. Only long-running accruals (bonus pools, legal reserves) stay unreversed and get
   adjusted — know which style each accrual uses.
4. **Run prepaids as a schedule, not a memory.** Payment for future service books to prepaid
   (Dr prepaid / Cr cash-or-AP), then amortizes straight-line over the service period
   (Dr expense / Cr prepaid monthly). Maintain one amortization schedule per item — vendor,
   total, service dates, monthly charge, remaining balance — and the sum of schedules **is**
   the GL balance; that's the reconciliation. Set a capitalization floor (e.g. expense anything
   under $5–10k) so the schedule isn't cluttered with trivia.
5. **True up and measure the estimating.** Each close, compare last period's accruals to actual
   invoices received: a per-vendor error report (accrued vs actual, %) both catches missed
   reversals and tells you which estimates to improve. Systematic bias (always accruing low)
   is a finding about the driver list, not bad luck.
6. **Test cutoff both directions.** Sample invoices posted just *after* period end for service
   dates *inside* the period (missing accrual) and expenses posted *inside* for service periods
   *after* (should be prepaid). The service/delivery date decides the period — never the invoice
   date or posting date. `references/accrual-workpapers.md` has the workpaper and test formats.
7. **Reconcile the balances.** Accrued liabilities: aged listing by item — anything sitting
   more than 2–3 cycles is a stale accrual to investigate and release with documentation, not
   silently. Prepaids: schedule total = GL, and every item's remaining life makes sense.

## Why / learn
Accruals exist because economic activity doesn't wait for paperwork: the expense happened when
the service was consumed, and the invoice is just the bill arriving later. Everything in the
process follows from taking that seriously. Completeness is the hard direction — recorded
accruals are easy to verify, but the *missing* one leaves no trace in the ledger, which is why
the driver list (POs, calendars, contracts — things that know about obligations pre-invoice) is
the core control, and why cutoff testing samples from *after* period end. The auto-reversal
pattern is an elegant self-correcting loop: you never need to remember what you accrued, because
reversal-plus-actual-invoice automatically books your estimate error where you can see it — and
that visible error stream is free feedback on your estimating. Prepaids are the mirror image
(cash first, expense later), and the schedule-equals-GL identity is what makes the balance
*provable* rather than plausible. Stale accruals, meanwhile, are where discipline goes to die:
an accrued liability nobody releases is either padding (a cookie-jar reserve) or a missed
reversal double-counting expense — both misstatements wearing a boring disguise.

## Common mistakes
- Accruing only what someone remembers → completeness comes from the driver list (POs, vendor calendar, contracts), not recall.
- Using the invoice date to decide the period → service/delivery date governs; the invoice date is when paper moved.
- Forgetting to reverse (or double-reversing) → auto-reversing flags at entry; the true-up report catches survivors.
- Accruals without a documented basis → plugs that fail audit; write the basis on the workpaper.
- Prepaid balance with no schedule behind it → unprovable; one schedule per item, schedules sum to GL.
- Stale accrued liabilities left "to be safe" → cookie-jar risk; age the listing, release with documentation.
- Same precision effort for $2k and $2M items → materiality allocates the effort; estimate hard where it matters.
- Ignoring systematic estimate bias → the true-up report is telling you a driver is missing; fix the list.

## Tailor to your environment
Keep your accrual universe in `references/your-environment.md` (real vendors and amounts in
`your-environment.private.md`, git-ignored): the standing driver checklist, recurring accruals
with their estimation bases, prepaid capitalization floor, materiality thresholds, and who owns
the true-up review. Sanitize amounts to bands — **never commit real vendor invoices or payroll
data**.

## References
- references/accrual-workpapers.md — accrual workpaper, true-up report, cutoff test, and prepaid schedule formats
- references/your-environment.md — your driver list, recurring accruals, thresholds (fill in)
