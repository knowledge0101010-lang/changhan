# Track 1A — 번역 엔진 (제품)

## CPT

- Han keywords.md ↔ 창제 키워드 ([KEYWORD_MAP.md](../spec/KEYWORD_MAP.md))
- 창제 고유 문법 vs Rust ([CANGJIE_VS_RUST.md](../spec/CANGJIE_VS_RUST.md))

## SFT

- `engine/` 토큰 번역기 (문자열·주석 보존)
- `examples/*.cjh` → `golden/*.cj`

## RL / VERIFY

- `python3 -m engine test`
- `python3 -m engine run examples/01_안녕.cjh` → `안녕하세요`

## SHIP

허용 — SCORE 후 채택 호스트로 승격.
