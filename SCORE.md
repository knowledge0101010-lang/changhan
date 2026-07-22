# 점수 — 축 병합 · 호스트 채택

날짜: 2026-07-22

## 축 1 — 구현 방식

| 트랙 | 결과 |
|------|------|
| **1A 번역 엔진** | **출시** — 제품 트렁크 `engine/` (파이썬 부트스트랩) |
| **1B 독립 컴파일러** | 학습용 대조 문서만 · **출시 금지** |

근거: 완전 한글판은 번역 엔진으로 고정. 한(Han)의 LLVM 파이프라인은 창제 ABI와 이어지지 않음.

## 축 2 — 툴체인 호스트

| 호스트 | 검증 | 평가 |
|--------|------|------|
| **2A 창제** | 스케치 `main.cj` + `cjpm run` → `안녕하세요` | 정책에 맞고 실제 런타임 확인 |
| **2B 러스트** | `cargo test` (맵: `func` ≠ `fn`) | UX·맵 참고용 |
| **2C 파이썬** | `python3 -m engine test` + 스케치 | **검증 속도·현재 트렁크** |

### 채택

- **지금 제품 CLI:** **2C 파이썬** — `python3 -m engine` / `./cjh` (골든·`cjpm` 연동 완료)
- **정책상 승격 목표:** **2A 창제** — 같은 키워드 표를 `.cj`로 이식 (`sketches/cangjie/`)
- **2B 러스트:** 한과의 대조·맵 단위 테스트만. 트렁크 아님

승격 조건: 창제 호스트가 파일 입출력·치환·CLI를 SDK 1.0.5에서 파이썬과 동등하게 통과하면 트렁크를 2A로 옮김.

## 창제 ≠ 러스트 (재확인)

- 번역 결과는 `func` / `var` / `if (…)` — 러스트의 `fn` / `let mut` 아님
- 자세한 표: [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md)

## 스모크 기록

```bash
export CANGJIE_HOME=/path/to/cangjie-official-1.0.5/cangjie
export PATH="$CANGJIE_HOME/bin:$CANGJIE_HOME/tools/bin:$PATH"
./cjh test
./cjh run examples/01_안녕.cjh
# → 안녕하세요
```

한글 식별자 검증: `examples/03_함수.cjh` → 출력 `8` (창제에서 허용 확인)
