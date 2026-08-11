---
name: sponsored-ar-aging-collections
description: >-
  Performs detailed aging, DSO, and collections analysis for sponsored/grant receivables at the
  sponsor, contract, and project level — public-standard metrics (current/overdue/future AR,
  aging amounts and counts on a declared invoice-date or schedule-date basis, % overdue,
  average days outstanding/overdue), breakdowns by award type, business unit, ledger, and
  receivable GL account, sponsor concentration and late-payment risk, and cross-referencing
  receipts and credit-memo applications — producing a prioritized collection list with
  cash-flow implications. Use for overdue invoices, aging buckets, collections prioritization,
  or cash-flow risk questions on sponsored data. Triggers: sponsored aging, overdue sponsor
  invoices, grant collections, aging buckets by sponsor, collection priority list, late paying
  sponsors, sponsor concentration, days overdue, past due grants AR, collections analysis.
---

# Sponsored-AR aging and collections analysis

## When to use
- Building the detailed aging picture of sponsored AR — who owes what, how old, on what basis
  — and turning it into a prioritized collections worklist.
- Assessing sponsor concentration, late-payment patterns, and the cash-flow impact of
  overdue sponsored balances.
- Not for: portfolio KPIs and trends (DSO series, CEI, forecasts) → see
  `sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast`. Working the collections
  process operationally → `oracle-fusion-finance-skills:fusion-ar-and-collections`. Draw-based
  federal awards → `sponsored-projects-ar-skills:federal-billing-cash-management` (no invoices
  to age). Enter via the router
  (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`).

## Do it
1. **Scope to the right grain first.** Filter/aggregate by **Contract Number, Project Number,
   and Sponsor (Customer)** — sponsored collections happen at the award/sponsor level, not the
   invoice level, and a sponsor's total position (all contracts) is what the collections call
   is about. Exclude draw-based (LOC/PMS) awards from invoice aging — their "aging" is the
   expenditure-to-draw lag, measured elsewhere.
2. **Declare the aging basis, then compute the standard metrics.** On payment-schedules data
   (the aging source), with the basis stated — **invoice-date** (how old is the paper) or
   **schedule/due-date** (how overdue is the obligation): **current / overdue / future** AR
   (future = billed, not yet due — real AR but not a collections problem), **aging amount and
   count per bucket** (current, 1–30, 31–60, 61–90, 90+ past due), **% overdue**, **average
   days outstanding** and **average days overdue** (weighted by amount, or the small balances
   drive the average). Always report open balances net of applications — not original amounts.
3. **Break down by the structural dimensions:** award type (cost-reimbursable vs milestone —
   their aging *should* differ), business unit, ledger, and **GL account, restricted to
   RECEIVABLE-class accounts for invoice aging** (mixing in unbilled or clearing accounts
   corrupts the total). Each cut answers a different owner's question — collections works
   sponsors, controllers work accounts, research admin works award types.
4. **Read the risk angles:**
   - **Sponsor concentration** — top-N sponsors' share of open and overdue AR; one sponsor
     holding 40% of the 90+ bucket is a different problem from forty sponsors holding 1% each.
   - **Historical patterns** — quarterly/YoY aging profiles per sponsor; a sponsor drifting
     one bucket rightward every quarter is deteriorating before any single invoice looks alarming.
   - **High-risk sponsors** — consistent late payment vs terms, rising disputed items, or
     payment behavior that changed recently (route pattern detection to
     `sponsored-projects-ar-skills:compliance-risk-anomaly`).
   - **DSO impact** — which sponsors/awards move the portfolio DSO most if collected
     (amount × days is the lever arm).
5. **Cross-reference receipts and adjustments before calling anything collectible.** Using
   receipts/applications and credit-memo-applications data: is the "overdue" balance actually
   an **unapplied receipt** waiting to land, a **partial payment** (age the remainder, note
   the behavior), a **credit memo in flight**, or a **short-pay/dispute** (a different
   workflow than late payment)? An aging report uncorrected for these overstates the
   collections problem and burns credibility with sponsors on the first call.
6. **Produce the deliverable:** the aging summary table (by sponsor × bucket, with the basis
   and as-of date in the header), heatmap-style insight callouts (which sponsor × bucket cells
   are hot, concentration, drift), the **prioritized collection list** (ranked amount × age ×
   sponsor-risk, with the specific invoices, the sponsor contact context, and the next
   action), and **cash-flow implications** (expected collections timing feeding
   `cash-management-skills:cash-forecasting`). `references/aging-worksheets.md` has the table
   formats and the prioritization scoring.

## Why / learn
Aging analysis is triage, and triage only works at the grain where action happens: nobody
calls an invoice — they call a sponsor about a relationship, which is why the sponsor/contract
rollup comes before any bucket math. The two aging bases exist because they answer different
questions (paper age vs obligation lateness), and sponsored portfolios make the distinction
sharper than commercial ones: a 75-day-old invoice on 60-day foundation terms is 15 days
overdue, not 75 — so an undeclared basis makes every downstream number unquotable. The
future-AR bucket teaches the same lesson from the other side: billed-not-due is real AR for
liquidity purposes but noise for collections, and blending them inflates the panic. The
cross-reference step is where analytical aging becomes *actionable* aging — the raw report
always overstates the problem, because unapplied cash, partials, credits in flight, and
disputes all masquerade as "overdue," and the fastest way to lose a sponsor's cooperation is
to dun them for money they already sent. And concentration is the quiet headline: aging
buckets describe *time* risk, concentration describes *counterparty* risk, and the
collections priority list is really the product of both — amount × age × sponsor pattern —
because that product is literally the expected cash unlocked per call made.

## Common mistakes
- Aging at invoice grain and calling it a worklist → roll up to sponsor/contract; that's where the call happens.
- Undeclared aging basis → invoice-date and due-date numbers differ materially; label every table.
- Aging original amounts instead of open balances → partials overstate exposure; net of applications, always.
- Including draw-based federal awards in invoice aging → no invoices by design; their metric is the draw lag.
- Mixing non-RECEIVABLE-class GL accounts into the aging total → unbilled/clearing balances corrupt it; filter the class.
- Treating "future" (billed, not due) as overdue → real AR, not a collections problem; separate the bucket.
- Skipping the receipts/credits cross-reference → dunning sponsors for cash already sent; reconcile before the call list.
- Ranking collections by amount alone → amount × age × sponsor-risk is the expected-cash lever; a big current balance isn't the priority.
- One aging yardstick across sponsor types → terms differ by sponsor; overdue is contractual (the anomaly skill's rule applies here too).

## Tailor to your environment
Record your collections setup in `references/your-environment.md` (sponsor balances and
contacts in `your-environment.private.md`, git-ignored): sponsor payment terms by category,
your bucket scheme if nonstandard, RECEIVABLE-class account list, sponsor risk tiers, the
collections owner per sponsor segment, and escalation thresholds. **Never commit sponsor
names tied to balances or contact details.**

## References
- references/aging-worksheets.md — aging table formats, heatmap reading, prioritization scoring, cash-flow handoff
- references/your-environment.md — your terms, buckets, accounts, owners (fill in)
