# The personal-lean method: board, limits, triage, timeboxes, review, renegotiation

Lineage: kanban and WIP limits from lean/flow practice, scaled to one person; the
urgent/important grid in the Eisenhower lineage; Little's Law (average WIP = throughput ×
average cycle time) supplying the intuition for why limits work.

## Contents
- [Board setup](#board-setup)
- [Choosing the WIP limit and the violation protocol](#choosing-the-wip-limit-and-the-violation-protocol)
- [The triage flow](#the-triage-flow)
- [Timebox and batch patterns](#timebox-and-batch-patterns)
- [The weekly review script](#the-weekly-review-script)
- [Renegotiation scripts](#renegotiation-scripts)
- [Little's Law, worked at intuition level](#littles-law-worked-at-intuition-level)

## Board setup

Three columns are enough to start: **to-do / doing / done**. Common useful additions, added
only when a real need appears:
- **Waiting-for** — items blocked on someone else, with the name and the date you asked.
  Keeps blocked work out of "doing" (it isn't consuming your attention) without letting it
  vanish. Check it in the weekly review and nudge anything older than its promise.
- **This-week** — a thin buffer between the full backlog and "doing", loaded only at the
  weekly review. Protects daily choices from the intimidating full list.

Card conventions that keep the board honest:
- **One card per commitment**, phrased as a finishable outcome ("draft sent to reviewer"),
  not a topic ("website"). A card that can't finish can't leave.
- **Big items get split** until each card fits inside a few deep-work blocks; the project
  itself can live as a header or a separate lane, but "doing" holds tasks, not projects.
- **Recurring obligations** get one standing card each, so they occupy visible capacity.
- **The initial sweep:** empty every hiding place onto the board in one sitting — email flags,
  chat promises, meeting notes, the mental "I owe them" list. The board only calms the mind
  once the mind trusts that the board holds everything.

Tool choice matters less than visibility: a wall of stickies, a text file, or any kanban app
works if you see it every day without effort. Pick the one you'll actually look at.

## Choosing the WIP limit and the violation protocol

**Start at 2–3 for "doing".** One slot for the main deep-work item, one for a second track
(the thing you switch to when genuinely blocked), and at most one more if your role has
constant small interrupts. The right number is discovered, not derived: if items sit in
"doing" untouched for days, the limit is too high; if you're often idle while everything
waits on others, it may be one too low (or your waiting-for column needs chasing).

**The violation protocol** — what happens when you want to start item N+1:
1. **Finish** something in "doing" first (the default answer), or
2. **Move back**: return a "doing" card to to-do explicitly — an honest un-start, with
   a note on where it stood — rather than letting it decay in place, or
3. **Drop or renegotiate**: decide the new item doesn't get done (say so, out loud, to
   whoever expects it), or that an existing one doesn't (same).

The point of the protocol is that all three moves are *explicit*. The un-limited version of
this decision happens anyway — as silent decay, forgotten cards, and surprise slips. The limit
doesn't create the trade-off; it surfaces it while it's still cheap.

**Emergencies:** a true drop-everything item bumps a card out of "doing" via move-back, not by
raising the limit. If emergencies bump the board more than occasionally, that's not a WIP
problem — it's an intake problem for the weekly review to examine.

## The triage flow

Run every arrival — email, meeting action, hallway ask — through the same short flow, ideally
at batch times rather than on arrival:

1. **Is it actually a commitment?** FYI-only items get read and archived; no card.
2. **Two-minute rule:** if doing it now is faster than tracking it, do it in the shallow
   window and move on; no card.
3. **Important?** Does it advance your actual goals or obligations — not someone else's
   convenience? **Urgent?** Is there a real clock with real consequences, or just an
   exclamation mark?
   - **Important + urgent** → to-do, ranked against what's there.
   - **Important, not urgent** → timebox it on the calendar now; this quadrant only happens
     by appointment, because urgency wins every tie.
   - **Urgent, not important** → smallest honest response: a bounded quick version, a
     redirect to the right owner, or a clarifying question that often dissolves it.
   - **Neither** → decline or delete, visibly enough that no one thinks it's quietly owned.
4. **Over capacity?** If adding the card makes the week implausible, go straight to a
   renegotiation script — don't let the board absorb a lie.

Honesty guard: the grid inflates under pressure — everything claims urgent-important. Two
counters: (a) ask "what actually happens if this waits a week?" and believe the answer;
(b) remember the WIP limit makes inflation harmless anyway, because even a column full of
"urgent-important" cards must still form a single-file sequence.

## Timebox and batch patterns

- **Deep-work blocks first.** Place 1–2 blocks (60–120 minutes) on the calendar before
  anything else claims the week; each block gets exactly one card from "doing". Guard them
  like meetings with your most important stakeholder, because they are.
- **Shallow batches.** Two fixed windows a day for email/chat/admin beats continuous
  monitoring: the work takes less total time in batch, and the rest of the day stops paying
  the switch tax. Notifications off outside the windows, if your role allows; if it doesn't,
  define what genuinely can't wait two hours and let only that through.
- **Theme days / half-days** when the calendar allows: grouping similar work (all reviews
  Tuesday afternoon, all admin Friday morning) cuts switches at a coarser grain.
- **The switch tax, stated honestly:** every switch costs re-loading time before you're
  actually working on the new thing, and attention residue from the old thing lingers —
  qualitatively certain, person- and task-dependent in size. Don't quote a precise
  percentage; the honest claim — fewer, longer stretches on one thing beat fast juggling —
  is enough to act on.

## The weekly review script

Fifteen to thirty minutes, same slot every week (protect it like a deep-work block — and
consider designing it deliberately as a habit, with a fixed cue and a small reward; that's
`learning-skills:habit-design` territory):

1. **Empty the inboxes** onto the board: anything committed this week that never got a card.
2. **Walk "done"** — notice what actually finished; it calibrates next week's plan.
3. **Walk "doing"** — anything untouched for a week gets moved back or dropped, with a note.
4. **Walk "waiting-for"** — chase anything past its promise date.
5. **Prune to-do** — stale cards (no longer matters, overtaken by events) are deleted aloud;
   a to-do list that only grows stops being consulted.
6. **Re-justify standing commitments** — each recurring card must re-earn its slot
   occasionally: does this still produce more than it costs? (For a big committed project
   that deserves a genuinely hard look, use `decision-science-skills:the-challenger`.)
7. **Load "this-week"** — pick the few items next week is about, checked against the real
   calendar, not the aspirational one.

## Renegotiation scripts

The principle behind all three: bring the trade-off to the person who owns the expectation,
while it's still cheap. You're not saying "no" — you're refusing to promise what the board
says can't happen.

- **Declining:** "I can't take this on without dropping something that matters more. If it's
  more important than X, tell me and I'll swap them — otherwise I have to pass."
- **Rescheduling:** "I said Thursday; with what's landed since, the honest date is Monday.
  I'd rather tell you now than surprise you Thursday. If Thursday is fixed, here's what I'd
  need to move: …"
- **Swapping / descoping:** "I can take the new item if X moves out a week — or I can hand
  you a smaller version of the new item today: just the summary table, not the full
  analysis. Which serves you better?"
- **For your own manager, show the board:** a visible, countable "doing" column turns "I'm
  busy" (a feeling, easily discounted) into "here are the four things in flight; which one
  does the new item displace?" (a decision, properly theirs to make).

## Little's Law, worked at intuition level

The law, for a stable system: **average WIP = throughput × average cycle time**. Solve for
cycle time: average cycle time = average WIP ÷ throughput.

**Term warning — "cycle time" means something different here than in value-stream mapping.**
In Little's Law it is the *end-to-end* time an item spends in the system from start to finish,
including every wait — days or weeks. In `continuous-improvement-skills:value-stream-mapping`
"cycle time" is the *hands-on touch time of one step*, minutes or hours, and the end-to-end
quantity is called **lead time**. Same two words, quantities an order of magnitude apart. If
you are drawing a value-stream map, use that skill's vocabulary; the law below is about lead
time in its sense.

One person finishing about five items a week:
- **WIP = 3** → average cycle time ≈ 3/5 of a week. Things come back in days.
- **WIP = 15** → average cycle time ≈ 3 weeks. Same person, same effort, same weekly output —
  but every individual item now takes roughly five times longer to return, everyone waiting
  on you waits weeks, and each open item charges attention rent the whole time.

The trap is that the aggregate throughput looks identical in both worlds, so the overloaded
world *feels* defensible — "I'm finishing just as much!" The difference is entirely in cycle
time, and cycle time is what everyone downstream experiences (plus, in practice, throughput
quietly *falls* as WIP rises, because switch taxes and re-loading eat real capacity — so the
second world is strictly worse, not just slower per item). Two honest limits of the intuition:
the law describes averages in a roughly stable system, not a guarantee per item; and the
personal-work version is an analogy to a queueing result, so use it to reason about direction
— more WIP, longer cycle times — not to compute precise dates.
