#!/usr/bin/env bash
# Lints every skill and manifest in this library against the house standard.
# Usage: bash scripts/validate.sh   (run from the repo root)
# Exit code 0 = clean, 1 = at least one ERROR.

set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT" || exit 2

errors=0
warns=0
err()  { echo "ERROR: $1"; errors=$((errors+1)); }
warn() { echo "WARN:  $1"; warns=$((warns+1)); }
ok()   { echo "OK:    $1"; }

json_ok() {
  # Validate a JSON file if a parser is available; otherwise skip.
  if command -v python3 >/dev/null 2>&1; then
    python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$1" 2>/dev/null
  elif command -v jq >/dev/null 2>&1; then
    jq empty "$1" >/dev/null 2>&1
  else
    return 0
  fi
}

echo "== Validating manifests =="
for mf in .claude-plugin/marketplace.json plugins/*/.claude-plugin/plugin.json; do
  [ -f "$mf" ] || { err "missing manifest: $mf"; continue; }
  if json_ok "$mf"; then ok "$mf (valid JSON)"; else err "$mf is not valid JSON"; fi
done

echo
echo "== Validating skills =="
shopt -s nullglob
for dir in plugins/*/skills/*/; do
  skill="${dir%/}"
  base="$(basename "$skill")"
  md="$skill/SKILL.md"
  [ -f "$md" ] || { err "$skill has no SKILL.md"; continue; }

  # Extract YAML frontmatter (between the first two '---' fences).
  fm="$(awk 'NR==1 && $0=="---"{f=1; next} f && $0=="---"{exit} f{print}' "$md")"
  [ -n "$fm" ] || { err "$base: no frontmatter"; continue; }

  # name
  name="$(printf '%s\n' "$fm" | awk -F':' '/^name:/{sub(/^name:[[:space:]]*/,""); print; exit}' | tr -d '"'"'"' ' )"
  if [ -z "$name" ]; then
    err "$base: missing 'name'"
  else
    [ "$name" = "$base" ] || err "$base: name '$name' != folder name '$base'"
    printf '%s' "$name" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$' || err "$base: name '$name' must be lowercase alphanumeric with single hyphens"
    [ "${#name}" -le 64 ] || err "$base: name longer than 64 chars"
    printf '%s' "$name" | grep -Eiq 'anthropic|claude' && err "$base: name must not contain 'anthropic' or 'claude'"
  fi

  # description present + length
  if printf '%s\n' "$fm" | grep -q '^description:'; then
    desc="$(printf '%s\n' "$fm" | awk '
      /^description:/{flag=1; sub(/^description:[[:space:]]*/,""); gsub(/^[>|]-?[[:space:]]*$/,""); buf=$0; next}
      flag && /^[a-zA-Z_-]+:([[:space:]]|$)/{flag=0}
      flag{gsub(/^[[:space:]]+/,""); buf=buf" "$0}
      END{print buf}')"
    dlen=$(printf '%s' "$desc" | wc -m | tr -d ' ')
    if [ "$dlen" -eq 0 ]; then err "$base: empty description"; fi
    if [ "$dlen" -gt 1024 ]; then err "$base: description is $dlen chars (max 1024)"; fi
  else
    err "$base: missing 'description'"
  fi

  # body under 500 lines
  body_lines=$(awk 'seen==2{c++} /^---$/{seen++} END{print c+0}' "$md")
  [ "$body_lines" -lt 500 ] || warn "$base: body is $body_lines lines (keep under 500)"

  # references one level deep
  if [ -d "$skill/references" ]; then
    if [ -n "$(find "$skill/references" -mindepth 1 -type d 2>/dev/null)" ]; then
      err "$base: references/ must be one level deep (no subdirectories)"
    fi
  fi

  [ "$errors" -eq 0 ] && ok "$base" || true
done

echo
echo "== Summary: $errors error(s), $warns warning(s) =="
[ "$errors" -eq 0 ]
