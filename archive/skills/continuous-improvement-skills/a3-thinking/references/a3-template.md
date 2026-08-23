# The A3 method: layout, box-by-box guidance, worked example

Method lineage: the A3 grew inside Toyota as the standard one-page carrier for
problem-solving proposals and status, and was codified for English-speaking readers by
Durward Sobek II & Art Smalley (*Understanding A3 Thinking*, 2008) and John Shook
(*Managing to Learn*, 2008, Lean Enterprise Institute). The underlying cycle is
Shewhart/Deming PDCA. Nothing in this file is a research claim; the worked example's
numbers are illustrative.

## Contents
- [The one-page layout](#the-one-page-layout)
- [PDCA mapping](#pdca-mapping)
- [Box-by-box guidance](#box-by-box-guidance)
- [Worked example — slow assignment of incoming requests](#worked-example--slow-assignment-of-incoming-requests)
- [Reading an A3 as a reviewer](#reading-an-a3-as-a-reviewer)
- [Nemawashi and the review ritual](#nemawashi-and-the-review-ritual)
- [Canon and misattribution notes](#canon-and-misattribution-notes)
- [Drafting notes](#drafting-notes)

## The one-page layout

The classic left-to-right A3, read as a left column (top→bottom) then a right column. Keep
it to a single page — the constraint is the thinking discipline.

```
┌───────────────────────────── TITLE: <the problem, in a few words> ───────────────────────────────┐
│  Owner: <…>   Date/version: <…>   Sponsor: <…>                                                     │
├──────────────────────────── LEFT (Plan) ──────────────┬──────────── RIGHT (Do / Check / Act) ─────┤
│ 1. Background (why this matters to the customer/biz)   │ 5. Countermeasures                        │
│                                                        │    - each traces to a cause in box 4      │
│ 2. Current condition  [DATA + a small visual]          │                                           │
│    - facts from the gemba, not impressions             │ 6. Implementation plan  (Do)              │
│                                                        │    | action | owner | by when | status |  │
│ 3. Goal / target condition                             │                                           │
│    - measurable target + date                          │ 7. Follow-up (Check → Act)                │
│                                                        │    - measure & date to confirm target     │
│ 4. Root-cause analysis                                 │    - actual result (fill in later)        │
│    - 5 Whys / fishbone, verified                       │    - standardize the win, or adjust &     │
│    - countermeasures must follow from here             │      cycle again                          │
└────────────────────────────────────────────────────────┴───────────────────────────────────────────┘
```

## PDCA mapping
- **Plan** — boxes 1–5: understand the problem with data, set a target, find the verified
  cause, and design countermeasures that answer that cause.
- **Do** — box 6: implement the plan (often piloted first).
- **Check** — box 7: measure the actual result against the target on the stated date.
- **Act** — box 7: if it hit, standardize it (see `continuous-improvement-skills:standard-work`);
  if not, adjust and run the loop again.

## Box-by-box guidance

**1. Background.** One or two sentences that make a reader outside the team care: who is
affected, what it costs (time, money, risk, trust), and why now. Quality test: could a new
manager read only this box and correctly say why the page exists?

**2. Current condition.** The persuading box. Facts observed where the work happens, plus a
small visual — a run of weekly counts, a simple sketch of the process with the problem step
circled, a two-column before/after. Prefer robust summaries on skewed data (median wait, not
mean). Quality test: no opinions, no causes, no proposals — only what *is*, with magnitude.

**3. Goal / target condition.** One measurable target with a date: "reduce X from a to b by
<date>." If several metrics matter, pick the primary one and let the others ride as guard
rails. Quality test: on the follow-up date, a neutral party could say hit/miss without debate.

**4. Root-cause analysis.** The chain from gap to cause — 5 Whys, a fishbone across
categories, or a Pareto that isolates the vital few — with the cause *verified* (turn it on
and off, or show it present in failing cases and absent in passing ones). Quality test: a
skeptic can walk background → current condition → this box without a leap of faith.

**5. Countermeasures.** One line per countermeasure, each naming the cause it counters.
Fewer, targeted changes beat a shotgun list. Quality test: draw an arrow from every
countermeasure to a cause in box 4; an arrow with no target means the item is a pet
solution and gets cut.

**6. Implementation plan.** A table: action, single owner, due date, status. Pilots first
where reversibility is cheap. Quality test: every row has one name (not a team) and a date.

**7. Follow-up.** Written at kickoff as a *promise*: the measure, the date, who checks.
Completed later with the *actual* result, what was learned, and the Act decision —
standardize, adjust and cycle, or abandon with reasons. Quality test: the box has blank
space at proposal time. A fully "done" box 7 on day one means the A3 is theater.

## Worked example — slow assignment of incoming requests

Domain-neutral on purpose: the "requests" below could be legal-intake matters, ops tickets,
analyst data requests, or bug reports. **All numbers are illustrative.**

- **Title:** Incoming requests sit unassigned too long. Owner: R. Alvarez. Sponsor: team lead.
- **1. Background.** Requesters escalate by email when nothing happens after submission;
  two internal customers raised it this quarter. Escalations consume senior attention and
  erode trust in the intake channel.
- **2. Current condition.** Last quarter: 412 requests. Median time from submission to
  assignment: 3.2 business days; 90th percentile: 9 days. Hand-sketch of the intake flow
  shows one triage step owned by a single person, batched twice weekly. (Median used —
  the distribution is right-skewed by a few 3-week outliers.)
- **3. Goal.** Median submission-to-assignment ≤ 1 business day, 90th percentile ≤ 3, by
  end of next quarter.
- **4. Root-cause analysis (5 Whys, verified).** Assignment waits → triage runs in batches →
  only one person can triage → triage requires knowing everyone's specialty and load →
  that knowledge lives in one head, undocumented. Verified: in the two weeks the triager
  was out, median rose to 6.1 days; a one-page routing guide drafted as a test let a
  colleague triage 20 sample requests with 19/20 matching the expert's routing.
- **5. Countermeasures.** (a) Routing guide capturing specialty/load rules → counters
  "knowledge in one head." (b) Daily 15-minute triage slot instead of twice-weekly batch →
  counters "batched triage." (c) Second trained triager → counters "single person."
- **6. Implementation plan.** Guide drafted (Alvarez, by the 15th); daily slot on calendar
  (team lead, by the 8th); backup triager trained and solo for one week (Kim, by the 30th).
- **7. Follow-up.** Re-pull the same metrics for the following quarter on its first Friday;
  check with both escalating customers. *Actual result — to be completed.* If hit: the
  routing guide becomes standard work with a review date. If missed: re-examine whether
  batching, not knowledge, was the binding cause.

Note what the one-page constraint did: no history of the team, no tool evaluation, no
org-chart commentary — only the chain a skeptic needs.

## Reading an A3 as a reviewer

Walk the page left to right and test the joints, not the boxes:
1. Does box 2's data make box 3's target meaningful (same metric, same population)?
2. Does box 4's chain start from box 2's facts, and was the cause *verified* or asserted?
3. Does every box 5 item answer a box 4 cause? Anything answering no cause is a pet solution.
4. Does box 6 name one owner and one date per action?
5. Is box 7 a checkable promise — measure, date, checker — with room for the actual result?

Coaching style per Shook: the reviewer asks questions ("how do you know?", "what did you
see?") rather than dictating answers — the A3 is how the owner learns to think, not how the
reviewer shows they already can.

## Nemawashi and the review ritual

Nemawashi — literally "going around the roots" to prepare a tree for transplanting — is the
practice of building consensus one conversation at a time *before* the formal decision
meeting. With an A3: take the draft to each person whose work the change touches, ask what
the page gets wrong, and revise. Objections surface cheaply, in private, while the document
is visibly a draft. By the review meeting, the decision confirms an agreement that already
exists. An A3 unveiled finished at a meeting invites objections at the most expensive
possible moment and reads as a conclusion to accept rather than reasoning to join.

## Canon and misattribution notes

- **The name** is the ISO paper size (roughly 11 × 17 in / 297 × 420 mm) — the discipline is
  "one sheet," not anything magical about the dimensions.
- **The fax-machine story** ("Toyota picked A3 because it was the largest page a fax could
  send") is widely repeated lore with poor sourcing. Retell it as lore, not history.
- **PDCA attribution:** Deming credited the cycle to Shewhart, and later taught PDSA —
  "Study" rather than "Check" — arguing analysis of results deserved more than a checkmark.
  Presenting PDCA as a Toyota invention is a common misattribution.
- **A3 ≠ template.** Sobek & Smalley's core argument is that the A3 is a thinking process
  an organization practices; buying the form without the dialogue produces paperwork.
  Toyota itself uses several A3 variants (problem-solving, proposal, status) — box layouts
  vary; the left-to-right logic chain is the invariant.

## Drafting notes
- Fill boxes 1–6 to launch; leave box 7's *actual result* blank and return to complete it.
  The A3 is a living record of a learning loop, not a proposal frozen at kickoff.
- Test the logic left-to-right before sharing: does the current condition justify the
  target? Does the analysis justify each countermeasure? Cut anything that answers no cause.
- Draft it *with* the people affected — the conversation the A3 forces is most of its value.
- Handwritten-rough beats polished-wrong: a pencil draft invites correction; a designed
  slide invites approval. Polish last, if at all.
