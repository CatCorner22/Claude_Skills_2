---
name: meeting-design
description: >-
  Designs meetings that produce decisions instead of discussion. Tests whether the meeting
  should exist (does it produce a decision or a commitment? status flows async); writes the
  agenda as a list of decisions to make, each with a timebox and a decision rule named
  before discussion opens (single owner, consent, consult-then-decide, or vote); sends
  pre-reads with silent reading at the start (documented Amazon practice);
  parks tangents visibly, calls the decision at the timebox, gives every
  action an owner and a date, and closes by reading back decisions and commitments. Drafts
  the decision-list agenda from a stated purpose, red-checks an agenda for non-decisions,
  turns a transcript into a decision log, and audits recurring meetings nobody has
  re-justified. Use when planning, tightening, or questioning any meeting. Triggers:
  meeting agenda, run this meeting, too many meetings, this should be an email, action
  items, decision protocol, pre-read, standing meeting audit, fix the agenda.
metadata:
  version: "1.1.0"
---

# Meeting design (decisions, not topics)

## When to use
- Planning a meeting and wanting it to end with things decided, not topics visited.
- Questioning whether a meeting should exist at all — yours or one you keep getting
  invited to.
- Red-checking an existing agenda: "which of these items are actually decisions?"
- Converting a transcript or messy notes into a decision log with owners and dates.
- Auditing a recurring meeting that nobody has re-justified since it was created.
- When `decision-science-skills:the-challenger` fires a revision trigger, the resulting
  go/no-go deserves a designed decision meeting — this skill builds that room.
- Not for: kaizen events and co-design workshops → see
  `continuous-improvement-skills:kaizen-and-codesign`, which owns workshop facilitation;
  this skill covers the ordinary working meeting.
- Not for: escalating a problem or transferring work under time pressure → see
  `safety-and-reliability-skills:sbar-structured-communication`.
- Not for: negotiating the substance once you are in the room → see
  `decision-science-skills:principled-negotiation`; this skill designs the container,
  not the bargaining.
- Not for: working out who must be in the room at all — power, interest, engagement
  moves → see `collaboration-skills:stakeholder-mapping`; this skill designs the
  meeting for the people the map surfaces.

## Do it
Full templates — the decision-list agenda, the four decision rules, silent-start
mechanics, the decision-log format, and the recurring-meeting audit — are in
`references/meeting-method.md`.

1. **Test whether the meeting should exist.** One question: will this gathering produce
   a decision or a commitment that would not happen async? Status, updates, and FYIs
   flow as written posts; a meeting is for the moments where synchronous judgment
   changes the outcome. If the answer is no, draft the async post instead — that is a
   success of the method, not a failure of nerve.
2. **Write the agenda as a list of decisions, not topics.** Each item is a decision
   question ("Do we ship with the current importer or slip two weeks?"), never a noun
   ("Importer status"). Give each item a timebox, and name the decision rule *before
   discussion opens*: single owner decides / consent (proceed unless someone states a
   principled objection) / consult-then-decide (the owner hears the room, then calls
   it) / vote. Name who holds the rule, out loud and on the agenda.
3. **Send the pre-read ahead; open with silent reading.** The author writes prose, not
   slides. The room reads silently for the first minutes — this is documented Amazon
   practice: narrative memos read at the start of the meeting in place of a
   presentation. Nobody presents what everyone can read faster themselves; the author
   answers questions once reading ends.
4. **Run the room to the rule.** Park tangents visibly (a named lot, on screen — not in
   someone's private notes), and call the decision when the timebox ends. With the rule
   named in advance, the call is mechanical rather than awkward. If the decision
   genuinely cannot be made, the output is a named blocker with an owner and a date —
   not a longer discussion.
5. **Every action leaves with an owner and a date.** "Someone should look into that" is
   a tangent wearing an action's clothes; assign it to a person with a date, or drop it.
6. **Close by reading back**: decisions made (with their rules), actions with owners
   and dates, and every parked item with its disposition. Publish the read-back as the
   decision log — the log, not the conversation, is the meeting's product.
7. **Audit recurring meetings on a cadence.** Re-run the step-1 test on every standing
   meeting you own: what decisions did its last few occurrences actually produce?
   Shrink it, merge it, demote it to an async post, or end it.

Division of labor: the assistant drafts the decision-list agenda from a stated purpose,
red-checks an existing agenda item by item, and converts a transcript or notes into the
decision log. The human owns the invite list (map it with
`collaboration-skills:stakeholder-mapping`), ratifies each decision rule, and makes
the calls in the room.

## Why / learn
A topic is a place to visit; a decision is a finish line. "Discuss Q3 roadmap" is
satisfied by any amount of talking, so talking is what happens, and it stops when the
clock runs out rather than when anything is settled. "Decide: cut feature X or slip the
date" can be *answered*, and everyone in the room can tell whether it has been. That is
the core mechanism: agendas phrased as answerable questions give a meeting a way to be
done, so discussion converges instead of expanding to fill the room.

Naming the decision rule up front is what prevents the fake-consensus meeting. When
nobody says who decides, the group defaults to an unspoken everyone-must-agree rule it
never chose: discussion runs until fatigue produces the appearance of agreement, the
loudest or most senior voice fills the vacuum, and people leave believing different
things were decided. Saying "Ana decides after hearing the room" before discussion
opens changes what the discussion is *for* — informing a named judgment rather than
winning a hidden vote — and makes calling the decision at the timebox a formality
instead of a confrontation.

Silent reading beats presenting for two reasons. First, everyone actually reads:
pre-reads sent "to review beforehand" reliably go unread, and the meeting quietly
re-derives the document out loud for the people who skipped it — so the reading time
moves inside the meeting, where it is short, shared, and honest. Second, written prose
is a stricter argument than a slide deck: it has to hold together without a performer,
so weak reasoning shows on the page before it costs the room an hour. The author's
prose is the argument; the meeting starts where the document ends.

A recurring meeting is a standing cost that renews by default. Multiply its length by
its headcount by its frequency and it is real capacity — yet unlike almost any other
recurring commitment, no one has to re-approve it, so it persists on the momentum of
its own existence long after the need that created it has gone. The audit exists
because the default is silence, and silence is a yes.

## Common mistakes
- Agenda items are nouns ("Budget", "Hiring update") → rewrite each as a decision
  question, or move it to the async status post where it belongs.
- The decision rule surfaces at the end ("so… who actually decides this?") → name the
  rule and its holder before discussion opens; the rule shapes the discussion.
- The pre-read gets presented as slides anyway → open with silent reading; the author
  answers questions, never walks the room through the document.
- Tangents eat the timebox → park them visibly, keep the lot on screen, and disposition
  every parked item at the close so parking is not a polite way of ignoring people.
- Actions leave without an owner and a date → they are not actions; assign or drop.
- The close gets skipped when time runs short → the read-back is the product; cut
  discussion to protect it, never the reverse.
- A status meeting survives because it has always existed → run the step-1 test;
  status flows async.
- Decisions evaporate within a week → publish the decision log where the team already
  works, and open the next occurrence by checking the last log's commitments.

## Tailor to your environment
Record house specifics in `references/your-environment.md`: where decision logs are
published, the default decision rule per forum, your standing-meeting inventory and
audit cadence, pre-read length norms, and the async channel of record. Anything
sensitive — named attendees, org dynamics, who actually holds which decision — belongs
in `your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/meeting-design.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/meeting-method.md — the decision-list agenda template with the four
  decision rules, the should-this-meeting-exist test, silent-start mechanics, the
  decision-log format, and the recurring-meeting audit protocol
- references/your-environment.md — your forums, logs, default rules, and audit cadence
