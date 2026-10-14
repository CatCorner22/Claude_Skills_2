# legal-skills — routing evals for `claude plugin eval`

Six cases, one directory each: three positive routes (the skill must fire and the answer must
respect its rail) and three near-misses (the skill must not fire). Each case runs once by default
(`runs: 1` in its `prompt.md`); override with `--runs`. Results land in `evals/results/`, which is
git-ignored.

```
claude plugin eval plugins/legal-skills --runs 1 --ablation none --max-cost-usd 2
```

The human-readable evals for these skills — the ones the house standard asks for — live at the
repository root in `evals/legal-skills/<skill>.md`; this directory holds only the machine-run cases.
