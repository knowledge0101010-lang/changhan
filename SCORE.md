# SCORE — 축 병합 · 호스트 채택

Date: 2026-07-22  
Identity: Cursor Grok 4.5

## 축1

| 트랙 | 결과 |
|------|------|
| **1A 번역 엔진** | **SHIP** — 제품 트렁크 `engine/` (Python 부트스트랩) |
| **1B 독립 컴파일러** | 학습 dossier만 · **SHIP 금지** 유지 |

근거: 완전한글판 = 번역 엔진 고정. Han LLVM 파이프라인은 창제 ABI와 단절.

## 축2 호스트

| 호스트 | VERIFY | 점수 |
|--------|--------|------|
| **2A 창제** | 스케치 `main.cj` + 제품 경로 `cjpm run` 스모크 `안녕하세요` | 정책 정렬 + 실런타임 |
| **2B Rust** | `cargo test` 맵 스모크 (`func` ≠ `fn`) | UX 참고용 |
| **2C Python** | `python3 -m engine test` + sketch | **VERIFY 속도·현재 트렁크** |

### 채택

- **제품 CLI 트렁크 (당장):** **2C Python** — `python3 -m engine` (골든·cjpm 오케스트레이션 완료)
- **정책 승격 목표:** **2A 창제** — 동일 KEYWORD_MAP을 `.cj`로 이식 (스케치 자리 `sketches/cangjie/`)
- **2B Rust:** Han 대조·맵 단위 테스트만. 창제 호출 언어 정책상 트렁크 아님

뒤집힘 조건: 창제 호스트가 파일 IO·치환·CLI를 SDK 1.0.5에서 동등 VERIFY하면 트렁크를 2A로 이동.

## 창제 ≠ Rust (SCORE 재확인)

- 번역 타깃은 `func`/`var`/`if (…)` — Rust `fn`/`let mut` 아님
- 상세: [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md)

## 스모크 기록

```bash
source system/untitled-bridge/envsetup-mac105.sh
cd lab/cangjie-hangul
python3 -m engine test
python3 -m engine run examples/01_안녕.cjh
# → 안녕하세요
```

한글 식별자 VERIFY: `examples/03_함수.cjh` → 출력 `8` (창제 허용 확인)
