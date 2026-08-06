# Evals — machine-learning-skills:bespoke-llm-architect

Note: the skill sets `disable-model-invocation: true`, so "loads" here means the user invokes it
explicitly (by name or slash command); it should never load by automatic description matching.

## 1. Positive trigger (should load the skill)
> "We want a custom LLM fine-tuned on our reconciliation runbooks — design the whole thing,
> training and eval included."

Expected: skill loads (on explicit invocation); it does NOT start drafting. It opens with the
intake gate — precise clarifying questions on goals/success criteria, data sources and
characteristics, compute budget, latency/throughput targets, evaluation metrics, and safety
constraints — and halts until the user confirms parameters. It then blueprints backward from the
end state, proposes the lowest effective rung of the efficiency hierarchy (likely prompting + RAG
or PEFT via QLoRA/DoRA before any full fine-tune) with an explicit justification for the rung
chosen, runs the triple audit and the self-audit, and delivers Risk Assessment → Blueprint
Summary → Deliverable with runnable artifacts (configs, scripts, Dockerfile, eval harness,
experiment tracking) and documented residual risks.

## 2. Near-miss (should NOT load this skill)
> "Write me a great system prompt for a support bot."

Expected: no training component — this is a prompt-engineering commission.
`coding-agent-skills:master-prompt-architect` should handle it. If this skill loads (or gets
suggested), tighten the description / cross-links.

## 2b. Near-miss (should NOT load this skill)
> "Predict invoice payment dates from these features."

Expected: tabular supervised learning, not an LLM build.
`machine-learning-skills:supervised-modeling` (with `ml-project-framing` upstream) should handle
it. If this skill loads, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** gates on parameter intake before drafting anything final; justifies its
  position on the efficiency hierarchy (and every climb past a cheaper rung); ships complete,
  runnable configs/scripts rather than fragments; includes the evaluation harness, monitoring
  design, and red-team suite as part of the deliverable; presents Risk Assessment first.
- **Teaches:** explains *why* the cheapest effective rung wins (cost per rung, most custom-LLM
  asks resolve at prompting + RAG or PEFT) and why the audit happens before presentation (design
  mode vs. auditor mode; predictability over benchmark scores) — not just what to run.
- **Stays honest:** cites only named, verifiable techniques (GRPO, DoRA/QLoRA, YaRN, conformal
  prediction, …) and flags currency where the landscape may have moved; surfaces uncertainty
  explicitly instead of asserting low-confidence claims; when relying on the self-audit
  checklist, acknowledges it is reconstructed past the marked truncation seam in
  `references/self-audit-protocol.md` rather than presenting it as the original protocol.
