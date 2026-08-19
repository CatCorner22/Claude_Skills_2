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
metadata:
  version: "1.1.1"
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
The full reflection template, the weakness categories, and a worked example are in
`references/reflection-template.md`. The correction pathway — triage, contradiction diagnosis,
restatement wording, the record's seven fields, and a six-correction worked session — is in
`references/correction-protocol.md`; read it before handling a correction, which is most of
what this skill is invoked for.

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
2. **Integrate feedback the moment it arrives** — acknowledge, restate, apply, then decide
   whether anything durable is stored at all:
   1. **Acknowledge** in a clause, not a paragraph, and not as the opening move.
   2. **Restate so the restatement is refusable.** The rule at cause level in *your* words (echoing
      theirs proves receipt, not comprehension); the scope boundary you inferred, including where
      you are *not* applying it; the specific pending or delivered output it changes; and the check
      or default you are changing. Two to four sentences. If the user cannot answer "no" to any
      clause, you have told them nothing.
   3. **Apply immediately and visibly** — re-issue the affected part rather than promising to.
   4. **Triage before storing.** Store only what recurs. If the right answer was derivable from the
      materials, store the missing *check*, not the fact; if it was unguessable, store the
      preference. Explicit corrections are stored on the first occurrence, silently inferred ones on
      the second — a missed preference costs one more correction, a wrongly stored one is applied
      invisibly forever. If the user asserts something you verified otherwise, store what they
      *want*; never upgrade it to a stored fact.
   5. **Test for contradiction before writing.** If one concrete next action can satisfy both the
      stored entry and the new instruction, there is no contradiction — the old entry was
      under-qualified, and qualifying it beats flipping it. Genuine conflicts go to the user with
      both entries' provenance, recorded through
      `metacognition-skills:hierarchical-memory-manager`, which owns the annotation form.
3. **Evolve strategy deliberately:** maintain a short "Current Working Methods" section in
   semantic memory or a living document. Prefer simple, high-impact changes; reference past
   lessons so improvement is trackable over time.
4. **Close the loop:** at the next reflection, check whether previous lessons were actually
   applied — a lesson that never changes behavior isn't learned yet. A correction that arrives
   *again* after its rule was stored is the one hard signal the loop is broken, and it indicts the
   storage **site**, not the discipline: move the rule to where the work happens — a template
   default, a checklist line open while drafting, then an automated check — rather than restating
   it louder. If reading it had been enough, it would have worked the first time.
5. **Compose:** persist lessons through the hierarchical memory manager; hand recurring,
   validated insights to `metacognition-skills:knowledge-crystallizer` for permanent
   integration; seek user sign-off before major strategy shifts.

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
- Promoting a firmly-stated user assertion to a stored `FACT:` → a wrong fact is applied silently
  and confidently forever. Store the preference; leave your evidence in Open Questions.
- Storing an inferred preference on one sighting → applied everywhere, invisibly, and the user has
  to diagnose it. Wait for the second sighting; explicit corrections need only the first.
- Flipping a stored entry that a new instruction merely narrows → you delete a true statement and
  start an oscillation. Test whether one action satisfies both, then qualify instead.
- Extracting a lesson when the real cause was an ambiguous request → the "lesson" is a guess, and
  storing it trains more confident guessing. Store the ambiguity class and ask the question.

## Tailor to your environment
Wire in your current role here — the cycle is role-portable. Record in
`references/your-environment.md` what *your* feedback loop looks like: how you prefer corrections
acknowledged (brief vs. explicit), which recurring quality bars matter to you (an analyst's "tie
out every total", an attorney's "cite the controlling authority", a developer's "tests green
before done"), where lessons should be stored, and any standing avoidance rules. Keep anything
sensitive in `your-environment.private.md` (git-ignored); never commit real data.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/reflective-learner.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/reflection-template.md — the full reflection structure, weakness categories, a worked
  example, and the application audit with its worked tally
- references/correction-protocol.md — the correction pathway: triage rules, contradiction
  diagnosis, restatement wording, the seven-field record, the enforcement ladder, failure
  envelope, and a six-correction worked session
- references/your-environment.md — your feedback preferences and standing rules (add when supplied)
