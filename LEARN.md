# 창한 (Changhan) — 분리 학습 진행판

> **이관:** 실행 트렁크는 **이도 (세종) · 2 degrees** → [`../../vendor/claude-science/geumcheok/`](../../vendor/claude-science/geumcheok/)  
> (`python3 -m geumcheok translate|run --host cangjie`)

제품: **완전한글 표면 → 공식 창제 `.cj` 번역 엔진**  
기준 UX: Han(한) 표면 완전한글 (키워드·타입·내장·식별자·논리어)  
산술 기호(`+` `>=` `=`)는 Han과 같이 **비한글 유지**

창제 벤치마크·러스트(Han)와 다른 점: [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md)

## 진행

| 트랙 | CPT | SFT | RL/VERIFY | 상태 |
|------|-----|-----|-----------|------|
| 1A 번역 엔진 | KEYWORD_MAP + VS_RUST | engine + examples | cjpm 스모크 | 진행 |
| 1B 독립 컴파일러 | Han src 독해 | dossier만 | SHIP 금지 | 진행 |
| 2A 호스트 창제 | cjpm IO | sketches/cangjie | 빌드 스모크 | 대기 |
| 2B 호스트 Rust | Han crate | sketches/rust | cargo test | 대기 |
| 2C 호스트 Python | 랩 패턴 | sketches/python | unittest | 대기 |
| SCORE | — | — | 호스트 채택 | 대기 |

## 고정

- 완전한글판 = **번역 엔진** (독립 LLVM 컴파일러 아님)
- SHIP = 제품 트렁크 채택/배포. 1B는 학습만, SHIP 금지
- 축 교차 병합은 SCORE 전 금지
