# Trim recommendation — 2026-08-18

> ## Status: DECLINED by the owner, 2026-08-18. Keep all 121 skills.
>
> **Nothing in this document was applied, and nothing should be.** The owner read the
> recommendation and decided to keep every skill, including all 13 unanimous cuts. The library
> stays at **121 skills across 14 plugins**.
>
> The analysis is kept because it is a real measurement of the library and useful as a map — which
> skills are name-gated, which are omnibus, which have no cross-plugin inbound citations, what each
> one costs. **It is not kept as a pending action.** Do not re-open it as a deletion question, do
> not re-derive it, and do not treat any row below as an outstanding recommendation.
>
> Two things follow from the decision and belong in the record:
>
> 1. **Per-install subsetting is now the only lever on context cost.** A full install costs
>    ~14.8% of a 200K window before the user asks anything, and that number is not going down by
>    deletion. `README.md` carries the measured per-plugin and per-bundle tables, and
>    `scripts/measure-listing-cost.py` keeps them honest. Install two to four plugins, not fourteen.
> 2. **The finding that survives the decision is depth, not count.** The measurement that most
>    deserves follow-through is not "cut 34" — it is that the most-cited skills were the shallowest,
>    and that 25 of 121 have no citation from outside their own plugin. Deepening the hubs and
>    building cross-plugin seams improves the library without removing anything, and that work is
>    underway.

## How this was produced, and what was checked

Two independent methods, run separately and compared:

1. **Per-plugin substance review** — one reviewer per plugin, reading every SKILL.md, every
   reference, and every eval, judging each skill on marginal uplift over an unaided assistant,
   reach, depth, and portability. Each proposed deletion was then handed to a second agent whose
   job was to *defend the skill*.
2. **Forced cross-plugin ranking** — five reviewers, each given only the 121 name+description
   pairs (the router's actual payload) and a different lens: marginal uplift, expected lifetime
   invocations, what is irrecoverably lost on deletion, routing coherence, and fit to this owner.
   Each was required to produce a strict ranking of all 121 with no ties and to place at least 25
   below a cut line. Consensus is the intersection.

The per-plugin reviewers could not make the comparative call — they see one plugin. The rankers
could not read the skills — they see only descriptions. Agreement between two methods with
different inputs is the reason to trust a row; disagreement is flagged as the owner's decision.

**Claims verified by hand before publishing this** (agent findings are not taken on trust — an
earlier reviewer in this same exercise produced two fabricated details alongside one real one):

| Claim | Verdict |
|---|---|
| `bespoke-llm-architect` sets `disable-model-invocation: true` — already opted out of routing | **True**, and it is the only skill in the library that does |
| Its self-audit protocol is reconstructed past a source truncation seam | **True**, stated in its own reference |
| `project-command-center`'s references are "preserved near-verbatim from the source spec", no tables | **True**, 161 lines, zero table rows |
| `lean-six-sigma-for-software` is 965 lines with four of six references being engineering, not lean | **True** |
| Resulting skill count of 87 | **True**, recomputed |
| The report's token figures | **Wrong** — it used an undisclosed ~4.0 chars/token divisor. Corrected below with the repo's disclosed 3.7 via `scripts/measure-listing-cost.py`. |

**Corrected budget arithmetic** (`python3 scripts/measure-listing-cost.py`):

| Scenario | Skills | ~Tokens | % of 200K | Reclaimed |
|---|---:|---:|---:|---:|
| Today | 121 | 29,638 | 14.82% | — |
| Cut the unanimous 13 | 108 | 26,344 | 13.17% | 3,295 tok (1.65pp) |
| Cut all 34 | 87 | 20,898 | 10.45% | 8,740 tok (4.37pp) |

**One caveat the whole "get under 100 skills" argument rests on.** The claim that the runtime
silently trims descriptions to name-only at roughly 100 installed skills traces to a single
uncontrolled observation recorded in `MEMORY.md` on 2026-07-18. It is a landmark, not a measured
cliff, and no part of this recommendation should be read as precision about where the line is.

---

# Skill Library Trim — Recommendation

## 1. Headline

**Cut 34. Library goes 121 → 87 skills, 14 plugins → 12.**

Description budget drops from **107,532 characters (~26.9K tokens) to 75,871 (~19.0K)** — a **29.4% reclaim, ~7,900 tokens back on every single turn**. The cut skews long: the average cut description is **931 characters vs 872 kept**, so this is not a shave of stubs, it is the removal of the most expensive-per-firing entries in the catalog.

Landing at 87 puts the library **13 slots under the ~100 truncation cliff** rather than kissing it — which is the entire point. Per `MEMORY.md`, the "zero collisions" claim is only true of *exact duplicate trigger strings*: 111 trigger phrases still appear as whole words inside other skills' description prose. Routing is already contended. Every skill removed here buys the survivors both budget and contrast.

Two of the 34 should be **archived, not deleted** (`archive/` is this repo's established pattern): `medical-research-detective` (1,044 reference lines + two working scripts) and `lean-six-sigma-for-software` (811 reference lines). Both are real work; neither should hold a permanent routing seat.

---

## 2. Cut — unanimous

All five lenses placed these below their own cut line.

### coding-agent-skills (6)

| Skill | What it is | Why it goes |
|---|---|---|
| `chicken-little` | Multi-domain persona "Aether" — Python + Lean Six Sigma + hybrid PM, taught through named analogies (Boiling Frog, Swiss Cheese, Whack-a-Mole) | Its own *Not for* block routes every real capability elsewhere: pure Python → `elite-python-engineer`, pure DMAIC → `dmaic-problem-solving`, autopsies → the two sibling editions. What remains after the referrals is the analogy vocabulary. Fires only on "chicken little / aether / sky is falling." |
| `chicken-little-executive-advisor` | Fixed strategic autopsy: AI-leverage intercept, blocker ultimatum, TPS waste audit, human-friction scan, MSCD linguistic-failure table | 957 chars — among the largest descriptions in the library — gated behind `/deploy_advisor`. The blocker protocol and TPS waste hunt are real, but a user who has to type a codename to reach them has already lost the routing benefit. |
| `chicken-little-technical-compiler` | Jenga cascading-failure analysis, fragility table with statistical likelihood, compute-bleed catalog | 972 chars, gated behind `/deploy_compiler`. The "bottom block" question (which single unpinned dependency collapses everything) is a good question that `board-review` and `weight-of-the-books` ask without the costume. Three variants of one persona consume ~2,580 chars — 3.4% of the surviving budget — on name-only triggers. |
| `extreme-ownership` | Jocko Willink homage: four Laws of Combat, Dichotomy of Leadership checks, blameless debriefs | Explicitly the "leadership CULTURE layer" over `project-command-center` (also cut). Cover-and-Move and Decentralized Command presume a team to decentralize *to*. The owner is going solo. |
| `stay-hard-accountability` | Goggins homage: Accountability Mirror, 40% Rule, Cookie Jar ledger, callusing the mind | Deleting this loses a voice, not a method. Its most defensible move — "a systemic cause gets named as a system fix, not absorbed as personal failure" — is Deming, and Deming survives in `root-cause-analysis` and `a3-thinking`. |
| `master-prompt-architect` | Clarify-first HALT gate, backward design, triple audit (red team / expert panel / MSCD pass) | The HALT gate is its only distinguishing behavior, and its own text concedes `script-wizard` differs only in that it "proceeds and flags" instead. `prompt-engineering` (mean rank 12.8, top-15 on every lens) owns this region cleanly. |

### decision-science-skills (2)

| Skill | What it is | Why it goes |
|---|---|---|
| `no-win-drills` | Kobayashi Maru simulation with the winning move removed; grades process not outcome; Conti & Caroland frame-refusal audit | Beautifully sourced — and the source note itself concedes the evidence is "a small pilot with a self-reported outcome, and the wider literature on simulated death is mixed." A rehearsal skill needing a scheduled rehearsal. Triggers are fiction-anchored ("kobayashi maru"). |
| `weak-signal-navigation` | Etak wayfinding — fuse weak independent cues into a re-estimated belief with a confidence band when the dashboard is down | The genuinely rare case where the romantic story is the documented one, and still cut: its operational core ("what would we expect to see if things were fine?") is what `competing-hypotheses-analysis` and `bayesian-updating` do on organic triggers. "Wayfinding" and "etak" route nowhere a person types. |

### continuous-improvement-skills (1)

| Skill | What it is | Why it goes |
|---|---|---|
| `project-command-center` | Nine-domain command doctrine: Van Riper red-teaming, nested OODA, TPS flow, Smart Brevity, MSCD, absolute-vs-relative risk, AI assurance, constructive paranoia | The clearest omnibus in the library — its description lists nine domains and every one has a sharper owner. It pays full rent and loses every routing race. **Salvage before deleting:** the prime directive block — *fix acceptance criteria before results are known; log every intervention as first-class data; separate continuation from validation; never represent a rehearsal as a falsifiable experiment* — has no other home. Move it into `a3-thinking` or `design-of-experiments`. |

### math-foundations-skills (2)

| Skill | What it is | Why it goes |
|---|---|---|
| `algebra-and-formulas` | Name-the-unknown-in-words, balance principle, rearranging for a variable, substitute-back verification | Aimed at a person who spent a career in treasury operations. "Let h = hours worked" is below this owner's floor by a wide margin, and it is below the model's floor too. |
| `exponential-growth-and-logs` | Growth factors, CAGR, doubling time, rule of 72 with accuracy band, geometric mean | The one non-obvious item is the rule-of-72 accuracy range (±2% for 4–12%). Everything else — CAGR, `t = ln(target/current)/ln(1+r)`, why +10% then −10% ends below start — a strong model emits cleanly and correctly cold. |

### writing-skills (1)

| Skill | What it is | Why it goes |
|---|---|---|
| `gonzo` | Thompson-style participatory dispatches in four registers, with the hyperbole doctrine mapped for counsel | The craft is real and the legal framing is careful. But the skill's own boundary is decisive: *"Gonzo is commentary — it runs BESIDE the record, never as the record."* A register that never produces a deliverable, gated on "get weird," at ~1,000 chars. |

### machine-learning-skills (1)

| Skill | What it is | Why it goes |
|---|---|---|
| `bespoke-llm-architect` | Efficiency hierarchy (prompting+RAG → PEFT → continued pretraining → full FT → from-scratch), named 2026 techniques, self-audit protocol | It sets `disable-model-invocation: true` — it has *already opted out of routing*, so it is paying description rent for a slot it cannot win. Worse, its own metadata records that the source spec "was truncated mid-Mandatory Self-Audit Protocol" and the checklist is reconstructed. Incomplete by its own admission. |

---

## 3. Cut — majority

### decision-science-skills (5 more)

| Skill | What it is | Why it goes | Dissent |
|---|---|---|---|
| `skin-in-the-game` | Consequence-symmetry mapping, Hammurabi §229–233 graduated harm table, named-owner attestations, vendor defect-liability terms | Every instrument it produces — attestations, warranty clauses, vendor liability terms — needs a counterparty and a contract. Institution-shaped. | **Marginal-uplift dissented (73):** the graduated harm-class → who-bears-what table is a real artifact a model won't build unprompted. Fair, but it needs someone to bind. |
| `rashomon-effect` | Reconciles conflicting good-faith accounts: cognitive-interview moves, observation/interpretation/stake split, sightline mapping, weights initial uncontaminated statements over rehearsed ones | Requires multiple human accounts of one event. That is an incident-cell input. | **Uplift dissented (54):** the eyewitness-memory weighting rule genuinely inverts a model default (models weight confidence and detail; this weights recency-to-event). Correct, and still not reachable solo. |
| `ulysses-pact` | Self-binding commitment devices with second signatures, cooling-off periods, pre-decided unbinding criteria | Enforcement is "quoting the user's own words back," which needs a persistent enforcer. `hierarchical-memory-manager` + a CLAUDE.md rule does this with zero extra description budget. | **Uplift dissented (61):** pre-deciding the *unbinding* criteria is the non-obvious half. Worth folding one sentence into `hierarchical-memory-manager`. |
| `tabletop-wargaming` | Kriegsspiel → action/reaction/counteraction, blue team, red cell, white-cell adjudicator, scripted injects | Its own text: *"humans adjudicate every consequential outcome."* Needs three staffed roles. The most explicitly multi-human skill in the library. | Deletion lens ranked it 46 on the commander's-intent structure. Structure survives in `pre-mortem` + `break-glass-playbooks`. |
| `minority-report` | Three-to-five structurally different named scenarios, one-variable-at-a-time flip testing, the filed dissent, reflexivity check | Defers its probabilities to `reference-class-forecasting` and its failure imagination to `pre-mortem` — both kept, both higher-ranked on every lens. What's left is scenario labeling. | Uplift (75) and deletion (69) both kept it; the reflexivity check (acting on a forecast changes it) is genuinely nice. Not worth 900 chars. |

### continuous-improvement-skills (5 more)

| Skill | What it is | Why it goes | Dissent |
|---|---|---|---|
| `lean-six-sigma-for-software` | Deming PDSA + TPS jidoka/andon/poka-yoke + DMAIC/DMADV + co-design + WCAG 2.2 AA + adversarial release gauntlet, 811 reference lines | The owner's signature synthesis and the hardest cut here. It is a six-domain omnibus whose every part has a sharper sibling (`dmaic-problem-solving`, `standard-work`, `testing-strategy`, `ui-and-ux-inspection`). **Archive, don't delete.** Relocate the WCAG 2.2 AA conformance material into `ui-and-ux-inspection` and the adversarial release gauntlet into `testing-strategy` — those two blocks have no other home. | **Fit (73) and deletion (76) both kept it**, on the 811 lines of genuine TPS-to-code translation. The content is real; the routing shape is not. |
| `qfd-house-of-quality` | House of Quality: weighted WHATs → HOWs, relationship matrix, correlation roof, computed importance, cascading matrices | Its own description positions it as *"the translation bridge between the customer input that kaizen-and-codesign produces and the CTQs that lean-six-sigma-for-software consumes."* Both endpoints are cut. A bridge with no banks. | **Uplift dissented (55):** the correlation roof exposing engineering tradeoffs is a real construct. It needs a weighted customer population to be worth building. |
| `kaizen-and-codesign` | Kaizen event facilitation: charter, gemba walk before design talk, brainwriting/affinity/dot-voting, same-day PDCA | Its own precondition: *"operators plus a downstream customer plus an on-the-spot decision-maker in the room."* The owner is walking out of that room deliberately. | **Coherence ranked it 46** — it carves cleanly. It carves cleanly around a thing he will not have. |
| `evolutionary-operation` | Box's EVOP: tiny factorial perturbation of 2–3 factors within owner-approved safe operating limits, cycled on live production | Requires a live tuned production process *and* an owner who approves operating limits. The examples it names — reconciliation tolerances, cash-forecast parameters, dunning cadence — are the archived treasury domain. | **Uplift (47) and deletion (56) kept it**; fit ranked it 113. Fit is right: this is the clearest surviving artifact of the archived domain. |
| `structured-ideation` | 6-3-5 brainwriting, SCAMPER, criteria-based convergence, grounded in Diehl & Stroebe production blocking | It does frame the LLM as "anonymity engine, fatigue-proof idea partner" for solo use — but production blocking and evaluation apprehension are *group* pathologies. Solo, the technique reduces to "generate many options, then score them," which is the default. | Coherence (67) kept it. |

### math-foundations-skills (2 more) — dissolving the plugin

| Skill | What it is | Why it goes | Dissent |
|---|---|---|---|
| `units-and-dimensional-analysis` | Factor-label chains with visible cancellation, per-unit rates, annualization, dimension-checking formulas | The dimension-check ("if the two sides disagree the formula is wrong however plausible its numbers look") is the good part and it is one sentence. Fold it into `number-sense-and-estimation`'s gut-check step. | Deletion ranked it 51 on the trap catalog (per-month vs per-year, thousands vs millions). Those traps are caught by the same gut-check. |
| `probability-fundamentals` | Complement/addition/multiplication rules, mutually-exclusive vs independent, prosecutor's fallacy, Bayes via natural frequencies, base-rate neglect | The weakest-evidenced cut on the list (only 1.5 cut votes) and I am making it on plugin grounds. `statistical-inference` (top-15 on all five lenses), `bayesian-updating`, and `ab-test-design` collectively own conditional probability, base rates, and Bayes. This is the textbook layer beneath three kept skills. | **Deletion ranked it 48, uplift 68** — both above their cuts. If the owner keeps one more math skill, make it this one, relocated into `data-analytics-bi-skills`. |

### safety-and-reliability-skills (3)

| Skill | What it is | Why it goes | Dissent |
|---|---|---|---|
| `sortition-review` | Athenian euthynai + Venetian doge protocol: universal floor with no exemptions, verifiable lot with pre-committed seed, reviewer-pair rotation, end-of-role handover review | Needs an enumerable reviewable population *and* the authority to impose allotted oversight on people who did not ask for it. Both are institutional. | **Uplift dissented hard (66):** the verifiable-lot mechanics (pre-committed seed, dice in the open) are unforgeable, and "every carve-out becomes the channel gaming flows through" is a genuine insight. Nothing to apply it to. |
| `split-tally-evidence` | Exchequer tally sticks: halve each record between adverse parties so verification is rejoining two halves neither can alter alone | The history is superb scholarship. The modern translation the skill itself lands on — counterpart-held confirmations, hash-anchored exports, signed receipts, append-only logs with external anchors — is what a competent agent proposes unprompted when asked to make a record tamper-evident. The history is what is lost, and history is not what a skill is for. | **Uplift dissented (64).** Deletion ranked it **121 of 121** after reading the full reference — the sharpest single disagreement in the table, and deletion had read the most. |
| `rebuild-rehearsal` | Ise Shikinen Sengu: bus-factor census, rebuild unit that produces the real thing from the surviving record, learn-lead-teach rotation | The rotation mechanics need three people across two cycles. Its own scheduling rule is "a cadence shorter than tenure," i.e. multi-year. | **Uplift (65) and deletion (70) kept it.** The salvageable half — *"if the unit can't fail, it isn't a rebuild"* and "stand up the environment from the docs alone" — belongs in `checklist-design`. That is one paragraph, not a seat. |

### Remaining majority cuts

| Skill | What it is | Why it goes | Dissent |
|---|---|---|---|
| `coding-agent-skills:script-wizard` | Frame → Diagnose → Design → Build → Audit → Refine, with three domain reference packs (417 lines) | Cut *because* of its reach, not despite it. Its trigger list — "write a script, review this code, clean this up, audit this, draft a document" — intercepts `python-for-analysts`, `git-and-code-review`, `sparring-partner`, `board-review`, and `technical-documentation`, all of which rank higher on every other lens. Its cost is not its own tokens; it is the precision it steals from five neighbours. | **Reach ranked it 2 of 121** — the single largest disagreement in the exercise. See §6. |
| `writing-skills:adams-plain-grade` | Ken Adams clarity at 5th-grade reading level, rejection of tested language, doublets, archaisms | The first clause of its own *When to use* is "the user asks for adams-plain-grade by name." Its remaining organic territory — patient materials, low-literacy audiences, easy-read — is aimed at readers the owner is leaving. `adams-smart-brevity` (reach rank 1) holds professional register. | Coherence (56) kept it; it does carve cleanly. |
| `metacognition-skills:dynamic-analysis-engine` | Orient → decompose → hypothesize → test → iterate with depth control | "Any non-trivial analysis where the path is not obvious" is the broadest umbrella in the library, and it is the one metacognition skill **not named in the CLAUDE.md standing directive** — which names MEMORY.md, `hierarchical-memory-manager`, `reflective-learner`, and `knowledge-crystallizer`. Cutting it honors the mandate exactly. | Reach (29) and fit (49) kept it. |
| `full-stack-dev-skills:ml-in-production` | Model as versioned artifact, FastAPI + Pydantic serving, batch vs realtime, training/serving skew, drift monitoring | Wrong plugin: ML content in the full-stack plugin, competing with `machine-learning-skills` for the same requests. **Merge, don't delete** — fold training/serving skew and drift monitoring into `machine-learning-skills:model-evaluation`, which already owns honest measurement. | Uplift ranked it 57 on the skew failure mode, which is exactly the part being preserved. |
| `deep-research-skills:medical-research-detective` | Multi-database literature search, dot-connection across symptoms/drugs/labs, graded case file, `verify_citation.py` + `search_pubmed.py` | **Archive whole, with its plugin.** A personal-health research tool holding a permanent seat in a professional, career-portable library — and the single most expensive artifact in the catalog (1,044 reference lines, 995-char description) for a use case that fires a handful of times a year. | **Deletion (25) and uplift (30) both ranked it top-quartile**, on the working citation-verification script and the real harm of a fabricated medical citation. Archiving preserves both; only the routing seat is reclaimed. |
| `collaboration-skills:stakeholder-mapping` | Power-interest grid (with the honest Johnson & Scholes / Eden & Ackermann attribution correction), RACI, Cohen & Bradford exchange currencies | Its own use cases: *"a process change with opponents, a multi-party matter, a migration, or a deprecation you lack authority to force."* Every one presumes an org chart. The scholarship correction is admirable and does not create a use. | **Uplift ranked it 103** — agreeing it goes. Reach (60) and deletion (65) kept it. |

---

## 4. Kept despite low ranks

The ranking is wrong about these four. Each carries a method the lenses scored as costume.

**`coding-agent-skills:soviet-space-graphite`** *(mean 106, 4.5 cut votes — four lenses cut it outright)*

The lenses saw a Soviet design-bureau pastiche and stopped. Underneath is a two-stage procedure, and the second stage is the part models never volunteer. The **Pencil Pass** generates radically simpler candidates from a priced ladder — do nothing, delete the requirement, use what exists, buy don't build, the spreadsheet not the app, the cron job not the platform — each priced in *build cost and carry cost*. Models do that willingly. The **Graphite Test** then hunts the hidden constraint that makes the simple thing dangerous, and it is named for the fact that the founding legend is *false*: graphite dust is conductive and flammable in a spacecraft, both programs bought the pen. Models do not do that. They propose the simpler thing and stop. For an owner building solo software with agents that cheerfully suggest simplifications, a skill whose entire second half is "now find the constraint that kills your simplification" is high-frequency, not theatrical. **Condition of keeping:** demote the persona triggers ("comrade engineer", "soviet space graphite") behind the organic ones already present — "simpler solution", "are we overengineering this", "better faster cheaper".

**`coding-agent-skills:the-foreman`** *(mean 93.8, 4 cut votes)*

Scored as a Bob-the-Builder costume. It is a draw inspection: verify claimed completion against actual built state *before releasing the next phase*, sorted into three bins — LOAD-BEARING DEFICIENCY (next phase stacks weight directly on this gap), PUNCH ITEM (real, fix in parallel), FUTURE WORK (not in this phase's claim at all, noted and set down). Its evidence standard is *"I ran X and saw Y, never vibes"* and its sharpest line is **"untested is unbuilt — a wall nobody has leaned on."** That is precisely the failure mode of agent-driven development, where every turn produces a claim of completion. And this repo is the case in point: `MEMORY.md` records **121 evals never executed** and a trigger-test compliance log that is **empty** — a library that claims done and has never been walked. Cutting the skill that inspects claimed-complete work, in a repo whose two open verifications are exactly that, is the ranking's clearest miss.

**`decision-science-skills:principled-negotiation`** *(mean 76.6, 2.5 cut votes; marginal-uplift 92, fit 94)*

Both lenses that cut it were reasoning about vendor contracts and fee schedules — institutional negotiation the owner is leaving. They missed the near-term event: a person leaving a role negotiates a salary, and then, if the work goes portable, negotiates every engagement. The two-layer structure (Fisher/Ury interest mapping and BATNA estimation, plus Voss accusation audits, mirrors, labels, calibrated how/what questions) plus counterpart roleplay for rehearsal is exactly the shape of that. This is the most time-sensitive skill in the library and it was ranked as if the next several years were the last several.

**`coding-agent-skills:rule-stress-testing`** *(mean 52.2, 2 cut votes; reach 91, coherence 95)*

Cut by reach and coherence as an Asimov novelty ("three laws"). It inventories a rule set's unstated precedence, extracts load-bearing undefined terms, and runs six named failure modes — conflict equilibrium, term widening, redundancy loss/literal compliance, scope creep/precedence inversion, definitional capture, information partitioning — then adds Goodhart and malicious-compliance passes and **re-tests the fixed set, because patches breed new conflicts.** The owner writes CLAUDE.md files, agent guardrails, and skill descriptions for a living. This is a linter for the artifact he produces most. Marginal-uplift (21), deletion (29), and fit (25) all had it top-quartile; they were right.

*Also spared against 1.5–2 cut votes, briefly:* `weight-of-the-books` (acceptance tests must run **loaded** at design and peak values — a step almost universally skipped), `survey-and-sampling-design` (Groves total survey error, the Squire 1988 nonresponse reading of Literary Digest, Schuman & Presser question audit — calibrated and cited, and the lenses that cut it were counting invocations, not damage-per-invocation), `data-file-hygiene` (its sanitize-before-git protocol is the enforcement arm of a documented `MEMORY.md` data-sensitivity posture), and `habit-design` (Gollwitzer implementation intentions and friction engineering need no institution at all — the most portable skill in `learning-skills`).

---

## 5. Plugin-level consequences

**Delete whole (2 plugins):**

- **`math-foundations-skills`** — dissolved. Four skills cut. The two survivors move to `data-analytics-bi-skills`: `number-sense-and-estimation`, because its function is not teaching arithmetic but guarding output (*"estimate before you calculate — and before you look"*; spurious calculator and spreadsheet precision; the independent re-derivation), and `percentages-and-proportions`, for the error-inoculation content models genuinely fumble — mix effects where a total moves opposite to every subgroup, markup vs margin, percentage points vs percent, base-first discipline. Neither is arithmetic instruction; both are checks on computed numbers. `data-analytics-bi-skills` goes 11 → 13.
- **`deep-research-skills`** — archived. A one-skill plugin holding a personal-health research tool is the plugin-level odd-one-out in a general-use professional library, and the cleanest violation of the post-2026-08-11 charter. Move to `archive/`, restorable, per `archive/README.md`.

**Below viable size — merge (2 plugins into 1):**

- **`writing-skills`** (5 → 3: `adams-smart-brevity`, `explanation-design`, `technical-documentation`) and **`learning-skills`** (3, unchanged: `deliberate-practice`, `habit-design`, `spaced-retrieval-learning`) are both under four. Merge them into **`communication-and-learning-skills`** (6). The pairing is real, not administrative: `explanation-design` and `spaced-retrieval-learning` are the same act from opposite ends — one structures an explanation for a reader, the other tests whether it stuck.

**Reshaped but healthy:**

- **`coding-agent-skills`** 20 → 13. The largest single reclaim: 7 cuts, ~6,700 description characters. What was a meta-engineering core (`writing-agent-skills`, `prompt-engineering`, `git-and-code-review`, `agent-harness-config`, `agentic-workflow-design`) buried under six personas and an umbrella becomes a legible plugin about building and driving agents.
- **`decision-science-skills`** 15 → 8 — the deepest proportional cut (47%), and the honest one: seven of the eight survivors (`after-action-review`, `bayesian-updating`, `competing-hypotheses-analysis`, `pre-mortem`, `principled-negotiation`, `reference-class-forecasting`, `systems-thinking`, `the-challenger`) work with a single person and a decision. The seven cut all needed a room.
- **`continuous-improvement-skills`** 16 → 10 — loses both sprawlers, both rarest methods, and both facilitation skills; keeps the ten a colleague would recognize by name.
- **`safety-and-reliability-skills`** 10 → 7, **`full-stack-dev-skills`** 11 → 10, **`collaboration-skills`** 5 → 4, **`machine-learning-skills`** 7 → 6 (+ `ml-in-production` content folded into `model-evaluation`), **`metacognition-skills`** 4 → 3 (mandate intact), **`data-tools-skills`** 7 → 7 (untouched — the only plugin where every skill earns its seat on every lens).

**Resulting count: 12 plugins, 87 skills.** After the writing/learning merge, **11 plugins**.

---

## 6. Where the lenses disagreed most

The forced rankings agreed almost everywhere. The five places they split by 80+ ranks are not noise — they are the owner's actual decisions, and each one is a question about what a skill library is *for*.

**1. `reliability-engineering` — ranked 2nd and 100th by different lenses (spread 98).**
Marginal-uplift and deletion both put it at #2 of 121; reach put it 100th and fit 99th. Both are right about different things. The content is genuinely unforgeable — the classification step (*a non-repairable population contributes one time-to-first-failure each; a repairable system produces recurrent-event data, and fitting a Weibull to one repaired system's inter-failure gaps mixes hazard shape with reliability trend and yields a β the interpretation table cannot legally read*) is a mistake competent people make constantly and models reproduce confidently. It also requires a maintained failure log the owner may never keep. **The decision: does this library optimize expected value per year, or insurance against confident wrongness?** I kept it on the second reading — a wrong β is worse than no β — but the owner should know he is buying insurance, not utility.

**2. `script-wizard` (spread 111) and `sparring-partner` (spread 103) — reach vs routing precision.**
Reach ranked `script-wizard` **2nd** and `sparring-partner` **7th**; coherence ranked them **113th** and **110th**. Same skills, opposite verdicts, and the mechanism is identical: both claim enormous request-space ("any script, tool, document, or technical artifact of real substance"; "any work product"). Reach reads that as organic firing. Coherence reads it as interception. **They are both describing the same behavior and disagreeing about whether it is a feature.** I split them: `sparring-partner` survives because "critique this" is a request with no better owner and it absorbs the function of six cut personas; `script-wizard` goes because "write a script / review this code / clean this up" all have sharper owners it would outrank by breadth alone. That is the general rule this disagreement produces: **an umbrella is a feature when nothing sits under it and a tax when something does.**

**3. `reflective-learner` (spread 103) and `knowledge-crystallizer` (spread 100) — mandate vs merit.**
Uplift and deletion ranked them 111/113 and 112/114 — near the bottom, as process ceremony around a `MEMORY.md` that persists without them. Fit and reach ranked them 10/16 and 14/26, purely because CLAUDE.md mandates the metacognition suite as permanently engaged. **Nothing here is a judgment about the skills; it is a judgment about whether a standing directive outranks a ranking.** It does. I resolved it by cutting `dynamic-analysis-engine` — the one metacognition skill the directive does *not* name — and keeping all three that it does. The owner should note that if the mandate ever lapses, two lenses want these gone immediately.

**4. `survey-and-sampling-design` (spread 91), `medical-research-detective` (86), `design-of-experiments` (85) — rigor per invocation vs invocations per year.**
A consistent pattern: uplift and deletion rank these top-15 (Lenth's PSE, the Squire 1988 nonresponse finding, working citation-verification scripts); reach and fit rank them 87–111. **The real question is whether a skill's job is to fire often or to prevent a specific expensive error the one time it fires.** I kept the first two and `design-of-experiments`, archived the third. The tiebreaker I used, and recommend: keep it if the error it prevents is *silent* — a badly-worded survey question and an unrandomized factorial both produce clean-looking numbers that are wrong, and nothing downstream flags it.

**5. `root-cause-analysis` (spread 80) and `git-and-code-review` (spread 70) — fame is not uplift.**
Coherence ranked `root-cause-analysis` **4th** and fit **12th** (17 inbound citations — the library's most-cited hub); marginal-uplift ranked it **84th**, on the grounds that 5 Whys is famous *because* it is everywhere in the training data, so the file buys back nothing. Same shape for `git-and-code-review`: coherence 1st, fit 3rd, uplift 71st. **This surfaces the sharpest structural insight in the whole exercise: inbound citation count measures how central an idea is to the library's own prose, not how much the model needs the file — and under a marginal-uplift lens those are nearly opposite signals.** I kept both, because cutting a 17-inbound hub forces edits across a dozen surviving skills and that maintenance cost is real. But the owner should stop treating citation count as evidence of value. It is evidence of *entanglement*, which is a reason cutting is expensive, not a reason the skill is good.