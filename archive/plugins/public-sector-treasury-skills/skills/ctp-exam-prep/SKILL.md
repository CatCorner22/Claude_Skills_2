---
name: ctp-exam-prep
description: >-
  Coaches structured preparation for the Certified Treasury Professional (CTP) exam: maps the
  exam's domain areas to skills the analyst already exercises daily, builds a spaced-repetition
  study plan weighted by blueprint weight and personal weakness, generates CTP-style practice
  questions to drill weak areas (working capital, cash and liquidity management, capital
  markets, risk, treasury operations and controls, banking relationships), and teaches exam
  technique — always confirming blueprint and eligibility against AFP's current publications.
  Use when studying for the CTP, requesting practice questions, or building a certification
  study plan. Triggers: CTP, certified treasury professional, treasury certification, CTP
  exam, practice questions treasury, study plan CTP, AFP certification.
---

# CTP exam prep

## When to use
- Building a study plan for the Certified Treasury Professional exam, from months out or weeks
  out.
- Requesting practice questions, drills, or a mock-exam session on any treasury domain.
- Diagnosing weak domains, reviewing an error log, or learning exam technique.
- Not for: studying for a Lean/quality certification → see
  `continuous-improvement-skills:dmaic-problem-solving`. For actually *doing* the treasury
  work the exam tests, use the underlying skills directly (e.g.
  `cash-management-skills:cash-positioning`, `banking-skills:payment-rails`,
  `finance-skills:short-term-investments`).

## Do it
1. **Confirm the current exam facts first.** AFP periodically revises the exam content outline
   (domains and weights), the underlying *Essentials of Treasury Management* (ETM) edition,
   eligibility requirements, testing windows, and calculator policy. Pull these from AFP's
   current publications before planning — a plan built on an old blueprint drills the wrong
   map. Everything below adapts to whatever the current outline says.
2. **Baseline yourself against the domains.** List the current domains (recent outlines cover
   the ground of: the treasury function and ethics; working capital management; cash and
   liquidity management and forecasting; payments and banking relationships; short-term
   investing and borrowing / capital markets; treasury operations, technology, and controls;
   financial risk management). For each: rate confidence 1–5, note whether your daily work
   exercises it, and compute priority = blueprint weight × (6 − confidence). Public-university
   analysts typically score high on cash positioning, payments, and controls, and lower on
   corporate finance, FX/derivatives, and working capital metrics — but measure, don't assume.
3. **Map each domain to the library you already use.** The study material *is* this skill
   library: working capital → `finance-skills:working-capital-management` and
   `finance-skills:financial-ratios`; cash/liquidity → `cash-management-skills:cash-positioning`,
   `cash-management-skills:cash-forecasting`, `cash-management-skills:liquidity-management`;
   payments/banking → `banking-skills:payment-rails`, `banking-skills:bank-account-structure`,
   `banking-skills:bank-fee-analysis`; investments/borrowing → `finance-skills:short-term-investments`,
   `finance-skills:time-value-of-money`; risk → `finance-skills:fx-risk-basics`,
   `treasury-accounting-skills:hedging-and-derivatives`; operations/controls →
   `cash-management-skills:cash-management-controls`. Reading a skill's "Why / learn" section
   and then answering questions on it is a study session.
4. **Build the calendar with spaced repetition.** Work backward from the exam date. Each domain
   gets three passes: **learn** (read ETM chapter + matching skills, make a one-page concept
   sheet), **drill** (practice questions until ~80% on that domain), **review** (short
   retrieval sessions at expanding intervals — roughly 1 day, 1 week, 1 month after learning).
   Interleave domains rather than finishing one completely before starting the next, and weight
   sessions by the priority scores from step 2. Reserve the final two weeks for full mocks.
5. **Drill with generated questions — used correctly.** Ask for CTP-style items: scenario-based,
   four options, one defensibly best answer, mixing conceptual and computational (day's sales
   outstanding, cash conversion cycle, effective annual cost of trade credit, discount vs
   yield on money-market instruments, collected-balance and earnings-credit math). After every
   question, require the *why* for the right answer **and** why each distractor is wrong — the
   explanation is where the learning happens. Log every miss in an **error log** (domain,
   concept, why missed); re-drill from the log weekly. Treat generated questions as drills
   calibrated to your weak spots, not as leaked exam content — verify anything surprising
   against the current ETM text. See `references/domain-map-and-drills.md` for question
   patterns and formula inventory.
6. **Train exam technique separately.** Compute your time budget per question from the current
   exam length and stick to it in mocks; first pass answers everything answerable, flagging the
   rest; eliminate distractors before choosing; answer every question if (as historically) there
   is no penalty for wrong answers — confirm current scoring policy. For computations, write
   the formula before touching numbers; the distractors are usually the results of predictable
   mistakes (wrong day-count, gross vs net, rate vs yield).
7. **Finish with full mocks and review.** Two or more timed, full-length mocks in the last two
   weeks; after each, spend as long reviewing as testing, folding misses into the error log.
   Taper before exam day — retrieval strength beats one more cram.

## Why / learn
Everything in this plan is applied learning science. **Retrieval practice** (answering
questions) builds durable memory far better than rereading — struggling to recall *is* the
strengthening event, which is why the plan drills from day one instead of "reading first,
practicing later." **Spaced repetition** works because memories consolidate when revisited at
expanding intervals just as they begin to fade; massed cramming feels productive precisely
because it is easy, and easy practice is weak practice. **Interleaving** domains forces you to
select the right method per question — exactly the discrimination the real exam demands, since
it shuffles domains item by item. Mapping domains to your daily work exploits **elaborative
encoding**: new material anchored to existing experience sticks; but note the inverse lesson —
the exam grades against **AFP's textbook framing and vocabulary**, not your shop's. Where your
practice differs from ETM's idealized treasury (a university's fund-driven world differs from
the corporate treasury ETM assumes), deliberately learn the textbook answer and file your
reality as a footnote. Weighting by blueprint-weight × weakness is just expected-value
maximization: marks come from weighted domains you haven't mastered, not from polishing your
strengths. And the error log matters because misses cluster — people don't miss randomly, they
miss the same three concepts repeatedly until the pattern is surfaced and attacked.

## Common mistakes
- Studying from an outdated blueprint or ETM edition → domains and emphasis shift between
  revisions; confirm the current outline before investing hours.
- Rereading and highlighting instead of retrieval practice → fluency illusion; if you haven't
  answered questions on it, you don't know it yet.
- Skipping strong domains entirely → blueprint weight still applies; keep light review passes
  even where confident.
- Drilling only conceptual questions → the computational items (CCC, EAR of trade credit,
  discount-basis yields, earnings credit) are predictable marks; practice them until mechanical.
- Answering from your institution's practice instead of the textbook's framing → the exam keys
  to ETM; learn its answer even where your shop does it differently.
- Treating generated practice questions as authoritative exam content → they are calibrated
  drills; verify surprises against the current ETM text.
- First timed experience being the real exam → run full mocks under time; pacing is a trained
  skill, not a disposition.

## Tailor to your environment
Record your personal campaign in `references/your-environment.md`: exam window and deadlines,
ETM edition in hand, weekly study-hour budget, the baseline confidence scores from step 2, and
your error log location. Keep anything you'd rather not publish — actual scores, employer
reimbursement details, application status — in `your-environment.private.md`, which is
git-ignored. Blueprint weights, exam length, eligibility, and calculator/scoring policies are
AFP's to change — record *where you confirm them* (AFP's CTP pages and candidate handbook)
rather than pinning numbers here.

## References
- references/domain-map-and-drills.md — domain-to-skill map, study-plan template, practice
  question patterns, computational formula inventory, exam-technique checklist
- references/your-environment.md — your exam date, baseline, budget, error log (add when
  supplied)
