# Your supervised-modeling setup (sanitized template)

Fill this in with your real setup. If any value is sensitive (real feature names, sample rows, target
distributions, business identifiers), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Target & task type:** <name; regression (numeric) | classification (binary/multiclass)>
- **Feature list (name → type):**
  - `<feature>` → <numeric | categorical (cardinality) | datetime | boolean>
  - `<feature>` → <type>
- **Class balance (if classifying):** <e.g. 3% positive> — cost of FP vs FN: <…>
- **Interpretability requirement:** <must explain to audit/risk? | accuracy-first internal tool?>
- **Preferred libraries:** <scikit-learn, XGBoost, LightGBM, statsmodels>
- **Baseline to beat:** <majority class | current heuristic | linear/logistic reference>
- **Validation approach:** <holdout | k-fold | time-series CV — see model-evaluation>
- **Known data issues:** <missingness, leaky columns to drop, collinear features>
