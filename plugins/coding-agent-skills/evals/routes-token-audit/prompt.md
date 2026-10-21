---
runs: 1
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Loads puppet-master; analyses where the run's tokens went (turns, re-sent context, large results) and proposes savings that keep every check the run made.
---

Last night's agent run used far more budget than a job that size should. Its transcript is run.jsonl in this folder. Where did it all go, and how do we bring it down without dropping any of the checks it ran?
