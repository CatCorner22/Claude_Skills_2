# Evals — full-stack-dev-skills:backend-api-development

## 1. Positive trigger (should load the skill)
> "Build the REST API for our invoice app — CRUD endpoints, login for the React frontend,
> and consistent errors. Last time our API returned 200 with error strings and nobody
> paginated anything."

Expected: skill loads; Pydantic request/response models as the whole validation layer; thin
routes calling feature services; JWT (SPA client) with short lifetimes + refresh; one error
shape via exception handlers with correct status codes; pagination with caps from day one;
OpenAPI kept honest as the contract.

## 2. Near-miss (should NOT load this skill)
> "Write a script that pulls all invoices out of the vendor's REST API with pagination and
> retries."

Expected: API consumption — `data-tools-skills:rest-api-data-pulls`. If this skill loads,
sharpen the build-vs-consume split.

## 3. Quality rubric
A good response:
- **Does the task:** working endpoint patterns (models, DI, auth, errors, pagination) with
  minimal code, auth chosen by client type.
- **Teaches:** types-are-the-API (one model, four jobs), cookies-vs-JWT threat models, why
  thin routes keep logic testable.
- **Safe:** no hand-rolled password hashing, no secrets in JWT payloads, no 200-with-error,
  no stack traces in responses.
