# ChatGPT adapter maintenance

This subtree contains portable ChatGPT/Work instructions, outside the Claude plugin
namespace. Follow the root's evidence/privacy requirements, but resolve installed
resources from actual host metadata. Do not introduce Claude plugin variables,
transcript discovery, plugin commands, or unsupported agent/model controls here.

Keep native Work frontmatter to name/description and version provenance in
`adapters.json`. Retain the source license. Preserve assistant ownership and all
required sources, checks, requested depth, and truthful installation status.

From the repository root, run the unit suite and script self-test documented in
`README.md` here. Validate skill package structure with the host's skill-creator
validator when available. Explicit-invocation forward tests do not verify automatic
routing. Preserve representative failures and unknown telemetry in the report.

Keep these adapters out of Claude catalog counts and plugin manifests. Rerun the
existing root validation/catalog tools to verify the original plugin library stays
coherent; change a Claude plugin version only if that plugin actually changes.
