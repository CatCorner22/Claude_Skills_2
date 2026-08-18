# Reflection template (with worked example)

## Contents
- The template
- Weakness categories
- Worked example
- Application audit

## The template
```markdown
## Reflection — <task> (<date/turn>)
**Situation:** <what was attempted and why>
**Outcome:** <what actually happened — results, user reaction, errors, surprises>
**Strengths:** <what worked well + why it worked>
**Weaknesses / Errors:** <specific failures, each categorized>
**Root cause:** <why the weaknesses occurred>
**Lessons learned:** <1–3 concise, generalizable insights>
**Actionable updates:**
- Method change: <what to do differently>
- Memory update: <fact/preference/rule to store>
- Avoidance rule: <explicit "don't do X when Y">
- Proposed skill/instruction update: <if warranted — needs user sign-off>
```

## Weakness categories
Categorizing makes patterns visible across reflections:
- **Reasoning gap** — a step was skipped or an inference unjustified.
- **Tool misuse** — wrong tool, wrong parameters, or missed verification.
- **Context loss** — earlier information was forgotten or contradicted.
- **Assumption error** — acted on an unverified assumption.
- **Style mismatch** — output didn't fit the user's format/tone/depth preference.
- **Scope error** — did more or less than asked.

## Worked example
```markdown
## Reflection — 13-week cash forecast build (2026-07-17)
**Situation:** Built a rolling forecast from AR/AP aging exports on request.
**Outcome:** Numbers correct, but user had to ask twice for weekly (not monthly) buckets.
**Strengths:** Variance columns anticipated the follow-up; tie-out totals matched.
**Weaknesses / Errors:** Style mismatch — defaulted to monthly granularity despite
"13-week" in the request naming the granularity implicitly.
**Root cause:** Pattern-matched to the more common monthly template instead of parsing
the horizon the user actually named.
**Lessons learned:** The horizon named in a forecasting request usually implies its bucket size.
**Actionable updates:**
- Memory update: user's forecasts are weekly-bucketed unless stated otherwise.
- Avoidance rule: never default granularity when the request names a horizon.
```

## Application audit
At each new reflection, scan the last few for their Actionable updates and mark each:
- **Applied** (behavior visibly changed) · **Partially applied** · **Not applied** (why?)

Marking honestly requires the counterfactual — what you would have done without the update. Without
it, "applied" cannot be distinguished from "never came up", and every audit comes back clean. That
is why the correction record carries the field (see `correction-protocol.md`).

### What the tally actually tells you
A worked audit over five cycles: **14** actionable updates recorded — **9** applied, **3** partially
applied, **2** not applied. The three states account for the whole cycle: 9 + 3 + 2 = 14. The
applied count is the least informative number in the set; read the other two first.

- **Partially applied** usually means the update was two updates wearing one sentence. Split it and
  re-audit; the half that keeps failing is the real one.
- **Not applied** is diagnostic only when you distinguish *never fired* from *fired and lost*. An
  update whose trigger situation never arose is not a failure and should not be counted as one — it
  is evidence the update was written too narrowly to be worth its scan cost.
- **Repeats** are the number that matters: updates in this cycle restating something already
  recorded in an earlier one. Of the 14 above, 2 were repeats. A repeat is not a discipline problem;
  it is evidence the storage *site* was never read at the moment of action, and the fix is to move
  the rule, not to write it again (the enforcement ladder in `correction-protocol.md`).

A working trigger: when repeats exceed roughly one in five of a cycle's updates, stop adding entries
and spend the cycle relocating the ones you already have, because past that ratio the store is
growing faster than the behavior. For this cycle the line sits just under three updates: 14 / 5 = 2.8.
Two repeats is below it — each still gets a site fix, but the cycle is not yet dominated by them. The exact fraction has no measured basis; pick one, write it down, and hold it, so
the trigger is a threshold rather than a mood.

A lesson repeatedly "not applied" after relocation is a candidate for a stronger mechanism — a
standing rule in project instructions, an automated check, or a skill update — via
`knowledge-crystallizer`.
