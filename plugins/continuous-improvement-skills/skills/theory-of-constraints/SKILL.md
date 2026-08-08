---
name: theory-of-constraints
description: >-
  Applies Goldratt's Theory of Constraints — the five focusing steps (identify, exploit,
  subordinate, elevate, repeat), drum-buffer-rope scheduling, and throughput accounting — to find
  the one step that limits a whole system's output and manage everything else to its pace. Use when
  one task or resource gates an entire process (a month-end close calendar, an AR collections
  pipeline, a team's WIP), when speeding up busy non-bottlenecks isn't moving the end date, or when
  deciding whether added capacity is worth the spend. Triggers: bottleneck, theory of constraints,
  five focusing steps, drum-buffer-rope, exploit the constraint, everything is waiting on X, the
  whole close waits on one task, throughput accounting.
---

# Theory of constraints

## When to use
- One step gates the output of a whole system: the close calendar has one task everything waits on;
  the plant has one machine; the collections pipeline has one approver; your own week has one
  deep-work slot. Goldratt's method (from *The Goal*) tells you what to do about it.
- The natural next step after a value-stream map: the VSM *finds* the bottleneck (its
  environment template even asks for known waits/bottlenecks); this skill says what to *do* with
  it — see `continuous-improvement-skills:value-stream-mapping`.
- Compressing the month-end close: the constraint task sets the close duration, so the calendar is
  subordinated to it and everything else pre-staged — see `accounting-skills:month-end-close`.
- Deciding whether to buy capacity (people, software, a second shift) — or whether the existing
  capacity is simply being wasted.
- Not for: mapping the whole stream end to end to see where time goes → see
  `continuous-improvement-skills:value-stream-mapping` (it feeds this skill). Formal queue-wait
  mathematics → out of scope here; this skill uses queueing *intuition* in prose only.

## Do it
Work the five focusing steps in order — `references/focusing-steps-and-dbr.md` expands each with a
close-calendar worked example, drum-buffer-rope mechanics, and throughput accounting.
1. **IDENTIFY the system constraint.** Look for where work piles up in front and everything
   downstream starves: the longest queue, the task whose finish date sets the system's finish date.
   From a described workflow or close calendar, draft the constraint hypothesis by tracing which
   task's delay would move the end date one-for-one. **Human gate:** the hypothesis is verified at
   the gemba — go watch where the work actually happens (genchi genbutsu) — never accepted from
   inference alone; a plausible-sounding wrong constraint wastes the whole cycle.
2. **EXPLOIT the constraint.** Squeeze the capacity you already have before spending anything: no
   idle time on the constraint, strip it of work others can do, quality-check its inputs so it
   never processes junk or reworks, cover its breaks, schedule its highest-value work first.
3. **SUBORDINATE everything else to its pace.** Non-constraints run at the constraint's rate, not
   their own maximum — a non-constraint at full speed just builds WIP that hides problems and
   inflates lead time. Gate the release of work to what the constraint can absorb; measure
   non-constraints on serving the constraint, not on their local efficiency.
4. **ELEVATE only if still binding.** If steps 2–3 haven't bought enough capacity, now add some:
   cross-train a second person, automate, buy the machine. Elevation costs money; exploitation is
   free — that's why it comes fourth.
5. **REPEAT — and beware inertia.** The constraint moves after you break it. Go back to step 1,
   and hunt down the rules, buffers, and habits built for the *old* constraint; policies outliving
   their constraint are the most common constraint of all.

Schedule with **drum-buffer-rope**: the constraint sets the **drum** (system pace); a **time
buffer** of ready work protects it from ever starving; the **rope** ties work release to the drum's
rate so WIP can't balloon. Judge every proposed action with **throughput accounting** — does it
raise throughput (T), cut inventory/WIP (I), or cut operating expense (OE)? — never by local
efficiency or cost-per-unit at a non-constraint.

## Why / learn
The core theorem is blunt: **a system's output is set by its constraint and nothing else.** An hour
lost at the constraint is an hour of output lost for the whole system, forever; an hour saved at a
non-constraint is a mirage — it just makes waiting. That is why "everyone stay busy" is actively
harmful: local-efficiency measures push non-constraints to produce at full tilt, which turns into
piles of WIP, longer lead times, and expediting — activity without throughput. Subordination feels
wrong (idle capacity!) and is the step organizations resist, but a queueing intuition explains it:
as any resource is pushed toward full utilization, its queue — and thus everyone's wait — grows
explosively, so deliberately running non-constraints below capacity is what keeps flow smooth and
the constraint fed. The five steps are ordered by economics: exploit (free) before elevate
(expensive), because most "we need more capacity" problems are really "we waste the capacity we
have" problems. The evidence base is unusually strong for a management method: an independent
meta-analysis across 80+ published applications reported mean lead-time reductions around 70% and
inventory reductions around 49% `[snippet-only]` (Mabin & Balderstone). And the constraint is a
system property, not a culprit — the person running the constraint task needs help and protection,
not blame. What once took a consultant walking the plant — spotting the constraint, drafting the
exploit/subordinate plan, running the throughput arithmetic — an LLM now drafts from a described
workflow in one conversation; what it cannot supply is the verification, which is why step 1's
gemba check is part of the method, not a formality.

## Common mistakes
- Elevating first (hiring, buying) before exploiting → you pay for capacity the process wastes. Exploit, then decide.
- Measuring local efficiency everywhere → non-constraints run flat out, WIP explodes, lead time grows. Subordinate.
- Accepting the inferred constraint without a gemba check → a wrong constraint wastes the full cycle. Verify where the work happens.
- Skipping step 5 → rules built for the old constraint outlive it (inertia), and the system quietly re-binds.
- Letting the constraint process junk → its scarce hours go to rework. Quality-check inputs upstream.
- "Balancing" capacity so every resource matches demand → random variation then starves the constraint. Protect it with a buffer instead.
- Treating the constraint as a person to blame → it's a system property; respect for people holds here as everywhere in lean.

## Tailor to your environment
Record your real system in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real people, vendors, or systems). Capture the process in scope, the
current constraint hypothesis and how it was verified, the exploit/subordinate decisions in force,
buffer sizes, what T/I/OE mean in your context, and the date the constraint was last re-identified.
Never commit real client or transaction data — sanitize to structure only.

## References
- references/focusing-steps-and-dbr.md — the five focusing steps expanded with a close-calendar
  worked example, drum-buffer-rope mechanics, throughput accounting, and the evidence base
- references/your-environment.md — your constraint, buffers, and measures (add when supplied)
