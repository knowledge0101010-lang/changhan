# 트랙 1A — 번역 엔진 (제품)

## 학습

- 한 키워드 ↔ 창제 ([KEYWORD_MAP.md](../spec/KEYWORD_MAP.md))
- 창제 고유 문법 vs 러스트 ([CANGJIE_VS_RUST.md](../spec/CANGJIE_VS_RUST.md))

## 실습

- `engine/` 토큰 번역기 (문자열·주석 보존)
- `examples/*.cjh` → `golden/*.cj`

## 검증

- `python3 -m engine test` 또는 `./cjh test`
- `./cjh run examples/01_안녕.cjh` → `안녕하세요`

## 출시

허용 — SCORE 후 채택 호스트로 승격.
