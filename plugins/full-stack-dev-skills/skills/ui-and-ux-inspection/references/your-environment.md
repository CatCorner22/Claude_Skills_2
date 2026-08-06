# Your environment (fill in)

Sanitized, structural entries only. Anything sensitive — real URLs, tenant names, test
credentials or how to obtain them, client identifiers, regulatory specifics — goes in
`references/your-environment.private.md`, which `.gitignore` keeps out of git.

## Application under inspection
- Repository root: <path>
- App URL / local run command: <e.g. `npm run dev` → http://localhost:5173>
- Framework / router / design system: <e.g. React + Vite, TanStack Router, in-house tokens>

## Target routes
- <route or route group> — <public | authenticated | role>
- <…>

## Critical processes (written as observable outcomes, not activities)
- <"The user submits a valid X and receives a trackable reference.">
- <"The user finds an overdue Y and records a partial payment.">

## Test accounts policy
- <least-privilege fixture accounts only; how they are provisioned; what is forbidden>
- Production access: <default: never — inspection runs against test/staging only>

## Browser matrix and input modes
- <browsers + versions; viewports beyond the standard 320/375/768/1024/1440;
  keyboard / touch / coarse pointer; reduced motion; dark or high contrast>

## Performance budgets (if stricter than the defaults)
- INP p75 ≤ <200 ms> · LCP p75 ≤ <2.5 s> · CLS p75 ≤ <0.1>
- <route-specific budgets>

## Other preferred inputs (record if available)
- Personas: <roles, domain expertise, access needs, devices, language>
- Analytics baseline: <task completion, funnels, errors, latency, support data>
- Design system: <component library, tokens, interaction standards>
- Constraints: <regulatory, security, technical, brand, deadline limits>
- Allowed commands: <commands the agent is authorized to execute>

## write_permission default
- <report-only | may propose patches | may modify code> (per-run overrides must be explicit)

## Privacy constraints
- <screenshot rules, data classifications in scope, jurisdictions, who reviews
  biometric/privacy questions>
- Eye-tracking mode: disabled (default). Enabling it requires the consent protocol in
  references/procedure.md; record the authorization in the private file, not here.
