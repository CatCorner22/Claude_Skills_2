# Trigger test — executed results

**Run date:** 2026-08-18 · **Protocol:** [`trigger-test.md`](trigger-test.md) · **Library:** 121 skills, 14 plugins
**Method:** blind-router simulation (8 agents × 10 prompts) · **Result: 80/80 PASS**

> **Read the method section before the headline.** A 100% pass rate is not a clean bill of health. It is
> the score this instrument returns, and the most useful thing this run produced is a much clearer
> picture of what the instrument cannot see.

---

## 1. Method, and what it cannot show

### What was actually run

This was **not** the protocol as written. `trigger-test.md` specifies up to 80 fresh Claude Code
sessions with the full 121-skill library installed, recording what the real plugin loader loads. That
run has still never happened.

What ran instead is a **blind-router simulation**:

- Eight fresh agents were each given the **121 `name` + `description` pairs** — the exact payload the
  real router sees, no bodies, no references — plus **ten prompts carrying opaque ids** (`P001`…`P080`).
- Each agent named the one skill it would load (or `NONE`), gave a confidence 1–5, quoted the
  description words that decided it, and named a runner-up.
- The **answer key was withheld structurally**: it lived in a separate file
  (`answer_key.json`) that no routing agent could read. The agents never saw a tier label, an
  expected target, or the `LOAD`/`NOT` polarity of any prompt. Prompt order was shuffled across
  agents so the tier grouping in the protocol carried no signal.
- Scoring was done afterwards by joining decisions to the key on `prompt_id`.

Two integrity checks passed: every one of the 80 primary picks and all 80 runner-ups resolve to a real
`plugin:skill` in the library (zero hallucinated names), and the `NONE` rate differs sharply between
`LOAD` prompts (1/41, the one row where `NONE` is correct) and `NOT` prompts (11/39) — the agents were
discriminating, not guessing.

### The contaminated first run, and why the gap matters

A first attempt at this run gave the routing agents a single file that **also contained the expected
answers**, with an instruction not to look at them. It returned **99%**.

That number was rejected — correctly — as non-credible. A routing surface that had never once been
tested does not score 99% on its first exposure, and the obvious explanation was that the agents were
reading the key. The run was treated as evidence the harness was broken, not evidence the library was
healthy.

**The blind run scored 100%.** Removing the key made the score go *up*, by one row.

That inverts the original diagnosis, and the inversion is the finding:

- The contamination was **not** what produced the high number. Whatever the first run's agents were
  doing, they were not reading their way to a ceiling — a genuinely blind panel matched them and then
  some.
- So the ceiling is a property of the **instrument**, not of the leak. Fixing the leak was necessary
  for the result to mean anything, and it changed the result by 1.25 percentage points.
- Which means the original instinct — "99% cannot be real" — was right about the *number* and wrong
  about the *cause*. The remaining sections are an attempt to say what the real cause is.

Four structural reasons this instrument reads high:

1. **Half the test is scored on a rule that is hard to fail.** 39 of 80 prompts are `NOT` prompts,
   where any answer except one specific skill out of 121 scores PASS. `NONE`, the right neighbour, or
   an unrelated skill all pass identically. The guard tiers are real tests of over-triggering, but
   they are cheap to pass, and they are 49% of the sample.
2. **A deliberating language model is not the plugin loader.** Each agent saw one prompt at a time,
   the entire listing in front of it, no other task in context, and unlimited time to reason. It
   produced a paragraph of justification quoting description text. The runtime router does none of
   that. This is a **best case**, and it should be read as an upper bound on routing quality, not an
   estimate of it.
3. **No degradation was simulated.** All 121 descriptions were present in full, every time.
4. **The prompts partly test string matching, not vocabulary reach.** See §4 — this is acute in
   Tier D, and it is the reason that tier produced no finding.

### Limits that are load-bearing

**(a) This does not reproduce silent listing truncation.** The runtime is reported to trim the
least-used skills' descriptions to **name-only** past roughly 100 installed skills, with no error.
A 121-skill install is past that point, so the real router may be matching some of these skills on
their *name alone* — a payload this simulation never presented.

That ~100 figure deserves to be handled carefully. It traces to **one uncontrolled observation** in
this repo's `MEMORY.md`:

> *LESSON: With ~100 installed skills, the skill-listing context budget trims least-used descriptions
> to name-only; direct `/plugin:skill` invocation still works, and newly installed plugins appear in
> the listing only at the next refresh. (observed 2026-07-18)*

One session, one day, no controls, no measurement of *which* skills were trimmed or by what rule.
Treat it as a **landmark, not a cliff**: sufficient reason to test the degraded regime, insufficient
reason to state that 121 skills are degraded and 99 are not. The threshold could be token-budget-driven
rather than count-driven, could vary by client, and could have changed since. Nothing in this run
tested it.

**(b) A language model's judgement is not the plugin loader's matching behaviour.** The agents were
asked "which skill would you load", and answered by reading. The loader's actual mechanism — how it
weights the name against the description, whether the trigger list is privileged, how it behaves when
two descriptions overlap — is not observable from here and was not measured. Every PASS in this
document means *a careful reader of the description would route correctly*. It does not mean
*the runtime does route correctly*.

**What this run is genuinely good for:** it tests whether the **descriptions carry enough
discriminating information** for correct routing to be *possible*. A failure here would have been
conclusive — the description cannot be matched even by a careful reader with the whole listing in
front of it. Zero failures means that necessary condition is met across all 45 rows. It is not the
sufficient condition.

---

## 2. Headline

**80 / 80 PASS (100%).** Zero MISS, zero WRONG, zero OVER.

| Tier | What it tests | Prompts | PASS | MISS | WRONG | OVER | Rate |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| A | routes that lost their phrases in collision surgery | 22 | 22 | 0 | 0 | 0 | 100% |
| B | did the moved phrases land with their new owner | 6 | 6 | 0 | 0 | 0 | 100% |
| C | over-trigger guards on bare common words | 12 | 12 | 0 | 0 | 0 | 100% |
| D | persona-named skills (name / in-scope / out-of-scope) | 24 | 24 | 0 | 0 | 0 | 100% |
| E | skills substantively rewritten, untested vocabulary | 16 | 16 | 0 | 0 | 0 | 100% |
| **Total** | | **80** | **80** | **0** | **0** | **0** | **100%** |

Split by prompt polarity, which is the more honest cut:

| Polarity | Prompts | PASS | Rate | Mean confidence |
|---|:--:|:--:|:--:|:--:|
| `LOAD` — the target must load | 41 | 41 | 100% | 4.56 |
| `NOT` — the target must not load | 39 | 39 | 100% | 3.69 |

### A stricter secondary score the key did not enforce

The 19 Tier A and Tier E near-miss rows each name, in the protocol, the skill that *should* have
loaded instead ("elite-python-engineer (should be `git-and-code-review`)"). The answer key encodes
only the prohibition, so any non-target answer scored PASS. Scored against the stronger rule — did the
router land on the protocol's named alternative? — the result is **19/19**.

That is the most substantive positive result in this run, because it cannot be passed by abstaining.
Eleven seams that collision surgery cut through this session (`elite-python-engineer` ↔
`git-and-code-review`, `↔ backend-api-development`, `exploratory-data-analysis` ↔
`descriptive-statistics`, `feature-engineering` ↔ `data-cleaning`, `data-cleaning` ↔ `standard-work`,
`assertion-evidence-deck` ↔ `executive-briefing`, `model-evaluation` ↔ `project-command-center`,
`rest-api-data-pulls` ↔ `backend-api-development`, `sql-for-analysts` ↔ `database-and-orm`) plus eight
rewritten-skill seams all resolved to the correct side, by name, on the first try.

### Row-level reading (Tier B)

- **B1** (`Standardize this.`) — the known orphaned-phrase defect. Expected outcome: nothing loads, or
  a clarifying question. **Result: `NONE`, confidence 1.** This is the correct outcome and the low
  confidence is the right shape: the router recognised the word was ambiguous rather than picking
  confidently. The reasoning identified four skills holding a qualified form of `standardize`
  (`standard-work`, `data-cleaning`, `feature-engineering`, `adams-plain-grade`) and declined. The
  qualification surgery worked as intended and the orphaned bare verb is behaving as designed.
- **B5 / A1 / A2 cross-check.** The protocol warns that `elite-python-engineer` still advertises "code
  review" in its description prose while `git-and-code-review` holds the trigger. Both A1
  (`must-load` elite-python-engineer) and B5 (`must-load` git-and-code-review) passed, and A1's
  near-miss routed to `git-and-code-review`. The seam holds under a careful reader.
- **B6 / A1 / A2 cross-check.** The protocol's failure signature — "if A1/A2 MISS **and** B6 PASSes,
  the split is wrong" — did not fire. A1, A2 and B6 all passed; analyst-grade Python is not absorbing
  production-grade requests in this run.

---

## 3. Failures

**There are none.** No MISS, no WRONG, no OVER across 80 prompts.

Per the protocol's "Acting on the results" section, MISS → add vocabulary, WRONG → reciprocal
`Not for:` lines, OVER → qualify the trigger. **None of those three fixes has evidence supporting it
in this run, and none should be made on the strength of this document.**

The honest reading is not "the descriptions are correct" but "**this instrument could not find a
defect in them**". Given §1, that is a weaker statement than it looks, and the sections below are
where the usable signal actually is: the routes that passed by a narrow margin, and the rows where
the forbidden skill was the runner-up. Those are the places a real run — or a degraded listing — is
most likely to break first.

---

## 4. Tier D: name-only-reachable skills

**Finding: none detected — and the column that was supposed to detect them cannot.**

All eight persona-named skills returned the healthy pattern (by-name loads, in-scope loads,
out-of-scope does not):

| Row | Skill | by-name | in-scope | out-of-scope | Pattern |
|---|---|:--:|:--:|:--:|---|
| D1 | `writing-skills:gonzo` | PASS (5) | PASS (3) | PASS (3) | healthy |
| D2 | `full-stack-dev-skills:elite-python-engineer` | PASS (5) | PASS (4) | PASS (4) | healthy |
| D3 | `coding-agent-skills:chicken-little` | PASS (4) | PASS (4) | PASS (3) | healthy |
| D4 | `coding-agent-skills:sparring-partner` | PASS (5) | PASS (5) | PASS (3) | healthy |
| D5 | `decision-science-skills:minority-report` | PASS (5) | PASS (5) | PASS (1) | healthy |
| D6 | `coding-agent-skills:the-foreman` | PASS (5) | PASS (5) | PASS (3) | healthy |
| D7 | `coding-agent-skills:soviet-space-graphite` | PASS (5) | PASS (5) | PASS (2) | healthy |
| D8 | `safety-and-reliability-skills:weight-of-the-books` | PASS (5) | PASS (5) | PASS (4) | healthy |

### Why this result carries almost no information

**Seven of the eight in-scope prompts contain a literal trigger phrase from the skill they are meant
to reach.** They are not paraphrases:

| Row | In-scope prompt | Literal trigger string it contains |
|---|---|---|
| D2 | "Refactor this module to production standards — typing, logging, error handling." | `refactor`, `error handling` |
| D3 | "**The sky is falling** on this integration — walk me through it." | `sky is falling` |
| D4 | "Tear this strategy apart and **be honest about** it." | `be honest about` |
| D5 | "**Branch the futures** — what happens if demand drops 20%?" | `branch the futures` |
| D6 | "**Is this ready to build on**, or is it **half-built**?" | `is this ready to build on`, `half-built` |
| D7 | "**Are we overengineering this**? Is there a **simpler solution**?" | `are we overengineering this`, `simpler solution` |
| D8 | "**Will it hold at real volumes**, or did we test it empty?" | `will it hold at real volumes` |
| D1 | "Give this a **savage**, first-person take…" | trigger `savage take`, split; `Savage` also in prose |

The protocol is transparent about this — it records that an earlier version of the tier scored these
same phrases as *failures*, and fixed that by reclassifying them as PASS, because the skills
"deliberately own" them. That fix was right for scoring and wrong for detection. The result is that
the in-scope column now asks the same question as the by-name column — *is this string in the
description?* — and cannot distinguish a skill reachable by vocabulary from one reachable only by
incantation.

The specific worry is visible in two descriptions whose **Use-when clause is purely name-gated**:

- `chicken-little`: *"Use when the user asks for Chicken Little or Aether by name."* The in-scope
  prompt reached it only via the trigger list entry `sky is falling` — the routing agent said so and
  docked its confidence for exactly that reason.
- `gonzo`: *"…on explicit request. … Use when the user asks for the gonzo treatment, weird-mode
  commentary, or a Thompson-flavored read."* The in-scope prompt reached it via the trigger `savage
  take` and the prose word "Savage", against a Use-when sentence that says it fires on explicit
  request only. Confidence 3, the joint-lowest of any Tier D in-scope row.

Both are the shape most damaged by name-only trimming: if the description is trimmed, the trigger list
goes with it, and only the persona name survives. Neither is a defect on this evidence. Both are the
first place to look when the degraded regime is finally tested.

**Recommended protocol change (not a description change):** rewrite the Tier D in-scope column so no
prompt contains any substring of the target's trigger list — describe the *situation* in a user's own
words instead. Until then, Tier D cannot produce the finding it exists to produce.

---

## 5. Routes that barely held

Seven passes came at confidence 1–2. These are the routes that will not survive listing degradation,
a distracted router, or a mid-conversation context already biased by a loaded skill body.

| id | Row | Prompt | Result | Conf | Why it is fragile |
|---|---|---|---|:--:|---|
| P023 | B1 | `Standardize this.` | PASS (`NONE`) | 1 | **Correct and correctly fragile.** The bare verb has no owner by design. Low confidence here is the intended outcome, not a defect. Do not "fix" this by giving `standardize` back to a skill. |
| P016 | C5 | `Rank these three vendors for me on price and support.` | PASS (`NONE`) | 1 | The guard on `rank`/`qualify` (`sql-for-analysts`) held, but the router had to actively reject `qfd-house-of-quality` — *"prioritizing features or requirements against weighted needs"*, *"competitive benchmarks"* — which is one trimmed clause away from looking like vendor ranking. |
| P055 | C11 | `What are the visitor permissions for the building on weekends?` | PASS (`NONE`) | 1 | Runner-up was **the forbidden skill itself**. `agent-harness-config` advertises the bare trigger `permissions` and `hooks`; only the surrounding words *"tool permission rules (allow/ask/deny)"* and *"Configures the Claude Code harness"* kept it out. Under name-only trimming, `agent-harness-config` presents as a name containing "config" and nothing to disambiguate `permissions`. |
| P025 | C9 | `There's too much waste in our packaging — can we use less cardboard?` | PASS (`NONE`) | 1 | `value-stream-mapping` holds bare `waste` and bare `flow`; the guard held only because its description scopes the eight wastes to *"office work"* and *"lead time"*. The word `waste` in its everyday material sense is genuinely close. |
| P019 | D5 | `What were last quarter's actual numbers?` | PASS (`NONE`) | 1 | A plain factual lookup. Nothing in the library claims it, which is correct, but the router reached that conclusion by elimination rather than by any description saying "not for retrieving reported figures". |
| P049 | C3 | `Who should lead this project, and what's the lag before we see results?` | PASS (`NONE`) | 2 | The `lead`/`lag` guard on `sql-for-analysts` held. `stakeholder-mapping` (*"writes the RACI"*, *"who needs to sign off"*) was close enough that the router had to argue it away. |
| P044 | D7 | `Implement the design we agreed on last week.` | PASS (`script-wizard`) | 2 | The `soviet-space-graphite` guard held, but the router landed on `script-wizard` purely on its very broad clause *"Use when asked to build, write, fix, review, scope, or improve any script, tool, document, or technical artifact of real substance — even when phrased casually"*, with **no trigger word matched**. `script-wizard` is a wide net; it is the skill most likely to absorb requests that belong elsewhere, and this row is the only evidence of it in the run. |

Note the pattern: **six of the seven fragile routes are `NONE` answers on guard prompts.** The
library's guards are holding on *reasoning about description context*, not on the absence of a
matching word. That is precisely the capability that disappears when the description is trimmed to
name-only — which makes Tier C the tier whose 100% is least transferable to the real runtime.

---

## 6. Where the runner-up was the answer the row forbids

Nine `NOT` rows passed while naming the forbidden skill as the runner-up. The guard held by exactly
one rank. These are live seams: the two descriptions are competing, the row passed, and nothing in
either description names the boundary.

| id | Row | Prompt | Loaded | Runner-up (= forbidden) | The seam |
|---|---|---|---|---|---|
| P027 | A2 near-miss | `What HTTP status code should I return when validation fails on a POST?` | `backend-api-development` | **`elite-python-engineer`** | elite-python-engineer's *"domain exceptions with deterministic error handling"* and trigger `error handling` overlap backend-api-development's *"one error shape with correct status codes"*. Nothing says which owns HTTP semantics. |
| P035 | A10 near-miss | `Design the paginated endpoint my own API should expose.` | `backend-api-development` | **`rest-api-data-pulls`** | Both descriptions own the word `pagination`: *"pagination on every list endpoint"* (serving) vs *"pagination until exhaustion"* (consuming). The consume/serve boundary is real but stated only implicitly. |
| P038 | A11 near-miss | `This query takes 40 seconds and the ORM generated it.` | `database-and-orm` | **`sql-for-analysts`** | sql-for-analysts holds `slow query`, `optimize query`; database-and-orm holds `N+1 query`, `ORM slow`. The router split on the word "ORM" alone. |
| P012 | A3 near-miss | `Which is the defensible measure of a typical value when the distribution is badly skewed?` | `descriptive-statistics` | **`exploratory-data-analysis`** | The reciprocal row (P028) shows the same pair inverted. This is the seam collision surgery cut this session; both sides route correctly but by narrow margins in both directions. |
| P009 | E7 near-miss | `Is this difference statistically significant?` | `statistical-inference` | **`ab-test-design`** | Symmetric with P059 below — the analyse/design boundary between these two is carried by "before any data arrives" in one description and nothing explicit in the other. |
| P059 | E6 near-miss | `How long should I run the experiment and how many users per arm?` | `ab-test-design` | **`statistical-inference`** | The mirror of P009. Both held; the pair is the single most-tested seam in the run and the one most worth a reciprocal `Not for:` line if any is ever written. |
| P020 | E1 near-miss | `My agent loops forever calling tools — how do I bound it?` | `agentic-workflow-design` | **`prompt-engineering`** | prompt-engineering was rewritten this session; the router split on `guardrails` appearing in agentic-workflow-design's trigger list. |
| P057 | E2 near-miss | `Before my grader model picks a prompt version, how do I show its scores can be trusted?` | `measurement-systems-analysis` | **`prompt-engineering`** | Held on measurement-systems-analysis's explicit *"LLM-as-judge scoring, where agreement across judges and repeated runs is measured before any eval score is trusted"* — an unusually well-defended boundary, and the model for how the others should read. |
| P055 | C11 guard | `What are the visitor permissions for the building on weekends?` | `(none)` | **`agent-harness-config`** | Also in §5. The only guard row where the forbidden skill was runner-up. |

None of these is a defect *today*. All nine are the rows to re-run first after any description edit,
and all nine are where a real-runtime run is most likely to diverge from this simulation.

---

## 7. Full log

```
Install set tested:  simulated full 121-skill listing (name + description only; no bodies)
Method:              blind-router simulation, 8 agents x 10 opaque-id prompts, key withheld in a separate file
Date:                2026-08-18
Client + version:    N/A — not a live-runtime run; see §1 limits
```

| Row | Tier | id | Prompt | Expected | Loaded | Conf | Result |
|---|---|:--|---|---|---|:--:|:--:|
| A1.must-load | A | P047 | Review this Python module and tell me what a principal engineer would change before it ships. | LOAD elite-python-engineer | elite-python-engineer | 5 | **PASS** |
| A1.near-miss | A | P067 | Walk me through reviewing a teammate's pull request without being a jerk about it. | NOT elite-python-engineer | git-and-code-review | 4 | **PASS** |
| A2.must-load | A | P033 | Give me a production-grade FastAPI service layout — typing, logging, error handling, the works. | LOAD elite-python-engineer | elite-python-engineer | 3 | **PASS** |
| A2.near-miss | A | P027 | What HTTP status code should I return when validation fails on a POST? | NOT elite-python-engineer | backend-api-development | 5 | **PASS** |
| A3.must-load | A | P014 | I've got a CSV I've never opened. What should I look at first before I trust any number from it? | LOAD exploratory-data-analysis | exploratory-data-analysis | 4 | **PASS** |
| A3.near-miss | A | P012 | Which is the defensible measure of a typical value when the distribution is badly skewed? | NOT exploratory-data-analysis | descriptive-statistics | 5 | **PASS** |
| A4.must-load | A | P062 | Report the centre and spread of this column and justify the choice for publication. | LOAD descriptive-statistics | descriptive-statistics | 5 | **PASS** |
| A4.near-miss | A | P028 | What does one row of this table actually represent? | NOT descriptive-statistics | exploratory-data-analysis | 5 | **PASS** |
| A5.must-load | A | P013 | Put my numeric predictors on the same scale before I fit the model. | LOAD feature-engineering | feature-engineering | 5 | **PASS** |
| A5.near-miss | A | P007 | Half my rows have blanks in three columns and I need to fix the file itself. | NOT feature-engineering | data-cleaning | 3 | **PASS** |
| A6.must-load | A | P060 | The city column has "NY", "N.Y." and "New York" all meaning the same thing. Make it consistent. | LOAD data-cleaning | data-cleaning | 5 | **PASS** |
| A6.near-miss | A | P041 | Write the one-page instruction sheet so everyone runs this the same way. | NOT data-cleaning | standard-work | 5 | **PASS** |
| A7.must-load | A | P021 | Everyone on the team does this differently. Write it down so there's one way. | LOAD standard-work | standard-work | 5 | **PASS** |
| A7.near-miss | A | P079 | Normalize these category labels so the group-by stops splitting. | NOT standard-work | data-cleaning | 5 | **PASS** |
| A8.must-load | A | P064 | Turn this finding into a short deck for the leadership meeting on Thursday. | LOAD assertion-evidence-deck | assertion-evidence-deck | 5 | **PASS** |
| A8.near-miss | A | P026 | Write the two-paragraph bottom-line-first memo for the exec, no slides. | NOT assertion-evidence-deck | executive-briefing | 5 | **PASS** |
| A9.must-load | A | P001 | Score this classifier — I need to know if it's actually any good before we ship it. | LOAD model-evaluation | model-evaluation | 5 | **PASS** |
| A9.near-miss | A | P008 | Set up the weekly status cadence and intervention log for this project. | NOT model-evaluation | project-command-center | 4 | **PASS** |
| A10.must-load | A | P015 | I need to pull all the records out of a vendor's API, but it only returns 100 at a time. | LOAD rest-api-data-pulls | rest-api-data-pulls | 5 | **PASS** |
| A10.near-miss | A | P035 | Design the paginated endpoint my own API should expose. | NOT rest-api-data-pulls | backend-api-development | 5 | **PASS** |
| A11.must-load | A | P010 | Compute a running total per customer ordered by date in SQL. | LOAD sql-for-analysts | sql-for-analysts | 5 | **PASS** |
| A11.near-miss | A | P038 | This query takes 40 seconds and the ORM generated it. | NOT sql-for-analysts | database-and-orm | 5 | **PASS** |
| B1.must-load | B | P023 | Standardize this. | none / clarify | (none) | 1 | **PASS** |
| B2.must-load | B | P030 | Give me the five-number summary and the coefficient of variation. | LOAD descriptive-statistics | descriptive-statistics | 5 | **PASS** |
| B3.must-load | B | P029 | Show me the confusion matrix and pick an operating threshold. | LOAD model-evaluation | model-evaluation | 5 | **PASS** |
| B4.must-load | B | P002 | Which fields are missing and should I impute or drop those rows? | LOAD data-cleaning | data-cleaning | 4 | **PASS** |
| B5.must-load | B | P050 | Read this diff and tell me if it's safe to merge. | LOAD git-and-code-review | git-and-code-review | 5 | **PASS** |
| B6.must-load | B | P076 | Write me a pandas script to summarize this spreadsheet. | LOAD python-for-analysts | python-for-analysts | 3 | **PASS** |
| C1.over-trigger-guard | C | P004 | Which branch of the company handles refunds? | NOT git-and-code-review | (none) | 5 | **PASS** |
| C2.over-trigger-guard | C | P077 | I need to commit to a decision by Friday — help me think it through. | NOT git-and-code-review | (none) | 3 | **PASS** |
| C3.over-trigger-guard | C | P049 | Who should lead this project, and what's the lag before we see results? | NOT sql-for-analysts | (none) | 2 | **PASS** |
| C4.over-trigger-guard | C | P069 | What's the range of salaries we should offer, and is remote on the table? | NOT descriptive-statistics | (none) | 3 | **PASS** |
| C5.over-trigger-guard | C | P016 | Rank these three vendors for me on price and support. | NOT sql-for-analysts | (none) | 1 | **PASS** |
| C6.over-trigger-guard | C | P034 | Give me feedback on my cover letter. | NOT reflective-learner | sparring-partner | 3 | **PASS** |
| C7.over-trigger-guard | C | P066 | My memory is terrible — how do I stop forgetting people's names? | NOT hierarchical-memory-manager | spaced-retrieval-learning | 3 | **PASS** |
| C8.over-trigger-guard | C | P070 | Book me a travel agent for the Denver trip. | NOT agentic-workflow-design | (none) | 5 | **PASS** |
| C9.over-trigger-guard | C | P025 | There's too much waste in our packaging — can we use less cardboard? | NOT value-stream-mapping | (none) | 1 | **PASS** |
| C10.over-trigger-guard | C | P031 | Refactor this paragraph so it reads better. | NOT elite-python-engineer | adams-smart-brevity | 3 | **PASS** |
| C11.over-trigger-guard | C | P055 | What are the visitor permissions for the building on weekends? | NOT agent-harness-config | (none) | 1 | **PASS** |
| C12.over-trigger-guard | C | P074 | Investigate why the office coffee order keeps arriving late. | NOT dynamic-analysis-engine | root-cause-analysis | 4 | **PASS** |
| D1.by-name | D | P017 | Get gonzo on this quarterly report. | LOAD gonzo | gonzo | 5 | **PASS** |
| D1.in-scope | D | P053 | Give this a savage, first-person take — I want the reader to feel it. | LOAD gonzo | gonzo | 3 | **PASS** |
| D1.out-of-scope | D | P080 | Proofread this quarterly report for typos and grammar. | NOT gonzo | (none) | 3 | **PASS** |
| D2.by-name | D | P005 | Bring in Pythagoras for this module. | LOAD elite-python-engineer | elite-python-engineer | 5 | **PASS** |
| D2.in-scope | D | P072 | Refactor this module to production standards — typing, logging, error handling. | LOAD elite-python-engineer | elite-python-engineer | 4 | **PASS** |
| D2.out-of-scope | D | P063 | What's the difference between a list and a tuple in Python? | NOT elite-python-engineer | (none) | 4 | **PASS** |
| D3.by-name | D | P018 | Chicken Little, look at this integration. | LOAD chicken-little | chicken-little | 4 | **PASS** |
| D3.in-scope | D | P045 | The sky is falling on this integration — walk me through it. | LOAD chicken-little | chicken-little | 4 | **PASS** |
| D3.out-of-scope | D | P058 | What could go wrong with this integration? | NOT chicken-little | fmea | 3 | **PASS** |
| D4.by-name | D | P040 | Be my sparring partner on this strategy. | LOAD sparring-partner | sparring-partner | 5 | **PASS** |
| D4.in-scope | D | P003 | Tear this strategy apart and be honest about it. | LOAD sparring-partner | sparring-partner | 5 | **PASS** |
| D4.out-of-scope | D | P061 | Summarize this strategy document in three bullets. | NOT sparring-partner | (none) | 3 | **PASS** |
| D5.by-name | D | P037 | Run precog on the next two quarters. | LOAD minority-report | minority-report | 5 | **PASS** |
| D5.in-scope | D | P036 | Branch the futures — what happens if demand drops 20%? | LOAD minority-report | minority-report | 5 | **PASS** |
| D5.out-of-scope | D | P019 | What were last quarter's actual numbers? | NOT minority-report | (none) | 1 | **PASS** |
| D6.by-name | D | P042 | Deploy the Foreman on this codebase. | LOAD the-foreman | the-foreman | 5 | **PASS** |
| D6.in-scope | D | P065 | Is this ready to build on, or is it half-built? | LOAD the-foreman | the-foreman | 5 | **PASS** |
| D6.out-of-scope | D | P078 | Write the release notes for this version. | NOT the-foreman | technical-documentation | 3 | **PASS** |
| D7.by-name | D | P024 | Comrade Engineer — is there a pencil for this? | LOAD soviet-space-graphite | soviet-space-graphite | 5 | **PASS** |
| D7.in-scope | D | P006 | Are we overengineering this? Is there a simpler solution? | LOAD soviet-space-graphite | soviet-space-graphite | 5 | **PASS** |
| D7.out-of-scope | D | P044 | Implement the design we agreed on last week. | NOT soviet-space-graphite | script-wizard | 2 | **PASS** |
| D8.by-name | D | P032 | Weight of the books on this schema. | LOAD weight-of-the-books | weight-of-the-books | 5 | **PASS** |
| D8.in-scope | D | P056 | Will it hold at real volumes, or did we test it empty? | LOAD weight-of-the-books | weight-of-the-books | 5 | **PASS** |
| D8.out-of-scope | D | P073 | Write the migration to add this column. | NOT weight-of-the-books | database-and-orm | 4 | **PASS** |
| E1.must-load | E | P075 | My extraction prompt returns valid JSON about 70% of the time. How do I make it reliable? | LOAD prompt-engineering | prompt-engineering | 5 | **PASS** |
| E1.near-miss | E | P020 | My agent loops forever calling tools — how do I bound it? | NOT prompt-engineering | agentic-workflow-design | 4 | **PASS** |
| E2.must-load | E | P043 | We're moving this system prompt to a reasoning model. It says "think step by step" — what changes? | LOAD prompt-engineering | prompt-engineering | 5 | **PASS** |
| E2.near-miss | E | P057 | Before my grader model picks a prompt version, how do I show its scores can be trusted? | NOT prompt-engineering | measurement-systems-analysis | 5 | **PASS** |
| E3.must-load | E | P022 | My tests pass individually but fail when run together, and rows leak between them. | LOAD testing-strategy | testing-strategy | 5 | **PASS** |
| E3.near-miss | E | P011 | Why is SQLite ignoring my foreign key constraint? | NOT testing-strategy | database-and-orm | 5 | **PASS** |
| E4.must-load | E | P054 | Postgres says too many connections and my app has eight workers. | LOAD database-and-orm | database-and-orm | 5 | **PASS** |
| E4.near-miss | E | P039 | How do I test that a 409 comes back on a duplicate insert? | NOT database-and-orm | testing-strategy | 4 | **PASS** |
| E5.must-load | E | P046 | My forecast beats seasonal-naive on MASE — is it good enough to ship? | LOAD time-series-forecasting | time-series-forecasting | 4 | **PASS** |
| E5.near-miss | E | P051 | How wide should the error bars on this single average be? | NOT time-series-forecasting | statistical-inference | 4 | **PASS** |
| E6.must-load | E | P052 | Revenue per user is zero-inflated with a long tail. Which test compares the two groups? | LOAD statistical-inference | statistical-inference | 5 | **PASS** |
| E6.near-miss | E | P059 | How long should I run the experiment and how many users per arm? | NOT statistical-inference | ab-test-design | 4 | **PASS** |
| E7.must-load | E | P071 | The test is underpowered and I can't get more traffic. | LOAD ab-test-design | ab-test-design | 4 | **PASS** |
| E7.near-miss | E | P009 | Is this difference statistically significant? | NOT ab-test-design | statistical-inference | 5 | **PASS** |
| E8.must-load | E | P068 | My AUC is 0.93 but the alert queue is almost all false positives. | LOAD model-evaluation | model-evaluation | 4 | **PASS** |
| E8.near-miss | E | P048 | Which features should I build from these timestamps? | NOT model-evaluation | feature-engineering | 5 | **PASS** |

**Legend.** `Expected` shows the polarity from the withheld key: `LOAD x` = skill x must load;
`NOT x` = skill x must not load (any other answer, including `(none)`, passes). `Conf` is the routing
agent's self-reported confidence 1–5, recorded before scoring. Row ids map to the protocol tables in
`trigger-test.md`; prompt ids are the opaque labels the routing agents saw.

---

## What to do next

1. **Do not edit any description on the strength of this document.** Zero failures means zero
   evidenced fixes.
2. **Run the degraded regime.** The one thing this simulation cannot touch is the finding the protocol
   is most worried about. Present the same 80 prompts against a **name-only listing** (names, no
   descriptions) and score again. The gap between that run and this one is the actual measurement of
   truncation risk — and it would also put a number on the `~100 skills` landmark instead of
   inheriting it from one observation.
3. **Fix Tier D before re-running it.** Rewrite the in-scope column so no prompt contains a substring
   of the target's trigger list (§4). As written it cannot detect name-only reachability.
4. **Run the real thing for the fragile rows.** The seven §5 routes and nine §6 seams are 14 distinct
   rows. That is a tractable number of fresh live sessions and would convert the weakest part of this
   result into runtime evidence.
5. **Keep the blind harness.** Structural withholding of the key cost nothing and is the only reason
   this run's number can be discussed at all.

---

# Tier C run — 2026-08-18 (all 16 guards, blind)

**16/16 guards PASS. 0 OVER.** Method as above: four fresh agents, only the 121 name+description
pairs plus opaque-id prompts, answer key withheld structurally. Three decoy prompts that *should*
load a skill were mixed in, so a panel that simply abstained on everything would score badly rather
than perfectly.

## The four new rows (C13–C16) and why they exist

`script-wizard` claims "improve any script, tool, document, or technical artifact of real substance
— even when phrased casually". Two independent methods flagged that breadth: the five-lens trim
ranking placed it **2nd of 121 on reach while every other lens placed it near the bottom** — its
largest single disagreement — and the Tier D re-run watched it absorb a prompt belonging to
`elite-python-engineer`. Each row hands it a casual phrasing whose substance another skill owns.

| Row | Prompt | Trigger at fault | Result | Landed on |
|---|---|---|---|---|
| C13 | "Half the rows in this export have blanks and the dates come in three different formats. Clean this up." | `clean this up` | PASS | `data-cleaning` (conf 5) |
| C14 | "Here's the diff for my branch — review this code before I open the PR." | `review this code` | PASS | `git-and-code-review` (conf 5) |
| C15 | "Our onboarding takes eleven days and nobody can say why. Improve this process." | `improve this process` | PASS | `value-stream-mapping` (conf 4) |
| C16 | "Our refund policy has an edge case people keep exploiting. Stress test it." | `stress test` | PASS | `rule-stress-testing` (conf 5) |

**Each landed on the correct owner, which is a stronger result than "did not load script-wizard".**
A guard only proves the skill stayed out of the way; landing on the right neighbour proves the
neighbour was reachable through the same words. Note that the two seam repairs shipped just before
this run had already moved `script-wizard` from *winning* two Tier D prompts to *runner-up* on both.

## The decoy that failed was my prompt, not the library

X3 — "Write me a Python script that pulls yesterday's export and flags anything unusual" — expected
`script-wizard` and got `coding-agent-skills:python-for-analysts` (conf 3).

That is my authoring error, and worth recording rather than filing as a defect. The prompt is
adapted from script-wizard's own eval, which reads "Write me a **script** that pulls yesterday's
transaction export…" — no language named. I added the word "Python", and `python-for-analysts` owns
the bare trigger `python` and is scoped to "scripting an analysis, automating a repetitive task".
For a prompt that says Python *and* describes analyst data work, `python-for-analysts` is the better
answer. The decoy was steered by one word I put there.

**This is the third time in this protocol's history that a test prompt, not a description, was the
defect** — after Tier D v1 (generic prompts that were really in-scope) and Tier D v2 (in-scope
prompts carrying the target's own trigger). The standing lesson: before scoring a routing prompt,
check it against *every* skill's trigger list, not just the target's.

## The remaining watch item

`C2` ("I need to commit to a decision by Friday") passed but loaded `minority-report` at confidence
2, and `C9` ("My memory is terrible…") loaded `spaced-retrieval-learning` at confidence 2. Both are
correct-by-the-letter — neither is the guarded skill — but both are weak pulls into a skill whose
own scope note arguably excludes the request. They are guards that held on reasoning rather than on
absence of a matching word, which is the capability most at risk under name-only listing truncation.
