---
name: ml-in-production
description: >-
  Puts machine-learning models into applications the lean way — packaging a trained model as
  a versioned artifact, serving it behind a FastAPI endpoint with Pydantic-validated inputs,
  choosing batch vs realtime inference by the product's actual latency need, keeping the
  feature pipeline identical between training and serving, and monitoring predictions and
  drift so the model earns continued trust. Use when deploying a model into an app, building
  an inference endpoint, choosing a serving pattern, debugging training/serving skew, or
  setting up prediction logging and drift checks. Triggers: deploy ML model, model serving,
  inference endpoint, predict API, batch scoring, model versioning, training serving skew,
  model monitoring, drift detection production, ml pipeline app, score in real time.
---

# ML in production

## When to use
- Wiring a trained model into a product: the serving pattern, the endpoint, versioning,
  monitoring.
- Debugging why a model performs worse in production than in evaluation.
- Not for: training the model → `machine-learning-skills:supervised-modeling` /
  `machine-learning-skills:time-series-forecasting`; judging it →
  `machine-learning-skills:model-evaluation`; framing whether ML is even warranted →
  `machine-learning-skills:ml-project-framing` (the leanest model is no model).

## Do it
1. **Choose the serving pattern by the product's latency need, cheapest first:**
   - **Batch scoring** (nightly/hourly job writes predictions to a table): the product reads
     predictions like any other data. Right whenever decisions aren't per-request —
     dashboards, rankings, risk flags. This covers *most* business ML and needs no serving
     infra at all (it's a background job — `full-stack-dev-skills:realtime-and-dynamic-features`).
   - **Realtime endpoint** (predict per request): only when the input isn't known until the
     moment of use (fraud check on a new transaction, interactive what-ifs).
   - Skip bespoke model servers until scale forces them; a FastAPI route loading a sklearn
     pipeline serves a very long way.
2. **Package the model as a versioned artifact:** serialized pipeline + a metadata sidecar
   (version, training-data window, metrics at validation, feature list, hash). Save the
   **whole pipeline** (preprocessing + model, e.g. sklearn `Pipeline`), never a bare
   estimator plus "remember to scale."
3. **Serve it thin, validated, and versioned:**

```python
model = load_model(settings.model_path)                 # once, at startup

class PredictIn(BaseModel):
    amount: Decimal
    customer_tenure_days: int = Field(ge=0)
    channel: Literal["web", "ach", "wire"]

@router.post("/predict")
def predict(x: PredictIn):
    score = float(model.predict_proba(to_frame(x))[0, 1])
    log_prediction(model.meta.version, x, score)        # the monitoring seed, day one
    return {"score": score, "model_version": model.meta.version}
```

   Pydantic guards the feature contract (types, ranges, categories); the response always
   carries the model version.
4. **Kill training/serving skew structurally.** The #1 silent failure: features computed one
   way in the training notebook and another way in the endpoint. Fix by *sharing code* — the
   same feature function (or the pipeline itself) runs in both places; no re-implementation
   in the route. (Feature craft: `machine-learning-skills:feature-engineering`.)
5. **Log predictions from day one:** timestamp, model version, inputs (or their hash where
   sensitive), output, and — when it arrives — the actual outcome. That table *is* your
   monitoring, your debugging, and your retraining set.
6. **Monitor like the model is drifting, because it is:** input distributions vs the
   training window (drift on key features), score distribution over time, and true
   performance once labels land. Alert on shift, review on schedule, and define *before
   launch* what triggers retraining or rollback. (`machine-learning-skills:anomaly-detection`
   patterns apply to the monitoring itself.)
7. **Ship new models like code:** new version = new artifact, deployed alongside; compare on
   logged traffic (shadow) or a slice (canary) against the incumbent *on the product metric*;
   promote or roll back by config. `references/serving-recipes.md` has the artifact layout,
   batch-job skeleton, prediction-log schema, and the pre-launch checklist.

## Why / learn
A model in production is a *dependency on the past*: it encodes the world as of its training
window, and the world moves — so unlike normal code, an untouched model degrades. Every
practice here follows from that one fact. Versioned artifacts and logged predictions exist
because "which model said what, given what?" is the first question in every ML incident, and
it's unanswerable retroactively. Monitoring is the model's regression test suite — except
the regressions come from reality changing, not code changing, so it must run continuously.
Training/serving skew deserves its structural fix because it's the failure mode evaluation
can't catch: the model is fine, the features lie, and offline metrics stay green while
production quietly scores garbage — sharing the literal code path is the only reliable cure.
The batch-first rule is lean-code economics applied to inference: a nightly job writing a
predictions table has no latency SLO, no cold starts, no per-request failure modes, and
turns "ML infrastructure" into "a cron job and a table" — the realtime endpoint is the
special case, earned by a product requirement, not the default. And staged rollout is the
honest admission that validation metrics are a *proxy*: the only measurement that finally
matters is the product metric on live traffic, so new models earn promotion there, not in
the notebook.

## Common mistakes
- Realtime serving for decisions made hourly → batch scoring into a table; read it like data.
- Persisting the bare model without preprocessing → the "remember to scale" bug; save the pipeline.
- Re-implementing features in the endpoint → training/serving skew; share the code path.
- No prediction logging "until we need it" → the incident arrives before the logs; day one.
- Responses without model version → undebuggable mixtures during rollouts; version every response.
- Loading the model per request → latency and memory churn; load at startup, reload on version change.
- Promoting on validation metrics alone → shadow/canary on the product metric first.
- No retraining/rollback triggers defined → drift becomes a debate instead of a runbook; decide before launch.
- ML where a rule would do → the leanest model is no model; re-check the framing skill.

## Tailor to your environment
Record your ML serving setup in `references/your-environment.md`: models in production with
their serving pattern, artifact store, prediction-log location, drift thresholds, and the
retrain/rollback triggers you committed to. **Never commit real prediction data or model
artifacts trained on sensitive data.**

## References
- references/serving-recipes.md — artifact layout, batch scoring job, prediction-log schema, rollout and pre-launch checklists
- references/your-environment.md — your models, patterns, thresholds, triggers (fill in)
