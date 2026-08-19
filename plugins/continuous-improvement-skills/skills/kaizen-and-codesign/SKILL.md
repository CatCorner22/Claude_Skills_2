---
name: kaizen-and-codesign
description: >-
  Plans and facilitates kaizen events and co-design sessions so the people who do the work — and
  their downstream customers — design the improvement themselves: a tight measurable charter,
  operators plus a downstream customer plus an on-the-spot decision-maker in the room, a gemba
  walk before any design talk, equal-voice facilitation (brainwriting, affinity grouping,
  dot-voting), rapid PDCA loops tested on real work the same day, and standard work plus a
  30/60-day check captured before close. Grounded in Imai's kaizen and the participatory-design
  tradition, respect-for-people throughout. Use when running an improvement workshop, kaizen
  event, or participatory/co-design session, or facilitating continuous improvement. Triggers:
  kaizen, kaizen event, kaizen blitz, co-design, co-creation, participatory design, improvement
  workshop, rapid improvement event, gemba, gemba walk, facilitation, continuous improvement
  event.
metadata:
  version: "1.2.0"
---

# Kaizen and co-design

Kaizen — Masaaki Imai's term for continuous improvement by everyone, mostly small and daily —
and co-design — the participatory-design tradition of having workers and users design the
change themselves — share one load-bearing belief: those closest to the work design the best,
most durable improvements. This skill runs the room where that happens.

## When to use
- Planning or facilitating a **kaizen event** (a focused, time-boxed improvement workshop,
  sometimes called a kaizen blitz or rapid improvement event) on a real process.
- Running a **co-design / participatory** session where the workers and customers design the
  change together, not consultants for them — a legal team redesigning intake, analysts
  redesigning a reporting handoff, developers redesigning code review, ops redesigning a
  fulfillment step.
- Facilitating any continuous-improvement session at the gemba with rapid PDCA.
- Not for: mapping the whole value stream that scopes the event → see
  `continuous-improvement-skills:value-stream-mapping`. Ordinary working meetings that
  should produce decisions → see `collaboration-skills:meeting-design` (this skill owns
  workshop facilitation; that one owns the everyday meeting).
- Not for: translating the weighted needs this event surfaces into engineering characteristics,
  with the correlation matrix and the competitive benchmark → see
  `continuous-improvement-skills:qfd-house-of-quality`. The prioritized needs a co-design
  session produces are exactly that skill's left wall.

## Do it
`references/facilitation-playbook.md` has the charter, agenda, technique details, and a
worked example.
1. **Scope and charter the kaizen tightly.** One narrow, real process; a specific,
   measurable objective; fixed dates and boundaries; a sponsor who removes obstacles. Kaizen
   events are *small, focused, fast* — a bounded problem you can move within days, not a
   boil-the-ocean program.
2. **Assemble the right room: the people who do the work + the downstream customer.**
   Include the actual operators (not just supervisors), a downstream "customer" who receives
   the output, and someone who can authorize changes on the spot. This mix is the whole
   design — the workers hold the knowledge, the customer holds the need.
3. **Go to the gemba first.** Start where the work actually happens: observe the real
   process, talk to the people doing it, gather facts. Much of what operators know is tacit —
   draw it out with low-stakes interviewing rather than interrogation
   (`collaboration-skills:disarming-elicitation`). Design from what *is*, not from a
   conference-room guess.
4. **Facilitate for equal voice.** Run the idea-generation segments as structured ideation —
   silent brainwriting before discussion, affinity grouping, dot-voting to converge
   (`continuous-improvement-skills:structured-ideation` owns the technique detail). Protect
   the quietest operator's idea from the loudest manager's. The facilitator owns the
   *process*; the group owns the *content*.
5. **Run rapid PDCA inside the event.** Don't just plan — **try**. Prototype a change, test
   it on real work that same day, observe, adjust, and try again. Several fast small loops
   beat one big rollout; the event's power is testing ideas live where the work is.
6. **Capture standard work and a follow-up plan before you close.** Document the improved
   method as standard work (`continuous-improvement-skills:standard-work`), assign owners
   and dates for anything unfinished, set the metric to watch, and schedule a 30/60-day
   check. If the change needs wider buy-in afterward, carry its story on a one-page A3
   (`continuous-improvement-skills:a3-thinking`). Debrief the event itself while it's warm —
   a four-question team review (`decision-science-skills:after-action-review`) makes the
   next event better. An event with no standard and no follow-up reverts.
7. **Honor respect-for-people throughout.** Frame every problem as a process problem, never
   a person problem; give credit to the people whose ideas were used; and make the
   improvement *theirs*. This is the principle that makes people bring the next idea, too.

## Why / learn
Those closest to the work design the best, most durable improvements — everything in the
method follows from that. The operator who does a task 200 times a day knows its real
failure modes, workarounds, and constraints in a way no outside analyst can reconstruct from
a diagram, so a solution designed *with* them starts from truer facts and skips the failures
a remote design would blunder into. The same conviction arrived independently from two
traditions: Imai's kaizen (his 1986 book carried the term into Western management) frames
improvement as everyone's daily work, not a specialist's project; and Scandinavian
participatory design grew from workplace projects where the people who would live with new
tools helped design them. Both converge on the deeper reason: ownership. **People support
what they help create.** A change handed down is complied with grudgingly and quietly reverts
the moment attention moves on; a change the team designed is *theirs* to defend, so it
sticks.

That is why you go to the gemba (design from reality, not imagination), why the downstream
customer sits in the room (so the improvement serves the actual need, not a proxy for it),
and why facilitation protects equal voice — the best idea is often the quietest person's,
and a session dominated by the highest-paid opinion wastes the very knowledge you convened
to capture. Rapid PDCA inside the event embodies the lean bias for *trying* over
*deliberating*: a small change tested on real work today teaches more than a week of
meeting-room debate, and it's reversible. **Respect-for-people** isn't soft framing — it is
one of the two pillars of the Toyota Way alongside continuous improvement, and it's the
engine: treat every problem as a process problem rather than a blame hunt, credit the people
whose ideas you use, and they'll surface the next hundred improvements. One honest caveat
about the word itself: the multi-day "kaizen event" is largely a Western adaptation — Imai's
kaizen is the *daily habit* of small improvements by everyone. Run events, but measure their
success by whether the habit takes root after the banners come down.

## Common mistakes
- Scoping too big → nothing moves in the time-box. Kaizen events are small, focused, and fast.
- Filling the room with managers, not the actual operators → you lose the real knowledge. Invite the doers.
- Leaving the downstream customer out → you improve for a proxy need. Put the receiver in the room.
- Planning without trying → analysis paralysis. Run rapid PDCA; test on real work the same day.
- The loudest voice dominates → the best (quiet) idea is lost. Facilitate for equal voice.
- Closing with no standard work or follow-up → it reverts in weeks. Capture the standard; schedule a check.
- Framing problems as people's faults → people hide problems and stop contributing. Respect-for-people first.
- Treating the event as the improvement program → events seed the habit; if nothing improves
  between events, only the theater happened.
- Facilitator injecting their own solution → the group's ownership evaporates. Own the
  process, never the content.

## Tailor to your environment
Wire in your current role here — the method is domain-neutral by design and runs the same
whether the room holds analysts, attorneys, ops staff, or developers, in this job or the
next. In `references/your-environment.md`, record your event format and length, who your
typical participants and downstream customers are, your sponsor/authorization path, your
facilitation toolkit, and how you store standard work and run follow-ups. Keep the committed
file structural; real people, teams, systems, or performance numbers go in
`your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/kaizen-and-codesign.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/facilitation-playbook.md — the charter, a two-day agenda, equal-voice
  facilitation techniques, rapid PDCA in practice, respect-for-people ground rules, a
  worked domain-neutral example, follow-up/sustainment, and canon notes
- references/your-environment.md — your event format, participants, and follow-up path (add when supplied)
