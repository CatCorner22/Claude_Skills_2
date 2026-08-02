# ML serving recipes (reference)

## Contents
- Artifact layout
- Batch scoring job
- Prediction-log schema
- Rollout patterns
- Pre-launch checklist

## Artifact layout
```
models/churn/
├── 2026-07-15_v3/
│   ├── pipeline.joblib          # the WHOLE sklearn Pipeline (preprocess + model)
│   └── meta.json                # version, trained_at, data_window, feature list,
│                                # validation metrics, git SHA of training code, hash
└── current -> 2026-07-15_v3/    # promotion = move the pointer (or a config value)
```
```python
def load_model(path: Path) -> Model:
    m = joblib.load(path / "pipeline.joblib")
    m.meta = Meta(**json.loads((path / "meta.json").read_text()))
    return m
```
Store artifacts wherever ops lives (object storage, a models/ volume); the pointer/config is
the deployment. Never retrain "in place" over a served artifact.

## Batch scoring job
```python
def score_batch(model: Model, db: Session) -> int:
    rows = fetch_scoring_population(db)          # same feature code as training!
    X = build_features(rows)                     # shared function — the skew killer
    scores = model.predict_proba(X)[:, 1]
    upsert_predictions(db, rows.index, scores, model.meta.version)
    log.info("scored %d rows with %s", len(rows), model.meta.version)
    return len(rows)
```
Run it as a background job on a schedule (see realtime-and-dynamic-features for the job
pattern). The product reads the predictions table like any other data — no serving infra.

## Prediction-log schema
```python
class PredictionLog(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    ts: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    model_version: Mapped[str] = mapped_column(index=True)
    inputs: Mapped[dict] = mapped_column(JSON)      # or input_hash where sensitive
    score: Mapped[float]
    outcome: Mapped[float | None]                   # backfilled when labels arrive
    outcome_at: Mapped[datetime | None]
```
This one table serves: debugging ("what did v3 say for input X?"), monitoring (score
distribution by day), evaluation (score vs outcome once labels land), and the next
training set. Retention per your data policy; hash inputs where they're sensitive.

## Rollout patterns
| Pattern | How | Use when |
|---|---|---|
| Shadow | New model scores logged, incumbent's answer served | Cheapest safety; always first |
| Canary | New model serves a small slice (user %, segment) | Product metric needs live traffic |
| A/B | Formal split + significance on the product metric | The decision is close or high-stakes |
Promotion/rollback = config change (the pointer), never a redeploy of code. Compare on the
*product* metric (conversion, loss rate), not just AUC — the validation metric is a proxy.

## Pre-launch checklist
- [ ] Whole pipeline serialized (no external preprocessing steps to "remember")
- [ ] Feature code shared between training and serving (one function, imported twice)
- [ ] Input schema validated at the endpoint (types, ranges, categories)
- [ ] Model loads at startup; version in every response
- [ ] Prediction logging on, day one
- [ ] Drift checks defined: which features, what threshold, who's alerted
- [ ] Retrain trigger and rollback trigger written down and agreed
- [ ] Shadow/canary plan for the *next* version already sketched
- [ ] Framing sanity check: would a rule/heuristic hit 90% of this value? (ml-project-framing)
