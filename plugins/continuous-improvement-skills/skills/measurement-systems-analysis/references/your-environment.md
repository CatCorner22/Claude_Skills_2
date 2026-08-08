# Your measurement systems and specs (sanitized template)

Fill this in with the metrics you actually decide on. If any value is sensitive (real system
names, reviewer names, actual limits), keep it in `your-environment.private.md` instead — that
suffix is git-ignored. Commit only sanitized, structural examples.

- **Metric 1:** <e.g. auto-match rate>
  - How measured: <system/query/report; who or what produces the number>
  - Judgment component: <e.g. reviewers classify borderline exceptions as match / no-match>
  - Judges/operators: <roles, engine runs, LLM judges involved>
  - Last agreement study + result: <date basis, %GRR or kappa, verdict>
  - Spec limits / target floor + who set them: <owner role>
- **Metric 2:** <e.g. forecast error; days-to-pay; eval pass rate in evals/>
- **Reference-answer source for attribute studies:** <who adjudicates the golden set>
- **Stability evidence:** <where the control charts live; which SPC skill/process owns them>
- **House thresholds:** <your %GRR / ndc / kappa / Cpk floors, if stricter than the defaults>
