# Evals — full-stack-dev-skills:full-stack-app-architecture

## 1. Positive trigger (should load the skill)
> "Starting a new internal app — invoice tracking with some dashboards. Should this be
> microservices? Pick the stack and lay out the project for me."

Expected: skill loads; recommends a modular monolith with the reference stack (FastAPI;
htmx vs React decided by the UI's nature; SQLite-first); feature-folder layout; one typed
settings object from env vars; writes the split criteria down instead of splitting.

## 2. Near-miss (should NOT load this skill)
> "My FastAPI endpoint returns 422 on valid-looking input — debug the validation."

Expected: endpoint mechanics — `full-stack-dev-skills:backend-api-development`. If this
skill loads, sharpen the structure-vs-implementation split.

## 3. Quality rubric
A good response:
- **Does the task:** stack choice with one-line reasons, concrete folder layout, module
  boundary rules, config/secrets handling, one-page architecture doc.
- **Teaches:** architecture as deciding-what-changes-together, why guessed service
  boundaries cost forever, feature-vs-layer layout economics, twelve-factor config.
- **Safe:** no microservices without proven criteria, no secrets in git, keeps the split
  option real via honest boundaries.
