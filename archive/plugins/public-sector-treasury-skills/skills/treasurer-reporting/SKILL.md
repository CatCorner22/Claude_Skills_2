---
name: treasurer-reporting
description: >-
  Turns cash, investment, and debt data into decision-grade treasury reports for leadership
  and boards: the standard package (cash position and trend, investment holdings versus
  policy, debt profile, forecast versus actual, exceptions), narrative that explains the
  so-what, and cadence and depth calibrated to the audience. Use when writing a treasury
  report, treasurer's report, board memo, or leadership update on cash and investments.
  Triggers: treasury report, board report, treasurer's report, cash report to leadership,
  investment report, monthly treasury package, executive summary cash.
---

# Treasurer's reporting to leadership and boards

## When to use
- Building or improving the recurring treasury package for a board or finance committee,
  a CFO/leadership team, or operating management.
- Writing the memo or narrative that accompanies treasury numbers; deciding what to report
  to whom, how often, and at what depth.
- Not for: designing interactive, self-serve dashboards and their visual mechanics → see
  `data-analytics-bi-skills:dashboard-design`. For producing the underlying daily cash
  numbers themselves → see `cash-management-skills:cash-positioning`.

## Do it
1. **Fix the audience and the decision it owns.** Boards and finance committees govern —
   they need to know funds are safe, legal, and sufficient (quarterly is typical).
   Executive leadership decides — funding, timing, risk responses (monthly). Operating
   management runs the machine (weekly or daily). Cadence and depth follow the audience;
   one package rarely serves all three, so define the tiers explicitly.
2. **Assemble the standard package.** Five exhibits, each from a verifiable source:
   - **Cash position and trend** — current balances by category (available vs restricted),
     trend vs the same period last year and vs forecast.
   - **Investment holdings vs policy** — every policy limit tested against custody data,
     with an explicit compliance affirmation (run the actual check via
     `treasury-accounting-skills:investment-policy-compliance` first).
   - **Debt profile** — outstanding by issue, fixed/variable mix, upcoming maturities and
     payment dates, covenant status.
   - **Forecast vs actual** — variance with drivers, split timing vs structural.
   - **Exceptions and actions** — policy breaches, waivers, fraud attempts, stale items,
     each with an owner and a status.
3. **Lead with the answer.** A one-page executive summary: where we stand, which direction
   we are moving, the top risks, and any decision requested — conclusion first, support
   behind it. If the committee reads only this page, they should still be correctly informed.
4. **Standardize the layout period over period.** Same exhibits, same order, same chart
   forms and definitions, so readers learn where to look and real changes stand out from
   format noise. Change the format deliberately, rarely, and with a note when you do.
5. **Make each exhibit answer one question.** Title it with the question or, better, the
   answer ("Liquidity remains above the target floor"). If an exhibit answers nothing, cut
   it — length is a cost the reader pays.
6. **Write the so-what narrative.** Explain *drivers*, not restatements: "receipts ran
   ahead of forecast because the tuition due date fell before month-end (timing)" beats
   "cash increased 4%." Quantify, separate timing from structural, and pair any decision
   request with a recommendation.
7. **Tie every number to source before publishing.** Balances to bank statements, holdings
   to custodian data, debt to the ledger and official documents; version-control the
   package. For a public institution the treasurer's report is often a public record and
   audit evidence of oversight — write every sentence as if an auditor or a journalist will
   read it, because either may.
8. **Close the loop.** Log the questions each edition provokes; recurring questions are the
   package telling you what is missing. Refine, then re-standardize.

## Why / learn
A treasury report is a decision product, not a data dump: the reader has minutes, and the
analyst's judgment about *what matters and why* is the actual deliverable — numbers do not
rank themselves. That is why the summary leads with the answer (readers who stop early still
leave correctly informed) and why each exhibit gets one question. Consistency is a reading
technology: a board member who sees the same page layout every quarter develops pattern
recognition, so a genuine anomaly registers in seconds — format churn destroys precisely
that. The no-surprises principle is the trust mechanism of treasury governance: bad news
must travel in the report before it travels around it, because a committee that learns of a
breach elsewhere stops believing the package. For a public entity there is an extra layer —
receiving the treasurer's report is part of how a governing board *evidences* oversight of
public funds (many public bodies are required by statute or bylaws to receive one — confirm
your own requirement), and the report may be a public record. That turns accuracy and
clarity from style choices into controls: the compliance affirmation is an attestation, so
it is written only after the checks actually ran, and every figure ties to a source you
could produce on request. Finally, calibrate precision to the audience: decision-makers need
direction, magnitude, and confidence — false precision (cents on a forecast) signals that
the author does not know what matters.

## Common mistakes
- Data dump with no narrative → the reader is left to do the analyst's job; lead with the so-what.
- Restating numbers in words ("cash decreased 3%") → explain the driver and whether it is timing or structural.
- Format churn every period → destroys reader pattern recognition; standardize, change rarely and deliberately.
- Reporting only good news, burying exceptions → the report loses its trust function; surface breaches with owners and actions.
- Affirming compliance without running the check → an attestation without evidence; run holdings-vs-policy first.
- False precision → cents on a forecast signal misplaced attention; match precision to the decision.
- Jargon for a lay board → committee members are rarely treasury specialists; define terms once, plainly.
- Publishing late → a decision-useful report on time beats a perfect one after the meeting.
- Numbers that do not tie to source → one caught discrepancy taints the whole package; reconcile before release.

## Tailor to your environment
Record in `references/your-environment.md`: your audiences and their cadences, the exhibit
list and definitions (what "cash" includes, which balances count as available), data sources
per exhibit, the sign-off chain, and any statutory or bylaw reporting requirement. Real
balances, holdings, and draft packages are data — keep them in
`your-environment.private.md` or other git-ignored `*.private.md` files, never committed.

## References
- references/treasury-report-package.md — package skeleton with per-exhibit specs, executive-summary template, narrative patterns, audience/cadence matrix, pre-publication checklist
- references/your-environment.md — your audiences, exhibits, sources, and sign-offs (fill in)
