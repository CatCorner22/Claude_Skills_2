# Feedback method — templates, rewrites, and the receiving field guide

Depth for `collaboration-skills:feedback-that-lands`. All examples are synthetic and
structural; adapt the wording to your own voice.

## Contents
1. [The SBI template](#1-the-sbi-template)
2. [Worked rewrites: character-language → behavior-language](#2-worked-rewrites-character-language--behavior-language)
3. [The COIN variant](#3-the-coin-variant)
4. [The feedforward pattern](#4-the-feedforward-pattern)
5. [Praise with the same machinery](#5-praise-with-the-same-machinery)
6. [The receiving protocol](#6-the-receiving-protocol)
7. [The triggered-reactions field guide](#7-the-triggered-reactions-field-guide)
8. [Auditing written comments for character-language](#8-auditing-written-comments-for-character-language)

## 1. The SBI template

Situation-Behavior-Impact is the Center for Creative Leadership's model. One sentence
per element is usually enough:

```
S — "In <one specific time and place>…"
B — "…<what a camera would have recorded>…"
I — "…and <the effect, stated as my own experience>."
→ (feedforward) "Next time, would you <specific forward request>?"
```

Three tests before delivering:
- **Specificity test (S)**: could the receiver locate the moment? "Lately" and
  "in meetings generally" fail; "in Thursday's standup" passes.
- **Camera test (B)**: would a camera and microphone have recorded it? "You
  interrupted three times" passes; "you were dismissive" fails — dismissiveness is an
  inference, and inferences are exactly what receivers contest.
- **Ownership test (I)**: is the impact reported as *your* experience ("I lost…",
  "I had to…", "I noticed…"), not a claim about their motives or everyone's feelings?

## 2. Worked rewrites: character-language → behavior-language

**Rewrite 1 — the "careless" teammate**
> *Before:* "You're careless with the numbers and honestly it's becoming a pattern."
>
> *After:* "On the month-end summary you sent Friday (S), two of the totals didn't
> tie to the detail tab (B). I found it the morning of the review, so I spent two
> hours re-checking every figure before I could send it up (I). Next time, would you
> run the tie-out check before it comes to me? (feedforward)"

What changed: "careless" (character, contestable) became two specific untied totals
(checkable); "becoming a pattern" (verdict) was dropped for the cleanest recent
example; the impact is the speaker's own two hours, which no one can argue away.

**Rewrite 2 — the interrupter**
> *Before:* "You dominate meetings and you don't respect other people's ideas."
>
> *After:* "In Tuesday's planning call (S), you answered before Priya finished her
> sentence, three times (B). I lost her input on the two items I most needed it for,
> and I noticed she stopped offering (I). Next time, would you let her finish and
> then respond? (feedforward)"

**Rewrite 3 — the code-review comment**
> *Before:* "This is sloppy. Did you even test this? You clearly don't understand
> the auth flow."
>
> *After:* "This branch returns before the session token is invalidated (B — the
> code is the situation), so a logged-out user's token stays live until expiry (I —
> impact on the system stands in for personal impact in written review). Would you
> add a test that asserts invalidation on early return? (feedforward)"

In written review, the observed behavior is *in the diff* — which is exactly why
character inference ("sloppy", "you clearly don't understand") is both unnecessary
and corrosive there. Describe the code and its consequence; leave the author's mind
out of it. (Process questions — who approves, when to rebase — belong to
`coding-agent-skills:git-and-code-review`.)

**Rewrite 4 — praise, upgraded**
> *Before:* "Great job on the incident yesterday."
>
> *After:* "During yesterday's outage (S), you posted a status update every twenty
> minutes without being asked, and each one said what was ruled out, not just what
> was still broken (B). I never had to interrupt the responders for information, and
> I could give leadership real answers (I). That cadence is exactly what I want us
> to standardize."

## 3. The COIN variant

COIN — Context, Observation, Impact, Next steps — is a widely taught SBI variant that
builds the forward move into the acronym, useful when the conversation must end with
an agreement rather than just awareness:

```
C — the context (SBI's Situation)
O — the observation (SBI's Behavior — same camera test)
I — the impact (same ownership test)
N — next steps, agreed aloud: what they'll try, what you'll do, when you'll check in
```

Use SBI when the goal is to surface something; use COIN when the goal is a commitment.
The N step pairs naturally with the owner-and-date discipline in
`collaboration-skills:meeting-design` — a next step with no owner and no date is a
hope, not an agreement.

## 4. The feedforward pattern

Marshall Goldsmith's feedforward: after the observation is on the table, spend the
conversation on the future, not the past.

- Shape: **"Next time, would you <specific, doable behavior>?"** — a request, not an
  order, about a situation that will recur.
- Keep the request as behavioral as the observation: "be more strategic" fails the
  camera test just like "you're not strategic" does. "Bring one slide on the
  downstream cost before we pick a vendor" passes.
- Invite their alternative: "…or is there something that would work better?" The
  receiver often knows a better fix, and a fix they proposed is one they'll do.
- One request. Feedforward degrades into a performance plan when it becomes a list.

Why it works: the past can only be defended or confessed; the future can be
co-designed. Asking for ideas about next time recruits the receiver as a collaborator
and makes clear the goal is change, not concession.

## 5. Praise with the same machinery

Praise is feedback; it steers behavior only when it carries the same specificity as
criticism — the situation, the exact behavior, the evidence, the impact. "Great work"
is pleasant noise; Rewrite 4 above is a repeatable instruction. This is the same rule
`coding-agent-skills:the-foreman` applies to inspection findings: real praise names
what is solid and why, so it can be built on. Two additional calibrations:
- Praise publicly only if the receiver wants that — public praise is a status event,
  and not everyone wants one.
- Don't spend praise as anesthetic before criticism (the sandwich); it teaches people
  that your praise is a warning.

## 6. The receiving protocol

Run this when feedback arrives — solicited or not, skilled or not:

1. **Buy time if triggered.** "Give me a second with that" is a complete sentence.
   You are allowed to hear feedback without ruling on it live.
2. **Name the trigger to yourself** (§7). Naming which reaction is firing is what
   loosens it enough to hear the content.
3. **Separate data from delivery.** Write down, literally or mentally, what was
   *observed* versus how it was *packaged*. Clumsy, harsh, or badly timed delivery is
   information about the giver's skill, not about whether the observation is true.
4. **Ask for the behavior behind the label.** Vague verdicts ("not strategic",
   "abrasive", "not a team player") are compressed data — decompress them: "Can you
   give me a recent specific example — what did I do or not do, and when?" Keep
   asking for instances, not definitions.
5. **Find the grain of truth before ruling on the rest.** Even mostly-wrong feedback
   usually contains one usable observation; extracting it is cheaper than winning.
6. **Close the loop.** Say what you'll try ("I'll send the summary before the call
   for the next two sprints — tell me if it helps"), then actually report back.
   Closing the loop is what converts one conversation into an open channel.

You are not obliged to accept every piece of feedback — but decline *after* steps
3–5, on the data, not at step 1, on the sting.

## 7. The triggered-reactions field guide

Stone & Heen (*Thanks for the Feedback*) name three reactions that block the data
channel. The move is the same for all three: notice it, name it, then return to the
content — but each has its own tell and its own question.

| Trigger | The internal tell | What it does to you | The counter-move |
|---|---|---|---|
| **Truth** — "that's just wrong" | Instant cataloguing of counter-examples | You litigate accuracy before you understand the claim | First understand: "what did you see me do?" Wrong-spotting can wait; difference-spotting can't. |
| **Relationship** — "not from *you*" | The giver's credibility, motives, or own flaws flood in | You switch topics from the feedback to the relationship | Untangle the two topics: judge the data on its content; raise the relationship issue separately if it's real. |
| **Identity** — "then what am I?" | Global self-verdicts ("I'm a fraud", "I'm terrible at this") from one data point | One observation rewrites your whole story | Right-size it: one behavior, one situation — "I did X badly" is survivable in a way "I am X" is not. |

A practical calibration: the stronger the reaction, the more likely a trigger — not
the giver's error — is doing the work. Strong signal to slow down, weak signal that
the feedback is false.

## 8. Auditing written comments for character-language

For a performance note, review comment, or peer-feedback form, scan for these and
rewrite each hit with the §1 template:

- **Totalizers**: always, never, constantly, "a pattern of" → replace with one dated
  instance.
- **Character nouns and adjectives**: careless, lazy, brilliant, sloppy, "not a team
  player", "rockstar" → replace with the behavior that generated the label (praise
  included — "rockstar" teaches as little as "sloppy").
- **Mind-reading**: "doesn't care", "wasn't trying", "clearly didn't read" → replace
  with what was observable; hand the interpretation question back.
- **Crowd-sourcing**: "everyone feels", "the team thinks" → replace with your own
  experience, owned; you can't testify for a crowd.
- **Verdicts without evidence**: "needs improvement in communication" → the specific
  situations and behaviors, or delete the line.

A comment that survives the audit reads like testimony — time, place, observable
event, stated impact — and testimony is what a receiver can actually use.
