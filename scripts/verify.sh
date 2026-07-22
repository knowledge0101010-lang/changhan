#!/usr/bin/env bash
# 창한 전체 VERIFY
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== engine test =="
python3 -m engine test

echo "== python sketch =="
python3 sketches/python/sketch.py

echo "== rust sketch =="
(cd sketches/rust && cargo test -q)

if [[ -f ../../system/untitled-bridge/envsetup-mac105.sh ]]; then
  # shellcheck disable=SC1091
  source ../../system/untitled-bridge/envsetup-mac105.sh >/dev/null
fi
if [[ -n "${CANGJIE_HOME:-}" ]]; then
  export PATH="$CANGJIE_HOME/bin:${CANGJIE_HOME}/tools/bin:$PATH"
fi

if command -v cjpm >/dev/null 2>&1; then
  echo "== cangjie sketch =="
  (cd sketches/cangjie && rm -rf target && cjpm build && cjpm run)
  echo "== examples =="
  for f in examples/*.cjh; do
    echo "-- $f"
    python3 -m engine run "$f"
  done
else
  echo "WARN: cjpm not on PATH — skipped cangjie/example runs"
fi

echo "FULL_OK"
