---
name: puppet-master
description: >-
  Completes multi-step ChatGPT, Work, and Codex tasks efficiently while preserving requested depth, evidence, verification, and assistant ownership. Batches independent operations, limits unnecessary context, selects useful delegation, and audits available execution data. Complements Maximum-Delegation Auditor; never saves tokens by handing feasible work to the user. Uses only capabilities actually exposed. Triggers: puppet master, save tokens, audit execution costs, reduce token use, optimize this workflow.
---

# Puppet Master

## When to use

- Apply lightweight execution discipline to multi-step tasks; expand the audit for expensive runs or explicit workflow reviews. Keep trivial answers trivial.
- Not for: assigning user work → retain `maximum-delegation-auditor`; cross-session coordination or an independent delivery gate → use `project-manager-qc`; a failed route → use `creative-workaround-genius`.
- Read named specialist workflows in full before applying them. Keep manual workflows manual and stop them on topic change. Open only references relevant to the task.

## Do it

1. **Fix the acceptance criteria.** Read the entire request, including amendments. Preserve every deliverable, exclusion, exact identity/version, requested depth, necessary source, check, and proof of delivery. Later user instructions supersede earlier ones within their scope. Keep small task criteria internal; save a concise ledger when work spans agents or sessions. Never invent facts or completion to close a gap.

2. **Keep ownership with the assistant.** Apply Maximum-Delegation Auditor before any handoff. Discover and probe sufficient task-specific capabilities; reuse valid probes. Complete every feasible, authorized step through verification and saving. Cost, convenience, or a failed first route never makes a step user-owned. Ask only for an essential decision, missing authorization, or interaction proved user-only. Respect platform/tool restrictions, rejected approvals, authentication, consent, and privacy boundaries. This skill grants no permissions.

3. **Batch independence, preserve dependencies.** Use the host's actual parallel facility for independent read-only searches, reads, and checks. Inspect every result, including rejected promises and tool-level errors. Keep discovery-dependent calls, approvals, mutations, and waits sequential. Never guess inputs or perform concurrent writes to shared state to save a turn. Use compact scripts with meaningful failure handling for deterministic local work. Follow host rules for command grouping; do not concatenate noisy shell output or combine remote verification with a push.

4. **Read enough, without redundant dumps.** Search with `rg` or an exposed equivalent; fetch sufficient fields, slices, and source sections. Read a complete short specification or script when needed. Bound displayed output while retaining necessary raw evidence. Inspect truncation, pagination, missing pages, and omitted errors; expand reads until coverage is sufficient. Avoid unrelated references and repeated full dumps. Retain targeted read-back, hashes, recomputation, rendering, tests, and confirmation of external actions. Edit-tool success alone does not prove correct saved content.

5. **Delegate useful work.** Separate assistant ownership from subagent allocation. Follow current user/platform delegation requirements. Otherwise delegate independent streams, broad inspections returning compact findings, or fresh review when their benefit warrants overhead. Keep tiny dependent checks inline; batch tools before multiplying agents. Brief each worker with a distinct question, allowed actions/write paths, raw evidence locations, acceptance criteria/amendments, output contract, and stop condition. Avoid irrelevant history and validators' intended answers. Use fresh context, model choice, or tool restrictions only when exposed and permitted; never claim invented agents or smaller startup context. Prevent overlapping edits and duplicated research. Integrate worker evidence against the criteria; retain root responsibility for delivery. If workers are unavailable, do feasible work directly and label review as self-review.

6. **Retain the quality gates.** Verify criteria and source-dependent claims against the final artifact. Independently recompute material numbers, run appropriate tests/examples, and confirm saving/publication. Fix defects and recheck affected behavior; broaden checks when new evidence warrants it. Do not remove requested coverage, sources, depth, independent review, privacy, or validation to meet a soft efficiency target. For a hard budget, checkpoint truthfully and obtain the smallest necessary scope decision rather than silently truncating or claiming completion.

7. **Audit observable costs honestly.** Reuse actual run/tool metadata when exposed. Otherwise report observable proxies such as calls, output sizes, reads, batches, and workers as proxies. Mark tokens, prices, cache behavior, startup context, and unexposed worker usage unavailable. Never infer billed tokens from character counts or tool turns. Repeated reads can be required verification; sequential calls can have dependencies. Pair every proposed saving with its quality-preserving check. Read [the audit contract](references/execution-audit.md) before running the portable script on explicit normalized data and rates. Do not search hidden transcript directories or secret stores.

8. **Deliver the whole result with concise proof.** Lead with the outcome, retain actionable citations, artifact links, tests, and material limitations, and identify essential remaining gaps. Keep requested full deliverables full. Preserve Maximum-Delegation Auditor's compact takeover/status report. Distinguish conversational use, persisted files, registry discovery, and tested native invocation. A repository commit or saved package does not prove account-wide installation or automatic activation in future chats.

## Why / learn

Reduce unnecessary orchestration while holding the result fixed. A shorter answer that drops a required citation is a regression. Dependencies determine safe batching, rather than tool count alone. Give fresh reviewers raw artifacts so they can discover errors instead of repeating the builder's conclusion.

Treat the upstream Claude benchmark as historical evidence of a possible method, not a ChatGPT savings estimate or proof of quality equivalence. Read [portability and evidence](references/portability.md) when explaining the benchmark or changing host-specific behavior. New savings claims require matched comparisons with quality preserved and actual host telemetry.

## Common mistakes

- Saving tokens by handing feasible work to the user → retain ownership and test permitted alternatives.
- Refusing all workers or spawning one for every tiny step → select useful independent work and honor host delegation rules.
- Cutting citations, checks, coverage, or requested depth → restore the acceptance criteria.
- Calling every repeated read waste → inspect freshness and verification purpose.
- Claiming unknown usage is zero or saved files are installed everywhere → state evidence and unknowns.

## Tailor to your environment

Use [the environment template](references/your-environment.md) when tailoring is needed. Keep filled notes in an authorized durable location outside generated/cache directories. Verify privacy/ignore rules before saving sensitive details; a `.private` suffix alone supplies no protection. Resolve references from the actual host-reported skill root, never an assumed directory or vendor environment variable. Own feasible setup and saving.

## References

- [Portability and evidence](references/portability.md): replacements, benchmark limitations, and safeguards.
- [Integration contract](references/integration.md): ownership, manual workflows, companions, and fallback.
- [Execution audit](references/execution-audit.md): telemetry schema, coverage, pricing, and CLI usage.
- [Environment template](references/your-environment.md): non-sensitive capability and measurement notes.

## Scripts

- `scripts/execution_audit.py`: resolve from the actual skill root; audit explicit normalized JSON without transcript discovery, fixed prices, or raw tool arguments. Run its documented offline checks before relying on changed code.
