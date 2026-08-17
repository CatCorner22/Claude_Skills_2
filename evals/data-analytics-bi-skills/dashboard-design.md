# Evals — data-analytics-bi-skills:dashboard-design

## 1. Positive trigger (should load the skill)
> "I'm building an executive dashboard for a team that approves incoming requests. What KPIs
> should go on it and what chart type should I use for showing our approval turnaround
> trending over the last 12 months versus target?"

Expected: skill loads; starts from the decision/audience; defines KPIs with
numerator/denominator, target, direction, timeframe, and grain (rejecting vanity metrics);
recommends a line chart for the trend with a target reference (position encoding, per the
perception ranking); checks the KPI is measurable at the data's grain; and advises layout
hierarchy plus context vs. target/prior (bullet graph or delta).

## 2. Near-miss (should NOT load this skill)
> "In our BI tool, how do I add a table layout and a bar view to my analysis and set up the column
> prompts?"

Expected: this is clicking together the report artifact in a specific product, not designing what the
dashboard should show — tool-mechanics that no active skill in this library owns, so nothing should
load as primary. If this design skill loads as primary, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** works backward from the decision, defines KPIs rigorously
  (numerator/denominator, target, direction, timeframe, grain), matches chart to the question
  via the perception-ranked table, verifies measurability against the data's grain, and
  advises layout hierarchy plus context vs. target/prior.
- **Teaches:** explains *why* every element must earn its place (drive a decision), why chart
  choice follows the question (Cleveland & McGill's encoding ranking — position/length before
  angle/area), why clutter-cutting is Tufte's data-ink discipline, and why context turns a
  number into a signal.
- **Honest:** attributes the canon correctly (data-ink → Tufte; bullet graph → Few) and does
  not invent perception statistics beyond the documented ranking.
- **Safe:** avoids vanity metrics, truncated bar axes, misleading dual axes, and burying the
  answer behind filters; defers palette/encoding craft to `dataviz`; hands KPI percent
  arithmetic to `math-foundations-skills:percentages-and-proportions` and summary-statistic
  choice to `data-analytics-bi-skills:descriptive-statistics` where they arise.
