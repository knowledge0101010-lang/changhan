#!/usr/bin/env bash
# 창한 전체 검증
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== 엔진 테스트 =="
python3 -m engine test

echo "== 파이썬 스케치 =="
python3 sketches/python/sketch.py

echo "== 러스트 스케치 =="
(cd sketches/rust && cargo test -q)

if [[ -f ../../system/untitled-bridge/envsetup-mac105.sh ]]; then
  # shellcheck disable=SC1091
  source ../../system/untitled-bridge/envsetup-mac105.sh >/dev/null
fi
if [[ -n "${CANGJIE_HOME:-}" ]]; then
  export PATH="$CANGJIE_HOME/bin:${CANGJIE_HOME}/tools/bin:$PATH"
fi

if command -v cjpm >/dev/null 2>&1; then
  echo "== 창제 스케치 =="
  (cd sketches/cangjie && rm -rf target && cjpm build && cjpm run)
  echo "== 예제 =="
  for f in examples/*.cjh; do
    echo "-- $f"
    python3 -m engine run "$f"
  done
else
  echo "경고: PATH에 cjpm 없음 — 창제·예제 실행 생략"
fi

echo "FULL_OK"
