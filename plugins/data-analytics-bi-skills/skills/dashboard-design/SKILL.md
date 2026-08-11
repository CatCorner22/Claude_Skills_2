---
name: dashboard-design
description: >-
  Designs decision-driving BI dashboards, reports, and scorecards on the Few, Tufte, and
  Cleveland & McGill canon: works backward from the reader's decision, defines each KPI rigorously (numerator,
  denominator, target, direction, timeframe, grain), picks the chart from the analytical
  question — position and length encodings before angle or area — builds a top-left,
  headline-then-support hierarchy, cuts non-data ink, gives every number context against
  target or prior period, and keeps the default view answering the main question with zero
  clicks. Use when building a report, dashboard, or scorecard, defining a KPI or metric,
  choosing a chart type, or cutting clutter from an existing view. Triggers: dashboard, KPI,
  metric, scorecard, chart choice, which chart, visualization, report layout, drill-down,
  report design, vanity metric, chart type, executive dashboard, KPI definition, data-ink,
  bullet graph, dashboard clutter, wall of numbers.
metadata:
  version: "1.1.0"
  source: >-
    Grounded in Few (Information Dashboard Design), Tufte (The Visual Display of Quantitative
    Information, data-ink), and Cleveland & McGill (JASA 1984, graphical perception). Claims
    marked [snippet-only] were cross-checked via web-search snippets, not the primary text.
---

# Dashboard design

## When to use
- Designing a new dashboard, report, or scorecard, or reworking one that isn't driving decisions.
- Defining a KPI/metric properly (what it counts, its target and direction) or auditing a shaky one.
- Choosing the right chart for a specific question, or reducing clutter on a busy view.
- Not for: a one-time narrative readout of a finished analysis — one claim per slide, proven by a
  visual → see `data-analytics-bi-skills:assertion-evidence-deck`. A dashboard is a standing
  instrument read repeatedly; a deck is a story told once.
- Not for: building the actual report artifact in a BI tool — e.g. an Oracle OTBI analysis with its
  subject areas, layouts, and prompts → that's an OTBI report build
  (archived: `oracle-otbi-skills:otbi-report-building`, restorable from `archive/`). For chart color
  palettes and encoding craft → use the built-in `dataviz` skill.

## Do it
1. **Start from the decision and the audience, not the data.** Name who reads this, the decision they
   make, and the action that changes based on it. A dashboard with no decision behind it becomes a wall
   of numbers nobody uses.
2. **Define each KPI rigorously.** Specify its **numerator and denominator**, its **target/benchmark**,
   its **direction** (is up good or bad?), the **timeframe**, and the **segment/grain**. Reject vanity
   metrics — a number that only ever goes up (cumulative signups, total pageviews) drives no decision.
   Prefer rates and ratios to raw counts, and get the percent arithmetic honest — the base, percent vs.
   percentage points, weighted averages across unequal groups →
   `math-foundations-skills:percentages-and-proportions`. KPI template:
   `references/chart-selection.md`.
3. **Confirm each KPI is measurable in the data.** Check the grain, completeness, and skew of the
   columns behind every tile before designing around them —
   `data-analytics-bi-skills:exploratory-data-analysis` for the profile,
   `data-analytics-bi-skills:descriptive-statistics` for whether the "typical value" tile should show a
   mean or a median. The query feeding each tile must aggregate at the dashboard's grain —
   `data-analytics-bi-skills:sql-for-analysts`.
4. **Choose the chart from the question, not from taste.** Match the visual to the analytical question:
   comparison → bar; trend over time → line; composition → stacked bar/100% bar (rarely pie);
   distribution → histogram/box; relationship → scatter; part-to-whole over time → area. The decision
   table in `references/chart-selection.md` is ordered by Cleveland & McGill's perception ranking —
   when in doubt, a plain bar or line beats a fancy chart.
5. **Build a visual hierarchy.** Put the most important number or chart **top-left** (where the eye
   starts), group related items, and follow a headline-then-support pattern: the answer big and first,
   the breakdown beneath it. Size and position should mirror importance.
6. **Cut clutter until only signal remains.** Remove gridlines, 3-D, redundant legends, and decorative
   color — Tufte's data-ink discipline: ink that shows no data competes with ink that does. Label
   directly where you can, keep axes starting at zero for bar length comparisons, and avoid dual-axis
   charts that imply false correlations.
7. **Give every metric context.** A bare "Revenue: 4.2M" means nothing. Show it against target, prior
   period, or benchmark, and indicate direction — that comparison is what turns a number into a signal.
   Few's bullet graph exists precisely for this: measure, target, and qualitative bands in one compact
   row.
8. **Add interactivity only where it serves the decision.** Filters/prompts and drill-down (summary →
   detail) are powerful, but the **default view must answer the primary question with zero clicks**.
   Interactivity is for follow-up questions, not for hiding the main answer.
9. **Test it on a real user.** Can someone in the audience answer the driving question in a few seconds
   without a tour? If not, the layout or chart choice is wrong — iterate before you ship.

## Why / learn
A dashboard is not a report of everything knowable; it is an instrument built to **drive one or a few
decisions** — Few's definition of a dashboard as a single-screen monitoring display exists to enforce
exactly that constraint — and that purpose is the test every element must pass: if a chart doesn't
change what someone does, it's clutter, however pretty. Working backward from the decision is what
makes the design converge instead of sprawl: the decision tells you which metrics matter, the metrics
tell you which comparisons matter, and the comparisons tell you which chart shows them. **Chart choice
is dictated by the question** because graphical perception is measurably unequal across encodings:
Cleveland & McGill's experiments (JASA 1984) ranked the elementary perceptual tasks from position on a
common scale (most accurate), through length, direction, and angle, then area, then volume and
curvature, down to shading and color saturation (least) [snippet-only] — which is exactly why bars
beat pies and why a line is unbeatable for trend. **KPI rigor** is where dashboards quietly fail: an
undefined metric ("engagement") or a vanity metric (a cumulative count that can't go down) gives the
illusion of measurement while steering nothing, so pinning down numerator, denominator, target, and
direction is what makes a metric actionable. **Context is the difference between a number and a
signal** — 4.2M is neither good nor bad until it sits next to a target or last quarter. And clarity
comes from subtraction — Tufte's data-ink ratio names the discipline: maximize the share of ink that
presents data. (Attribution note: the data-ink ratio is Tufte's, from The Visual Display of
Quantitative Information; it is often misattributed to Few, whose own contributions are the
dashboard-specific application and the bullet graph.)

## Common mistakes
- Designing from available data instead of the decision → a dashboard nobody acts on. Start from the decision and audience.
- Vanity metrics (cumulative totals, raw pageviews) → look impressive, drive nothing. Use rates and ratios with targets.
- Pie chart with many slices → angles are hard to compare. Use a bar chart; reserve pie for 2–3 parts.
- Truncated bar-chart axis → exaggerates differences. Start bar axes at zero (line axes may differ).
- Dual axes to overlay unrelated series → implies a correlation that may not exist. Use two charts or index to 100.
- Numbers with no comparison → no meaning. Always show vs. target / prior / benchmark.
- Burying the answer behind filters and drill-downs → the default view should answer the main question.
- Rainbow of colors → color should encode meaning, not decorate. For palette craft, use `dataviz`.
- KPI defined only in the BI tool's formula box → nobody can audit it. Write the definition down (template in the reference) and check it against the data's grain.

## Tailor to your environment
Wire in your current role here — this skill is deliberately domain-neutral, and the same method serves
an analyst's revenue dashboard, an attorney's matter-status board, an ops manager's queue monitor, or a
developer's service scorecard, wherever you work next. Record your setup in
`references/your-environment.md` (keep sensitive material — real KPI targets, client names, actual
figures — in `your-environment.private.md`, which is git-ignored). Capture your BI tool (Power BI,
Tableau, Oracle OTBI, Looker), your audiences and the decisions each dashboard serves, your standard
KPI definitions and targets, and any branding/layout conventions. To build the artifact, follow your BI
tool's own build path (wire tool-specific build notes into this file); for color and encoding, use
`dataviz`.

## References
- references/chart-selection.md — the perception-ranked chart-by-question table, KPI definition
  template, layout and decluttering method, and a worked domain-neutral example (a work-queue
  dashboard designed end to end)
- references/your-environment.md — your BI tool, audiences, KPI targets, and conventions (sanitized
  stub; live detail goes in the `.private.md` twin)
