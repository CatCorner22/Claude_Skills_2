---
name: dynamic-analysis-engine
description: >-
  Performs adaptive, iterative, hypothesis-driven analysis of data (tabular, numerical, logs,
  datasets) or text (documents, narratives, arguments, codebases) — orienting on the material,
  decomposing into prioritized sub-questions, mixing quantitative and qualitative methods,
  testing explicit hypotheses with code, controlling its own depth, and synthesizing findings
  with calibrated confidence and stated limitations. Use for any non-trivial analysis where the
  path is not obvious upfront and depth, methods, or framing should adapt to what emerges.
  Triggers: analyze this, deep analysis, investigate, dig into this data, what is driving,
  explore this dataset, form a hypothesis, root cause the numbers, multi-angle analysis,
  iterative analysis, adaptive analysis, why did this change.
---

# Dynamic analysis engine

## When to use
- Analyzing a dataset, log, document set, or codebase where the right approach isn't obvious
  upfront and should adapt as findings emerge.
- Questions that need hypothesis testing, multi-perspective reasoning, or tool-assisted iteration
  ("what's driving X?", "is this pattern real?").
- Not for: a first-pass profile of a fresh dataset → see
  `data-analytics-bi-skills:exploratory-data-analysis`; a single formal significance test →
  see `data-analytics-bi-skills:statistical-inference`. This skill *orchestrates* those moves
  inside a larger adaptive loop.

## Do it
1. **Orient & characterize.** Assess the material's type, size, quality, domain, structure, the
   goal, constraints, and uncertainty. State assumptions and missing information explicitly
   before analyzing anything.
2. **Decompose adaptively.** Break the goal into sub-questions and prioritize by information
   value — answer first what would most change the conclusion. Re-decompose as findings emerge.
3. **Select & combine methods dynamically**, switching as the data demands:
   - *Quantitative*: descriptive stats, distributions, correlations, hypothesis tests, simple
     models — prefer executed code (pandas/scipy) over mental arithmetic.
   - *Qualitative/textual*: thematic analysis, claim-evidence mapping, discourse structure,
     stakeholder perspectives, contradiction detection.
   - *Multi-lens*: causal, comparative, adversarial, historical, systems views; triangulate
     quantitative against qualitative. Escalate or simplify based on what emerges.
4. **Hypothesize → test → update.** Make candidate explanations explicit; design a check for
   each (a query, a computation, a document pass); update beliefs on the evidence. Prune weak
   branches, deepen promising ones.
5. **Iterate with depth control.** Start high-level when uncertainty is high; drill down only
   where the value is clear. Say explicitly when more data, a different method, or an external
   tool is needed. Avoid both superficiality and rabbit holes.
6. **Synthesize honestly.** Report structured findings with alternative interpretations,
   calibrated confidence, limitations, and actionable insight. Prefer living outputs —
   tables, charts, executable notebooks, annotated documents — over static prose.
7. **Meta-monitor throughout:** track remaining uncertainty and whether the current approach is
   still working; flag when it isn't. Persist durable findings via
   `metacognition-skills:hierarchical-memory-manager`, and after a major analysis, evaluate the
   *process* with `metacognition-skills:reflective-learner`.
8. The method menu and a hypothesis-log template are in `references/methods-and-hypotheses.md`.

## Why / learn
One-shot analysis fails on non-trivial questions because the right method depends on facts you
don't have until you start looking — the shape of the data, where the variance hides, which
early hunch dies first. The engine's core discipline is making that adaptation *explicit*:
hypotheses are written down before testing, so confirmation bias has less room; sub-questions are
prioritized by information value, so effort lands where a finding would actually change the
conclusion; and depth is a controlled variable, not an accident of enthusiasm. Explicit
hypothesis logs also make the analysis auditable — a reader can see what was considered, what was
ruled out, and on what evidence, which is the difference between an argument and a vibe.
Calibrated confidence closes the loop: an analysis that reports "likely, because X and Y, unless
Z" survives contact with reality far better than one that reports a single confident number.

## Common mistakes
- Jumping to a method before characterizing the material → the method dictates the findings.
- Testing only the favored hypothesis → write down rivals and try to kill the favorite.
- Uniform depth everywhere → shallow where it matters, deep where it doesn't. Prioritize by
  information value.
- Mental arithmetic on real data → run code; small silent errors compound.
- A single confident conclusion with no alternatives or limitations → overclaiming. Calibrate.
- Endless exploration with no synthesis → set a checkpoint: "what would change my answer?"

## Tailor to your environment
Record in `references/your-environment.md` the data sources and formats you analyze most (e.g.
Oracle BSL exports, OTBI extracts, bank fee statements), your preferred tools and output forms,
and standing analytical conventions (fiscal calendar, currency handling, materiality thresholds).
Keep anything sensitive in `your-environment.private.md` (git-ignored); never commit real data.

## References
- references/methods-and-hypotheses.md — the method menu, depth-control heuristics, and a hypothesis-log template
- references/your-environment.md — your data sources, tools, and conventions (add when supplied)
