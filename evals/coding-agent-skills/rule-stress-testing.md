# Evals — coding-agent-skills:rule-stress-testing

## 1. Positive trigger (should load the skill)
> "Here's our CLAUDE.md plus the house git rules — stress test the rules. I want a
> loophole hunt before we let more agents push to the shared branch: where do these
> rules conflict, where do they go silent, and where does following them to the letter
> hurt us?"

Expected: loads the Asimov pass; inventories the rules verbatim with sources and asks
for (or flags the absence of) intended precedence as finding #1; extracts load-bearing
undefined terms with widening and capture risks; runs all six modes with one concrete
collision story per hit (and a one-line verdict for modes with no hit); runs the
Goodhart pass on every rule referencing a measure and the malicious-compliance pass on
the set as a whole; classifies every finding as conflict, gap, or perverse
instantiation; proposes fixes in the legal-canon vocabulary (explicit
specific-over-general precedence, term definitions with a named adjudicator, rule
repair); then re-tests the fixed set and logs residual open items.

## 2. Near-miss (prompt-commission guard)
> "Engineer me a production-grade system prompt for our support agent — lock the
> parameters first, then red-team it and deliver the blueprint and final prompt in one
> code block."

Expected: `coding-agent-skills:master-prompt-architect` owns commissioning and
adversarially auditing a prompt under construction, including its clarify-first gate
and triple audit. rule-stress-testing owns collision discovery inside an EXISTING rule
set; if it loads on a build-me-a-prompt ask, the seam is failing.

## 2b. Near-miss (process-failure guard)
> "Rank what could go wrong in our reconciliation process — severity, occurrence,
> detection — so we know what to test hardest before go-live."

Expected: `continuous-improvement-skills:fmea` owns failure-mode analysis and ranking
of a process or design. rule-stress-testing is not about how a process fails but about
where written rules fight each other, fall silent, or reward the letter over the
spirit; a severity/occurrence/detection ask should not load it.

## 3. Quality rubric
- **Does**: verbatim numbered rule inventory with owners; unstated precedence surfaced
  as a finding in itself; undefined-term drill with narrow/wide readings and who
  benefits from each; all six modes run with concrete situation stories, not abstract
  labels; Goodhart pass tied to specific measures in the rules; malicious-compliance
  pass framed as drafting diagnosis, not accusation; findings classified
  (conflict/gap/perverse instantiation) with the smallest sufficient fix each; the
  fixed set re-tested and new collisions from the fixes themselves reported.
- **Teaches**: why generation beats read-through (property-based testing — state the
  invariant, hunt the counterexample); why each story is a minimal reproduction case of
  one failure mode; Goodhart's Law and the specification-gaming lineage as the
  measure-rule risk; work-to-rule as the documented human form of letter-over-spirit;
  the legal canons as centuries-old fix vocabulary, with later-over-earlier anchored to
  statutes and flagged weaker for contracts; why fixes breed new conflicts (the
  Zeroth-Law lesson).
- **Stays honest**: the Three Laws cited as fiction that catalogs failure modes, never
  as an engineering standard, with the EPSRC/AHRC set-aside noted; the First Law always
  quoted with its inaction clause; "fail in interesting ways" flagged as commentary and
  Asimov's real ambiguity quote used instead; the thinner-sourced exhibits ("That Thou
  Art Mindful of Him," *The Naked Sun*) presented with their provenance caveats; no
  invented statistics; findings never framed as accusations against named colleagues.
