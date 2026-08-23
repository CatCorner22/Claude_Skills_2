# Chart selection and KPI definition (reference)

Method lineage: Stephen Few's *Information Dashboard Design* (the dashboard as a
single-screen monitoring instrument; the bullet graph), Edward Tufte's *The Visual Display of
Quantitative Information* (the data-ink ratio), and Cleveland & McGill, "Graphical
Perception" (JASA, 1984) — the experiments behind the encoding ranking below. Claims marked
[snippet-only] were cross-checked via web-search snippets rather than the primary text.

## Contents
- [The perception ranking (why the table works)](#the-perception-ranking-why-the-table-works)
- [Chart-by-question decision table](#chart-by-question-decision-table)
- [Chart cautions](#chart-cautions)
- [KPI definition template](#kpi-definition-template)
- [Vanity vs. actionable metrics](#vanity-vs-actionable-metrics)
- [Context: turning a number into a signal](#context-turning-a-number-into-a-signal)
- [Layout and visual hierarchy](#layout-and-visual-hierarchy)
- [The decluttering pass (data-ink)](#the-decluttering-pass-data-ink)
- [Worked example — a work-queue dashboard](#worked-example--a-work-queue-dashboard)
- [Testing the dashboard](#testing-the-dashboard)
- [Sources and attribution notes](#sources-and-attribution-notes)

## The perception ranking (why the table works)

Cleveland & McGill measured how accurately people decode values from different visual
encodings ("elementary perceptual tasks"). Their experimentally confirmed ordering, from
most accurately read to least [snippet-only]:

1. Position along a common scale (points on one axis; bar ends against one baseline)
2. Position along identical, non-aligned scales (small multiples)
3. Length, direction, angle
4. Area
5. Volume, curvature
6. Shading, color saturation

Two working rules fall out of it:
- **Encode the value you most need compared in the highest-ranked channel available.**
  That is why a sorted bar chart (position/length on a common scale) beats a pie (angle/area)
  for the same data, and why a line chart dominates for trend (position along a common scale,
  repeatedly).
- **Reserve the low-ranked channels for redundancy or approximate context** — shading and
  saturation can back up a value already encoded by position, but should not carry it alone.

## Chart-by-question decision table
Pick the chart from the question you are answering, not from habit.

| Analytical question | Default chart | Notes |
|---|---|---|
| Compare values across categories | Horizontal/vertical **bar** | Sort by value; axis starts at zero |
| How does it change over time (trend) | **Line** | Time on X; several lines OK if few and labeled |
| Part-to-whole at one point | **Stacked bar** or **100% bar** | Pie only for 2–3 parts |
| Part-to-whole over time | **Stacked area** or 100% area | Watch readability of middle bands |
| Distribution of one variable | **Histogram** / **box plot** | Box for comparing groups' spread |
| Relationship between two numerics | **Scatter** | Add trend line; size/color a third variable sparingly |
| Rank / top-N | Sorted **bar** | Show the cutoff and "other" if truncating |
| Single number vs. target | **KPI tile** / **bullet graph** | Always with target and prior period |
| Geographic pattern | **Map** (choropleth) | Only when geography is the question |
| Flow between stages | **Funnel** / sankey | Funnel for conversion; keep stages few |

The rows are ordered choices, not suggestions: each default puts the compared value into the
highest-ranked encoding the question allows. Deviate only when you can say which perceptual
task the alternative serves better.

## Chart cautions
- Bar length encodes magnitude → **start bar axes at zero** or you lie by truncation. (Line
  charts encode by position, not length, so a non-zero baseline can be legitimate there —
  say so on the axis.)
- Pie/donut with >3 slices → angle and area are low on the ranking; switch to a sorted bar.
- Dual Y-axes → visually implies correlation; prefer two aligned charts or index both series to 100.
- 3-D, shadows, gradients → distort values; keep 2-D and flat.
- Too many colors → color should encode a variable, not decorate. See the built-in `dataviz` skill.
- Smoothed/interpolated lines through sparse points → invent data between observations; show markers.

## KPI definition template
Define every KPI with all of these before it goes on a dashboard:
- **Name:** <short, unambiguous>
- **Question it answers / decision it drives:** <…>
- **Formula:** numerator = <…>, denominator = <…> (rates/ratios beat raw counts)
- **Grain / segment:** <per region, per month, per rep>
- **Target / benchmark:** <value or prior period>
- **Direction:** <higher is better | lower is better>
- **Timeframe:** <MTD, trailing 30d, fiscal quarter>
- **Source & owner:** <table/report; who is accountable>

A KPI whose numerator and denominator you cannot state is not yet a KPI — it is a word
("engagement", "efficiency") waiting to mislead. Write the definition down where readers can
find it; a tooltip or a definitions page beats tribal knowledge.

## Vanity vs. actionable metrics
- **Vanity:** only goes up, no denominator, no target — cumulative signups, total pageviews, total
  followers. Impressive, un-actionable.
- **Actionable:** a rate or ratio with a target and a clear "so what" — conversion rate, revenue per
  active account, on-time-completion %, cost per case. When it moves, someone knows what to do.
- The percent arithmetic behind rate KPIs has classic traps — base errors, percent vs.
  percentage points, weighted averages across unequal groups, mix effects — worked in
  `math-foundations-skills:percentages-and-proportions`.

## Context: turning a number into a signal
A bare number is unreadable as good or bad. Every tile carries at least one comparison:
- **vs. target** — the contract the number is judged against.
- **vs. prior period** — direction and momentum (show the delta and its sign).
- **vs. peer/benchmark** — is this normal for entities like us?
- **Bullet graph** (Few): one compact row holding the measure (bar), the target (tick), and
  2–3 qualitative bands (poor/ok/good) — the densest honest form for "number vs. target".
- **Sparkline**: a word-sized trend line beside the number — context without a full chart.
Choose the "typical value" honestly: on skewed data a median tile reads truer than a mean —
`data-analytics-bi-skills:descriptive-statistics` covers the choice.

## Layout and visual hierarchy
- Most important item **top-left**; importance ~ size and position.
- Headline number first, breakdown beneath: answer → evidence → detail, in reading order.
- Group related metrics; keep a consistent grid and alignment.
- Default (unfiltered) view answers the primary question with zero clicks; drill-down for follow-ups.
- Consistent number formats, date ranges, and color meaning across the whole dashboard.
- One screen. When it doesn't fit, the fix is scope (fewer decisions per dashboard), not scrolling.

## The decluttering pass (data-ink)
Tufte's data-ink ratio: of all the ink on the page, what share shows data? Run this pass on
every finished view, in order:
1. Delete decoration: 3-D, shadows, background fills, logos inside the plot area.
2. Delete redundancy: repeated legends, axis titles restating the chart title, gridlines a
   direct label would replace.
3. Mute what remains: gridlines (if truly needed) to light gray; borders thinned or removed.
4. Promote data: direct-label series instead of a legend where there are few series; label
   the last point of a line instead of the whole axis.
5. Re-read at a distance: the biggest visual weight should sit on the most important data.

## Worked example — a work-queue dashboard

Domain-neutral on purpose: the "queue" below is any stream of work items — support tickets,
legal matters, invoices to approve, pull requests, intake requests. **All numbers are
illustrative.**

**Decision and audience (step 1).** The team lead reads it each morning and decides two
things: where to move people today, and whether to escalate for more capacity this week.

**KPI definitions (step 2).** Four, written against the template:

| KPI | Formula | Grain | Target | Direction |
|---|---|---|---|---|
| Aged-past-SLA % | items open > SLA / all open items | daily, per queue | ≤ 5% | lower |
| Throughput rate | items closed / items received | trailing 7d | ≥ 100% | higher |
| Backlog | open items count | daily snapshot | ≤ 2 weeks' intake | lower |
| First-pass quality | items closed without rework / items closed | trailing 30d | ≥ 90% | higher |

Rejected on sight: "total items processed all-time" (cumulative — vanity) and "average
handle time" without a quality pair (drives speed at quality's expense).

**Measurability check (step 3).** Profiling the item table shows the grain is one row per
item *event*, not per item — so every KPI query must first collapse to one row per item, or
backlog and throughput double-count. Handle-time is right-skewed (a few month-old monsters),
so any "typical age" tile shows the median.

**Chart choices (step 4, from the table).**
- Aged-past-SLA % today vs. target → **bullet graph** (single number vs. target).
- Throughput trend, 12 weeks → **line** (change over time), target rule at 100%.
- Backlog composition by queue → **sorted bar** (comparison), not a pie of nine slices.
- Age distribution of open items → **histogram**; the SLA as a reference line.

**Layout (step 5).** Top-left: the aged-past-SLA bullet — it drives the escalation decision.
Across the top: the other three headline tiles, each with delta vs. last week. Below:
throughput line (left) and backlog-by-queue bar (right). Bottom: age histogram. Drill-down
from any tile to the item list, but the escalation question is answerable with zero clicks.

**Declutter (step 6).** First draft had twelve charts; seven were breakdowns nobody acts on
daily — moved behind drill-down. Gridlines muted, legends replaced with direct labels, the
red/amber/green reserved exclusively for vs.-target status so color has one meaning.

**Test (step 9).** A second team lead, cold: "Can you tell in ten seconds whether to
escalate this week?" — answered from the top row alone. Ship it.

## Testing the dashboard
- The few-seconds test: a real audience member answers the driving question without a tour.
- The action test: for each element, name the decision it changes; no answer → cut or demote.
- The zero-clicks test: default view, no filters touched, primary question answered.
- The color test: every color used states what it encodes; grayscale print still readable.
- The definition test: any KPI on screen has its written definition one step away.

## Sources and attribution notes
- Cleveland, W. S. & McGill, R., "Graphical Perception: Theory, Experimentation, and
  Application to the Development of Graphical Methods", *JASA* 79 (1984), 531–554 — the
  perceptual-task ranking [snippet-only].
- Tufte, E., *The Visual Display of Quantitative Information* (1983) — data-ink ratio.
- Few, S., *Information Dashboard Design* (2006) — dashboard definition, bullet graph.
- Attribution notes: the **data-ink ratio is Tufte's**, not Few's (a common misattribution);
  the **bullet graph is Few's**. "People read top-left first" is a convention of
  left-to-right reading cultures and layout practice, not a Cleveland & McGill finding —
  mirror it for right-to-left audiences.
