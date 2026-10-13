#!/usr/bin/env bash
# Register this checkout as a plugin marketplace and install its plugins.
#
# WHY THIS EXISTS. A fresh session does NOT pick the library up on its own. The committed
# `.claude/settings.json` declares `extraKnownMarketplaces` and lists all 13 plugins under
# `enabledPlugins`, and that configuration is **inert until the marketplace is registered**:
# a clone with those settings in place reports "No plugins installed", so every one of the
# library's skills is simply absent — not trimmed, not name-only, absent. Registering the
# marketplace is still not enough on its own either; `enabledPlugins` does not trigger an
# install, so the install step below is required too. Both halves were verified by running
# them against a clean HOME.
#
# It registers THIS CHECKOUT (`./`) rather than the GitHub source the README quotes, because
# a directory marketplace is read in place: no network, no clone, no dependence on the remote
# being reachable from wherever the session runs — and what gets loaded is the tree you are
# looking at, which is what you want when you are editing skills.
#
# Usage, from anywhere:
#   bash scripts/bootstrap-plugins.sh                 # all 13 plugins
#   bash scripts/bootstrap-plugins.sh deep-research-skills coding-agent-skills
#
# Installing FEWER is often the better choice, and is not a compromise. The session's skill
# listing is a character budget (~8,000 at the defaults), and all 13 plugins overrun it: most
# skills then reach the session as a bare name, with no description and no trigger phrases, so
# automatic matching cannot route to them. They stay invocable as `/plugin-name:skill-name`.
# `python3 scripts/measure-listing-cost.py` prints what a given set costs.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MARKET="treasury-analyst-skills"

if ! command -v claude >/dev/null 2>&1; then
  echo "error: the 'claude' CLI is not on PATH — nothing to register the marketplace with." >&2
  exit 2
fi
if [ ! -f "$REPO/.claude-plugin/marketplace.json" ]; then
  echo "error: $REPO is not a marketplace checkout (no .claude-plugin/marketplace.json)." >&2
  exit 2
fi

# The source of truth for what ships is the marketplace manifest, not this script and not
# .claude/settings.json — a hardcoded list here would go stale the first time a plugin is added.
mapfile -t ALL < <(python3 -c '
import json, sys
m = json.load(open(sys.argv[1]))
for p in m.get("plugins", []):
    if p.get("name"):
        print(p["name"])
' "$REPO/.claude-plugin/marketplace.json")

if [ "$#" -gt 0 ]; then
  WANT=("$@")
  for w in "${WANT[@]}"; do
    found=0
    for a in "${ALL[@]}"; do [ "$a" = "$w" ] && found=1; done
    if [ "$found" -eq 0 ]; then
      echo "error: '$w' is not a plugin in this marketplace. Available:" >&2
      printf '  %s\n' "${ALL[@]}" >&2
      exit 2
    fi
  done
else
  WANT=("${ALL[@]}")
fi

# `marketplace add` resolves a relative path against the working directory, so run it from the
# repo root and pass './' — the bare '.' form is rejected by the CLI.
cd "$REPO"
echo "Registering $REPO as marketplace '$MARKET'…"
claude plugin marketplace add ./

echo
for p in "${WANT[@]}"; do
  printf 'installing %-32s ' "$p"
  if out=$(claude plugin install "${p}@${MARKET}" 2>&1); then
    echo "ok"
  else
    echo "FAILED"
    printf '%s\n' "$out" | sed 's/^/    /'
    exit 1
  fi
done

echo
# Verify from the installed artifact rather than from this script's own success: the repository
# is not the product, and an install that reports success while reading a stale cache path is
# the failure this check exists to catch.
installed=$(claude plugin list 2>/dev/null | grep -c "Read from: $REPO/plugins" || true)
echo "verified: $installed plugin entr(ies) read from $REPO/plugins"
if [ "$installed" -eq 0 ]; then
  echo "error: plugins installed but none are being read from this checkout — inspect" >&2
  echo "       'claude plugin list' before relying on any skill." >&2
  exit 1
fi
skills=$(find "$REPO/plugins" -name SKILL.md | wc -l | tr -d ' ')
echo "this checkout ships $skills skills across ${#ALL[@]} plugins; ${#WANT[@]} plugin(s) installed"
echo
echo "A skill is always reachable by its full address, e.g."
echo "  /deep-research-skills:dna-raw-data-audit"
echo "which works even when the listing budget has trimmed its description away."
