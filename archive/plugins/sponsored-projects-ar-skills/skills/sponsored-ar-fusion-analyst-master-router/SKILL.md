---
name: sponsored-ar-fusion-analyst-master-router
description: >-
  Routes and coordinates every analysis of sponsored projects, awards, and grants receivables
  data in Oracle Fusion Cloud (Receivables + PPM/Grants integration) — classifying the question,
  confirming the award/bill-plan type, requiring data or a clear description before any
  calculation, dispatching to the right sub-skill, and enforcing the standard output structure.
  Use FIRST for any sponsored-AR question, before any analysis. Triggers: sponsored projects,
  grants, awards, project invoices, PPM receivables, unbilled AR, project contract billing,
  sponsor AR, grant receivables, award billing, sponsored research billing, grants AR analysis.
---

# Sponsored AR analyst — master router

## When to use
- Always first, for any question touching sponsored projects/awards/grants receivables in
  Oracle Fusion — before any sub-skill or calculation.
- Coordinating a multi-part analysis (e.g. "how healthy is our sponsor AR?") that will use
  several of this plugin's skills in sequence.
- Not for: general (non-sponsored) Fusion AR operations → see
  `oracle-fusion-finance-skills:fusion-ar-and-collections`. For general OTBI mechanics → see
  `oracle-otbi-skills:otbi-report-building`.

## Do it
1. **Classify the question before answering it.** Sponsored-AR questions fall into four types,
   each owned by a sub-skill:
   - *"What does this data/term mean, where does it come from?"* →
     `sponsored-projects-ar-skills:fusion-ar-ppm-domain-knowledge` (also the default first stop
     for any new dataset or engagement).
   - *"What's unbilled vs billed / stuck in the billing pipeline?"* →
     `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`.
   - *"Revenue vs invoiced / over- or under-billed / GL tie-out?"* →
     `sponsored-projects-ar-skills:revenue-billing-reconciliation` (the accounting view;
     the pipeline skill above is the operational view).
   - *"How are we performing / trending / what's coming?"* →
     `sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast`.
   - *"Who's overdue / who do we chase / aging detail?"* →
     `sponsored-projects-ar-skills:sponsored-ar-aging-collections` (detailed aging and the
     prioritized collections worklist; the KPI skill above is the portfolio trend view).
   - *"Summarize / build a report / what should we do?"* →
     `sponsored-projects-ar-skills:reporting-visualization-recommendations` (also the standard
     final step of any multi-part analysis).
   - *"What's risky / broken / unusual?" (any sponsor type)* →
     `sponsored-projects-ar-skills:compliance-risk-anomaly` (exceptions, anomalies, funding
     limits, cross-pillar checks; routes federal items onward to the federal risk skill).
   - *Federal-sponsor questions get the compliance layer too:* Uniform Guidance frame,
     thresholds, allowability →
     `sponsored-projects-ar-skills:uniform-guidance-federal-core`; draws/advances/reimbursement
     and federal aging → `sponsored-projects-ar-skills:federal-billing-cash-management`;
     salary/effort charges → `sponsored-projects-ar-skills:federal-effort-reporting-basics`;
     "can this cost be charged/billed?" item screening →
     `sponsored-projects-ar-skills:federal-cost-allowability`;
     risk assessment, write-offs, questioned costs, Single Audit exposure →
     `sponsored-projects-ar-skills:federal-sponsored-ar-compliance-risk`.
2. **Confirm the award/bill-plan type up front — it changes every downstream answer.**
   **Cost-reimbursable** awards bill actual incurred expenses (unbilled AR is expense-driven);
   **fixed-price/milestone** awards bill pre-set amounts on events (unbilled AR is
   schedule-driven). Mixed portfolios must be segmented before any metric is computed.
3. **Require the data — or a precise description — before calculating anything.** No metric
   gets computed from assumption. Acceptable inputs: an uploaded extract (OTBI export, BIP
   output, CSV), or an exact description of the source (subject area, columns, filters, as-of
   date). If neither exists, the deliverable is the *data request*, not a guess.
4. **Ground every step in public Oracle Fusion concepts only** — documented OTBI subject areas,
   bill plans, and AR integration flows (the domain-knowledge skill carries the map). No
   invented tables, columns, or undocumented behavior; where something is
   implementation-specific (invoice grouping rules, descriptive flexfields), say so and ask.
5. **Enforce the standard output structure on every deliverable:**
   1. **Executive Summary** — the answer in three sentences.
   2. **Data Validation** — what was received, completeness, date range, caveats.
   3. **Key Metrics & Insights** — multi-angle: financial health, compliance/risk,
      trends/implications.
   4. **Actionable Recommendations** — specific, owned, sequenced.
   5. **Edge Cases & Next Questions** — what the data couldn't answer.
6. **Carry the standing nuances into whichever sub-skill runs:** project/task attributes are
   visible on AR lines only if the contract's invoice grouping rule includes them; aging can be
   invoice-date- or schedule-date-based (state which); aging/pipeline metrics are only as fresh
   as the extract — daily incremental runs are the recommended cadence for accurate aging.

## Why / learn
Sponsored AR sits on a seam between two Fusion modules — PPM/Grants generates the billing
events, Receivables owns the invoices and cash — and most bad sponsored-AR analysis comes from
answering a two-module question with one module's data (billed AR that ignores the unbilled
pipeline, or PPM revenue that never checks what Receivables actually collected). A router skill
exists to force the two questions that prevent that: *which side(s) of the seam does this
question live on* (the classification), and *what kind of award is this* (because
cost-reimbursable and milestone awards make the same words — "unbilled," "overdue," "burn" —
mean different things). The data-before-calculation rule is the analyst's version of
evidence-based practice: a DSO computed on an imagined extract is not an estimate, it's
fiction with confidence. And the fixed output structure isn't bureaucracy — sponsored-AR
consumers (research administrators, controllers, sponsors) need to find validation caveats and
recommendations in the same place every time, because these analyses feed compliance
conversations where "what data was this based on?" is always the first challenge.

## Common mistakes
- Jumping straight to a metric without classifying the question → wrong sub-skill, one-module answer; route first.
- Computing one blended metric over cost-reimbursable and milestone awards → segment by bill-plan type first.
- Calculating from assumed data → fiction with confidence; require the extract or its precise description.
- Citing non-public or invented Fusion structures → stick to documented subject areas and flows; flag implementation-specific config.
- Skipping the Data Validation section when the answer seems obvious → the first audience challenge is always the data's provenance.
- Treating a week-old extract's aging as current → state the as-of date; recommend daily incremental refreshes.

## Tailor to your environment
Record your sponsored-AR landscape in `references/your-environment.md` (award and sponsor
specifics in `your-environment.private.md`, git-ignored): your award-type mix, standard
extracts and their refresh cadence, invoice grouping rule behavior, and who consumes these
analyses. **Never commit sponsor names, award numbers, or real balances.**

## References
- references/routing-map.md — question types → sub-skill, with the intake checklist
- references/your-environment.md — your award mix, extracts, cadence, consumers (fill in)
