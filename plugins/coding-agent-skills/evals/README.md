# coding-agent-skills — routing evals for `claude plugin eval`

Nine cases, one directory each. Five for `creative-workaround-genius`: three positive routes (the
skill must fire, and two carry a rail grader) and two near-misses that belong to sibling skills in
this plugin. Four for `project-manager-qc`: three positive routes (one with a plan grader) and a
near-miss that belongs to `continuous-improvement-skills:project-command-center`. Each case runs once by default (`runs: 1` in its `prompt.md`); override with `--runs`.
Results land in `evals/results/`, which is git-ignored.

```
claude plugin eval plugins/coding-agent-skills --runs 1 --ablation none --max-cost-usd 2
```

The human-readable evals the house standard asks for live at the repository root in
`evals/coding-agent-skills/<skill>.md`; this directory holds only the machine-run cases.
