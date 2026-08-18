# Meeting method — templates and protocols

Depth for `collaboration-skills:meeting-design`. Everything here is structural; adapt
names and cadences to your environment.

## Contents
1. [The should-this-meeting-exist test](#1-the-should-this-meeting-exist-test)
2. [The decision-list agenda template](#2-the-decision-list-agenda-template)
3. [The four decision rules](#3-the-four-decision-rules)
4. [Pre-reads and the silent start](#4-pre-reads-and-the-silent-start)
5. [Running the room](#5-running-the-room)
6. [The decision-log format](#6-the-decision-log-format)
7. [The recurring-meeting audit protocol](#7-the-recurring-meeting-audit-protocol)

## 1. The should-this-meeting-exist test

Ask, in order:

1. **What decision or commitment will exist after this meeting that does not exist
   now?** If the honest answer is "none — people will be informed," it is an async
   post. Write it.
2. **Does the decision need synchronous judgment?** A decision one owner can make from
   written input is an async decision: post the context, name the deadline for
   objections, decide. Reserve the room for decisions that need live back-and-forth —
   real trade-offs between people who each hold part of the picture.
3. **Is this the smallest group that can decide?** Every attendee beyond the deciders,
   the consulted, and the owner of an agenda item is an audience member; audiences
   read the decision log instead.

Outcomes: **meeting** (decision needs live judgment), **async decision** (owner decides
from written input by a stated time), **async post** (information only), or **nothing**.

A useful phrasing when declining: "I think this is an email — here's a draft." Doing
the async work on the spot is what makes the decline land as help, not obstruction.

## 2. The decision-list agenda template

```
MEETING: <name>                     DATE: <date>    LENGTH: <total>
PURPOSE: <the one-line reason this is synchronous>
PRE-READ: <link> — sent <when>; 10 min silent reading at the start

1. DECIDE: <decision question, phrased so it can be answered>   [15 min]
   Rule: consult-then-decide — <name> decides
   Options on the table: <A / B / C — from the pre-read>

2. DECIDE: <decision question>                                  [10 min]
   Rule: consent — proceed unless a principled objection stands
   Owner: <name>

3. COMMIT: <who will do what by when — confirm live>            [5 min]

CLOSE: read-back — decisions, actions (owner + date), parked items  [5 min]
```

Conventions that keep it honest:
- Every numbered item starts with a verb of closure: DECIDE, COMMIT, RESOLVE. If an
  item cannot be phrased that way, it is status — move it to the pre-read or the async
  channel.
- Timeboxes total less than the slot, **and the silent-reading block counts toward the
  total** — it is meeting time. The template above spends 10 (reading) + 15 + 10 + 5 +
  5 (close) = 45 of a 60-minute slot; the close is a protected line item, never a
  leftover.
- The decision rule and its holder appear on the agenda itself, so nobody discovers
  them mid-discussion.

### Red-checking an existing agenda
Go item by item and ask: *what question does this item answer, and who decides?* Items
with no answerable question become pre-read content or get cut. Items with a question
but no named rule get one. A typical topic-agenda compresses by half; that is the
finding, not a problem.

## 3. The four decision rules

| Rule | How it closes | Use when | Failure mode if unnamed |
|---|---|---|---|
| **Single owner** | The owner decides; the room may not even meet | Reversible calls inside one person's remit | The room relitigates what was never theirs |
| **Consent** | Proceed unless someone states a principled objection (not a preference) | Low-risk changes where speed beats polish | Preferences masquerade as vetoes |
| **Consult-then-decide** | The owner hears the room, then calls it — in the meeting, out loud | Most real decisions: one accountable owner, several informed voices | Fake consensus: discussion runs until fatigue looks like agreement |
| **Vote** | Majority (or a stated threshold) binds | Genuine peer decisions with no natural owner | Politicking replaces argument if used where an owner exists |

Two disciplines make any rule work: name it (and its holder) **before discussion
opens**, and record it in the decision log next to the decision — a decision whose rule
is on record is much harder to quietly reopen.

## 4. Pre-reads and the silent start

The mechanics, as Amazon documented the practice — meetings open with attendees
silently reading a narrative memo, in place of a presentation:

- **The author writes prose**, not bullets: full sentences and paragraphs that carry
  the argument, its evidence, and the options with their trade-offs. Prose has to hold
  together without a presenter; that is the quality gate.
- **Length is bounded** (Amazon's famous bound is six pages; set your own and hold it).
  A bound forces the author to decide what matters — the work the meeting would
  otherwise do.
- **Reading happens in the room**, silently, at the start — typically 10–20 minutes
  scaled to the document. In-room reading is what guarantees a shared, complete picture;
  "please read beforehand" guarantees the opposite.
- **Questions follow reading.** The author answers; the author does not re-present.
  Discussion starts from page-level questions ("on the risk in section 3…"), which is
  the tell that the room actually read.
- Margin notes during reading are encouraged — they become the first round of questions.

If a full memo is too heavy for the decision at hand, scale down (a one-page brief:
question, context, options, recommendation) — but keep the invariant: **the document
carries the argument; the meeting starts where the document ends.**

## 5. Running the room

- **Open**: state the purpose in one line, confirm the agenda's decision rules, start
  silent reading.
- **Per item**: restate the decision question, confirm the rule and holder, open
  discussion, watch the timebox.
- **The parking lot** lives on screen with a name on every entry. Parking is a promise,
  not a dismissal — the close dispositions every entry: becomes an action (owner +
  date), goes async, lands on a future agenda, or is dropped by name.
- **Calling the decision**: at the timebox, the rule executes. Consult-then-decide:
  the owner decides aloud, now. Consent: "any principled objection?" — silence is
  consent. If new information genuinely blocks the call, the fallback is explicit:
  named blocker, owner, date, and the decision question returns on a stated agenda.
- **The close** (protected, ~5 minutes): read back each decision with its rule, each
  action with owner and date, each parked item with its disposition. Read-back
  surfaces misunderstandings while they are still cheap — people who heard different
  decisions find out in the room, not a week later in the work.

## 6. The decision-log format

One entry per decision, published where the team already works (wiki, channel, repo):

```
DECISION: <the question, and the answer chosen>
DATE / FORUM: <when, which meeting>
RULE: <single owner / consent / consult-then-decide / vote> — held by <name>
OPTIONS CONSIDERED: <A / B / C, one line each>
WHY: <one or two sentences — enough for a reader a year out>
ACTIONS: <owner — action — date> (one line each)
REVISIT IF: <the trigger that would legitimately reopen this>
```

The `REVISIT IF` line is what stops both failure modes at once: quiet relitigation
("I never agreed to that") and blind persistence when the world changes. A fired
revisit trigger is exactly the moment for `decision-science-skills:the-challenger` —
and the revision review it prescribes deserves its own designed decision meeting.

## 7. The recurring-meeting audit protocol

Run on a stated cadence (quarterly is common) over every standing meeting you own:

1. **Pull the evidence**: the last 3–5 decision logs of the meeting. No logs is itself
   the finding.
2. **Re-run the existence test** (§1) against what those occurrences actually
   produced — not against the meeting's original charter.
3. **Compute the standing cost** honestly: length × headcount × frequency, in
   person-hours per quarter. A weekly 60-minute sync with 8 attendees is
   1 h × 8 × 13 weeks = **104 person-hours per quarter** — 2.6 working weeks of one
   person, renewed by default. No invented dollar figures needed; hours are
   persuasive on their own.
4. **Disposition** each meeting: keep as is / shrink (time or headcount) / reduce
   frequency / merge / demote to async post / end. Default for a meeting producing no
   decisions: demote to async for a cycle and see who objects.
5. **Record** the disposition in the decision log, with a `REVISIT IF` line — audits
   are decisions too.

A gentle forcing function: every recurring invite carries an expiry (e.g., two
quarters). Renewal takes one sentence of justification from the owner; a meeting no
one will spend a sentence on has answered the question.
