# Sponsored-AR routing map (reference)

## Contents
- Question type → sub-skill
- Intake checklist
- Standing nuances to carry forward

## Question type → sub-skill
| The user is asking... | Route to | Typical phrasing |
|---|---|---|
| What a term/field means; where data comes from; which subject area to use; "profile this extract" | `fusion-ar-ppm-domain-knowledge` | "what is unbilled AR", "which subject area", "map these columns" |
| Unbilled vs billed; WIP; billing status; draft invoices; stuck/exception invoices | `unbilled-billed-ar-wip-recon` | "how much is unbilled", "invoices in error", "billing backlog" |
| Revenue vs invoiced; over/under-billing; unbilled balance substantiation; GL tie-out | `revenue-billing-reconciliation` | "recognized vs billed", "over billed", "substantiate unbilled" |
| Performance, KPIs, benchmarks, trends, forecasts | `sponsored-ar-kpi-trends-forecast` | "DSO by sponsor", "aging trend", "collections forecast" |
| Detailed aging, overdue detail, collections prioritization | `sponsored-ar-aging-collections` | "who do we chase", "aging by sponsor", "collection priority list" |
| Summaries, dashboards, report designs, recommendations, next steps | `reporting-visualization-recommendations` | "build me a report", "executive summary", "what should we do" |
| Risk sweep, exceptions, anomalies (any sponsor type) | `compliance-risk-anomaly` | "risk review", "anything unusual", "exception scan" |
| Federal rules: Uniform Guidance, thresholds, allowability, Single Audit | `uniform-guidance-federal-core` | "2 CFR 200", "is this allowable", "de minimis rate" |
| Federal money movement: LOC/PMS draws, advances, reimbursement, federal aging | `federal-billing-cash-management` | "drawdown", "SF-270", "expenditure to draw lag" |
| Salary/effort charging on federal awards | `federal-effort-reporting-basics` | "effort certification", "salary allocation", "§200.430" |
| Item-level "can this be charged/billed?" screening | `federal-cost-allowability` | "is this allowable", "charge this to the grant", "admin salary direct" |
| Federal risk: questioned costs, write-offs, Single Audit exposure | `federal-sponsored-ar-compliance-risk` | "can we write this off", "audit risk", "SEFA" |
Multi-part questions run the chain: domain-knowledge (profile) → recon and/or KPI (analyze) →
reporting (deliver). The router owns sequencing and the final structure.

## Intake checklist (run before any sub-skill)
- [ ] Award/bill-plan type(s) identified: cost-reimbursable / fixed-price-milestone / mixed
      (if mixed: segment before computing anything)
- [ ] Data in hand or precisely described: source (subject area / report), columns, filters,
      as-of date, refresh cadence
- [ ] Scope filters agreed: sponsor(s), project/contract range, business unit, date window
- [ ] Aging basis declared: invoice date vs schedule (due) date
- [ ] Currency handling agreed if multi-currency (report in which currency, at what rate?)
- [ ] Output consumer known (research admin, controller, sponsor-facing) — tunes the framing

## Standing nuances to carry forward
1. **Attribute visibility:** project/task/award attributes appear on Receivables lines only if
   the contract's invoice grouping rule carries them; their absence in AR data is configuration,
   not missing data — join back to PPM data instead.
2. **Aging basis:** invoice-date aging and schedule-date aging answer different questions
   (how old is the paper vs how overdue is the obligation); always label which is in use.
3. **Freshness:** pipeline and aging metrics decay fast; daily incremental extract runs are the
   recommended cadence, and every deliverable states its as-of date.
4. **Public concepts only:** documented OTBI subject areas, bill plans, AutoInvoice flow;
   implementation-specific config (grouping rules, DFFs) is asked about, never assumed.
