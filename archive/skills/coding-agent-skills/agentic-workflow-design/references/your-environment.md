# Your agent workflow environment (sanitized template)

Fill in the real constraints of the workflow you're building. Keep anything sensitive — API keys,
endpoints, customer data, real case examples — in `your-environment.private.md` (git-ignored).
Commit only sanitized structure here.

- **Task the workflow automates:** <one sentence: input → desired outcome>
- **Agent or script?** <why an agent is needed, or note this could be a deterministic script>
- **Steps / decomposition:** <the subtasks, and the pattern — chain / router / parallel / orchestrator>
- **Tools the agent may call:** <name → purpose → inputs/outputs → side effects → permission level>
- **Read-only vs. destructive tools:** <which tools change state; which require confirmation/dry-run>
- **Verification per step:** <the deterministic checks + where an LLM-judge is used>
- **Guardrails:** <max steps, max tool calls, time/cost budget>
- **Human-in-the-loop gates:** <which decisions or actions require a person to approve>
- **Failure handling:** <retry/backoff, fallback path, escalation>
- **Eval set:** <where your representative test cases with known-good outcomes live>
- **Where it runs:** <local, a job runner, a serverless function, a scheduler>
