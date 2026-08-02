# Your feature setup (sanitized template)

Fill this in with your real setup. If any value is sensitive (real column names, category lists, sample
rows, business identifiers), keep it in `your-environment.private.md` instead — that suffix is git-ignored.
Commit only sanitized, structural examples.

- **Categorical fields (name → cardinality → encoding):**
  - `<field>` → <#levels> → <one-hot | ordinal | frequency | target(out-of-fold)>
  - `<field>` → <#levels> → <encoding>
- **Skewed numerics needing transform:** <e.g. invoice_amount, balance → log>
- **Model type consuming the features:** <linear/regularized (scale) | tree/boosting (no scale)>
- **Timestamp columns & calendar effects:** <month-end, quarter-end, payroll dates, holidays, business days>
- **Lag / rolling features you use:** <lags 1/7/28; trailing 7-day mean; strictly past windows>
- **Missingness — where it arises and what it means:** <field → reason blank → informative? yes/no>
- **Aggregations / ratios that matter:** <per-customer avg, amount ÷ typical amount>
- **Pipeline tooling:** <scikit-learn Pipeline/ColumnTransformer, feature-engine, category_encoders>
