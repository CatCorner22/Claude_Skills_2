# Evals — finance-skills:fx-risk-basics

## 1. Positive trigger (should load the skill)
> "We're a USD company. In 90 days we owe a German supplier EUR 2M and we'll collect EUR 1.2M from a
> French customer. EUR/USD is 1.08. Should we hedge, and how — and how much is really at risk?"

Expected: skill loads; classifies this as transaction exposure; nets the EUR 1.2M inflow against the
EUR 2M outflow to a net EUR 0.8M payable; reads the quote direction correctly; recommends a forward (or
natural hedge) on the net at a stated hedge ratio; explains the forward is spot adjusted for the rate
differential, not a forecast, and that hedging removes volatility rather than taking a view.

## 2. Near-miss (should NOT load this skill)
> "Set up a monthly netting cycle so our subsidiaries settle intercompany balances through the treasury
> center instead of paying each other directly."

Expected: this is the operational mechanics of intragroup settlement — the
`cash-management-skills:intercompany-cash-netting` skill should handle it. FX netting informs it but is
not the deliverable. If fx-risk-basics loads as primary, tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** classifies the exposure type, nets offsetting flows before hedging, reads the
  quote correctly, selects an appropriate hedge, and states the hedge ratio and residual.
- **Teaches:** stresses identifying the exposure type first, and that hedging manages volatility on a
  known exposure — it is not speculation and a forward is not a spot forecast.
- **Safe:** nets before hedging, does not hedge translation exposure with cash forwards, does not
  over-hedge or hedge a rate view, and never calls a partial hedge fully covered.
