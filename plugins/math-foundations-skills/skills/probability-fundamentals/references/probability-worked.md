# Probability, worked and recomputed

Every table below is built from whole-number counts and cross-checked by summing
rows and columns. If you change an input, rebuild the whole table — the counts must
still sum.

## Contents
1. The rules as counting (plain-language walkthroughs)
2. Mutually exclusive vs independent
3. Conditional probability and the flipped conditional
4. Bayes via natural frequencies — two tables and the odds shortcut
5. Expected value — worked decisions, including EV-yes/ruin-no
6. The fallacy catalog

## 1. The rules as counting
Picture the sample space as a floor of equally likely tiles; an event is a region.

**Complement.** The whole floor is 1, so P(not A) = 1 − P(A). If 22 of 52 cards
qualify, 30 of 52 do not: 22/52 + 30/52 = 52/52 = 1 ✓.

**Addition (overlap subtracted).** Two overlapping regions: adding their areas
counts the lens-shaped overlap twice. Heart or face card in one draw:
- Hearts: 13. Face cards (J, Q, K in four suits): 12. Both at once (J♥, Q♥, K♥): 3.
- Count of distinct qualifying cards: 13 + 12 − 3 = 22.
- P = 22/52 ≈ 42.3%. (Naively adding 13/52 + 12/52 = 25/52 would claim ≈ 48.1% and
  double-count the three face-hearts.)
If the events cannot co-occur, the overlap is 0 and plain addition is correct — that
is the *only* case where it is.

**Multiplication.** The general law is P(A and B) = P(A) × P(B|A): first the chance
of A, then the chance of B *in the world where A happened*.
- Dependent: two aces without replacement = 4/52 × 3/51 = 12/2652 = 1/221 ≈ 0.45%.
  The second factor is 3/51 because the first draw removed an ace from the deck.
- Independent (with replacement): 4/52 × 4/52 = (1/13)² = 1/169 ≈ 0.59%.
Independence is exactly the condition P(B|A) = P(B) — A's happening doesn't move B.

## 2. Mutually exclusive vs independent
These are near-opposites, not synonyms:

| | Mutually exclusive | Independent |
|---|---|---|
| Definition | Cannot co-occur: P(A and B) = 0 | P(A and B) = P(A) × P(B) |
| Knowing A happened | Tells you B did **not** | Tells you nothing about B |
| Dependence | Maximal | None |

One die makes both visible:
- A = "even" {2,4,6}, B = "5 or higher" {5,6}: P(A) = 1/2, P(B) = 1/3,
  P(A and B) = P({6}) = 1/6 = 1/2 × 1/3 → independent.
- A = "even", C = "equals 3": P(A and C) = 0, and P(A | C) = 0 ≠ P(A) = 1/2 →
  mutually exclusive, hence strongly dependent.

Two events with nonzero probabilities can never be both: exclusivity forces
P(A and B) = 0 while independence forces P(A and B) = P(A)P(B) > 0.

## 3. Conditional probability and the flipped conditional
P(A|B) = P(A and B)/P(B) — shrink the universe to the outcomes where B is true,
renormalize, and read off A's share.

Worked: P(5 or higher | even). The universe shrinks to {2, 4, 6} (three tiles); of
those, only {6} qualifies → 1/3. Compare the unconditional P(5 or higher) =
2/6 = 1/3: conditioning on "even" happened not to move it — which is independence
again, seen from the other side.

The flip is never free: P(A|B) and P(B|A) share a numerator but have different
denominators. In section 4's screening table: P(positive | condition) = 90/100 = 90%
while P(condition | positive) = 90/981 ≈ 9.2% — a tenfold gap. Courtroom form (the
prosecutor's fallacy): "the chance of this evidence if innocent is 1 in a million"
is P(evidence | innocent); the verdict needs P(innocent | evidence), and with
millions of innocent people the two can differ enormously. The base rate of
innocence is the missing denominator.

## 4. Bayes via natural frequencies
Method: choose a round crowd; split by the **base rate first**; then apply the
test's behavior to each branch; then read the answer as a ratio of counts.

**Table A — rare-condition screening.** Base rate 1%, sensitivity 90% (of true
cases, 90% test positive), false-alarm rate 9% (of non-cases, 9% test positive).
Crowd: 10,000.

| | Test + | Test − | Total |
|---|---|---|---|
| Condition | 90 | 10 | 100 |
| No condition | 891 | 9,009 | 9,900 |
| Total | 981 | 9,019 | 10,000 |

Cell arithmetic: 10,000 × 1% = 100 with the condition; 100 × 90% = 90 true
positives; 100 − 90 = 10 missed. 10,000 − 100 = 9,900 without; 9,900 × 9% = 891
false alarms; 9,900 − 891 = 9,009 correct negatives. Column check: 90 + 891 = 981
positives; 10 + 9,009 = 9,019 negatives; 981 + 9,019 = 10,000 ✓.

Read-off: P(condition | positive) = 90/981 = 10/109 ≈ **9.2%**. Nine positives in
ten are false — with a 1% base rate, even a 90%-sensitive, 91%-specific test mostly
alarms on healthy people, because 9% of 9,900 out-produces 90% of 100.

Formula check (same answer, hidden denominators):
P = (0.01 × 0.90) / (0.01 × 0.90 + 0.99 × 0.09) = 0.009 / (0.009 + 0.0891)
= 0.009/0.0981 ≈ 0.0917 ✓.

**Odds shortcut.** Posterior odds = prior odds × likelihood ratio.
Prior odds: 100:9,900 = 1:99. Likelihood ratio: 90%/9% = 10.
Posterior odds: 10:99 → probability 10/109 ≈ 9.2% ✓ (matches the table exactly).

**Table B — fraud flag.** Base rate 0.5%, detection 98%, false-alarm rate 2%.
Crowd: 10,000 payments.

| | Flagged | Passed | Total |
|---|---|---|---|
| Fraudulent | 49 | 1 | 50 |
| Legitimate | 199 | 9,751 | 9,950 |
| Total | 248 | 9,752 | 10,000 |

Cell arithmetic: 10,000 × 0.5% = 50 fraudulent; 50 × 98% = 49 caught; 1 slips
through. 9,950 × 2% = 199 false flags; 9,950 − 199 = 9,751 passed. Checks:
49 + 199 = 248 flagged; 1 + 9,751 = 9,752 passed; 248 + 9,752 = 10,000 ✓.

Read-off: P(fraud | flagged) = 49/248 ≈ **19.8%**. Four of five flags are false even
with a 98%-detection, 98%-specific screen — and the review queue is 248 items to
catch 49. Improving the flag-precision means either raising the base rate of what
enters the screen (pre-filtering) or cutting the false-alarm rate; better detection
of true fraud barely moves it (a perfect 50/249 ≈ 20.1%).

## 5. Expected value — worked decisions
EV = Σ probability × payoff: the long-run average per play.

**Decision 1 — take the repeatable small bet.** 80% win 500, 20% lose 1,500, offered
monthly, stakes small next to your resources.
EV = 0.8 × 500 − 0.2 × 1,500 = 400 − 300 = **+100** per play. Repeatable and
survivable → EV is the right summary; take it and expect ≈ +100 × plays over time.

**Decision 2 — EV says yes, ruin says no.** A firm holding 2,000 total can take a
one-shot venture: 80% chance of gaining 5,000, 20% chance of losing 2,000 — all of
it. EV = 0.8 × 5,000 − 0.2 × 2,000 = 4,000 − 400 = **+3,600**: hugely positive. But
this is one draw, and one branch is insolvency. There is no long run in which the
average materializes — 20% of the time the game simply ends. Positive EV cannot
answer "can we survive the loss?"; that answer comes from the balance sheet, not the
average. (Same logic in reverse makes insurance rational: the premium exceeds the
expected loss — negative EV by construction — and buying it is still sound, because
it deletes the ruin branch.)

**Decision 3 — ruin by repetition.** Bet your entire stake each flip: heads +50%,
tails −40%, fair coin.
- EV per flip: 0.5 × 0.5 + 0.5 × (−0.4) = +5% — positive.
- Typical (median) path: half heads, half tails → per-two-flips factor
  1.5 × 0.6 = 0.9, so per-flip factor √0.9 ≈ 0.949 — about −5.1% per flip.
- After 20 flips: EV multiplier 1.05²⁰ ≈ 2.65, but the median path is
  0.9¹⁰ ≈ 0.35 — typical wealth is down two-thirds while the average is up 165%.
  The average is dragged up by a few enormous lucky paths you will almost surely not
  be on. Repeated outcomes multiply, so the geometric factor — not the arithmetic
  EV — governs what actually happens to one player (see
  `math-foundations-skills:exponential-growth-and-logs`).

When EV **is** the right summary: many independent repeats, each small relative to
the bankroll, outcomes settled additively (not reinvested wholesale). That is the
insurer's side of the table, and it is why casinos and insurers profit from bets
that individuals rightly refuse.

## 6. The fallacy catalog
Each entry: the failure, a counted example, and the one-line inoculation.

**Base-rate neglect.** Judging by fit-of-evidence alone. Table A: the test is 90%
accurate in the direction quoted, yet a positive means only 9.2% — because the base
rate is 1%. *Inoculation: "How common is this before I look at the evidence?"*

**Gambler's fallacy.** Expecting deviations to correct. After 5 heads,
P(heads) = 1/2 still: P(5 heads) = 1/32 ≈ 3.1% is a statement about the *future*
sequence from the start, not about the next flip once 4 heads are sunk. The long
run levels out by swamping — 10 extra heads vanish inside 10,000 further flips —
not by tails being owed. *Inoculation: "The coin has no memory; the law of averages
works by dilution, not correction."*

**Conjunction fallacy.** Rating "A and B" as likelier than A because the pair tells
a better story (Tversky and Kahneman's Linda problem). Counting kills it: every
world with A-and-B is a world with A, so P(A and B) ≤ P(A) — always. Detail makes
stories more plausible and events less probable. *Inoculation: "Does the added
detail add cases or remove them? It can only remove."*

**Hot hand vs small samples.** Reading a short streak as a changed process. Random
sequences are streakier than intuition expects, so a handful of makes or misses is
weak evidence about skill or regime change in either direction. Honesty note: the
research seesaw runs both ways — later analyses (Miller and Sanjurjo) showed the
classic studies "debunking" the hot hand carried a subtle selection bias, so
overclaiming "streaks are always an illusion" is itself an overread. The durable
lesson is about evidence weight: small samples cannot carry strong conclusions.
*Inoculation: "How many observations is this streak, and what would chance alone
produce in a sample this size?"*
