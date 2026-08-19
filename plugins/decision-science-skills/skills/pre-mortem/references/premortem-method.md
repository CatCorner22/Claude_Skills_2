# Pre-mortem method (facilitation script, solo variant, prompts, evidence)

## Contents
- Facilitation script (team version)
- Solo-analyst variant (LLM-amplified)
- Failure-category prompt list
- Ranking and mitigation worksheet
- Evidence base (and its honest limits)

## Facilitation script (team version)

Total time: 35–45 minutes. Works with 3–12 people who know the plan.

1. **Set-up (5 min).** Restate the plan in one paragraph: what ships, when, who owns it.
   Confirm everyone recognizes that statement as *the* plan.
2. **The declaration (say it verbatim).**
   > "It is a year from now. We implemented the plan exactly as written, and it failed —
   > a fiasco. Take two to three minutes and write down every reason you can think of
   > for why it failed."
   Do not say "might fail," "could fail," or "what are the risks." Failure is a fact in
   this room; participants are explaining it, not predicting it.
3. **Silent writing (2–3 min).** No talking, no shared screens, no peeking. Everyone
   writes their own list — including the facilitator and the most senior person present.
4. **Round-robin (10–15 min).** Go around the room; each person reads ONE reason per
   pass. Record each verbatim on a shared list. No rebuttals, no "that can't happen,"
   no solutioning yet. Continue passes until everyone says "pass."
5. **Consolidate and rank (10 min).** Merge duplicates. Rank the list on three dimensions —
   damage, likelihood, and how late you would detect it — ordered by **dominance rather than
   multiplied into a single score**. Take damage first and break ties within a band by the
   other two. Do not compute damage × likelihood × lateness: a severity-9 item that is rare
   (2) and detectable (3) scores 54, while a severity-3 nuisance that is common (6) and
   invisible (6) scores 108, so the product ranks the near-catastrophe *below* the nuisance.
   `continuous-improvement-skills:fmea` documents that failure and the severity ceiling that
   blocks it. The team ranks; a facilitator or LLM may cluster and propose, never decide.
6. **Strengthen (10 min).** For each of the top 3–7 items decide: change the plan, add a
   detection tripwire, or accept explicitly. Assign a named owner and a date to each.
7. **Close.** File the output with the plan; schedule the after-action review now.

Facilitation notes: keep the tone matter-of-fact, not gleeful or gloomy; thank
contributors for damaging reasons — the exercise exists to make those speakable; if a
senior person starts evaluating reasons mid-round, restate rule 4.

## Solo-analyst variant (LLM-amplified)

When you are a team of one, the LLM substitutes for the missing room — for breadth, not
for judgment.

1. Paste the actual plan (sanitized) and the real process documents it touches.
2. Declare the fiasco exactly as in the team script.
3. Ask the LLM for ~20 failure narratives, **forced across the categories below** — a
   specific story each ("the bulk load finished clean but every row landed in the prior
   period, so the first anyone noticed was the month-end variance report"), not
   risk-register abstractions.
4. Then run the stakeholder round: "Each of the following people writes their reason the
   plan failed, in their own voice" — name your real roster (e.g. the operations lead,
   the approver, the vendor contact, the DBA, the internal auditor).
5. Have the LLM bucket and deduplicate. **You rank.** You assign owners — even if every
   owner is you, the date and tripwire still matter.
6. Anti-agreement discipline: instruct the LLM not to soften ("but this is unlikely...")
   and not to converge on your favorite risk; ask it to argue for the reason you find
   least plausible before you discard it.

## Failure-category prompt list

Force at least two narratives per category; the tired mind writes only the first one.

- **Technical:** configuration wrong or untested path; migration/load partially applied;
  interface or connectivity down at the worst hour; performance collapse at real volume;
  rollback never rehearsed and doesn't work.
- **Data:** reference fields corrupted in transit (leading zeros, encodings); duplicate
  or missing rows; period/date semantics wrong; test data passed but production data has
  the ugly 2%; a mapping nobody owned.
- **People / political:** the one person who understood it left or was out; approver
  bottleneck; a stakeholder never actually agreed and resists after go-live; training
  assumed, not done; incentives reward the old process.
- **Timing / external:** go-live collides with month-end, payroll, or an audit; bank or
  vendor changes something on their side; holiday calendars; a regulator or policy
  change lands mid-rollout.
- **Process / control:** no tripwire, so the failure ran silent for weeks; success
  declared on a demo, not the real flow; the workaround became permanent; nobody
  compared post-go-live output against the old process.

## Ranking and mitigation worksheet

| # | Failure reason (verbatim) | Category | Likelihood | Damage | Detected when? | Decision (change / tripwire / accept) | Owner | Date |
|---|---------------------------|----------|-----------|--------|----------------|----------------------------------------|-------|------|

A row is closed only when the decision column is filled and the owner has confirmed.

## Evidence base (and its honest limits)

- Mitchell, D. J., Russo, J. E., & Pennington, N. (1989), "Back to the future: Temporal
  perspective in the explanation of events": prospective hindsight — treating the
  outcome as already having happened — improved reason identification by roughly 30% in
  controlled studies. This is the lab mechanism the exercise borrows.
- Klein, G. (2007), "Performing a Project Premortem," *Harvard Business Review*: the
  meeting format above; Klein's supporting evidence is field experience with teams, not
  a controlled trial of the full ritual.
- Be honest about the seam: the ~30% figure is about *reason generation* under the
  hindsight frame, measured in the lab; the claim that the whole meeting improves plan
  outcomes is practitioner-grounded. State both when asked how strong the evidence is.
