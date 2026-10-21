---
runs: 1
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Loads project-manager-qc; writes a requirement ledger, phases with testable acceptance criteria, owners, a budget and checkpoints that a later session can pick up, before building.
---

We're moving forty reporting tables to the new warehouse over the next few weeks. It will take several sessions, and I want subagents doing the per-table work. Before anything starts, plan it so any session can pick up where the last one stopped, and keep the token spend under control — the last migration burned through a lot.
