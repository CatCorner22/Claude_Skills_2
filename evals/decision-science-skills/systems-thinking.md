# Evals — decision-science-skills:systems-thinking

## 1. Positive trigger (should load the skill)
> "Our support backlog keeps coming back. Every quarter we run an overtime push and it drops,
> then a few weeks later it's worse than before, and now customer escalations are eating the
> team's day in status meetings. It feels like a vicious cycle — map the feedback loops and tell
> us where to actually intervene."

Expected: skill loads and treats the recurrence as structure, not events. It restates the
behavior over time; identifies the backlog as a stock with arrivals and resolutions as its flows
(and fatigue as a slow stock); drafts the causal-loop diagram from the user's own prose with
signed links, offering a Mermaid render and explicitly inviting correction; classifies the
overtime push as a balancing loop and the fatigue→reopen spiral as reinforcing; marks the delays
and uses them to explain why "we fixed it" and "it's back" are both true; names the
fixes-that-fail archetype; places candidate fixes on the simplified Meadows ladder (labeled as
simplified) and explains why the already-tried quota/overtime push is a parameter-rung move the
structure compensates for; asks who compensates when the backlog is pushed; and specifies
measurements (both flows separately, reopen rate, delay length) with the quantitative test
routed to the data skills. The diagram is presented as a hypothesis to correct, never as proof.

## 2. Near-miss (should NOT load this skill)
> "Our month-end close all waits on one task — the bank-side matching step gates the whole
> calendar. How do we speed up the close?"

Expected: `continuous-improvement-skills:theory-of-constraints` owns single-bottleneck
throughput improvement — five focusing steps, exploit before elevate, subordinate the calendar.
One step gating a whole process is a named, located leverage point; no loop discovery is being
asked for. If systems-thinking loads here, its description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "AP posted 14 duplicate payments in Q2, up from 2 in Q1. Walk the causal chain on this and
> find the root cause."

Expected: `continuous-improvement-skills:root-cause-analysis` owns a single problem's causal
chain — 5 Whys, fishbone, containment vs. cause. "Causal chain" sounds adjacent to causal-loop
diagramming, but the ask is a linear dig into one recurring defect, not the mapping of feedback
structure. The boundary tell: if the why-chain closes on itself (the fifth why lands back on the
first), root-cause-analysis should hand off *to* systems-thinking — not the reverse.

## 3. Quality rubric
A good response:
- **Does the task:** separates stocks from flows correctly (backlog/balance = stock; payment
  run/arrivals = flow) and names each stock's feeding and draining flows; drafts the causal-loop
  diagram from the user's prose with signed links and loop labels, doing the diagramming labor
  itself and handing the result to the human for correction; derives loop polarity by the
  minus-count rule rather than vibes; marks delays explicitly; checks the archetype catalog and
  claims a match only when the predicted loops are actually in the diagram; places every
  candidate intervention on the leverage ladder with the rung named; anticipates policy
  resistance by asking whose goals hold the stock where it is; and ends with a measurement plan
  (both flows, stock trajectory, delay length, one loop-specific tell) plus what would falsify
  the diagram.
- **Teaches:** explains why event-thinking cannot explain recurrence; the bathtub intuition (a
  stock moves only through its flows); why delays produce oscillation and overshoot; why
  unintended consequences are usually an undrawn balancing loop; and why higher ladder rungs
  beat parameter-tuning (loops compensate for parameters).
- **Stays honest:** presents the diagram as a hypothesis about structure, not proof; flags
  asserted-but-unobserved links; attributes the field to Forrester, the leverage ladder to
  Meadows (stating the six-rung form is simplified from her twelve), and the archetypes'
  popularization to Senge; invents no statistics; and routes quantitative testing to the data
  skills instead of claiming the diagram settles the question.
