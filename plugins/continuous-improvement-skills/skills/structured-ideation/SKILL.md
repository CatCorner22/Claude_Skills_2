---
name: structured-ideation
description: >-
  Runs structured idea-generation sessions that separate divergence from convergence and never
  let the room do both at once: brainwriting (6-3-5 silent rounds) as the default over open
  brainstorming, quantity targets with judgment deferred, SCAMPER prompts and creative
  constraints when the well runs dry, and convergence by explicit criteria (effort/impact
  matrix, weighted scoring) instead of applause volume — with the LLM as anonymity engine,
  fatigue-proof idea partner, and wild-card generator of deliberately distant analogies.
  Grounded in why interacting groups underproduce (production blocking and evaluation
  apprehension — Diehl & Stroebe) and why silent writing fixes it. Use when a person or team
  needs many options for a defined problem, an idea session is stalling or dominated by a few
  voices, or a raw pile of ideas needs honest narrowing. Triggers: brainstorm better,
  brainwriting, SCAMPER, generate options, out of ideas, ideation session, diverge and
  converge, six three five.
---

# Structured ideation (diverge, then converge)

## When to use
- Generating many options for a defined problem: improvement ideas, countermeasures, design
  alternatives, names, approaches — alone, with a team, or human-plus-LLM.
- An idea session keeps landing on the same three ideas, stalls early, or is dominated by the
  loudest or most senior voices.
- A raw pile of ideas already exists and needs narrowing by stated criteria rather than by the
  volume of the room.
- As one stage inside a larger event: a kaizen or co-design event calls this skill for its
  idea-generation segments.
- Not for: planning or running a kaizen event or co-design workshop end to end → see
  `continuous-improvement-skills:kaizen-and-codesign` (ideation is one stage that event can call).
- Not for: generating competing hypotheses to test against a body of evidence → see
  `decision-science-skills:competing-hypotheses-analysis`.
- Not for: imagining the ways a specific plan could fail → see `decision-science-skills:pre-mortem`
  (that is divergence aimed at one question, with its own protocol).
- Not for: inventive-principle problem solving from a technical contradiction — that is TRIZ
  territory, which this library has not built as a skill; treat it as further reading when the
  problem is "improve X without worsening Y" rather than open option generation.

## Do it
The full session plan, brainwriting variants, SCAMPER prompt bank, constraint-injection
patterns, and a worked convergence matrix are in `references/ideation-method.md`.

1. **Frame one question and split the session in two.** Write the prompt as a single "How might
   we…" question — concrete enough to aim at, open enough to allow surprise; not compound, not
   pre-solved. If the framing itself is suspect, run a short question-storming round first
   (divergence that generates questions, not answers) and re-frame. Announce the two phases up
   front: first divergence (generate, judgment deferred), then convergence (judge, by named
   criteria), with a hard boundary between them. The room never does both at once.
2. **Diverge by brainwriting, not open talk.** Default to 6-3-5: six people each write three
   ideas on a sheet in five minutes, silently and simultaneously; sheets rotate; each round you
   read what arrived and build on it or add fresh ideas; six rounds yields up to 108 raw ideas
   in about half an hour. Adjust the numbers to the room — the load-bearing parts are *silent*,
   *simultaneous*, and *building on others' sheets*. Solo and async variants are in the
   reference; the LLM can play the missing seats.
3. **Set a quantity target and defer every judgment.** Name a number ("40 ideas before we
   evaluate anything") and welcome wildness. Osborn's original brainstorming rules — defer
   judgment, go for quantity, welcome wild ideas, build on others — held to their evidence:
   the rules alone don't fix a talking group's underproduction; silence does. Keep the rules
   *and* the silence.
4. **When the well runs dry, inject constraints and SCAMPER.** Fresh prompts restart a stalled
   round: SCAMPER's transformations (substitute, combine, adapt, modify/magnify, put to other
   uses, eliminate, reverse — Eberle's mnemonic) applied to existing ideas; deliberate
   constraints ("zero budget", "must work by Friday", "how would a hospital do this"); and the
   LLM as fatigue-proof partner — the thirtieth idea costs it the same as the third — and as
   wild-card generator of analogies from deliberately distant domains.
5. **Anonymize before anything is evaluated.** Have the LLM collect every idea, deduplicate
   (flagging merges rather than silently deleting), shuffle, and strip authorship, then
   present one flat numbered list. Ideas should meet judgment without status attached — the
   intern's idea and the director's idea arrive identically dressed. Keep the attributed
   original in the log so credit can be given *after* selection: anonymity is for judging,
   not for erasing credit.
6. **Converge by explicit criteria, staged.** Dot-voting is a pre-filter only: use it to cut the
   long list to a shortlist, never to decide. Then place the shortlist on an effort/impact
   matrix, or score it in a weighted criteria matrix whose criteria and weights were named
   *before* scoring began. Applause volume, seniority, and recency are not criteria. The worked
   matrix in the reference shows the mechanics.
7. **Give every surviving idea a disposition.** Each shortlisted idea leaves with an owner and a
   next step (a test, a pilot, a decision date) or goes explicitly to the parking lot. Log the
   full pool, not just the winners — today's discard is often next quarter's answer. Feed
   chosen countermeasures onward — to `continuous-improvement-skills:a3-thinking` for a
   problem-solving cycle, or back to the kaizen event that called this session.

## Why / learn
The counterintuitive finding that anchors this skill: **interacting groups produce fewer ideas
than the same number of people working alone** (nominal groups), and Diehl and Stroebe's
experiments located the causes. First, **production blocking**: in conversation only one person
speaks at a time, so everyone else is holding an idea in memory, rehearsing it, and losing the
next one — ideas die in the wait queue. Second, **evaluation apprehension**: with an audience
that judges, people quietly withhold the wild ideas, and the wild ideas are where the option
space actually widens. Open brainstorming feels energetic precisely while it underdelivers,
which is why "we brainstormed for an hour" so often yields a whiteboard of the obvious.

Brainwriting fixes both causes at once, which is why it is the default and not a variant:
writing is simultaneous, so nobody waits (no blocking), and silent paper mutes the judging
audience (less apprehension) — while the sheet rotation preserves the one genuine benefit of
groups, building on someone else's half-idea. The diverge/converge separation follows from the
same mechanism: judgment kills generation. The fastest way to stop idea flow is to evaluate
idea three in front of the person about to offer idea four; deferred judgment is not politeness,
it is throughput protection. And constraints help rather than hurt because a blank page offers
no traction — "any idea welcome" gives the mind nothing to push against, while "solve it with
zero budget" forces a different region of the option space.

The LLM changes the economics of every piece of this. It is **anonymous** by construction — as
collector and shuffler it makes status-blind evaluation cheap, where anonymity used to cost
index cards and a typist. It is **tireless** — human divergence degrades sharply past the first
dozen ideas, and the LLM's fortieth idea arrives as fresh as its first, exactly when the group
has stopped. And it is **status-blind and distant** — asked for analogies from marine biology or
medieval logistics, it reaches domains no tired room would. Its honest limitation: unprompted,
LLM idea lists regress to the plausible middle. So use it to *extend and anonymize* human
divergence — seeded with constraints, SCAMPER operators, and distant-domain requests — not to
replace the humans who know the problem.

## Common mistakes
- Evaluating during divergence ("that won't work because…") → judgment kills generation; park
  critiques, converge later.
- Open discussion as the default format → production blocking guarantees underproduction; write
  silently and simultaneously, then talk.
- Stopping at the first good idea → the early ideas are the obvious ones; hold the quantity
  target and push into the awkward second half.
- The senior person speaks first, or ideas carry names into evaluation → status ranks ideas
  before criteria can; anonymize the pool first.
- Dot-voting as the final decision → dots measure popularity in the room, not effort or impact;
  use dots to shortlist, criteria to decide.
- Criteria invented after seeing the shortlist → that is choosing the winner and back-fitting
  the rules; name criteria and weights before scoring.
- Diverging on a suspect framing → an hour of ideas aimed at the wrong question; run a
  question-storming round and re-frame first.
- Treating the LLM's list as the ideation → it regresses to the plausible middle unprompted;
  seed it with constraints and distant analogies, and keep human ideas in the pool.
- Ideas leave the room with no owner → the session evaporates; every survivor gets a
  disposition or the parking lot.

## Tailor to your environment
Record your recurring practice in `references/your-environment.md`: the problems you ideate on
repeatedly, your usual group size and format (in-room, remote, async), the convergence criteria
and weights you reuse, and where idea logs and parking lots live. If details are sensitive
(real teams, clients, initiatives), keep them in `your-environment.private.md` — that suffix is
git-ignored. Commit only sanitized, structural examples.

## References
- references/ideation-method.md — the session plan, brainwriting mechanics and variants, the
  SCAMPER prompt bank, constraint-injection patterns, and convergence protocols with a worked
  criteria matrix
- references/your-environment.md — your formats, criteria, and idea-log locations (fill in)
