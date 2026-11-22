#!/usr/bin/env bash
# Secret scan for the ex-redteam repo. Reports FILE:LINE and the rule name only; NEVER prints the matched value.
# Scans tracked files (git) if available, else the working tree. Excludes the venv, caches and runs/.
set -u
cd "$(dirname "$0")/.." || exit 2

if git rev-parse --git-dir >/dev/null 2>&1; then
  mapfile -t FILES < <(git ls-files --cached --others --exclude-standard)
else
  mapfile -t FILES < <(find . -type f -not -path './.git/*')
fi

EXCLUDE_RE='(^|/)(\.venv|\.git|__pycache__|\.pytest_cache|\.ruff_cache)(/|$)|^(\./)?(runs|agent-tools)/|\.(pyc|png|jpg|jpeg|gif|pdf|zip|tar|gz|bin|pt|pth|safetensors|ckpt|npz|npy|parquet)$'

# rule name -> ERE. Kept deliberately conservative; the point is to catch real credentials, not prose.
declare -A RULES=(
  [openai_key]='sk-[A-Za-z0-9]{20,}'
  [anthropic_key]='sk-ant-[A-Za-z0-9_-]{20,}'
  [aws_access_key]='AKIA[0-9A-Z]{16}'
  [google_api_key]='AIza[0-9A-Za-z_-]{35}'
  [slack_token]='xox[baprs]-[0-9A-Za-z-]{10,}'
  [github_token]='gh[pousr]_[0-9A-Za-z]{30,}'
  [jwt]='eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}'
  [private_key_block]='BEGIN (RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY'
  [aws_secret_assign]='aws_secret_access_key[[:space:]]*[=:][[:space:]]*[A-Za-z0-9/+]{30,}'
  [generic_secret_assign]='(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token|bearer)[[:space:]]*[=:][[:space:]]*["'"'"']?[A-Za-z0-9/+_.=-]{16,}'
)

hits=0
for f in "${FILES[@]}"; do
  [[ -f "$f" ]] || continue
  [[ "$f" =~ $EXCLUDE_RE ]] && continue
  # skip this scanner and docs that legitimately discuss secret *patterns*
  case "$f" in
    tools/secret_scan.sh) continue;;
  esac
  for rule in "${!RULES[@]}"; do
    while IFS=: read -r line _; do
      [[ -z "$line" ]] && continue
      echo "POSSIBLE SECRET [$rule] $f:$line"
      hits=$((hits+1))
    done < <(grep -nIE "${RULES[$rule]}" "$f" 2>/dev/null | cut -d: -f1 | sed 's/$/:/')
  done
done

if [[ $hits -eq 0 ]]; then
  echo "secret scan: clean ($(printf '%s\n' "${FILES[@]}" | grep -vcE "$EXCLUDE_RE") files scanned, values never printed)"
  exit 0
fi
echo "secret scan: $hits possible secret(s) found (values not shown); review before committing"
exit 1
