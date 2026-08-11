---
name: reporting-visualization-recommendations
description: >-
  Turns sponsored-AR analysis into finished deliverables — the standard structured report
  (executive summary, data validation, detailed tables, visual descriptions, insights by
  financial/operational/compliance/strategic angle), suggested OTBI-style report patterns
  (AR aging by project, project invoices prior to acceptance), and actionable recommendations
  covering collection priorities, billing acceleration, and data quality, with multi-currency,
  intercompany, and partial-payment edge cases handled. Use as the final step of any
  sponsored-AR analysis, or when the user asks for summaries, dashboards, report designs, or
  next steps on sponsored/grants receivables. Triggers: sponsored AR report, grants AR summary,
  AR dashboard for projects, executive summary receivables, OTBI report for sponsored projects,
  aging by sponsor report, what should we do about unbilled, present sponsored AR, next steps
  grants AR.
---

# Sponsored-AR reporting, visualization, and recommendations

## When to use
- Final step of a sponsored-AR analysis: packaging findings from the recon and KPI skills into
  a presentable, exportable deliverable.
- Designing recurring OTBI-style reports or dashboards for sponsored receivables, or turning
  findings into an action plan.
- Not for: producing the numbers themselves → run
  `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon` /
  `sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast` first. For general dashboard
  craft → see `data-analytics-bi-skills:dashboard-design`; for OTBI build mechanics → see
  `oracle-otbi-skills:otbi-report-building`.

## Do it
1. **Assemble the standard structure** (the router's contract, rendered in full):
   - **Executive Summary** — the three sentences a dean/CFO reads: level, direction, the one
     action that matters.
   - **Data Validation** — sources, as-of date, aging basis, segments, known gaps. Never omit;
     this section is what survives challenge.
   - **Detailed Tables** — the pipeline cut, aging by segment, KPI trends, exception queues —
     each with its as-of date and basis labeled.
   - **Visual Descriptions** — describe each chart precisely enough to build ("stacked bar of
     open AR by aging bucket, one bar per sponsor category, 12-month trend line of 90+ share
     overlaid"); match chart to question (composition → stacked bar, trend → line, ranking →
     sorted bar, flow → waterfall for unbilled→billed→collected).
   - **Insights by Angle** — financial (liquidity/working capital), operational (pipeline,
     queues, cycle times), compliance/risk (close-out exposure, aged federal balances,
     single-sponsor concentration), strategic (sponsor mix, terms, staffing).
   - **Actionable Recommendations** and **Edge Cases & Next Questions** (below).
2. **Suggest durable OTBI-style report patterns** for anything the user will need monthly —
   an analysis that recurs belongs in a report, not a re-run: **AR Aging by Project/Sponsor**
   (payment schedules basis), **Project Invoices Prior to Acceptance** (the generate-to-accept
   gap), **Unbilled Pipeline by Status** (bill transactions), **Exception/Error Queue**,
   **Award Close-out Exposure** (unbilled + open AR on ending awards).
   `references/report-patterns.md` specifies each (area, columns, filters, prompts); build
   mechanics per `oracle-otbi-skills:otbi-report-building` and scheduling per
   `oracle-otbi-skills:otbi-report-scheduling-sharing`.
3. **Write recommendations that name an owner and a sequence.** Three standard families:
   **collection priorities** (which billed AR to chase, ranked by amount × age × sponsor
   risk), **billing acceleration** (clear the error queue by owner, shorten generate-to-accept,
   align billing calendar to cost collection — from the recon skill's findings), and
   **data quality fixes** (grouping-rule gaps, missing attributes, stale extracts). "Improve
   collections" is not a recommendation; "call these five sponsors holding 60% of the 90+
   bucket, this week, per the attached list" is.
4. **Handle the edge cases explicitly in the deliverable:** **multi-currency** (state the
   reporting currency and rate date; never sum mixed currencies silently), **intercompany/
   internal awards** (segregate — internal balances aren't sponsor risk; tie to
   `treasury-accounting-skills:intercompany-accounting` if they must reconcile), and
   **partial payments** (report open balance, not original amount, and show
   partially-paid status where it changes the collections story).
5. **Finish export-ready.** Tables formatted for the medium (spreadsheet deliverables via
   `data-tools-skills:excel-automation-python` when scripted), every figure dated, every
   metric's definition footnoted, and the next-questions list honest about what the data
   couldn't answer.

## Why / learn
The last mile is where sponsored-AR analysis succeeds or dies, because its audience is
unusually mixed: research administrators who know the awards but not the ledger, controllers
who know the ledger but not the awards, and executives who know neither but sign for both.
The fixed structure is a contract with that audience — the summary is for the signer, the
validation section is for the inevitable "based on what data?" challenge, and the
insights-by-angle section exists because the same table genuinely means different things to
different readers, and making each meaning explicit is the analyst's job, not the reader's.
The report-pattern step encodes a deeper operational truth: an analysis that will be asked for
again is a *product*, and products belong in the reporting system with a refresh schedule, not
in an analyst's notebook — the OTBI pattern list is how one-off insight becomes standing
capability. And the edge cases are listed not because they're rare but because they're
silent: mixed currencies sum without complaint, internal awards inflate "sponsor" risk
unnoticed, and an original-amount aging overstates exposure on every partially-paid invoice.
A deliverable that names its edge cases is one the reader can trust past the first question.

## Common mistakes
- Leading with tables instead of the three-sentence summary → executives read the first block only; put the answer there.
- Dropping Data Validation "to keep it short" → the first challenge is always provenance; it stays.
- Vague chart requests ("add a dashboard") → describe each visual precisely enough to build.
- Recommendations without owner and sequence → they read well and change nothing; name who does what first.
- Re-running the same analysis monthly by hand → promote it to an OTBI report with a schedule.
- Summing mixed currencies / including internal awards in sponsor risk / aging original amounts → the three silent edge cases; handle each explicitly.
- Hiding what the data couldn't answer → the next-questions list is credibility, not weakness.

## Tailor to your environment
Keep your deliverable standards in `references/your-environment.md` (real report instances in
`your-environment.private.md`, git-ignored): house report template, chart conventions, the
standing report catalog with owners/schedules, currency policy, and your escalation path for
recommendations. **Never commit real sponsor data or balances.**

## References
- references/report-patterns.md — the five standing OTBI-style report specs + visual-choice and recommendation formats
- references/your-environment.md — your templates, catalog, conventions (fill in)
