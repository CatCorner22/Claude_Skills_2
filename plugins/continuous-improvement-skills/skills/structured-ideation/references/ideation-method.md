# The structured-ideation method: session plan, brainwriting, prompts, convergence

Method lineage: Osborn's original brainstorming rules (defer judgment, quantity, wildness,
build on others); Diehl & Stroebe's experimental work on production blocking and evaluation
apprehension, with nominal groups outperforming interacting groups; brainwriting 6-3-5 in the
Rohrbach lineage; SCAMPER as Eberle's mnemonic organizing Osborn's idea-spurring questions.

## Contents
- [The session plan](#the-session-plan)
- [Brainwriting mechanics and variants](#brainwriting-mechanics-and-variants)
- [SCAMPER prompt bank](#scamper-prompt-bank)
- [Constraint-injection patterns](#constraint-injection-patterns)
- [The LLM's three roles](#the-llms-three-roles)
- [Convergence protocols](#convergence-protocols)
- [Worked criteria matrix](#worked-criteria-matrix)

## The session plan

A 60–90 minute template. Times scale down for solo work, up for large rooms.

| Phase | Time | What happens |
|---|---|---|
| Frame | 5–10 min | Present the "How might we…" question, the ground rules, and the quantity target. State the phase boundary: no evaluation until convergence begins. |
| Diverge 1 | 25–30 min | Brainwriting rounds (6-3-5 or a variant). Silent, simultaneous, sheets rotating. |
| Re-energize | 10 min | When output thins: SCAMPER pass over existing ideas, a constraint injection, or an LLM wild-card round. |
| Pool + anonymize | 5–10 min | All ideas collected, deduplicated, shuffled, authorship stripped (the LLM does this well). Read the flat list once, clarifications only — no critiques. |
| Converge | 15–25 min | Dot-vote pre-filter to a shortlist (~6–10 ideas), then effort/impact placement or a weighted criteria matrix. |
| Dispose | 5 min | Owner + next step for each survivor; parking lot for the rest; log the whole pool. |

Framing the question well is half the session. Good frames are single, concrete, and open:
"How might we cut the time from statement arrival to first reconciliation pass?" Bad frames are
compound ("…and also improve morale"), pre-solved ("how do we get tool X approved"), or so broad
no idea can miss ("how do we improve the department").

## Brainwriting mechanics and variants

**Classic 6-3-5.** Six participants, one sheet each with a 3-column × 6-row grid. Each round:
write three ideas in five minutes, silently; pass the sheet left; read what you received; next
round, build on those ideas or add new ones. Six rounds ≈ 30 minutes ≈ up to 108 idea slots.
The numbers are conventions, not physics — what carries the effect is **silent** (no evaluation
audience), **simultaneous** (no waiting for the floor), and **rotation** (building on others).

**Variants.**
- **Brainwriting pool:** instead of fixed rotation, finished sheets go to a central pool; take a
  different sheet whenever you stall. Better for uneven writing speeds.
- **Fewer than six people:** run more rounds, or let the LLM hold the empty seats — it writes
  three ideas per round onto the rotating sheet like any participant.
- **Solo:** run timed rounds against yourself — three ideas per five minutes, then a SCAMPER or
  constraint pass over your own list, then another round. Alternate with LLM rounds so someone
  else's ideas still arrive on your "sheet".
- **Remote/async:** a shared document with one section per participant, a round timer, and
  section rotation; or fully async over a day with three scheduled visits. Anonymity is easier
  remotely — collect into a form the LLM pools and shuffles.
- **Question storming:** a divergence round that generates *questions* about the problem instead
  of answers — useful when the frame itself is suspect.

## SCAMPER prompt bank

Run SCAMPER over an existing idea, the current process, or the problem statement. Two to four
prompts per letter; pick a handful, don't march through all of them.

- **Substitute:** What component, step, material, data source, or person could be swapped? What
  if another team's method replaced ours? What rule could a different rule replace?
- **Combine:** Which two ideas on the sheet merge into a stronger one? What could this be bundled
  with so it rides an existing process? Which steps could happen in one pass?
- **Adapt:** Where has a similar problem been solved (another industry, another era)? What would
  the best-run version of this look like elsewhere, adapted here?
- **Modify / Magnify / Minify:** What if it were 10× bigger, 10× faster, one-tenth the size?
  What if the rare case were the common case? Exaggerate a feature until it becomes the idea.
- **Put to other uses:** Who else could use this output? What existing byproduct or report has
  a second life? What could this process do in its idle time?
- **Eliminate:** What step, approval, field, or report disappears entirely? What is done only
  because it has always been done? What is the simplest version that still works?
- **Reverse / Rearrange:** What if the sequence flipped — pay before approve, check after ship?
  What if the customer did this step, or we did theirs? What is the opposite of the current
  approach, taken seriously for five minutes?

## Constraint-injection patterns

Inject one when a round comes back thin. Constraints work because a blank page gives the mind
nothing to push against; a hard constraint forces a new region of the option space.

- **Extreme budget:** solve it with zero money; solve it with unlimited money — then extract the
  transferable part of each.
- **Extreme deadline:** what would we do if it had to work by Friday? Ten years from now?
- **Remove the default:** the current tool/system/vendor is unavailable — now what?
- **Persona shift:** how would an airline ops team handle this? An ER triage nurse? A street
  market vendor? (Pick personas with real operational analogies, then translate.)
- **Forced analogy:** name a random distant domain and force three mappings from it — the LLM is
  strong here precisely because it holds many domains at once.
- **Scale shift:** solve it for one transaction; solve it for a million; look at what changed.
- **Inversion:** list ways to guarantee failure, then negate each (a light version of what
  `decision-science-skills:pre-mortem` does with full protocol for plans).

## The LLM's three roles

1. **Anonymity engine.** Paste or forward every raw idea; the LLM deduplicates near-duplicates
   (flagging merges rather than silently deleting), shuffles order, strips names, and returns a
   numbered flat list for evaluation. Keep the original attributed pool in the log so credit can
   be given *after* selection — anonymity is for judging, not for erasing credit.
2. **Fatigue-proof partner.** When humans stall at idea twelve, ask for ten more — but seed the
   request: "ten ideas that assume zero budget", "ten that eliminate a step rather than add
   one", "ten a competitor would gladly see us not think of". Unseeded requests return the
   plausible middle.
3. **Wild-card generator.** Ask for analogies from named distant domains and force the mapping:
   "How do container ports handle surge arrival? Map three of those mechanisms onto our intake
   queue." Discard freely — wild cards are cheap and only one needs to land.

## Convergence protocols

Converge in stages, coarse to fine, criteria before scores.

1. **Clarify, don't defend.** One pass through the anonymized list for meaning only. Authors
   stay silent unless asked a factual question.
2. **Dot-vote pre-filter.** Each person gets ~N/5 dots for N ideas, placed freely. Take the top
   ~6–10 into the shortlist. Dots measure *resonance* — good for cutting a long tail, unsafe
   for deciding, because they hide criteria and follow the room's mood.
3. **Effort/impact matrix** (fast, visual): place each shortlisted idea on a 2×2 of
   implementation effort vs expected impact. Quick wins (low effort, high impact) get owners
   now; big bets (high/high) get a sponsor conversation; fill-ins (low/low) go to the parking
   lot; thankless tasks (high effort, low impact) are dropped aloud.
4. **Weighted criteria matrix** (deliberate, auditable): name 3–5 criteria and weights *before*
   scoring; score each idea 1–5 per criterion; multiply and sum. Use when the choice is
   consequential or contested — the matrix makes the disagreement specific ("we differ on
   feasibility, not on impact"), which a dot cloud never does.
5. **Disposition.** Every shortlisted idea leaves with owner + next step + date, or an explicit
   parking-lot entry. Log the full pool: today's discard is next quarter's answer.

## Worked criteria matrix

Question: "How might we cut rework in invoice processing?" Shortlist of four after dot-voting.
Criteria and weights agreed before scoring (impact weighted highest because rework is the pain;
effort scored inverted so higher = easier):

| Criterion (weight) | A: Validate at entry | B: Vendor portal | C: Dual-monitor recheck | D: Error-type Pareto first |
|---|---|---|---|---|
| Impact on rework (0.4) | 4 | 5 | 2 | 3 |
| Ease of pilot (0.3) | 4 | 1 | 5 | 5 |
| Speed to first result (0.2) | 4 | 1 | 5 | 4 |
| Low risk to current ops (0.1) | 4 | 2 | 5 | 5 |
| **Weighted total** | **4.0** | **2.7** | **3.8** | **3.7** |

Reading it: A wins on balance; B has the highest ceiling but fails every speed/effort criterion
— it becomes a sponsored big bet, not a discard; C and D are near-ties behind A, and D
(analyze error types before fixing anything) is arguably a *prerequisite* — which the matrix
surfaces for discussion. The totals start the final conversation; they don't end it. A matrix
that merely confirms the loudest voice's favorite was probably scored after the winner was
chosen — re-check the weights' paper trail.
