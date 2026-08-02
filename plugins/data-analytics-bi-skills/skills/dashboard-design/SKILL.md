---
name: dashboard-design
description: >-
  Designs decision-driving BI dashboards and reports — defining robust KPIs (numerator, denominator,
  target, direction), choosing the right chart for the question being asked, and laying out for the
  audience and the decision. Use when building a report, dashboard, or scorecard, defining a KPI or
  metric, choosing a chart type, or cutting clutter from an existing view. Triggers: dashboard, KPI,
  metric, scorecard, chart choice, which chart, visualization, report layout, drill-down, report
  design, vanity metric, chart type.
---

# Dashboard design

## When to use
- Designing a new dashboard, report, or scorecard, or reworking one that isn't driving decisions.
- Defining a KPI/metric properly (what it counts, its target and direction) or auditing a shaky one.
- Choosing the right chart for a specific question, or reducing clutter on a busy view.
- Not for: building the actual report artifact in Oracle Fusion (subject areas, layouts, prompts) →
  see `oracle-otbi-skills:otbi-report-building`. For chart color palettes and encoding craft → use the
  built-in `dataviz` skill.

## Do it
1. **Start from the decision and the audience, not the data.** Name who reads this, the decision they
   make, and the action that changes based on it. A dashboard with no decision behind it becomes a wall
   of numbers nobody uses.
2. **Define each KPI rigorously.** Specify its **numerator and denominator**, its **target/benchmark**,
   its **direction** (is up good or bad?), the **timeframe**, and the **segment/grain**. Reject vanity
   metrics — a number that only ever goes up (cumulative signups, total pageviews) drives no decision.
   See the KPI template in `references/chart-selection.md`.
3. **Choose the chart from the question, not from taste.** Match the visual to the analytical question:
   comparison → bar; trend over time → line; composition → stacked bar/100% bar (rarely pie);
   distribution → histogram/box; relationship → scatter; part-to-whole over time → area. When in doubt,
   a plain bar or line beats a fancy chart.
4. **Build a visual hierarchy.** Put the most important number or chart **top-left** (where the eye
   starts), group related items, and follow a headline-then-support pattern: the answer big and first,
   the breakdown beneath it. Size and position should mirror importance.
5. **Cut clutter until only signal remains.** Remove gridlines, 3-D, redundant legends, and decorative
   color. Label directly where you can, keep axes starting at zero for bar length comparisons, and
   avoid dual-axis charts that imply false correlations. Every pixel should carry information.
6. **Add interactivity only where it serves the decision.** Filters/prompts and drill-down (summary →
   detail) are powerful, but the **default view must answer the primary question with zero clicks**.
   Interactivity is for follow-up questions, not for hiding the main answer.
7. **Give every metric context.** A bare "Revenue: 4.2M" means nothing. Show it against target, prior
   period, or benchmark, and indicate direction — that comparison is what turns a number into a signal.
8. **Test it on a real user.** Can someone in the audience answer the driving question in a few seconds
   without a tour? If not, the layout or chart choice is wrong — iterate before you ship.

## Why / learn
A dashboard is not a report of everything knowable; it is an instrument built to **drive one or a few
decisions**, and that purpose is the test every element must pass — if a chart doesn't change what
someone does, it's clutter, however pretty. Working backward from the decision is what makes the design
converge instead of sprawl: the decision tells you which metrics matter, the metrics tell you which
comparisons matter, and the comparisons tell you which chart shows them. **Chart choice is dictated by
the question**, because our visual system reads position and length far more accurately than angle or
area — which is exactly why bars beat pies and why a line is unbeatable for trend. **KPI rigor** is
where dashboards quietly fail: an undefined metric ("engagement") or a vanity metric (a cumulative
count that can't go down) gives the illusion of measurement while steering nothing, so pinning down
numerator, denominator, target, and direction is what makes a metric actionable. And **context is the
difference between a number and a signal** — 4.2M is neither good nor bad until it sits next to a
target or last quarter. Clarity comes from subtraction: the fewer things on the screen, the faster the
one that matters is found.

## Common mistakes
- Designing from available data instead of the decision → a dashboard nobody acts on. Start from the decision and audience.
- Vanity metrics (cumulative totals, raw pageviews) → look impressive, drive nothing. Use rates and ratios with targets.
- Pie chart with many slices → angles are hard to compare. Use a bar chart; reserve pie for 2–3 parts.
- Truncated bar-chart axis → exaggerates differences. Start bar axes at zero (line axes may differ).
- Dual axes to overlay unrelated series → implies a correlation that may not exist. Use two charts or index to 100.
- Numbers with no comparison → no meaning. Always show vs. target / prior / benchmark.
- Burying the answer behind filters and drill-downs → the default view should answer the main question.
- Rainbow of colors → color should encode meaning, not decorate. For palette craft, use `dataviz`.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep sensitive material — real KPI targets,
client names, actual figures — in `your-environment.private.md`, which is git-ignored). Capture your
BI tool (Power BI, Tableau, Oracle OTBI, Looker), your audiences and the decisions each dashboard
serves, your standard KPI definitions and targets, and any branding/layout conventions. This skill
then applies its generic design logic to your real reports. To build the artifact in Oracle Fusion,
hand off to `oracle-otbi-skills:otbi-report-building`; for color and encoding, use `dataviz`.

## References
- references/chart-selection.md — chart-by-question decision table and the KPI definition template
- references/your-environment.md — your BI tool, audiences, KPI targets, and conventions (add when supplied)
