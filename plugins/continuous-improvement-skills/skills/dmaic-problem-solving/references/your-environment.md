# Your DMAIC environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (real customers, systems, or numbers),
keep it in `your-environment.private.md` instead — that suffix is git-ignored. Commit only sanitized,
structural examples.

- **Typical project types:** <e.g. reduce duplicate payments, cut close cycle time, reduce recon breaks>
- **CTQs and specs:** <the customer-critical characteristics you measure and their limits>
- **Baseline data source:** <where you pull it — ERP, exception report, ticketing, timestamps>
- **Operational-definition notes:** <ambiguities to pin down, e.g. how "late" or "defect" is counted>
- **Measurement-system practice:** <how you sanity-check data trustworthiness before baselining>
- **Analyze conventions:** <significance level / test types you accept; who reviews the analysis>
- **Pilot practice:** <how you run small-scale pilots here; guardrails>
- **Control practice:** <control chart / KPI limits you use; where standard work is stored>
- **Chart and rule set:** <chart type per metric, subgroup rule, which run rules are armed and why>
- **Limit-recompute rule:** <what change justifies recomputing limits, and who approves it>
- **Counterweight metrics:** <for each common project type, the metric a fix here tends to damage>
- **Tollgate owners:** <who signs off each phase; cadence of reviews>
- **Tollgate reviewer:** <who asks the stop questions and is independent of the project team>
- **Closure convention:** <how met / partially met / missed is reported, and who re-charters residuals>
