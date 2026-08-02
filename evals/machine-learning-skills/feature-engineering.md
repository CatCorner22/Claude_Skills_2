# Evals — machine-learning-skills:feature-engineering

## 1. Positive trigger (should load the skill)
> "I'm building features for a payment-default model. I have a 900-value merchant category, some very
> skewed amount fields, timestamps, and lots of missing values. How should I encode, scale, and build
> time features without leaking?"

Expected: skill loads; recommends target/frequency encoding (out-of-fold) for the high-cardinality
merchant; log-transform for skewed amounts and scaling only if the model needs it; datetime + strictly
past lag/rolling features; imputation with a missingness indicator; and wiring it all into a train-only-fit
pipeline. Emphasizes not letting future/test information leak into any feature.

## 2. Near-miss (should NOT load this skill)
> "Which cross-validation scheme and metric should I use to prove these features actually improved the model?"

Expected: this is validation and metric selection. The `machine-learning-skills:model-evaluation` skill
should handle it. If this feature-engineering skill loads, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** matches encoding to cardinality, scales only where needed, builds leakage-safe
  datetime/lag/rolling features, handles missing values as information, and assembles a train-only-fit pipeline.
- **Teaches:** explains *why* good features can beat fancier algorithms and *why* every learned transform must
  be fit on training data only — not just a list of transforms.
- **Safe:** never fits transforms on the full dataset, never target-encodes without out-of-fold/smoothing, and
  never builds rolling/lag features that include the current or future rows.
