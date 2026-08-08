---
name: pre-mortem
description: >-
  Runs Gary Klein's pre-mortem — the prospective-hindsight exercise — on a plan before
  commitment: declare that the plan has already failed outright, have every participant
  silently and independently write reasons why, round-robin the reasons until exhausted,
  rank them, and strengthen the plan against the top items with named owners. Includes a
  solo-analyst variant where the LLM generates a heterogeneous set of failure narratives
  (technical, political, data, timing) and writes each stakeholder's reason for the human
  to rank. Use before committing to an Oracle configuration change, a
  reconciliation-engine go-live, an FBDI load, a dental-app release, or any plan the team
  is about to lock in. Triggers: premortem, pre-mortem, assume it failed, what could sink
  this, before we go live, prospective hindsight.
---

# Pre-mortem (prospective hindsight)

## When to use
- A concrete plan exists, the team is briefed, and commitment is imminent — the last calm
  moment when the plan can still absorb changes cheaply.
- Before-go-live gates in this environment: Oracle CM configuration or ruleset changes,
  reconciliation-engine go-lives, FBDI conversions (pair with
  `oracle-fusion-finance-skills:fusion-fbdi-data-loading`), dental-app releases,
  bank-migration cutovers, month-start process changes.
- As the BEFORE companion to `continuous-improvement-skills:project-command-center`: that
  doctrine red-teams and logs interventions on plans under way but has no structured
  prospective-hindsight step — run the pre-mortem first, file its output there.
- Also worth running when a decision feels unanimous suspiciously fast: unanimity under
  planning momentum is often silence, not agreement, and this is the cheapest way to
  find out which.
- Not for: adversarially attacking a live plan or auditing a benchmark's validity → see
  `continuous-improvement-skills:project-command-center`. Looking BACK at what actually
  happened → see `decision-science-skills:after-action-review`. The assistant reflecting
  on its own corrections → see `metacognition-skills:reflective-learner`.

## Do it
1. **Put the plan on the table.** Everyone participating has read or been briefed on the
   actual plan — scope, dates, owners. A vague plan yields vague failures; if the plan
   cannot be stated in a paragraph, sharpen it first.
2. **Declare the failure as fact.** Say it verbatim: *"It is a year from now. We
   implemented the plan exactly as written, and it failed — a fiasco."* Certainty, not
   possibility. Do not soften it to "what might go wrong?" — the certainty framing is the
   active ingredient (see Why / learn). Fit the horizon to the plan: a year for a
   program, a quarter or a single close cycle for a cutover.
3. **Independent silent writing, 2–3 minutes.** Every participant writes their own reasons
   the plan failed — no discussion, no screens shared. Silence and independence are what
   kill anchoring and deference to the highest-paid opinion.
4. **Amplify with the LLM as a tireless failure-imaginer.** Have it generate ~20
   heterogeneous failure narratives, forced across categories — technical, data, people
   and politics, timing and external events — then bucket and deduplicate them. When the
   user is a team of one (the analyst's usual condition), have it write "each
   stakeholder's reason" in role: the AP manager, the bank contact, the DBA, the auditor.
   Ground every narrative in the real plan and process documents, not generic risk lists.
   Use the prompt list in `references/premortem-method.md`.
5. **Round-robin.** Each person (and each LLM bucket) contributes one reason per pass, no
   rebuttals, recorded verbatim, until the room is empty. Duplicates are consolidated, not
   argued.
6. **Rank — and the humans rank.** The LLM may cluster reasons and propose criteria
   (likelihood × damage × how late you'd detect it), but ordering the list and accepting
   items onto it belongs to the team; ranking encodes responsibility.
7. **Strengthen the plan against the top items.** For each: change the plan, add a
   detection tripwire, or accept the risk explicitly — and assign a named owner and date.
   A tripwire is a concrete observable with a check date ("if unreconciled lines exceed
   N by day 3, we halt and roll back"), not a resolution to stay alert. A pre-mortem
   that ends at a list changed nothing.
8. **File and connect.** Put the ranked list and mitigations where the project is
   commanded (the project-command-center watch list or go-live checklist), and set the
   after-action-review date now — pre-mortem before, AAR after, same plan.

## Why / learn
The exercise rests on a 1989 finding by Mitchell, Russo, and Pennington: *prospective
hindsight* — assuming an outcome has already occurred rather than asking whether it might —
improved people's ability to identify reasons for the outcome by roughly 30%. Klein's
pre-mortem (published in HBR, 2007) turns that lab effect into a meeting: declaring the
fiasco as fact moves participants from defending a plan to explaining a known failure,
which is a cognitively easier and more productive task. Just as important is what the
framing does socially. Planning momentum suppresses dissent — once a team has invested in
a plan, voicing doubts reads as disloyalty or obstruction — but in a pre-mortem, finding
failure reasons *is the assigned job*, so the exercise legitimizes the dissent that was
already in the room. The silent independent-writing step exists because the first idea
spoken anchors everyone after it, and because the senior voice otherwise sets the frame.
Note what the exercise is *not*: a critique session asks people to attack a colleague's
work, which carries social cost and gets softened accordingly; a pre-mortem asks them to
explain a hypothetical past in which nobody is being attacked, which is why sharper
material surfaces. The LLM earns its place as breadth, not judgment: it imagines failures
tirelessly, across categories a fatigued team skips, and it has no career risk — but
ranking and ownership stay human, because a mitigation without a responsible owner is a
wish, and because what a team ranks highest reveals what it actually fears.

## Common mistakes
- Asking "what might go wrong?" instead of declaring "it failed" → hedged brainstorming;
  the certainty framing is the mechanism, keep the script.
- Discussing before writing → anchoring and HiPPO deference; silent and independent first.
- Running it after commitment or go-live → theater; the plan can no longer absorb changes.
- Letting the LLM rank items or assign owners → it generates and clusters only; the team
  ranks and owns.
- Ending with a list and no plan change → every top item gets a change, a tripwire, or an
  explicit acceptance, each with an owner and date.
- Only technical failures imagined → force the categories: data, political, timing,
  external; use the reference prompt list.
- Inviting only the planners → the people who will operate the thing on day two (the AP
  clerk, the help desk) see failures planners cannot; include at least one.
- Three mild reasons and early consensus → the room still fears the sponsor; re-run the
  silent-writing round anonymously.
- Confusing it with adversarial challenge of a live plan → that is
  `continuous-improvement-skills:project-command-center`; this runs before commitment.

## Tailor to your environment
Record in `references/your-environment.md`: the go-live gates that should always get a
pre-mortem, your stakeholder roster for the solo role-play variant, a sanitized catalog of
past failures (your best category prompts), and where ranked outputs get filed. If real
incidents, vendors, or people must be named, use `your-environment.private.md` — that
suffix is git-ignored. Never commit real client or bank data.

## References
- references/premortem-method.md — facilitation script, solo-analyst variant,
  failure-category prompt list, and the evidence base
- references/your-environment.md — your gates, roster, and filing conventions (fill in)
