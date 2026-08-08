# AAR method (four questions, facilitation, timeline protocol, evidence)

## Contents
- The four questions, expanded
- Ground rules (read them aloud)
- Facilitation guide
- Timeline-reconstruction protocol (the LLM's step)
- Output record template
- Evidence and provenance (honest version)

## The four questions, expanded

1. **What was SUPPOSED to happen?**
   Restate the plan/standard as it existed *before* the event: the close checklist, the
   cutover runbook, the reconciliation SOP, the payment-approval flow. Pull the document;
   do not reconstruct it from memory — hindsight quietly rewrites intentions. If there
   was no plan, that is finding #1, recorded without irony.
2. **What ACTUALLY happened?**
   Ground truth first, interpretation later. Build the timeline (protocol below) and get
   the room to agree it is factually right before anyone explains anything. Factual
   disputes are settled by artifacts — a log line beats a recollection.
3. **WHY the difference?**
   Walk gap by gap: plan said X at 9:00, timeline shows Y at 11:40 — why? Look for
   process, information, timing, tooling, and assumption causes; treat "someone erred"
   as the start of a why-chain (what let the error through?), not the end. A defect that
   needs real causal depth leaves the AAR and becomes an RCA.
4. **What do we SUSTAIN and what do we IMPROVE?**
   Sustain: practices that worked, named specifically enough to repeat on purpose.
   Improve: changes specific enough to verify, each with an owner, a date, and a durable
   home (SOP edit, checklist line, next plan). Aim for a handful of each — ten vague
   items lose to three owned ones.

Time split: roughly 25% on Q1, 25% on Q2, 50% on Q3+Q4. Most sessions die in Q2; the
facilitator's main job is getting the room out of it with the timeline agreed.

## Ground rules (read them aloud)

- Blameless: we examine the event, not the people; systems let errors through.
- Rank-free: inside this room, the best observation wins, not the highest title.
- Everyone talks; no one is graded. There are no passing or failing AARs.
- Facts before interpretation. "Because" waits until the timeline stands.
- What is said here feeds the record's findings, not performance reviews.

## Facilitation guide

- Open with the event, the rules, and the four questions visibly posted.
- Ask the most junior or closest-to-the-work observers first in Q2 and Q3.
- Park early arrivals: blame, solutions, and tangents go to a visible lot, revisited in Q4.
- Watch for hindsight creep ("we obviously should have...") — translate it into what was
  knowable at the time.
- The LLM's facilitation role: track the live question, draft the timeline and record,
  prompt for missing voices, flag when discussion drifts off the rails. It never rules on
  fault, never scores participants, never decides which improvement "matters most" — the
  blameless norm and rank suspension are human culture that the humans own.

## Timeline-reconstruction protocol (the LLM's step)

The tedious step the LLM does best. Before the session:

1. Collect artifacts: scheduler/job logs, ERP process histories (e.g. FBDI load and
   posting jobs), ticket queues, email threads, chat exports, bank statement and portal
   timestamps, calendar invites. Sanitize before pasting anything sensitive.
2. Extract events into rows: timestamp (with timezone), actor/system, what happened,
   source artifact. One fact per row; no adjectives.
3. Order, merge, and flag conflicts (two sources disagreeing on a time or sequence) —
   conflicts are questions for the room, not editorial decisions.
4. Mark gaps explicitly ("no artifact covers 13:00–15:30") — gaps often locate the
   interesting divergence.
5. Present as a table the room can correct. The session's Q2 is a review of this draft,
   not archaeology from scratch.

| Time | Actor/system | Event (fact only) | Source |
|------|--------------|-------------------|--------|

## Output record template

- **Event / date / participants (roles):**
- **Q1 — plan as written:** (link the actual document)
- **Q2 — timeline:** (attach the agreed table)
- **Q3 — why the differences:** (gap → cause, one line each)
- **Q4 — sustain:** (practice → where it enters the standard)
- **Q4 — improve:** (change → owner → date → durable home)
- **Spawned RCAs / follow-ups:**
- **Fed to:** next plan / standard-work updates / MEMORY.md crystallization

## Evidence and provenance (honest version)

- Primary source: U.S. Army TC 25-20, *A Leader's Guide to After-Action Reviews* — the
  four questions, the blameless/rank-free norms, and the facilitation posture come from
  doctrine refined across decades of training rotations.
- Corporate adoption: Shell, BP, and GE are widely reported adopters for knowledge
  management and operations learning [snippet-only]. This is practitioner provenance —
  case reports and knowledge-management literature, not controlled trials. No randomized
  evidence shows AARs improve organizational outcomes; the honest claim is that the
  format reliably surfaces information teams otherwise suppress, at low cost.
- When a user asks "does this work?", give that two-part answer rather than borrowing
  the Army's authority for an effectiveness claim doctrine never made.
