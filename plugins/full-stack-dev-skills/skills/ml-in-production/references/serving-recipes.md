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
│                                # validation metrics, git SHA of training code,
│                                # decision threshold + the split it was fit on,
│                                # sha256 of pipeline.joblib (verified at load)
└── current -> 2026-07-15_v3/    # promotion = move the pointer (or a config value)
```
```python
import hashlib, hmac, io, json
from pathlib import Path


def load_model(path: Path) -> Model:
    # joblib.load() unpickles: loading an artifact EXECUTES code from it. Verify the
    # artifact is the one you published before handing it the interpreter.
    blob = (path / "pipeline.joblib").read_bytes()
    meta = Meta(**json.loads((path / "meta.json").read_text()))
    digest = hashlib.sha256(blob).hexdigest()
    if not hmac.compare_digest(digest, meta.sha256):
        raise RuntimeError(
            f"model artifact hash mismatch at {path}: meta.json says {meta.sha256}, "
            f"file is {digest} — refusing to load")
    m = joblib.load(io.BytesIO(blob))
    m.meta = meta
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
    __tablename__ = "prediction_log"                # required: SQLAlchemy 2.0 raises without it
    id: Mapped[int] = mapped_column(primary_key=True)
    ts: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                         server_default=func.now(), index=True)
    model_version: Mapped[str] = mapped_column(index=True)
    inputs: Mapped[dict] = mapped_column(JSON)      # or input_hash where sensitive
    score: Mapped[float]
    outcome: Mapped[float | None]                   # backfilled when labels arrive
    outcome_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
```
`DateTime(timezone=True)` on both timestamps, not the bare `Mapped[datetime]`: a bare
annotation compiles to `TIMESTAMP WITHOUT TIME ZONE` on Postgres (verified on SQLAlchemy
2.0.52), and the two timestamps here are the ones you subtract — a label backfilled by a job
running in a different zone, or the hour a DST change lands, silently shifts every
score-to-outcome delay by an hour. Same rule as
`full-stack-dev-skills:database-and-orm`, whose SQLite→Postgres checklist lists portable
`DateTime(timezone=True)` as a required item.

This one table serves: debugging ("what did v3 say for input X?"), monitoring (score
distribution by day), evaluation (score vs outcome once labels land), and the next
training set. Retention per your data policy; hash inputs where they're sensitive.

## Rollout patterns
| Pattern | How | Use when |
|---|---|---|
| Shadow | New model scores logged, incumbent's answer served | Cheapest safety; always first |
| Canary | New model serves a small slice (user %, segment) | Product metric needs live traffic |
| A/B | Formal split + significance on the product metric | The decision is close or high-stakes |
Promotion/rollback = config change (the pointer), no rebuild of the image. Compare on the
*product* metric (conversion, loss rate), not just AUC — the validation metric is a proxy.

**But it is still a code change, so treat the artifact store as a production-code path.**
`joblib.load()` and `pickle.load()` do not read data — they *execute* the stream, calling
whatever constructors and `__reduce__` hooks it names. Anyone who can write to the artifact
store, or influence the pointer, can run arbitrary code inside the serving process. That
makes "promotion is only a config change" true about your build pipeline and false about
your threat model: the pointer flip is as privileged as a deploy, and it usually has none
of a deploy's review.

So: restrict write access to the artifact store to the same set that can ship code; record
the artifact's SHA-256 in `meta.json` at training time and **verify it before loading**
(above), with the manifest signed or held somewhere the store's writers cannot reach —
a hash sitting beside the file it describes protects nothing, exactly as with the split
tally's anchor; and never load an artifact from a path a request can influence. If models
arrive from outside your own training pipeline, pickle is the wrong format entirely —
prefer ONNX or a pure-data format for those.

## Pre-launch checklist
- [ ] Whole pipeline serialized (no external preprocessing steps to "remember")
- [ ] **Decision threshold in the sidecar**, with the split it was chosen on, the FP/FN costs
      or alert budget that set it, and the prevalence it assumed — it is a fitted parameter,
      and left in application code the one number that turns scores into actions is versionless
- [ ] Feature code shared between training and serving (one function, imported twice)
- [ ] Input schema validated at the endpoint (types, ranges, categories)
- [ ] Model loads at startup; version in every response
- [ ] Model artifact integrity verified at load (SHA-256 vs the signed manifest) — loading a
      pickle executes code, so this is the same control as verifying a deployed binary
- [ ] Artifact-store write access limited to whoever may ship code
- [ ] Prediction logging on, day one
- [ ] Drift checks defined: which features, what statistic (PSI / KS / chi-square) at what
      threshold, and who's alerted — plus prevalence, since a threshold frozen at training
      prevalence silently changes precision as prevalence moves
- [ ] Retrain trigger and rollback trigger written down and agreed
- [ ] Shadow/canary plan for the *next* version already sketched
- [ ] Framing sanity check: would a rule/heuristic hit 90% of this value? (ml-project-framing)
