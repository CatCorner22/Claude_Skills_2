---
runs: 1
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Does not load puppet-master; rewriting a prompt so the model follows its output format belongs to prompt-engineering.
---

This system prompt makes the model ramble and ignore the output format we asked for. Rewrite it so the answers come back in the right shape.
