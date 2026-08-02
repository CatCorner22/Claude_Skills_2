# Evals — full-stack-dev-skills:deploy-and-operate

## 1. Positive trigger (should load the skill)
> "Containerize the app and set up CI/CD — right now we deploy by SSH-ing in and pulling,
> the image is 2GB, secrets are in a config file in the repo, and when prod breaks we
> can't tell what happened."

Expected: skill loads; multi-stage slim non-root Dockerfile; lint→test→build→deploy CI with
SHA-tagged images; secrets moved to the platform store (and scrubbed from git awareness);
migrations as a deploy step; healthz/readyz split; structured stdout logs with request IDs;
rehearsed pointer-flip rollback.

## 2. Near-miss (should NOT load this skill)
> "Should this app be one service or several, and how do I organize the modules?"

Expected: architecture — `full-stack-dev-skills:full-stack-app-architecture`. If this skill
loads, sharpen the ship-and-run framing.

## 3. Quality rubric
A good response:
- **Does the task:** working Dockerfile/CI shape, env-only config, health endpoints,
  logging middleware, rollback runbook — the go-live checklist satisfied.
- **Teaches:** deployment as a reproducibility problem (four invariants), alive-vs-ready
  consumers, request-ID correlation as minimum observability.
- **Safe:** no latest tags, no baked secrets, no app-startup migrations racing replicas,
  flags the git-history problem with the committed secrets file.
