# Evals — coding-agent-skills:agentic-workflow-design

## 1. Positive trigger (should load the skill)
> "I want to build an agent that reads incoming vendor invoices, extracts the fields, checks them
> against our PO system, and files them — but it keeps making mistakes on messy PDFs. How should I
> structure it so it's reliable?"

Expected: skill loads; decomposes into checkable steps (extract → validate → match → file); defines
each tool as a contract; adds per-step verification and a human-approval gate before filing; bounds
the loop; and recommends building an eval set of real invoices. May note that the deterministic parts
should be plain code, not LLM calls.

## 2. Near-miss (should NOT load this skill)
> "Rewrite this system prompt so the model stops adding a preamble and just returns the JSON."

Expected: this is single-prompt wording / output-format control, handled by
`coding-agent-skills:prompt-engineering`, not multi-step workflow design. If this skill loads
instead, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** decomposes into small verifiable steps, defines tool contracts, adds guardrails
  (step/cost bounds), verification, and a human-in-the-loop gate for irreversible actions.
- **Teaches:** explains that reliability comes from decomposition and verification, not a bigger
  prompt; treats the agent as a testable process; and argues for script-over-agent where possible.
- **Safe:** requires approval before irreversible actions, least-privilege tools, and an eval set
  rather than vibes-based tuning.
