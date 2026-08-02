---
name: reflective-learner
description: >-
  Runs structured self-reflection and error-analysis cycles — situation, outcome, strengths,
  weaknesses, root cause, lessons, actionable updates — and integrates user corrections into
  durable working methods, turning experience into explicit, auditable improvement instead of
  leaving learning implicit. Use after a significant task or major response, immediately after
  user feedback or corrections, at natural session breakpoints, or when errors, suboptimal
  outcomes, or high uncertainty are detected. Triggers: reflect, retrospective, lessons learned,
  what went wrong, post-mortem, error analysis, self-review, you got this wrong, that's not what
  I meant, feedback, correction, improve your approach, do better next time.
---

# Reflective learner

## When to use
- After delivering a major response or completing a multi-step task.
- Immediately after explicit or implicit user feedback or corrections.
- When high uncertainty, a suboptimal outcome, or a detected error warrants examination.
- Briefly at session start (recall recent lessons) and fully at session end or on request.
- Not for: analyzing external data or documents → see
  `metacognition-skills:dynamic-analysis-engine`; this skill analyzes *the work itself*.

## Do it
1. **Produce a structured reflection** (concise — in a memory note or artifact, not sprawling
   into the conversation). Cover, in order:
   - **Situation** — what was attempted and why.
   - **Outcome** — what actually happened: results, user reaction, errors, surprises.
   - **Strengths** — what worked well, and the reasons it worked.
   - **Weaknesses / Errors** — specific failures or suboptimal choices, categorized
     (reasoning gap, tool misuse, context loss, assumption error, style mismatch, …).
   - **Root cause** — why the weaknesses occurred (not just what they were).
   - **Lessons learned** — 1–3 concise, generalizable insights.
   - **Actionable updates** — changes to working methods; new facts/preferences/rules for
     semantic memory; proposed updates to skills or project instructions; explicit avoidance
     rules for recurring problems.
2. **Integrate feedback the moment it arrives** (the four-step protocol):
   1. Acknowledge the correction clearly.
   2. Restate the corrected understanding in your own words.
   3. Apply it immediately in subsequent reasoning.
   4. Log the preference/rule into semantic memory (via
      `metacognition-skills:hierarchical-memory-manager`) and confirm the update when appropriate.
3. **Evolve strategy deliberately:** maintain a short "Current Working Methods" section in
   semantic memory or a living document. Prefer simple, high-impact changes; reference past
   lessons so improvement is trackable over time.
4. **Close the loop:** at the next reflection, check whether previous lessons were actually
   applied — a lesson that never changes behavior isn't learned yet.
5. **Compose:** persist lessons through the hierarchical memory manager; hand recurring,
   validated insights to `metacognition-skills:knowledge-crystallizer` for permanent
   integration; seek user sign-off before major strategy shifts.
6. The full reflection template is in `references/reflection-template.md`.

## Why / learn
Learning that stays implicit doesn't compound: an error acknowledged in passing gets repeated,
because nothing durable changed. The structured cycle forces the two moves that make improvement
real. First, **root-cause honesty** — "the forecast was late" is an outcome, not a cause; the
cause might be "assumed last month's file layout without checking," and only the cause-level
statement generalizes to future work. Second, **conversion into artifacts** — a lesson becomes a
rule in memory, an avoidance note, or a method change, which is why the cycle ends in actionable
updates rather than resolutions. The feedback protocol works for the same reason people trust a
colleague who restates a correction: restating proves the correction landed, applying it
immediately proves it took, and logging it makes it permanent. And tracking whether lessons get
applied guards against the failure mode of reflection theater — polished retrospectives that
change nothing.

## Common mistakes
- Generic self-assessment ("could be more thorough") → useless. Name the specific error and its
  category.
- Stopping at the weakness without the root cause → the fix targets a symptom and the error recurs.
- More than ~3 lessons per cycle → nothing sticks. Distill to the few that generalize.
- Acknowledging a correction without restating it → misunderstandings survive the apology.
- Logging lessons but never checking application → reflection theater. Audit at the next cycle.
- Letting reflections bloat the conversation → keep them concise; store detail externally.

## Tailor to your environment
Record in `references/your-environment.md` what *your* feedback loop looks like: how you prefer
corrections acknowledged (brief vs. explicit), which recurring quality bars matter to you (e.g.
"always tie out totals", "cite the Oracle doc"), where lessons should be stored, and any standing
avoidance rules. Keep anything sensitive in `your-environment.private.md` (git-ignored); never
commit real data.

## References
- references/reflection-template.md — the full reflection structure with a worked example
- references/your-environment.md — your feedback preferences and standing rules (add when supplied)
