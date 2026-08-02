# Evals — data-analytics-bi-skills:dashboard-design

## 1. Positive trigger (should load the skill)
> "I'm building an executive dashboard for our AR team. What KPIs should go on it and what chart type
> should I use for showing DSO trending over the last 12 months versus target?"

Expected: skill loads; starts from the decision/audience; defines KPIs with numerator/denominator,
target, and direction (rejecting vanity metrics); recommends a line chart for the DSO trend with a
target reference; and advises layout hierarchy and context.

## 2. Near-miss (should NOT load this skill)
> "In Oracle OTBI, how do I add a table layout and a bar view to my analysis and set up the column
> prompts?"

Expected: this is building the OTBI report artifact, not designing what the dashboard should show —
the `oracle-otbi-skills:otbi-report-building` skill should handle it. If this design skill loads as
primary, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** works backward from the decision, defines KPIs rigorously (numerator/denominator,
  target, direction), matches chart to the question, and advises layout hierarchy plus context vs.
  target/prior.
- **Teaches:** explains *why* every element must earn its place (drive a decision), why chart choice
  follows the question, and why context turns a number into a signal.
- **Safe:** avoids vanity metrics, truncated bar axes, misleading dual axes, and burying the answer
  behind filters; defers palette/encoding craft to `dataviz`.
