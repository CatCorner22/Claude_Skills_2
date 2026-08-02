# Your Python environment (sanitized template)

- **Python version pin:** <e.g. 3.14.x exactly, or ">=3.13" if 3.14 not yet approved>
- **Package index:** <internal registry URL name for uv `[[tool.uv.index]]` — no credentials here>
- **Line length / style deviations:** <if not the default 100>
- **Mandated frameworks:** <e.g. FastAPI only, no Litestar; pandas required by team X>
- **Logging sink and schema:** <where JSON logs ship, required field names, redaction rules>
- **Coverage gate:** <if different from 95%>
- **CI system:** <GitHub Actions / other — adjust the CI template accordingly>

Keep secrets, tokens, internal hostnames, and client data out of this file. Real,
sensitive details belong in `your-environment.private.md` or `*.local.*` files, which
`.gitignore` keeps out of the repo.
