# Trigger test protocol

**Status: written 2026-08-17, revised 2026-08-18. Two blind-router simulation runs; the live
fresh-session run specified below has still never been performed.**

- **Run 1 (2026-08-18) — 80/80 PASS, partly unearned.** Eight fresh agents, 121 name+description
  pairs, ten opaque-id prompts each, answer key withheld in a separate file. Results, method, and
  limits: [`trigger-test-results.md`](trigger-test-results.md). Read §1 and §4 before treating the
  100% as a clean bill of health: **Tier D's result did not count**, because seven of its eight
  in-scope prompts contained a literal trigger phrase of their own target, so that column asked the
  same question as the by-name column.
- **Run 2 — Tier D re-run (2026-08-18) — 41/45.** Tier D rewritten (0 trigger leakage, verified by
  `scripts/check-trigger-test.py`) and extended from 8 rows to 15, then re-executed with five fresh
  agents and the key withheld structurally. by-name 15/15 · in-scope **11/15** · out-of-scope 15/15.
  **11 HEALTHY · 4 NAME-ONLY (`gonzo`, `elite-python-engineer`, `chicken-little`,
  `chicken-little-executive-advisor`) · 0 OVER.** Write-up:
  [`trigger-test-tier-d-rerun.md`](trigger-test-tier-d-rerun.md).

Both runs test whether the descriptions *can* be routed correctly by a careful reader, **not**
whether the runtime router does so, and neither reproduces name-only listing truncation. A
simulation is an upper bound on live performance.

This is the compliance record for the one
definition-of-done item in `writing-agent-skills/references/review-checklist.md` that no skill in
this library has ever met — the fresh-session trigger test. Four review passes checked conformance,
arithmetic, and link integrity. None of them could tell you whether a single skill actually *routes*,
because routing cannot be tested from inside the session that authored the skill.

Running this protocol is the only thing that converts "valid and conformant" into "findable."

---

## Why a trigger test cannot be faked

Three properties of the runtime make every cheaper substitute worthless:

1. **The router sees only `name` + `description`.** Not the body, not the references. A skill whose
   body brilliantly covers your question is invisible if the description does not carry the scent.
2. **`/plugin:skill` direct invocation always works** — including for a skill the router would never
   reach on its own. So the path an author naturally uses to test their own skill is exactly the path
   that cannot detect the failure.
3. **The listing degrades silently at scale.** Observed at roughly 100 installed skills: the least-used
   skills' descriptions are trimmed to **name-only**, with no error. This library ships 121 skills
   (~29,640 tokens, **14.8% of a 200K window** — see the install-cost table in `README.md`). A full
   install is therefore *past* the observed degradation threshold, which means results from a
   121-skill session and a 40-skill session are different experiments. **Record which install you
   tested.**

Corollary: pasting a trigger phrase verbatim proves nothing. Every prompt below is deliberately
written in *natural user language* that avoids the exact trigger string, because that is the only
thing the test can usefully measure.

---

## Setup

1. **Choose and record an install set.** Either:
   - **Full install** (121 skills, 14.8% of context) — tests the real degradation regime; or
   - **Focused install** — the plugins covering the rows you are testing. Cheaper, cleaner
     attribution, but it will *not* reproduce name-only trimming.

   Note the set at the top of your log. A pass under a focused install is not evidence of a pass
   under a full one.

2. **One fresh session per row.** This is not optional and it is the expensive part. Once a skill is
   loaded its body is in context and biases every later turn in that session, so a second prompt in
   the same session tests nothing. **Budget accordingly: 52 rows carry 101 distinct prompts**, so a
   full run is up to 101 fresh sessions. A cheaper first pass is 52 sessions — the must-load column
   only — following up on the other columns for anything that passes.

   | Tier | Rows | Prompts/row | Prompts |
   |---|---:|---:|---:|
   | A — routes that lost their phrases | 11 | 2 | 22 |
   | B — did the moved phrases land? | 6 | 1 | 6 |
   | C — over-trigger guards | 12 | 1 | 12 |
   | D — name-gated skills | 15 | 3 | 45 |
   | E — skills rewritten this session | 8 | 2 | 16 |
   | **total** | **52** | | **101** |

3. **Paste the prompt verbatim.** No preamble, no "can you", no follow-up clarification. Any editing
   makes the row unrepeatable.

4. **Record what loaded, not what was answered.** Skills announce themselves in the transcript. If
   your client does not show it, ask as the *second* turn: "Which skills did you load for that?" —
   never as the first.

## Scoring a row

| Result | Meaning |
|---|---|
| **PASS** | The expected skill loaded. |
| **PASS+** | Expected skill loaded *and* the near-miss prompt correctly did not load it. |
| **MISS** | Nothing loaded, or something unrelated loaded. The description lacks the scent. |
| **WRONG** | A *different, plausible* skill loaded. This is a seam defect, not a description defect — two descriptions are competing and neither names the boundary. |
| **OVER** | The near-miss prompt loaded the skill. It is too pushy. |

**MISS and WRONG have different fixes.** MISS → the description is missing the user's vocabulary; add
it. WRONG → both skills need a reciprocal `Not for: … → see plugin:other-skill` line naming the
boundary in matching words. Do not fix a WRONG by deleting the loser's trigger — that is what created
the orphaned-phrase defect recorded in Tier C.

---

## Tier A — routes that gave up their most natural phrases (highest risk)

These nine skills lost trigger phrases during this session's collision surgery. Each row uses the
vocabulary a real user would reach for, *not* the qualified replacement phrase. A MISS here means the
surgery broke a live route.

| # | Prompt (paste verbatim) | Must load | Near-miss prompt | Must NOT load |
|---|---|---|---|---|
| A1 | `Review this Python module and tell me what a principal engineer would change before it ships.` | `full-stack-dev-skills:elite-python-engineer` | `Walk me through reviewing a teammate's pull request without being a jerk about it.` | elite-python-engineer (should be `git-and-code-review`) |
| A2 | `Give me a production-grade FastAPI service layout — typing, logging, error handling, the works.` | `full-stack-dev-skills:elite-python-engineer` | `What HTTP status code should I return when validation fails on a POST?` | elite-python-engineer (should be `backend-api-development`) |
| A3 | `I've got a CSV I've never opened. What should I look at first before I trust any number from it?` | `data-analytics-bi-skills:exploratory-data-analysis` | `Which is the defensible measure of a typical value when the distribution is badly skewed?` | exploratory-data-analysis (should be `descriptive-statistics`) |
| A4 | `Report the centre and spread of this column and justify the choice for publication.` | `data-analytics-bi-skills:descriptive-statistics` | `What does one row of this table actually represent?` | descriptive-statistics (should be `exploratory-data-analysis`) |
| A5 | `Put my numeric predictors on the same scale before I fit the model.` | `machine-learning-skills:feature-engineering` | `Half my rows have blanks in three columns and I need to fix the file itself.` | feature-engineering (should be `data-cleaning`) |
| A6 | `The city column has "NY", "N.Y." and "New York" all meaning the same thing. Make it consistent.` | `data-analytics-bi-skills:data-cleaning` | `Write the one-page instruction sheet so everyone runs this the same way.` | data-cleaning (should be `standard-work`) |
| A7 | `Everyone on the team does this differently. Write it down so there's one way.` | `continuous-improvement-skills:standard-work` | `Normalize these category labels so the group-by stops splitting.` | standard-work (should be `data-cleaning`) |
| A8 | `Turn this finding into a short deck for the leadership meeting on Thursday.` | `data-analytics-bi-skills:assertion-evidence-deck` | `Write the two-paragraph bottom-line-first memo for the exec, no slides.` | assertion-evidence-deck (should be `executive-briefing`) |
| A9 | `Score this classifier — I need to know if it's actually any good before we ship it.` | `machine-learning-skills:model-evaluation` | `Set up the weekly status cadence and intervention log for this project.` | model-evaluation (should be `project-command-center`) |
| A10 | `I need to pull all the records out of a vendor's API, but it only returns 100 at a time.` | `data-tools-skills:rest-api-data-pulls` | `Design the paginated endpoint my own API should expose.` | rest-api-data-pulls (should be `backend-api-development`) |
| A11 | `Compute a running total per customer ordered by date in SQL.` | `data-analytics-bi-skills:sql-for-analysts` | `This query takes 40 seconds and the ORM generated it.` | sql-for-analysts (should be `database-and-orm`) |

## Tier B — did the moved phrases land with their new owner?

Tier A tests the skill that *lost* a phrase. These rows test the reciprocal: the skill that was
supposed to *gain* it. A MISS here means a phrase was taken from one skill and delivered to nobody.

| # | Prompt (paste verbatim) | Must load | Why it's at risk |
|---|---|---|---|
| B1 | `Standardize this.` | *(nothing, or a clarifying question)* | **Known defect.** Three skills each held the bare word `standardize`; collision surgery qualified all three, so the bare phrase now has **no trigger owner**. Testing whether a bare ambiguous verb *should* route is the point — a clarifying question is the correct outcome, a confident wrong pick is not. |
| B2 | `Give me the five-number summary and the coefficient of variation.` | `data-analytics-bi-skills:descriptive-statistics` | Received `summary statistics`, `central tendency`, `spread` from exploratory-data-analysis. |
| B3 | `Show me the confusion matrix and pick an operating threshold.` | `machine-learning-skills:model-evaluation` | Received `confusion matrix`, which `project-command-center` had held incorrectly. |
| B4 | `Which fields are missing and should I impute or drop those rows?` | `data-analytics-bi-skills:data-cleaning` | Retained `missing values` after feature-engineering yielded it. |
| B5 | `Read this diff and tell me if it's safe to merge.` | `coding-agent-skills:git-and-code-review` | Holds `code review`, which elite-python-engineer yielded — but elite-python-engineer still advertises "code review" in its description *prose*, so both compete in the router. |
| B6 | `Write me a pandas script to summarize this spreadsheet.` | `coding-agent-skills:python-for-analysts` | Sole owner of bare `python` after elite-python-engineer yielded it. If A1/A2 MISS **and** B6 PASSes, the split is wrong: analyst-grade Python is absorbing production-grade requests. |

## Tier C — over-trigger guards (bare common words)

The library has **285 single-word trigger phrases**. Most are precise jargon (`weibull`, `cpk`,
`duckdb`) and carry no risk. These rows probe the subset that are ordinary English words with a
dominant non-skill meaning — the ones most likely to fire on an unrelated request. Every prompt here
uses the word in its **everyday** sense. Loading the skill is a **failure**.

| # | Prompt (paste verbatim) | Must NOT load | Trigger at fault |
|---|---|---|---|
| C1 | `Which branch of the company handles refunds?` | `coding-agent-skills:git-and-code-review` | `branch`, `commit` |
| C2 | `I need to commit to a decision by Friday — help me think it through.` | `coding-agent-skills:git-and-code-review` | `commit` |
| C3 | `Who should lead this project, and what's the lag before we see results?` | `data-analytics-bi-skills:sql-for-analysts` | `lead`, `lag` |
| C4 | `What's the range of salaries we should offer, and is remote on the table?` | `data-analytics-bi-skills:descriptive-statistics` | `range`, `mode` |
| C5 | `Rank these three vendors for me on price and support.` | `data-analytics-bi-skills:sql-for-analysts` | `rank`, `qualify` |
| C6 | `Give me feedback on my cover letter.` | `metacognition-skills:reflective-learner` | `feedback` |
| C7 | `My memory is terrible — how do I stop forgetting people's names?` | `metacognition-skills:hierarchical-memory-manager` | `memory` |
| C8 | `Book me a travel agent for the Denver trip.` | `coding-agent-skills:agentic-workflow-design` | `agent` |
| C9 | `There's too much waste in our packaging — can we use less cardboard?` | `continuous-improvement-skills:value-stream-mapping` | `waste`, `flow` |
| C10 | `Refactor this paragraph so it reads better.` | `full-stack-dev-skills:elite-python-engineer` | `refactor` (bare, and the skill's broadest remaining route) |
| C11 | `What are the visitor permissions for the building on weekends?` | `coding-agent-skills:agent-harness-config` | `permissions`, `hooks` |
| C12 | `Investigate why the office coffee order keeps arriving late.` | `metacognition-skills:dynamic-analysis-engine` | `investigate` |

> A single OVER here is not automatically a defect — a slightly pushy skill that offers itself and is
> waved off costs one line. An OVER on **C6, C7, C8 or C12** is more serious, because those skills
> load large always-on bodies.

## Tier D — persona-named skills

This library deliberately contains skills named for a persona rather than a task. That is a valid
design *provided* the name reaches the skill, the skill is still findable by someone who does not
know the name, and it does not squat on work outside its scope. Those are three different questions,
so each row asks all three.

**Extended to 15 rows (2026-08-18)** to cover every genuinely name-gated skill in the library, not
just eight of them. `machine-learning-skills:bespoke-llm-architect` is deliberately **excluded**:
it sets `disable-model-invocation: true`, so the router cannot reach it by any prompt and a routing
row for it would measure nothing. It is user-invoke-only by construction — worth knowing, not worth
testing.

**Two by-name prompts deliberately use a name that is NOT in the target's trigger list**, because
the skill's own text presents that name to the user:

- **D11** says "The Commander" — `extreme-ownership`'s description opens `Acts as "The Commander"`,
  but its triggers are `jocko`, `extreme ownership`, `laws of combat`… The persona's own name is
  not among them.
- **D14** says `adams-plain-grade` hyphenated — the skill's When-to-use says "the user asks for
  adams-plain-grade by name", while the trigger reads `adams plain grade` with spaces.

A MISS on either is a finding about the description, not a broken prompt. Read it as: the skill
tells the user a name that does not reach it.

**The middle column has now been wrong twice, in opposite directions.** Version 1 asked only "does
a generic prompt fail to load it?", and six of its eight generic prompts were
paraphrases of trigger phrases those skills *deliberately own* (`is this ready to build on`,
`simpler solution`, `will it hold at real volumes`, `future outcomes`, `how good is this`,
`refactor`). Run as written, it would have recorded correct routing as a defect and invited deleting
a real route. The in-scope column now makes that a **PASS**, and only the third column is a guard.

| # | By-name (must load) | In-scope paraphrase (**should** load) | Out-of-scope (must NOT load) | Skill |
|---|---|---|---|---|
| D1 | `Get gonzo on this quarterly report.` | `Write this up the way a magazine columnist would — first person, in the room, no corporate hedging.` | `Proofread this quarterly report for typos and grammar.` | `writing-skills:gonzo` |
| D2 | `Bring in Pythagoras for this module.` | `This module works but I would not put it in front of a paying customer. Bring it up to the bar you would hold yourself to.` | `What's the difference between a list and a tuple in Python?` | `full-stack-dev-skills:elite-python-engineer` |
| D3 | `Chicken Little, look at this integration.` | `Three dashboards went red this morning and everyone is in a war room. Is this actually an emergency?` | `What could go wrong with this integration?` | `coding-agent-skills:chicken-little` |
| D4 | `Be my sparring partner on this strategy.` | `I have talked myself into this plan and I no longer trust my own judgement on it. Push back hard.` | `Summarize this strategy document in three bullets.` | `coding-agent-skills:sparring-partner` |
| D5 | `Run precog on the next two quarters.` | `Give me three genuinely different ways the next two quarters could go, not a best and worst case.` | `What were last quarter's actual numbers?` | `decision-science-skills:minority-report` |
| D6 | `Deploy the Foreman on this codebase.` | `The team says this feature is done. I do not believe them. How do I check what is actually finished?` | `Write the release notes for this version.` | `coding-agent-skills:the-foreman` |
| D7 | `Comrade Engineer — is there a pencil for this?` | `We have three engineers on a six-month build for something I suspect a spreadsheet could do.` | `Implement the design we agreed on last week.` | `coding-agent-skills:soviet-space-graphite` |
| D8 | `Weight of the books on this schema.` | `It flies in staging with our seed data. What happens in March when the real volume shows up?` | `Write the migration to add this column.` | `safety-and-reliability-skills:weight-of-the-books` |
| D9 | `Deploy advisor on our new pricing model.` | `Tear our new pricing model apart like someone who wants it to fail — where does the whole thing come undone?` | `Summarize the pricing model in a paragraph for the board deck.` | `coding-agent-skills:chicken-little-executive-advisor` |
| D10 | `Deploy compiler on this service.` | `Which single dependency in this service, if it went away tomorrow, takes everything down with it?` | `Add a health-check endpoint to this service.` | `coding-agent-skills:chicken-little-technical-compiler` |
| D11 | `Bring in The Commander on this postmortem.` | `This writeup blames three other teams. Rewrite it so we own our part.` | `Who on the team has capacity to pick up this ticket?` | `coding-agent-skills:extreme-ownership` |
| D12 | `Hold up the mirror on this project.` | `Status says green but I know it isn't. Tell me the real state in plain words.` | `How many hours of sleep should I be getting?` | `coding-agent-skills:stay-hard-accountability` |
| D13 | `Master prompt architect: build me a system prompt.` | `I need a system prompt for a customer-facing agent, and I want the requirements pinned down before you write a line of it.` | `Why does my prompt sometimes return prose instead of JSON?` | `coding-agent-skills:master-prompt-architect` |
| D14 | `Run adams-plain-grade over this notice.` | `Rewrite this so someone who left school at fourteen can act on it without asking anyone.` | `Tighten this memo for the executive team — they have two minutes.` | `writing-skills:adams-plain-grade` |
| D15 | `Run the board on this module.` | `I want several specialists looking at this from different angles at once, not one opinion.` | `Is this function's variable naming consistent with the rest of the file?` | `coding-agent-skills:board-review` |

How to read the three results together:

- **Name loads, in-scope loads, out-of-scope does not** — the skill is healthy. The persona name is
  a convenience, not the only door.
- **Name loads, in-scope MISSES** — the skill is *name-only reachable*. It is not broken, but it is
  invisible to anyone who has not been told its name, and it is the shape most damaged by name-only
  listing degradation. This is the finding to act on, and the fix is adding the user's vocabulary to
  the description — never removing the persona name.
- **Out-of-scope loads (OVER)** — the skill is squatting on general work under an evocative name,
  which is the failure the authoring standard warns about. Qualify the offending trigger.
- **Name MISSES** — the name is not in the description's trigger list, or the listing has trimmed
  this skill. Check the install set before concluding anything.

## Tier E — skills substantively rewritten this session

These bodies changed enough that their descriptions were rewritten with them. Untested vocabulary.

| # | Prompt (paste verbatim) | Must load | Near-miss prompt | Must NOT load |
|---|---|---|---|---|
| E1 | `My extraction prompt returns valid JSON about 70% of the time. How do I make it reliable?` | `coding-agent-skills:prompt-engineering` | `My agent loops forever calling tools — how do I bound it?` | prompt-engineering (should be `agentic-workflow-design`) |
| E2 | `We're moving this system prompt to a reasoning model. It says "think step by step" — what changes?` | `coding-agent-skills:prompt-engineering` | `Before my grader model picks a prompt version, how do I show its scores can be trusted?` | prompt-engineering (should be `measurement-systems-analysis`) |
| E3 | `My tests pass individually but fail when run together, and rows leak between them.` | `full-stack-dev-skills:testing-strategy` | `Why is SQLite ignoring my foreign key constraint?` | testing-strategy (should be `database-and-orm`) |
| E4 | `Postgres says too many connections and my app has eight workers.` | `full-stack-dev-skills:database-and-orm` | `How do I test that a 409 comes back on a duplicate insert?` | database-and-orm (should be `testing-strategy`) |
| E5 | `My forecast beats seasonal-naive on MASE — is it good enough to ship?` | `machine-learning-skills:time-series-forecasting` | `How wide should the error bars on this single average be?` | time-series-forecasting (should be `statistical-inference`) |
| E6 | `Revenue per user is zero-inflated with a long tail. Which test compares the two groups?` | `data-analytics-bi-skills:statistical-inference` | `How long should I run the experiment and how many users per arm?` | statistical-inference (should be `ab-test-design`) |
| E7 | `The test is underpowered and I can't get more traffic.` | `data-analytics-bi-skills:ab-test-design` | `Is this difference statistically significant?` | ab-test-design (should be `statistical-inference`) |
| E8 | `My AUC is 0.93 but the alert queue is almost all false positives.` | `machine-learning-skills:model-evaluation` | `Which features should I build from these timestamps?` | model-evaluation (should be `feature-engineering`) |

---

## Log

Copy this table and fill it in. **Record the install set** — results are not comparable across
different install sizes.

```
Install set tested: ................................ (full 121 / plugins: ..................)
Date: ..............   Client + version: ..............................
```

| Row | Result | What actually loaded | Note |
|---|---|---|---|
| A1 | | | |
| A2 | | | |
| A3 | | | |
| A4 | | | |
| A5 | | | |
| A6 | | | |
| A7 | | | |
| A8 | | | |
| A9 | | | |
| A10 | | | |
| A11 | | | |
| B1 | | | |
| B2 | | | |
| B3 | | | |
| B4 | | | |
| B5 | | | |
| B6 | | | |
| C1 | | | |
| C2 | | | |
| C3 | | | |
| C4 | | | |
| C5 | | | |
| C6 | | | |
| C7 | | | |
| C8 | | | |
| C9 | | | |
| C10 | | | |
| C11 | | | |
| C12 | | | |
| D1 | | | |
| D2 | | | |
| D3 | | | |
| D4 | | | |
| D5 | | | |
| D6 | | | |
| D7 | | | |
| D8 | | | |
| E1 | | | |
| E2 | | | |
| E3 | | | |
| E4 | | | |
| E5 | | | |
| E6 | | | |
| E7 | | | |
| E8 | | | |

## Acting on the results

- **MISS** → add the user's actual vocabulary to the description. The phrase the user typed is the
  evidence; use it, don't invent a synonym for it.
- **WRONG** → write reciprocal `Not for:` lines in *both* skills, naming the boundary in matching
  words. Then re-run both the row and its mirror row.
- **OVER** → qualify the offending trigger (`standardize` → `standardize values`). **Then check that
  the bare phrase still has an owner somewhere** — B1 exists because three skills qualified the same
  word simultaneously and left it orphaned.
- **Two rows disagreeing about the same boundary** (e.g. A1 MISS and B6 PASS) is a seam defect, not
  two description defects. Fix the seam once.

Any change to a description invalidates every row that mentions it. Re-run those rows; do not assume
the fix worked because it looked right.
