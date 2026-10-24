# Portability and evidence

Adaptation version: 1.0.0-chatgpt.1. Source: CatCorner22/Claude_Skills_2 PR #65,
merge commit `44a01bceb2083f174a07d652a1d078abca19617c` (2026-10-21).
The MIT notice is retained with this adaptation. The upstream versions are
puppet-master 1.0.0, project-manager-qc 2.1.0, and creative-workaround-genius 2.0.0.

## Replacement map

| Upstream feature | ChatGPT / Work replacement |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}` and installed-cache assumptions | Resolve the actual skill root from host metadata; read relative resources through that provider or use the returned local path. |
| `~/.claude/projects/` transcript discovery and Claude JSONL fields | Use supported, authorized exports or explicit normalized call metadata; no hidden-log probing. |
| Claude `Read`, `Bash`, `Agent`, `Task` names | Discover the exposed read, execution, connector, and collaboration interfaces and use their actual schemas. |
| Fixed cache/input/output price weights | Explicit dated per-model rates only; otherwise no monetary total. |
| Whole-context replay, 50k worker startup, cache-write premiums | Historical Claude assumptions; do not assert them for ChatGPT. Measure only exposed usage. |
| Restricted custom agent type and smallest-model selection | Use exposed collaboration controls when allowed. A prompt asking for fewer tools does not prove fewer tool definitions or lower startup cost. |
| PLAN/CHECKPOINT/QC project-manager agent definition | Actual available worker with a scoped brief; otherwise a labeled self-review. |
| Never reread an edited file | Avoid redundant full dumps; retain targeted read-back and required verification. |
| Chain dependent commands to reduce turns | Follow host command rules; keep approvals, mutations, and remote verification/push boundaries sequential. |
| `.claude/skills-env` private notes and plugin-update commands | Supported durable storage outside caches; verify ignore/privacy rules. Do not assume a private suffix is excluded. |
| Claude plugin registration and slash commands | Conversational invocation plus persisted native skill package where supported; verify registration and invocation separately. |

## Preserved safeguards

Freeze requirements, source coverage, checks, and requested depth before optimizing.
Batch only known independent calls; inspect all results. Keep exact source/version
identity, evidence, permissions, privacy, and quality gates. Complete all feasible
assistant work. Classify technical obstacles separately from controls. Verify
delivery, do not transfer achievable checks to the user, and never hide work or
invent missing facts. Review worker evidence against the whole request.

## What the benchmark establishes

The opened PR reports 17 matched runs **per arm**, not necessarily 17 distinct
tasks. Approximate mean price-weighted use was 102k without and 80k with the skill:
an absolute reduction of approximately 22k input-token equivalents per run, or
21.6% using those rounded means; upstream reports 21%. This is not a reduction in
ordinary billed ChatGPT tokens or subscription cost.

Scripted checks were 62/62 in both arms. Initial blind grading was 66/68 without
the skill and 65/68 with it: one additional missed criterion in the skill arm,
about 1.47 percentage points lower (97.06% versus 95.59%) across graded criteria.
Those criteria are not independent task-success observations. A lost citation
prompted a safeguard amendment and two reportedly passing reruns. Those reruns
do not erase the initial regression or establish equivalence across tasks.

The eval prose calls the workload eleven sandboxed tasks but enumerates categories
that sum to twelve; the aggregate does not resolve that discrepancy. The two-run
audit-task comparison is separate from the main 17-run comparison. These are
upstream reports, not a reproduced benchmark. A single model/environment, small
sample, rounded means, unavailable raw per-run variance, and an amended instruction
limit inference. Median, mode, spread, confidence intervals, and a general causal
ChatGPT savings estimate cannot be recovered from these aggregates. Do not invent
them or treat equal scripted scores as proven noninferiority.

Sources:
- https://github.com/CatCorner22/Claude_Skills_2/pull/65
- https://github.com/CatCorner22/Claude_Skills_2/blob/44a01bceb2083f174a07d652a1d078abca19617c/evals/coding-agent-skills/puppet-master.md
- https://learn.chatgpt.com/docs/build-skills
- https://developers.openai.com/plugins/concepts/skills

## New evaluation standard

Freeze task prompts, acceptance checks, exclusion rules, and cost basis before
running matched with/without comparisons. Use fresh contexts and raw artifacts;
hold out cases and disclose every amendment. Preserve all failures and include
parent plus worker usage, cache basis, model/rate date, and missing coverage.
Compare actual costs only when telemetry exists. Otherwise report functional
results and resource proxies without claiming token savings or quality equivalence.
