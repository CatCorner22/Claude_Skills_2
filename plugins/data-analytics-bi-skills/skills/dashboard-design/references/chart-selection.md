# Chart selection and KPI definition (reference)

## Contents
- Chart-by-question decision table
- Chart cautions
- KPI definition template
- Vanity vs. actionable metrics
- Layout quick rules

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
| Single number vs. target | **KPI tile** / bullet chart | Always with target and prior period |
| Geographic pattern | **Map** (choropleth) | Only when geography is the question |
| Flow between stages | **Funnel** / sankey | Funnel for conversion; keep stages few |

## Chart cautions
- Bar length encodes magnitude → **start bar axes at zero** or you lie by truncation.
- Pie/donut with >3 slices → angles are hard to compare; switch to bars.
- Dual Y-axes → visually implies correlation; prefer two aligned charts or index both series to 100.
- 3-D, shadows, gradients → distort values; keep 2-D and flat.
- Too many colors → color should encode a variable, not decorate. See the built-in `dataviz` skill.

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

## Vanity vs. actionable metrics
- **Vanity:** only goes up, no denominator, no target — cumulative signups, total pageviews, total
  followers. Impressive, un-actionable.
- **Actionable:** a rate or ratio with a target and a clear "so what" — conversion rate, revenue per
  active account, on-time-payment %, DSO. When it moves, someone knows what to do.

## Layout quick rules
- Most important item **top-left**; importance ~ size and position.
- Group related metrics; keep a consistent grid and alignment.
- Headline number first, breakdown beneath.
- Default (unfiltered) view answers the primary question with zero clicks; drill-down for follow-ups.
- Consistent number formats, date ranges, and color meaning across the whole dashboard.
