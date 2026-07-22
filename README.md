# 창한 (Changhan)

창제(Cangjie) **완전한글 표면** — Han(한) UX를 벤치마크하되, 제품은 독립 컴파일러가 아니라 **번역 엔진**이다.

```text
.cjh (한글)  →  cjh 번역  →  .cj (공식 창제)  →  cjpm build/run
```

창제 ≠ Rust/Han 문법: [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md)

## Quick start

```bash
# 공식 Cangjie SDK 1.0.5 필요 (cjpm / cjc)
export CANGJIE_HOME=/path/to/cangjie-official-1.0.5/cangjie
export PATH="$CANGJIE_HOME/bin:$CANGJIE_HOME/tools/bin:$PATH"

./cjh test
./cjh run examples/01_안녕.cjh
# → 안녕하세요

bash scripts/verify.sh   # 전체 VERIFY
```

## Docs

- [LEARN.md](LEARN.md) — 분리 학습 진행판
- [spec/KEYWORD_MAP.md](spec/KEYWORD_MAP.md) — Han ↔ 창제 맵
- [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md) — **창제 ≠ Rust/Han**
- [SCORE.md](SCORE.md) — 호스트 채택

## 하지 않음

- Han급 독립 LLVM 컴파일러를 창제 대체로 SHIP
- 산술 연산자 한글화 (Han도 C 기호 유지)

## Related

국산 언어 랩 **이도 / 금척**: 별도 레포 트렁크일 수 있음 (`geumcheok`). 창한은 창제 한글 **번역 엔진** 제품.
