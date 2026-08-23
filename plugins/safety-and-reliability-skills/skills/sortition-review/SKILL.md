---
name: sortition-review
description: >-
  Designs selection-by-lot oversight channeling Athenian euthynai (scheduled end-of-term
  review by allotted reviewers, generals included, universal, never suspicion-triggered) and
  the 1268 Venetian doge protocol (ten alternating rounds of lot and vote, blind draws, 529
  years): define the reviewable population, set a universal floor with no exemptions, draw
  items by verifiable lot (pre-committed seed,
  dice in the open), rotate reviewer pairs by lot too, make end-of-role handover review
  the default so departure carries no stigma, size the draw to real attention (the
  assistant first-passes every drawn item, the human adjudicates), and publish the rule,
  never the draw. Use when selection must be unriggable, review must carry no accusation,
  or the same person always checks the same people. Triggers: sortition, review by lot,
  spot-check by lot, they know which ones get looked at, same person always reviews,
  rotate reviewers, end-of-term handover, draw at random, unriggable selection.
metadata:
  version: "1.3.1"
---

# Sortition review (euthynai and the ballotino)

Classical Athens made accountability *boring*. Every magistrate — even the generals —
underwent euthynai at the end of every term: a financial accounting before allotted
logistai, then a general conduct examination before allotted euthynoi, within a month of
leaving office (Oxford Classical Dictionary; Aristotle, *Ath. Pol.*) [snippet-only]. No
exceptions, no suspicion required: being examined implied nothing, because everyone was.
Venice attacked the other half of the problem. Its 1268 doge-election protocol ran ten
alternating rounds of lot and vote (30→9→40→12→25→9→45→11→41), with the blind draws
performed by the ballotino — a boy picked at random off the street — and it ran
essentially unchanged for 529 years, until the Republic fell in 1797 [snippet-only].

Two distinct controls hide in those stories, and this skill installs both:
(a) **universality** — review happens to everything by schedule, so selection carries no
accusation and evasion cannot target the trigger; (b) **verifiable randomness,
interleaved** — who reviews, and what gets reviewed, is drawn by a lot nobody can steer,
so capturing the process means corrupting the whole pool rather than one known
gatekeeper.

## When to use
- Whatever flows through your process — approvals, changes, expense lines, filings,
  closed tickets, drafted contracts — gets checked either never, or only when someone
  is already suspected, so being checked reads as an accusation.
- People have learned which items get looked at, and quality follows the spotlight:
  "they know which ones get reviewed" is the tell.
- The same person always checks the same colleague's work — a standing pair that
  familiarity, friendship, or fatigue will eventually hollow out.
- A role transition is coming and you want the departing person's items examined
  without it reading as distrust — or you want that to be true for *every* departure.
- The selection mechanism itself must be beyond argument: nobody, including the person
  running the draw, can steer what comes up.
- Not for: generalizing from the drawn items to a population error rate → see
  `data-analytics-bi-skills:statistical-inference`. The seam: that skill owns sampling
  theory — confidence intervals, test choice, power; this skill designs the *governance
  draw* — who reviews, what is drawable, and why nobody can rig it. Use both when you
  also want inference from what the draw finds.
- Not for: what to look for *inside* a drawn item → the domain skill that owns the
  item's subject matter; this skill decides what gets drawn and by whom, never what a
  finding is.
- Not for: rehearsing against an adaptive adversary → see
  `decision-science-skills:tabletop-wargaming`; sortition is selection design, not
  adversarial testing.
- Not for: designing the control architecture around a hazard → see
  the archived `safety-and-reliability-skills:bowtie-barrier-analysis`; a sortition draw is one
  barrier that skill might place, not the map.

## Do it
Verifiable-lot mechanics, the universality-floor design, reviewer-rotation patterns,
the handover-review default, the assistant-first-pass protocol, and a worked example
are in `references/sortition-method.md`.

1. **Define the population.** Name the unit that flows through the process — an
   approval, a change, an expense line, a filing, a closed ticket — and the boundary
   (period, team, system). Everything in the boundary must be enumerable: a numbered
   list a draw can point into. If items can exist off-list, fix that first; an
   unenumerated item is an exempt item.
2. **Set the universal floor: everything is eligible, nothing is exempt.** Exemptions
   are the vulnerability — every carve-out ("too small," "too senior," "already
   approved twice") becomes the channel through which gaming flows, because evaders
   route to wherever the draw cannot reach. Seniority is the test case: euthynai bound
   the generals precisely because unreviewable office is where capture starts
   [snippet-only].
3. **Draw by verifiable lot.** The draw itself must be un-steerable and provably so.
   Simple mechanics that work: dice rolled in the open at a standing meeting; a seed
   committed in advance (write it down, hash it, or email it before the period closes)
   fed to a *pinned* formula; or index by an external value nobody controls, such as
   the hash of tomorrow's publicly posted number. Pin the formula, not just the seed —
   "seed the standard random generator" is not reproducible across tools, so the
   reference gives a hash-rank draw (`rank = SHA256("<seed>|<item id>")`, sort, take
   the first N) that a verifier can re-run in a shell, plus its weighted-ticket variant
   for stratified odds. The test: could the person running the draw have chosen the
   outcome, and could anyone else tell? If either answer is wrong, redesign.
4. **Rotate who reviews, by lot too.** Draw reviewer pairs from the qualified pool the
   same way you draw items, and bar permanent reviewer-reviewee pairs. Venice's
   interleaved rounds are the model: randomness at *multiple stages* means capturing
   the outcome requires corrupting the pool, not befriending a gatekeeper
   [snippet-only].
5. **Make end-of-role handover review the default.** The euthynai move: every role
   transition — departure, promotion, rotation — gets its accounting, scheduled by the
   transition itself, not by anyone's decision. Because it is universal, it carries no
   stigma; the person who leaves cleanly is *served* by the record it produces.
6. **Size the draw to real attention — let the assistant carry the volume.** Random
   selection historically died of workload: nobody genuinely examines thirty drawn
   items a month, so the draw shrank until it was theater. The assistant does the
   first pass on *every* drawn item — pulls the record, checks it against the stated
   policy, drafts findings with the evidence attached — and the human adjudicates.
   Discipline: the assistant drafts findings; the human owns every judgment. A finding
   no human has adjudicated is not a finding.
7. **Publish the rule, never the draw.** Everyone should know the population, the
   floor, the odds, and the mechanics — that knowledge is the deterrent, because it
   makes every item potentially examined. Nobody learns which items came up, or when
   the next draw lands, before it happens. Announce the system loudly; keep the
   selections quiet until done.

## Why / learn
Targeted review has two structural failures that no diligence fixes. First, targeting
leaks: whatever rule decides "which ones get looked at" is learnable, and once learned,
effort migrates to wherever the rule doesn't reach — quality follows the spotlight and
the dark corners rot. Second, targeting accuses: if being selected implies suspicion,
selection becomes politically expensive, so it happens rarely, late, and mostly to the
weak. Universality dissolves both at once. When everything is eligible and the schedule
is fixed, there is no rule to learn and no inference to draw from being picked — the
Athenians could examine their most powerful officials *routinely* because the routine
implied nothing [snippet-only].

Randomness solves a different problem: capture. A known reviewer or a predictable
selection is a single point of purchase — one relationship, one bribe, one friendship,
and the control is hollow while its paperwork continues. A verifiable lot has no one to
befriend. Venice interleaved lot and vote ten times not from mysticism but from
arithmetic: each random stage multiplies the number of people a fixer would have to own,
until owning them all is harder than just being electable [snippet-only]. The lot's
verifiability matters as much as its randomness — a draw performed in the dark is just a
gatekeeper with dice-themed stationery, which is why the ballotino drew blind and in
public.

The two controls also protect the *reviewed*. A clean record produced by a process
nobody could steer is worth something — to the departing employee, the promoted manager,
the vendor whose invoices keep coming up clean. That is the quiet reason end-of-term
accounting survived in Athens for generations: it manufactured legitimacy, not just
deterrence.

The economics changed recently and the design should notice. Universality was always
correct and always unaffordable — the reason real programs quietly shrank to theater.
An assistant that first-passes every drawn item makes the honest version affordable for
a two-person office: the draw can be sized to what deters, not to what exhausts, so
long as the human adjudication gate stays absolute.

## Common mistakes
- Exempting small, senior, or "already-checked" items → exemptions are where gaming
  routes; the floor is only a floor if the generals are under it.
- A draw the operator could steer → pre-commit the seed or roll in the open; if the
  person drawing could have picked the outcome, it is selection with extra steps.
- Publishing the draw results in advance, or leaking the schedule → publish the rule
  and the odds; keep individual selections quiet until the examination is done.
- Permanent reviewer-reviewee pairs → rotate reviewers by lot; familiarity is capture
  on an installment plan.
- Sizing the draw to look thorough rather than to available attention → thirty
  unexamined items deter less than five genuinely examined ones; let the assistant
  carry volume, and let the human gate set the count.
- Letting the assistant's first-pass findings stand unadjudicated → the draft is
  evidence-gathering; a human owns every judgment, or the control's legitimacy
  inverts.
- Treating selection as inference → "we drew 10 and found 2 issues" needs
  `data-analytics-bi-skills:statistical-inference` before it becomes a population
  claim.
- Reserving review-by-lot for suspects → the moment selection follows suspicion, it
  accuses again, and the universality dividend is gone.

## Tailor to your environment
Record your standing draw in `references/your-environment.md`: the population
definition and where it is enumerated, the floor statement (and the exemptions you
refused), the lot mechanics and where the seed commitment lives, the reviewer pool and
rotation rule, the handover-review default, and the draw size with its rationale. Keep
the committed file structural — mechanisms and roles, not names or live identifiers.
Real names, system paths, and anything sensitive belong in
`your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/sortition-review.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/sortition-method.md — the two controls with their documented mechanics
  (euthynai, the Venice protocol), verifiable-lot designs, universality-floor design
  and the exemption vulnerability, reviewer-rotation patterns, the handover-review
  default, the assistant-first-pass protocol with the human-adjudication gate, and a
  worked domain-neutral example
- references/your-environment.md — your population, floor, lot mechanics, reviewer
  pool, and draw size (sanitized stub; sensitive detail goes in the `.private.md` twin)
