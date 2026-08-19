# The reconciliation method (full protocol)

Contents: 1. Account intake · 2. The three-layer split (worked example) · 3. The vantage
map · 4. The invariant core · 5. Divergence classification · 6. Adjudication rules ·
7. The reconciled-account template · 8. Memory science at claim level · 9. Attribution
corrected (film and story)

## 1. Account intake (cognitive-interview moves)
Collect every account whole, separately, before any comparison. The moves come from the
cognitive interview (Fisher & Geiselman; the enhanced version adds rapport-building
first) [snippet-only, ×4]:

- **Report everything.** Ask for the full account including details the witness thinks
  are irrelevant or out of order. Do not interrupt; do not correct; do not react. Partial
  detail the witness self-censors is often the detail that later breaks a fork.
- **Reinstate context.** Before the telling: where were you, what were you doing just
  before, what was on your screen, who else was around, what did the room/channel look
  like. Context cues unlock retrieval that direct questions miss.
- **Changed-order retelling.** After the free account, ask for the sequence backwards or
  from the middle. For honest witnesses this surfaces additional detail; fabricated
  accounts are rehearsed forward, so order changes are also gently diagnostic — but use
  that as a cue for more questions, not as a verdict.
- **Neutral wording.** Ask "what happened next," not "how fast was it going when it
  smashed" — the verb plants the answer (see §8, Loftus & Palmer).
- **Capture vantage with the account.** Physical: where they sat, what they could see and
  hear, which dashboard or channel they watched. Organizational: role, team, what they
  were responsible for, what they were paged about.
- **Timestamp the intake itself.** When the account was given, how long after the event,
  and what the witness had already heard or read about it (meetings, threads,
  retrospectives). This is the contamination history §6 weights by.

If a witness is guarded or defensive, the interviewing stance belongs to
`collaboration-skills:disarming-elicitation`; this protocol resumes once an account
exists.

## 2. The three-layer split — worked example
Split each account into OBSERVATIONS (directly saw/heard/read, vantage attached),
INTERPRETATIONS (conclusions drawn), and STAKES (what this version protects). Worked
example — a production outage, three engineers, three contradictory write-ups:

**Account A — on-call engineer (paged at 14:41, watching the alerting dashboard):**
- Observations: page fired 14:41; checkout errors were elevated when she opened the graph
  at 14:49, and on its default window that graph showed them already climbing before the
  14:35 deploy; database connection pool at ceiling by 14:50.
- Interpretations: "The system was degrading before anyone did anything; the deploy just
  happened to land in the middle of it."
- Stakes: she acknowledged the page eight minutes late; a timeline where degradation
  started early and quietly makes the slow acknowledgment matter less.

**Account B — deploy engineer (shipped a checkout change at 14:35, watching CI and the
deploy pipeline):**
- Observations: pipeline green at 14:35; canary metrics normal for the five-minute
  window; the first page he saw arrived 14:43.
- Interpretations: "The deploy was clean — the canary proved it; the outage came from the
  database side."
- Stakes: it is his change; a database-first story exonerates it.

**Account C — database engineer (in a vendor call until 14:45, then watching DB
metrics):**
- Observations: connection saturation visible when he first looked at 14:47; a slow-query
  spike beginning "around 14:35–14:40" on the retrospective graph.
- Interpretations: "The new code opened connections it never released; classic leak from
  the deploy."
- Stakes: the pool sizing is his configuration; a code-leak story means the pool was
  fine.

Note what the split already shows: A's "already climbing" is an observation with a
vantage (her graph's window); B's "the canary proved it" is an interpretation resting on
a five-minute window; C's timeline is retrospective (he was in a call), read off a graph
after hearing the deploy discussed. None of the three is lying.

## 3. The vantage map
One table: person → physical vantage (screens, rooms, channels) → organizational vantage
(role, responsibility) → time windows actually observed vs reconstructed afterwards.
Divergences between two people who never watched the same layer at the same time are
prime candidates for perspective artifacts, not contradictions. In the example: A watched
the paging dashboard, B watched the canary, C watched the database — three layers, no
overlapping window before 14:47.

## 4. The invariant core
List what all accounts agree on, with the physical record beside it. Example: a deploy
landed 14:35; a page fired 14:41; connection saturation existed by 14:50; checkout
recovered 15:20 after a rollback plus a pool restart. The core is usually larger than the
argument suggests, and it is the frame every divergence hangs from — and the standard
genuine contradictions are tested against in §6.

## 5. Divergence classification
For each point of disagreement, classify:

| Type | Signature | Test | Disposition |
|---|---|---|---|
| Perspective artifact | Accounts differ but vantages never overlapped; both can be true | Check the vantage map: could each have seen what they describe from where they were? | Keep both, attributed to vantage; no adjudication |
| Memory artifact | Late, retold, or discussed account; timeline drift; detail that appeared after a retrospective | Check contamination history from §1 intake notes; compare early vs late versions | Prefer the earliest uncontaminated version; name the mechanism (misinformation, leading question, delay, stress) |
| Stake artifact | The shading consistently favors the teller; facts match others', framing doesn't | Strip interpretation, compare bare observations across accounts | Keep the observations, flag the framing; a stake is calibration, not an accusation |
| Genuine contradiction | The versions cannot both be true at the observation layer | Adjudicate per §6 | Resolve against evidence, or file as an open fork |

Worked example, classified: A vs B on "degradation before the deploy" — partly
perspective (different graphs, different windows) and, once the metrics are pulled, a
genuine contradiction about when error rates rose. B's "canary proved it clean" vs C's
"leak from the deploy" — interpretations, not observations; neither adjudicable as
stated. C's "spike around 14:35–14:40" — memory artifact risk: retrospective reading,
after hearing the deploy discussed; his own first-hand window starts 14:47.

## 6. Adjudication rules
Only genuine contradictions get adjudicated, and only against:
1. **Physical evidence** — logs, metrics with timestamps, recordings, commit history,
   badge/access records, message timestamps. In the example: the metrics store shows
   checkout error rate flat until 14:37, rising after the 14:35 deploy — resolving the
   A-vs-B contradiction against A's "already climbing before the deploy" reading (her
   graph's default window smoothed the baseline, so the rise looked older than it was)
   without impugning her honesty. Note the scope of what was settled: A also observed
   elevated errors when she opened the graph after 14:41, and that observation stands.
2. **The invariant core** — a version inconsistent with what every account plus the
   record agrees on loses.

Explicitly not evidence: confidence (see §8), seniority, eloquence, or headcount — three
people who compared notes are one contaminated source, not three independent ones.
Weighting when no physical record exists: earliest uncontaminated account, from the best
vantage, given to a neutral asker, wins provisionally — marked as such. If nothing
separates the versions, the fork stays open: state both at full strength, plus what
specific evidence would close it. Filing an open fork honestly is a result; the filing
discipline is `decision-science-skills:minority-report`.

## 7. The reconciled-account template
```
RECONCILED ACCOUNT — <event>, <date compiled>
Accounts taken: <who, when, delay after event, contamination noted>
Vantage map: <one line per witness>

TIMELINE (each line marked):
  [CORROBORATED] <fact supported by physical evidence or all accounts>
  [SINGLE-VANTAGE] <fact from one witness, unopposed, vantage stated>
  [INFERRED] <fact no one observed, reasoned from the record — say from what>
  [FORK] <the contradiction, each version at full strength, whose account,
         what evidence would close it>

DIVERGENCES AND CLASSIFICATION: <the §5 table for this event>
STAKES NOTED: <one line per witness — calibration, not accusation>
OPEN FORKS: <restated; owner for chasing the closing evidence>
```
Every claim carries a mark; a reconciled account with no [FORK] and no [SINGLE-VANTAGE]
lines has probably been smoothed, which is the namesake failure. What happens next is out
of scope here: rival causal explanations go to
`decision-science-skills:competing-hypotheses-analysis`, with this document as evidence.

## 8. Memory science at claim level
- **Misinformation effect** (Loftus): information encountered after an event alters
  recollection of the event; the mechanism behind contamination-weighting
  [snippet-only, ×3-4].
- **Loftus & Palmer (1974)**: the verb in the question ("smashed" vs "hit") shifted speed
  estimates and produced false memories of broken glass a week later — leading questions
  write into memory, they don't just bias answers [snippet-only, ×3-4].
- **Confidence vs accuracy**: weakly related in general, and jurors overweight confidence
  [snippet-only, ×3]. Nuance, stated with its conditions (Wixted & Wells, 2017): INITIAL
  confidence at a first, uncontaminated, fairly-conducted identification is substantially
  diagnostic; the relationship degrades with delay, unfair procedures, post-event
  information, and repeated questioning [snippet-only, ×3]. Practical form: an early
  clean "I'm sure" means something; a late, discussed, re-asked "I'm sure" does not.
- **Cognitive interview** (Fisher & Geiselman; enhanced version adds rapport):
  report-everything, context reinstatement, changed order, changed perspective — on the
  order of 40%+ more correct details at comparable accuracy than standard interviews
  [snippet-only, ×4].
- **Triangulation** (Denzin): four types — data, investigator, theory, method
  [snippet-only, ×4]; independent-vantage convergence as warrant, which §4 applies.
- **Jury instructions** (standard forms): witnesses may honestly differ; "innocent
  misrecollection is not an uncommon experience"; weigh discrepancies
  important-vs-trivial and innocent-vs-intentional; vantage, stress, and perception
  limits recognized [snippet-only, ×4].

## 9. Attribution corrected (film and story)
- Kurosawa's *Rashomon* (1950) takes its PLOT from Akutagawa's "In a Grove" (1922) —
  seven accounts of a samurai's death, compressed to four in the film — and only its
  TITLE and frame from Akutagawa's "Rashōmon" (1915), which has no testimony plot. The
  two stories are routinely conflated; cite them separately [snippet-only, ×4].
- The term "Rashomon effect" is Heider's (American Anthropologist 90(1):73–81, 1988),
  naming good-faith divergence between ethnographers traced to observer circumstances,
  not lying [snippet-only, ×4]; it since appears in legal and evidence literature on
  eyewitness reliability [snippet-only, ×3] and in film/communication scholarship
  (Anderson 2016; the Routledge volume *Rashomon Effects*, 2015) [snippet-only, ×3].
- The film does not claim "there is no truth." Kurosawa's autobiography frames it as
  being about people unable to be honest with themselves, embellishing self-servingly
  (direction well-supported [snippet-only, ×3]; exact wording unverifiable here — quote
  at claim level only). Each account is self-flattering; even the woodcutter's
  "objective" version is compromised (the dagger he evidently took); the ending is moral
  restoration. The effect names good-faith divergence, not deliberate lying
  [snippet-only, ×2].
