---
name: anomaly-detection
description: >-
  Detects anomalies and outliers in transactions or time series using statistical and unsupervised
  methods — z-score and robust z (median/MAD), IQR, time-series residual anomalies, and multivariate
  models (isolation forest, local outlier factor, clustering) — with thresholds tuned to the
  precision/recall trade-off under scarce labels, and attention to alert fatigue. Use when flagging
  unusual activity such as reconciliation breaks, fee spikes, duplicate or out-of-pattern payments, or
  possible fraud. Triggers: anomaly detection, anomaly, outlier, outlier detection, unusual transaction,
  fraud detection, isolation forest, local outlier factor, LOF, z-score, novelty detection, unusual activity.
metadata:
  version: "1.3.0"
---

# Anomaly detection

## When to use
- Flagging unusual transactions or values: reconciliation breaks, fee/interest spikes, duplicate or out-of-pattern payments, suspicious activity.
- Finding outliers in a time series (a day's cash movement far from its seasonal norm) or in multivariate transaction data.
- Setting a detection threshold when you have few or no labels, and managing the resulting alert volume.
- Not for: mechanically matching a statement to the ledger and classifying breaks — that is reconciliation, a finance-domain procedure this library does not carry; use this skill to *rank* which breaks are unusual. Designing the control framework alerts feed into is controls work, also outside this library.
- Not for: operating a whole *queue* of detectors — disposition audits, tolerance lists with
  expiry, paging gates, and the economics of alert volume → see
  `safety-and-reliability-skills:detection-system-tuning`. This skill builds and tunes one
  detector; that one runs the system those detectors feed.

## Do it
1. **Define "anomalous" for this context, and the cost of each error.** Decide what unusual means here
   (a value, a pattern, a rate) and weigh a **missed anomaly** against a **false alarm**. In treasury a
   missed fraudulent payment is costly; a wall of false alerts destroys trust — both costs set the threshold.
2. **Start statistical on single features.** For one numeric field, flag points beyond a threshold: the
   classic **z-score**, or better the **robust z-score** using **median and MAD** (resistant to the very
   outliers you're hunting), or the **IQR rule** (below Q1 − 1.5·IQR or above Q3 + 1.5·IQR). Simple, explainable,
   and often enough. See `references/methods-and-thresholds.md`.
3. **For a time series, model the expected value, then flag the residual.** Forecast or decompose the series
   (`machine-learning-skills:time-series-forecasting`) and flag points whose **residual** is large relative to
   the local, season-aware spread — so a normal month-end spike isn't flagged, but an off-pattern one is.
4. **Go multivariate/unsupervised when features interact.** When "unusual" only shows up across several
   fields together (amount + counterparty + hour + channel), use **isolation forest** (fast, scales well),
   **local outlier factor** (density-based, catches local outliers), **DBSCAN** (points in no cluster), or
   **Mahalanobis distance** (correlation-aware). Scale features first for distance-based methods.
5. **Set the threshold by the precision/recall trade-off, not a default.** These methods output a **score**;
   the alert is a cut on it. Tune the cut (contamination rate, score quantile) to your **alert budget** and
   the FP/FN cost. With few labels, estimate precision by having reviewers check a sample of top alerts.
6. **Rank, and say what drove each flag.** Emit a ranked score and route the **top-N** the team can
   actually investigate, rather than a raw binary flag — prioritization is what makes detection usable when
   everything above a hard cutoff would swamp the reviewers. A score alone is not investigable, so attach
   the **drivers**: for each alert, report the two or three fields whose robust z (step 2:
   `0.6745·(x − median)/MAD`) is most extreme, and the first check a reviewer should run. That recipe works
   for any scorer, including isolation forest and LOF, which give no native attribution.
   **When no field is individually extreme, the anomaly is a joint one** — the combination is
   unusual though every value is ordinary (a routine amount, to a routine vendor, at a routine
   hour, but never that trio together). Marginal robust z is blind to it by construction, so
   branch: if the top |z| is unremarkable (say < 3), attribute by *what the point is unusual
   relative to* instead — the nearest normal neighbours and which fields differ from them (LOF
   and DBSCAN give you these directly), or a drop-one pass that re-scores the point with each
   field removed and names the field whose removal collapses the score. Report that as
   "unusual combination: X given Y", never as a bare score, and say plainly that no single value
   is out of range — otherwise a reviewer checks each field, finds nothing, and learns to
   distrust the feed.
7. **Close the loop and manage alert fatigue.** Track precision on reviewed alerts, suppress known-benign
   recurring patterns (a scheduled large transfer isn't news every month), fold confirmed cases back as labels,
   and re-tune. An alert stream nobody trusts is worse than none.

**Deliverable — the detection design + ranked alert feed.** The finished output contains:
(1) a one-paragraph definition of "anomalous" for this data, with the missed-anomaly vs
false-alarm cost trade-off stated; (2) the method(s) chosen and why they fit the data's shape;
(3) the threshold and the alert budget it was tuned to; (4) a ranked top-N alert list — score,
the fields driving each flag, and a suggested first check per alert; (5) the feedback plan:
how reviewed alerts feed the precision estimate and re-tuning. The assistant drafts the design
and the ranked alerts; the human owns the investigation and the verdict on every alert.

## Why / learn
The mental shift is that **an anomaly is "unusual," not automatically "wrong."** These methods find points
that don't fit the historical pattern; whether a given point is an error, fraud, or a perfectly legitimate
one-off (a genuine large acquisition payment) is a question only investigation answers. So detection is a
*triage* step that decides where humans look, and it must be paired with investigation, never treated as a
verdict. The second hard truth is **labels are scarce**, which is why this is mostly unsupervised: you rarely
have a clean history of "these were the frauds," so you can't train a straightforward classifier and you can't
compute recall honestly (you don't know how many anomalies you *missed*). That reframes evaluation — you can
estimate **precision** on the alerts you review, but true recall is usually unknowable, so you tune to an alert
budget and the cost of misses rather than chasing an F1 you can't measure. Robust statistics matter for a
subtle reason: the ordinary mean and standard deviation are themselves distorted by the outliers you're
hunting (a single huge value inflates the std so nothing looks extreme anymore), whereas the **median and MAD**
barely move — so robust methods keep their sensitivity in exactly the messy data where detection matters.
And alert fatigue is not a soft concern: precision that's too low trains reviewers to ignore the stream, at
which point even the true positives are lost. Detection is only as valuable as the investigation it feeds.

## Common mistakes
- Treating a flag as a verdict → an anomaly is unusual, not proven wrong. Pair every alert with investigation.
- Plain z-score/mean-std on data with big outliers → the outliers inflate the std and mask themselves. Use robust z (median/MAD).
- Chasing recall/F1 with almost no labels → you can't measure what you didn't catch. Tune to precision on reviewed alerts + an alert budget.
- Ignoring seasonality in a time series → normal month-end/quarter-end spikes flood the alerts. Flag residuals against a season-aware baseline.
- Distance/density methods on unscaled features → the largest-unit feature dominates. Standardize for LOF and DBSCAN; isolation forest is split-based and Mahalanobis is covariance-aware (Σ⁻¹ already absorbs per-feature scale), so neither needs it.
- A hard binary cutoff that swamps reviewers → nobody can act. Rank and route the top-N to an alert budget.
- Never suppressing known-benign recurrences → alert fatigue. Whitelist scheduled/expected patterns and re-tune.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real transaction data, counterparties, amounts,
and sample rows in `your-environment.private.md`, which is git-ignored): what "anomalous" means for your
process, the fields you monitor, whether you have any labels, your alert budget (how many alerts/day the team
can investigate), known-benign recurring patterns to suppress, and the cost of a missed anomaly vs a false
alarm. This skill then maps its generic methods onto your data — to rank reconciliation breaks by
unusualness, point it at whatever reconciliation process you already run.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/anomaly-detection.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/methods-and-thresholds.md — statistical, time-series, and unsupervised methods, with threshold-setting and evaluation under label scarcity
- references/your-environment.md — your definition of anomalous, monitored fields, labels, and alert budget (add when supplied)
