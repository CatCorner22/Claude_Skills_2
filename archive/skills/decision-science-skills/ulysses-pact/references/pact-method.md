# The pact method

Contents:
1. [The degradation-scenario interview](#1-the-degradation-scenario-interview)
2. [The pact template](#2-the-pact-template)
3. [Enforcement etiquette — quote, never scold](#3-enforcement-etiquette--quote-never-scold)
4. [The renegotiation protocol](#4-the-renegotiation-protocol)
5. [Failure-mode table](#5-failure-mode-table)

Provenance: the instrument channels psychiatric advance directives as Ulysses
contracts [peer-reviewed, PubMed/PMC-sourced] and behavioral-economics commitment
devices. The templates and etiquette below are the house implementation of those
mechanisms, not claims from the sources.

## 1. The degradation-scenario interview

Run only in a calm state — the interview's product is a map of where the *future* self
goes bad, drawn by the self that can still see clearly. Questions, in order:

1. **The record.** "When did you last do something under pressure that your calm self
   had already ruled out? Walk me through the last three." Patterns, not incidents —
   a pact against a one-off binds nothing.
2. **The pressure inventory.** For each pattern, name the pressure class: deadline
   squeeze, sunk-cost fog ("we've spent too much to stop"), panic (market, outage,
   social), the late-night incident, the anger window after a provocation, fatigue at
   the end of a long push, an authority figure asking directly.
3. **The tell.** "What is the observable early sign that you are entering this state?"
   The tell must be visible from outside the feeling — a clock time, a phrase you catch
   yourself saying, a physical act (opening the admin console, drafting the reply).
   Pacts trigger on tells, not on self-diagnosed states; the degraded self is the worst
   judge of whether it is degraded.
4. **The typical bad move.** One sentence, concrete: "I force-push to make the branch
   look clean," "I widen the scope to justify what we already spent," "I send the reply
   the same hour."
5. **The bill.** What did it cost last time, in kind — rework, trust, money, sleep?
   The bill becomes the raw material for the "why" paragraph, which is the enforcement
   payload later.

Output: a shortlist of degradation situations with tell → bad move → bill. Each line
that shows a repeat pattern is a pact candidate. Draft at most a few — see failure
mode "pacts multiplying."

## 2. The pact template

One pact per rule. Every field filled at adoption, in the author's own words.

| Field | What it is | Test of a good entry |
|---|---|---|
| Rule | One sentence, testable, barring a specific act | A third party could say yes/no whether it was broken |
| Trigger context | The narrow situation where the rule applies (the tell) | Fires rarely — only inside the degradation window |
| Second signature | Who must co-sign an exception | Someone reachable in the window who has actually refused you before |
| Cooling-off | Mandatory delay between wanting the barred act and doing it | Long enough to outlast the degradation peak (overnight beats an hour for anger; an hour beats zero for deploys) |
| Pre-committed default | What happens if no decision is made in time | Safe and specific — "the deploy waits for morning," not "we'll see" |
| Unbinding criteria | Evidence that legitimately releases the pact entirely | Named in advance, about the world changing — not about the pressure being strong |
| Review date | When the pact is deliberately kept, resized, or retired | On the calendar, in calm season |
| Registration | Where the future self will physically hit the pact | In the path of the act itself |
| Adopted + why | Date, plus a short paragraph in the calm self's voice explaining the bill this pact prevents | Reads as a letter to the future self, not a policy memo |

**Filled example.**

- **Rule:** No force-push to any shared branch between 00:00 and 08:00.
- **Trigger context:** Late-night incident work on shared branches; the tell is
  reaching for `--force` after midnight to "clean up."
- **Second signature:** An exception requires an explicit OK from the other person on
  the rotation, awake and named in the message — not a Slack emoji.
- **Cooling-off:** If the urge is cosmetic (history cleanup), it waits for 09:00 by
  default — that is the pre-committed default, not a decision to be made at 2am.
- **Unbinding criteria:** This pact releases if the branch protection rules change to
  make force-push technically impossible (the pact is then redundant), or if the
  rotation moves to a follow-the-sun model where midnight is someone's midday.
- **Review date:** First calm week of each quarter.
- **Registration:** A comment in the repo's contributing doc at the push instructions,
  a line in the incident runbook, and the assistant's pacts file with enforcement on.
- **Adopted + why (the calm self's voice):** "Adopted <date>. Twice now a 2am force-push
  has cost us a morning of recovering someone else's commits — both times I was sure I
  understood the branch state, and both times I was wrong in a way morning-me spotted in
  minutes. Midnight-me does not get to be sure about branch state. It can wait six
  hours; the mess it makes cannot be waited out."

## 3. Enforcement etiquette — quote, never scold

The assistant's enforcement move is a quotation, not a judgment. The full script:

1. **Produce the pact verbatim.** "You adopted a rule against exactly this on <date>.
   Here is what you wrote:" — then the rule and the why paragraph, unedited. The calm
   self's own words are the payload; paraphrase weakens them.
2. **Name the machinery, neutrally.** "The pact's exception path is: <second signature>
   after <cooling-off>. Its pre-committed default is: <default>." No editorializing on
   whether an exception is wise.
3. **Stop.** No lecture, no disappointment, no "are you sure?" loops. The assistant
   delivered the letter; the argument is between the two selves.
4. **Distinguish override from unbinding.** An *override* goes through the pact's own
   exception machinery (signature + cooling-off) and leaves the pact standing. An
   *unbinding* claim ("the pact no longer applies") is checked against the written
   unbinding criteria — if the evidence named at adoption is genuinely present, the
   pact releases; if the claim is really "the pressure is very strong tonight," that is
   the situation the pact was written for, and the assistant says so once, by pointing
   at the trigger-context field.
5. **Log the encounter.** Every enforcement moment — held, overridden, or released — is
   logged with a line for the review date. Near-misses are the best renegotiation data
   there is.

Why quotation works and scolding fails: an enforcer the pressured self resents is an
enforcer the pressured self routes around — next time it will not ask. A letter from
the calm self keeps the authority where it belongs, with the pact's own author.

## 4. The renegotiation protocol

- **On schedule, in calm state.** Renegotiation happens at the review date, or ad hoc
  only when the initiator is demonstrably outside the trigger context (not mid-incident,
  not mid-deadline, not angry).
- **Refuse renegotiation under fire — by construction.** A request to renegotiate from
  inside the degradation window is itself evidence the pact is working. The assistant's
  response is the enforcement script plus: "renegotiation is on the calendar for
  <review date>; tonight's objection is logged for it."
- **The three outcomes.** Keep (the pact earned its place — the log shows real
  near-misses), resize (trigger context too broad or too narrow; cooling-off wrong
  length; signer unreachable — amend the fields, restate the why), or retire (the
  degradation pattern is gone, the world changed per the unbinding criteria, or the
  pact never fired and binds nothing). Retirement is deliberate and recorded — a pact
  that silently lapses teaches the future self that pacts lapse.
- **Amendments cool off too.** A resized rule takes effect after its own cooling-off
  period, so a renegotiation cannot be a slow-motion override: loosening a pact today
  because next week looks hard is the same move the pact bars, in better clothes.
- **Consolidate.** At each review, merge overlapping pacts and cut the herd. A few
  pacts with real teeth bind more than a policy manual nobody remembers.

## 5. Failure-mode table

| Failure mode | How it presents | The fix |
|---|---|---|
| Pact too broad | Fires in ordinary work, gets waved through daily, becomes wallpaper | Narrow the trigger context to the actual degradation window; the rule should feel almost never applicable |
| No unbinding clause | First legitimate exception becomes the precedent that dissolves the pact | Pre-decide release evidence at adoption; retrofit criteria at the next review for any pact missing them |
| Registered nowhere | The future self learns the pact existed only at the retrospective | Register in the path of the act (template, runbook, checklist, assistant's pacts file) |
| Written under fire | Rule drafted mid-crisis binds the wrong self, overcorrects, dies at first calm read | Log the impulse during the crisis; draft the pact at the review that follows |
| Rubber-stamp signer | Exceptions always granted; the mast is a handrail | Choose a signer with a documented record of telling you no |
| Scolding enforcer | The pressured self stops consulting the pact at all | Quotation etiquette only; the calm self's why paragraph does the persuading |
| Mid-crisis renegotiation | "This rule doesn't fit tonight's situation" every time the rule bites | Refuse by construction; objection logged for the review date |
| Pact sprawl | Dozens of rules, none remembered, none binding | Consolidate at review; keep the few with near-miss logs, retire the rest |
