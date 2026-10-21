---
runs: 1
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Loads project-manager-qc; writes testable acceptance criteria, a task breakdown, a delegation shape and a budget before building.
---

Build me a small pipeline that pulls last quarter's orders, cleans them, totals them by region and writes a one-page summary with a chart. Plan it properly and keep the token spend sensible; last time this kind of job burned through a lot.
