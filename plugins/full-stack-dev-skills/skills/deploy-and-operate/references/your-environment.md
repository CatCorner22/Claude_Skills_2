# Your ops setup (sanitized template)

Never commit real secrets or tokens.

- **Platform / deploy mechanism:** <where it runs; what deploy.sh actually does>
- **Registry and tagging:** <registry; SHA tags; retention>
- **Secret store:** <platform secrets / vault; who can read prod>
- **Environments:** <dev / staging / prod; env-var sources per env>
- **Migration step:** <where alembic runs in the pipeline>
- **Health wiring:** <healthz/readyz consumers; check contents>
- **Log destination:** <where stdout lands; retention>
- **Alerting:** <what pages whom>
- **Rollback runbook:** <the exact commands; last rehearsal date>
