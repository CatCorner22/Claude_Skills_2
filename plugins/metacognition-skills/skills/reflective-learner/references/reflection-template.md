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
A lesson repeatedly "not applied" is a candidate for a stronger mechanism — a standing rule in
project instructions or a skill update — via `knowledge-crystallizer`.
