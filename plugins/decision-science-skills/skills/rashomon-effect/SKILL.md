---
name: rashomon-effect
description: >-
  Reconciles contradictory good-faith accounts of one event (witness statements, incident
  write-ups, contested post-mortems) using Rashomon-effect scholarship and
  eyewitness-memory science: takes each account whole (cognitive-interview moves) before
  comparing, splits accounts into observations, interpretations, and stakes, maps who
  could see what from where, finds the invariant core, sorts each divergence into
  perspective, memory, or stake artifact vs genuine contradiction, weights initial
  uncontaminated statements over late rehearsed ones, adjudicates only against physical
  evidence, never confidence or seniority, and writes a reconciled account marking
  confidence, filing unresolved forks instead of dropping them. Bad faith must be earned
  with evidence. Use when accounts of one event conflict.
  Triggers: rashomon, conflicting accounts, witnesses disagree, everyone
  remembers it differently, whose story is right, reconcile the statements, contradictory
  testimony.
metadata:
  version: "1.1.0"
  source: >-
    Commissioned by the user, named for the Rashomon effect — the scholarly term (Karl G.
    Heider, American Anthropologist, 1988) that honors Kurosawa's film Rashomon (1950),
    whose testimony plot comes from Akutagawa's "In a Grove" (1922) and whose title and
    frame come from Akutagawa's "Rashōmon" (1915). Homage in triggers and teaching only;
    no affiliation. The mechanism is documented professional method: the cognitive
    interview (Fisher & Geiselman), eyewitness-memory research (Loftus; Wixted & Wells),
    triangulation (Denzin), and standard jury instructions on honest disagreement.
---

# The Rashomon effect (reconciling good-faith accounts)

Four people watched the same event; four accounts contradict each other; nobody is lying.
"The Rashomon effect" is established scholarship for exactly this: Karl G. Heider coined it
for ethnographers who studied the same culture and disagreed in good faith — divergence
traced to observer circumstances, not deceit (American Anthropologist, 1988)
[snippet-only, ×4]. The attribution behind the name is commonly garbled, so this skill
corrects it up front: Kurosawa's film takes its plot from Akutagawa's "In a Grove" (1922,
seven accounts of a samurai's death, compressed to four) and only its title and framing
from Akutagawa's "Rashōmon" (1915), which contains no testimony plot at all
[snippet-only, ×4]. The working stance here is the term's scholarly meaning: when honest
people contradict each other about one event, the contradiction is data about vantage,
memory, and stakes before it is evidence of anyone lying.

## When to use
- Witness statements, incident write-ups, or interview notes about one event contradict
  each other and you need one defensible account of what happened.
- "Everyone remembers that meeting differently" — a decision, a commitment, or a warning
  is now disputed and the participants' recollections have hardened.
- A post-mortem where the engineers disagree about the sequence of events, not just the
  cause — the timeline itself is contested.
- Not for: weighing competing hypotheses about CAUSES →
  `decision-science-skills:competing-hypotheses-analysis` — this skill reconciles
  testimonies into one account of what happened; that one weighs rival explanations of
  why. A reconciled account is often its best input.
- Not for: the structured team debrief after an event →
  `decision-science-skills:after-action-review` (four questions, sustain and improve; it
  can call this skill when its what-actually-happened step hits contradictions).
- Not for: tracing a failure's causal chain →
  `continuous-improvement-skills:root-cause-analysis`.
- Not for: the interviewing stance that gets a guarded person talking →
  `collaboration-skills:disarming-elicitation` — use it during step 1's intake when a
  witness is defensive; this skill owns what happens to the accounts afterward.

## Do it
The full protocol — intake moves, the worked outage example, the divergence table, the
adjudication rules, and the reconciled-account template — is in
`references/reconciliation-method.md`.

1. **Collect each account whole, separately, before any comparison.** No interruptions,
   no challenges, no showing one witness another's version — every account someone hears
   before giving their own contaminates theirs. Use the cognitive-interview moves
   (Fisher & Geiselman): ask for everything including "irrelevant" detail, reinstate
   context (where were you, what were you doing, what was on screen), and for honest
   witnesses ask for a changed-order retelling. Record each account's vantage point with
   it: where the person was, physically and organizationally.
2. **Split every account into three layers.** OBSERVATIONS — what they directly saw,
   heard, or read, with the vantage attached. INTERPRETATIONS — what they concluded from
   it. STAKES — what this version of events protects: reputation, a decision they made, a
   team they lead. Everyone's account is self-flattering before it is false; naming the
   stake is not an accusation, it is calibration.
3. **Map the vantage points.** Who could actually see what, from where — seating,
   dashboards, channels, meetings attended, access held. Many "contradictions" dissolve
   here: two people looking at different layers of one system both told the truth.
4. **Find the invariant core.** List what every account agrees on. It is almost always
   more than the conflict suggests, and it becomes the fixed frame the divergences hang
   from — and the standard genuine contradictions get tested against.
5. **Classify each divergence** (table in the reference): a PERSPECTIVE artifact (both
   true from different vantages), a MEMORY artifact (post-event contamination, delay,
   stress — name the mechanism: misinformation effect, leading questions, retellings), a
   STAKE artifact (self-flattering shading of the same facts), or a GENUINE contradiction
   (the versions cannot both be true). Only the last kind needs adjudication.
6. **Weight statements by contamination, not confidence.** An initial, uncontaminated
   account given promptly to a neutral asker carries more weight than a late one shaped
   by delay, group discussion, repeated questioning, or knowing what the "right" answer
   is — the Wixted & Wells nuance, stated with its conditions: initial confidence at a
   first clean identification is substantially diagnostic; that relationship degrades as
   the contaminants pile up [snippet-only, ×3].
7. **Adjudicate only the genuine contradictions.** Test them against physical evidence —
   logs, timestamps, recordings, documents — or against the invariant core. Confidence,
   seniority, eloquence, and majority vote are not evidence: three people who compared
   notes in a hallway are one contaminated source, not three.
8. **Write the reconciled account with honest seams.** Mark each element's confidence
   level (corroborated / single-vantage / inferred), and file every unresolved fork
   explicitly — the dissenting version stated at full strength alongside what evidence
   would close the fork. Unresolved forks are filed the way a scenario cell files its
   dissenting future (`decision-science-skills:minority-report` is the filing
   discipline): never silently dropped to make the story smooth.

## Why / learn
The memory science explains why good-faith accounts diverge and why the protocol is
ordered the way it is. Loftus's misinformation effect shows that information encountered
after an event alters the memory of the event itself; in Loftus & Palmer's study, the verb
in the question ("smashed" vs "hit") changed witnesses' speed estimates and produced false
memories of broken glass [snippet-only, ×3-4]. That is why intake comes before comparison,
why questions stay neutral, and why a late account that has been discussed and re-asked is
weighted below an early clean one — every retelling and every hallway comparison is a dose
of post-event information. It is also why confidence is not the tiebreaker: confidence and
accuracy correlate poorly in general, and jurors are known to overweight confidence
anyway [snippet-only, ×3] — with the honest nuance that initial confidence, captured clean
and early, is substantially diagnostic before contamination erodes it (Wixted & Wells)
[snippet-only, ×3]. The cognitive interview earns its place in step 1 the same way:
report-everything, context reinstatement, and changed-order retelling yield on the order
of 40%+ more correct details at comparable accuracy than standard questioning
[snippet-only, ×4].

The reconciliation logic is triangulation: Denzin's four types — data, investigator,
theory, method [snippet-only, ×4] — say convergence from independent vantages is the
strongest warrant available, which is exactly what the invariant core operationalizes. And
the law reached the same conclusions from centuries of witnesses: standard jury
instructions tell jurors that witnesses may honestly differ, that "innocent
misrecollection is not an uncommon experience," and that discrepancies should be weighed
as important-vs-trivial and innocent-vs-intentional, with vantage, stress, and the limits
of perception all recognized [snippet-only, ×4] — the divergence classification in step 5
is that instruction turned into a procedure.

The film contributes a warning about misreading, not a license for nihilism. Rashomon does
not say "there is no truth": Kurosawa's own framing of the film is about people unable to
be honest with themselves, embellishing self-servingly (direction well-supported at claim
level [snippet-only, ×3]; exact wording not verified here). Each account in the film is
self-flattering — even the woodcutter's supposedly objective version is compromised by
the dagger he took — and the ending is moral restoration, not despair. Hence the two rails
this skill runs on: stakes shade every account, including the "neutral" one; and good
faith stays the default hypothesis, because that is what the term names
[snippet-only, ×2] — bad faith is a conclusion you earn with evidence, not a starting
assumption.

## Common mistakes
- Letting witnesses compare notes before intake → hallway comparison is post-event
  contamination; collect whole accounts separately first, then compare on paper.
- Asking leading questions ("how fast was it going when it smashed into…") → the verb
  plants the answer; ask neutral open questions and let report-everything do the work.
- Treating confidence as accuracy → weight by contamination history instead; a hesitant
  early account can outrank a confident late one.
- Adjudicating by seniority → seniority is a stake, not a vantage; test contradictions
  against logs and invariants.
- Reading every divergence as a lie → most divergences are perspective or memory
  artifacts; the term names good-faith divergence, and accusation-first analysis makes
  witnesses defensive and accounts worse.
- Counting three matching accounts as three sources → if they discussed it, they are one
  source; independence is what makes convergence evidence.
- Smoothing the reconciled account into one clean story → a dropped dissenting detail is
  the namesake failure; file unresolved forks at full strength with what would close them.
- Citing the film as "proof there is no truth" → misreading; the film is about
  self-serving embellishment, and the method exists precisely because a best-supported
  account is reachable.

## Tailor to your environment
Record in `references/your-environment.md`: where accounts originate in your organization
(incident tickets, standup notes, interview memos, deposition summaries), the physical
evidence you can adjudicate against (log systems, audit trails, recordings, timestamps),
your confidence-mark conventions, and where reconciled accounts get filed. Real names,
client matters, and personnel specifics stay in `your-environment.private.md`
(git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/rashomon-effect.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/reconciliation-method.md — the intake protocol with cognitive-interview
  moves, the observation/interpretation/stakes split with a worked outage example, the
  divergence-classification table, the adjudication rules, the reconciled-account
  template, the memory-science summary with provenance marks, and the film/story
  attribution corrected
- references/your-environment.md — your account sources, evidence systems, confidence
  conventions, and filing (fill in)
