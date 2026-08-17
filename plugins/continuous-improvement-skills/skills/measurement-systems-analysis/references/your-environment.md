# Your measurement systems and specs (sanitized template)

Fill this in with the metrics you actually decide on. If any value is sensitive (real system
names, reviewer names, actual limits), keep it in `your-environment.private.md` instead — that
suffix is git-ignored. Commit only sanitized, structural examples.

- **Metric 1:** <e.g. auto-match rate>
  - How measured: <system/query/report; who or what produces the number>
  - Judgment component: <e.g. reviewers classify borderline exceptions as match / no-match>
  - Judges/operators: <roles, engine runs, LLM judges involved>
  - Last agreement study + result: <date basis, %GRR or kappa **with the base rate and the 2×2
    table**, verdict>
  - Spec limits / target floor + who set them: <owner role>
- **Metric 2:** <e.g. forecast error; days-to-pay; eval pass rate in evals/>
- **Reference-answer source for attribute studies:** <who adjudicates the golden set>
- **Item-set base rate:** <the pass rate of your reference set — kappa is read against it, so record
  it; note whether borderline cases were added to move it toward 50%>
- **Stability evidence:** <where the control charts live; which SPC skill/process owns them>
- **House thresholds:** <your %GRR / ndc / kappa / Cpk floors, if stricter than the defaults>

## LLM judges in use (if any)

- **Judge configuration that is QUALIFIED** — and it must be the one you ship: <model + version,
  prompt/rubric version, temperature and decoding parameters, context policy (fresh per item?)>
- **What counts as a repeat trial here:** <swapped A/B order | reshuffled item order | re-ordered
  rubric criteria> — never a temperature change; and if you run greedy, say so, because within-judge
  agreement is then ~1.0 by construction and carries no information.
- **Swapped-order consistency rate (position bias):** <%, date measured>
- **Second judge from a different model family:** <which, and its between-judge agreement>
- **Self-preference exposure:** <does any judge grade output from its own family? which items?>
- **Verbosity check:** <does verdict correlate with response length? how tested>
