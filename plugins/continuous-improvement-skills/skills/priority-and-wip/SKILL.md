---
name: priority-and-wip
description: >-
  Applies personal lean to an overloaded workload: put every current commitment on one visible
  personal kanban (to-do / doing / done — nothing hidden in inboxes or memory), cap "doing" with
  a hard WIP limit of two or three and finish before starting, triage incoming work with an
  honestly held urgent/important split (Eisenhower lineage), timebox deep work and batch shallow
  work, renegotiate or decline explicitly when the week is over capacity, and prune stale
  commitments in a weekly review. Teaches the Little's Law intuition — at fixed throughput, more
  WIP means proportionally longer cycle time — this is theory of constraints for one person,
  where attention is the limiting resource. Use when someone is juggling too many open tasks,
  everything feels urgent, or nothing seems to finish. Triggers: WIP limit, personal kanban,
  timeboxing, too many priorities, drowning in tasks, context switching, Eisenhower matrix,
  finish before starting.
metadata:
  version: "1.2.0"
---

# Priority and WIP (personal lean)

## When to use
- One person's workload is overloaded: many tasks in flight, everything feels urgent, nothing
  finishes, and new work keeps arriving on a full plate.
- Deciding what to start next, whether to accept incoming work, and how to lay out the week so
  deep work actually happens.
- Standing up a personal work-visualization system (a personal kanban) or repairing one that
  quietly died.
- Not for: finding the system constraint in a multi-step process or a team → see
  `continuous-improvement-skills:theory-of-constraints` (this skill is that method scaled down
  to a single person).
- Not for: mapping a process end to end to see where the time goes → see
  `continuous-improvement-skills:value-stream-mapping`.
- Not for: drive and effort on the task already chosen → see
  `coding-agent-skills:stay-hard-accountability` (this skill picks what earns the next hour;
  that one gets it done).
- Not for: deciding whether a committed project still deserves its slot after the evidence
  changed → see `decision-science-skills:the-challenger`.

## Do it
Board setup, WIP-limit selection and the violation protocol, the triage flow, timebox/batch
patterns, the weekly review script, and renegotiation scripts are in
`references/personal-lean-method.md`. The assistant drafts the sweep, the card splits, the triage
calls, and the renegotiation scripts; the human owns the WIP limit, every yes and no, and the
weekly review.

1. **Visualize all current work in one place.** Build a personal kanban — three columns are
   enough: to-do / doing / done. Sweep everything into it: flagged emails, chat promises,
   meeting actions, "I'll get to it" mental notes. One card per commitment, phrased as a
   finishable outcome ("draft sent"), not a topic ("website"); project-sized items get split
   until each card fits inside a few deep-work blocks. The board is the single source of
   truth: anything not on it does not exist, and anything hiding in an inbox is invisible
   load you're still paying for. Work blocked on someone else moves to a waiting-for column
   with a chase date — out of "doing" (it isn't consuming attention) but never out of sight.
2. **Set a hard WIP limit on "doing" and finish before starting.** Start at 2–3 cards. The
   limit is a rule, not a hope: when you want to start something and the column is full,
   something must finish, move explicitly back to to-do, or be explicitly dropped. Wanting a
   fourth slot is the signal the system is working — it forces the sequencing decision that
   used to happen silently and badly.
3. **Triage incoming work with the urgent/important split, held honestly.** Two questions per
   arrival (Eisenhower lineage): does this matter to my actual goals, and does it have a real
   clock on it? Important-and-urgent goes to to-do, ranked; important-not-urgent gets a
   timebox on the calendar; urgent-not-important gets the smallest honest response, delegated
   or bounded; neither gets declined or deleted. Know the grid's failure mode: under pressure
   everything migrates to urgent-important. The fix is not better sorting — it is the WIP
   limit, which forces a sequence no matter how many cards claim to be both.
4. **Timebox deep work and batch shallow work.** Put deep-work blocks on the calendar first —
   they never happen "when things calm down" — and give each block one card. Collect shallow
   work (email, small approvals, admin) into one or two fixed windows a day. Context switching
   is expensive: each switch pays a re-loading tax on attention, and the residue of the last
   task blunts the next one — so the win comes from fewer, longer stretches on one thing, not
   from faster juggling.
5. **Renegotiate or decline explicitly when the system is over capacity.** When to-do outgrows
   any plausible week, saying yes and silently slipping is the worst move — an unowned "yes"
   is a schedule slip someone else discovers later. Go back with the board visible: "I can take
   this, and it means X moves to Thursday — or I can hand you a smaller version today." The
   scripts in the reference cover declining, rescheduling, and swapping.
6. **Run a weekly review.** Once a week, walk the board: prune cards that have gone stale,
   re-justify standing commitments (does this recurring task still earn its slot?), celebrate
   the done column, and pick the few things next week is actually about. A board that isn't
   pruned weekly rots into another guilt list. The review itself is a habit worth designing
   deliberately — see `learning-skills:habit-design`.

## Why / learn
The load-bearing result is **Little's Law**: for a stable system, average WIP = throughput ×
average cycle time. Rearranged for one person, whose throughput is roughly fixed — you finish
what you finish — average cycle time is proportional to average WIP. Ten items in flight means
each one takes, on average, five times longer to come back than two in flight would. That is
the whole argument, and it needs only the intuition level: starting more work does not create
capacity, it only dilutes the capacity you have across more open items, so *everything*
finishes later. Starting feels like progress because it is visible and immediate; finishing is
the only progress anyone downstream can use.

Why a visible board beats a memory-resident list: the mind is a bad kanban. It has no columns,
no counts, and no done pile — open loops resurface at random, each one interrupting the task in
hand, and the load itself is invisible so overcommitment never looks like what it is. A board
externalizes the loops (they stop interrupting once they're trusted to a system), makes load
countable (a full "doing" column is an argument you can show someone), and makes finishing
visible (the done column is the evidence that the limit works).

Why WIP limits feel slower and are faster: the limit forces queueing — work waits in to-do
instead of being "started" — and waiting work feels like failure. But work that has been
started and abandoned mid-flight is *also* waiting, just invisibly, while charging rent:
every open item costs re-loading time on each return and background attention in between.
The limit converts hidden, expensive waiting into visible, cheap waiting, and single-tasking
removes the switch tax — same throughput mechanics as any flow system, experienced as calm.

And that is the frame worth keeping: this is **theory of constraints for one person**. The
constraint is your attention — the one resource every commitment queues for. The board makes
the queue visible; the WIP limit exploits the constraint (no half-loaded switching, no rework
from dropped context); triage subordinates everything else to it (only work that earns the
constraint's next hour gets it); and renegotiation is honest capacity management instead of
quiet overload. When one task gates a whole *team's* output, scale back up to
`continuous-improvement-skills:theory-of-constraints`.

## Common mistakes
- Work scattered across email flags, sticky notes, chat, and memory → one board, one card per
  commitment; sweep the inboxes into it.
- The WIP limit as an aspiration ("usually three-ish") → a hard rule with a violation protocol:
  finish, move back, or drop — explicitly.
- Everything graded urgent-and-important → grid inflation is the Eisenhower failure mode; let
  the WIP limit force a sequence instead of re-sorting.
- Starting new work to feel productive while five items sit open → finish before starting;
  starting is not progress.
- Project-sized cards squatting in "doing" for weeks → split until each card can finish
  within a few deep-work blocks; a card that can't finish can't leave.
- Blocked items held in "doing" out of guilt → move them to waiting-for with a chase date;
  they're not consuming your attention, so they shouldn't consume a slot.
- Deep work scheduled for "when things calm down" → they don't; timebox it first, then fit the
  shallow work around it.
- Absorbing new work silently when over capacity → an unowned "yes" is a schedule slip in
  disguise; renegotiate with the board visible.
- The board quietly dies after two weeks → the weekly review is the maintenance habit; without
  pruning, the board becomes another guilt list.
- Using this skill to fix a team's delivery flow → one person's attention is not the system
  constraint of a process; use `continuous-improvement-skills:theory-of-constraints` or
  `continuous-improvement-skills:value-stream-mapping`.

## Tailor to your environment
Record your setup in `references/your-environment.md`: where the board lives (tool or wall),
your current WIP limit and what violates it most, your deep-work windows and shallow-batch
times, the standing commitments on trial, and when the weekly review happens. If cards would
name real clients, matters, or colleagues, keep specifics in `your-environment.private.md` —
that suffix is git-ignored. Commit only sanitized, structural examples.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/priority-and-wip.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/personal-lean-method.md — board setup, WIP-limit selection and violation
  protocol, the triage flow, timebox/batch patterns, the weekly review script, and
  renegotiation scripts for declining and rescheduling
- references/your-environment.md — your board, limits, windows, and review slot (fill in)
