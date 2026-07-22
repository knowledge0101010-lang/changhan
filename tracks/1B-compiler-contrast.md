# Track 1B — 독립 컴파일러 (대조 학습 · SHIP 금지)

## CPT

Han `vendor/claude-science/zodiac-lab/han/src/`:

| 모듈 | 역할 |
|------|------|
| lexer.rs | 한글 키워드 토큰 |
| parser.rs | AST |
| typechecker.rs | 타입 |
| interpreter/ | 즉시 실행 |
| codegen/ | LLVM IR |

## SFT (메모만)

- 범위: 렉서→파서→타입→인터프리터→LLVM = 수개월급
- 창제 ABI/`cjc`와 단절 → Harmony/cjpm 생태계 재사용 불가
- 에러 메시지 한글화는 컴파일러 소유 시 자연스럽지만, 우리는 번역+창제 진단 위임

## RL

**SHIP 금지.** dossier 학습만. 제품 우회(독립 컴파일러 배포) 불가.
