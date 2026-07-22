# 창한 (Changhan)

> **고지:** 이 프로젝트는 **화웨이(Huawei) 공식 제품이 아니며**, 창제(Cangjie) 언어·SDK의 **원본 소유자·출처자가 아닙니다.**  
> SDK·컴파일러를 재배포하지 않습니다. 자세한 내용: [`NOTICE.md`](./NOTICE.md)

**창한**은 창제 위에 올린 **완전 한글 표면**입니다.  
한(Han) 언어의 한글 UX를 참고하되, 독립 컴파일러가 아니라 **번역 엔진**으로 공식 창제 소스(`.cj`)를 만듭니다.

```text
.cjh (한글)  →  cjh 번역  →  .cj (공식 창제)  →  cjpm build / run
```

창제 문법은 러스트(Rust)·한(Han)과 다릅니다. → [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md)

## 빠른 시작

```bash
# 공식 창제 SDK 1.0.5 필요 (cjpm / cjc)
export CANGJIE_HOME=/path/to/cangjie-official-1.0.5/cangjie
export PATH="$CANGJIE_HOME/bin:$CANGJIE_HOME/tools/bin:$PATH"

./cjh test
./cjh run examples/01_안녕.cjh
# → 안녕하세요

bash scripts/verify.sh   # 전체 검증
```

## 문서

| 문서 | 내용 |
|------|------|
| [NOTICE.md](NOTICE.md) | 화웨이·창제 비소유·비공식 고지 |
| [LEARN.md](LEARN.md) | 분리 학습 진행판 |
| [spec/KEYWORD_MAP.md](spec/KEYWORD_MAP.md) | 한글 ↔ 창제 키워드 대응 |
| [spec/CANGJIE_VS_RUST.md](spec/CANGJIE_VS_RUST.md) | 창제 ≠ 러스트 / 한 |
| [SCORE.md](SCORE.md) | 호스트 채택 결과 |

## 하지 않는 일

- 한(Han)급 독립 LLVM 컴파일러를 창제 대체품으로 출시하지 않음
- 산술·비교·대입 연산자 한글화 (한도 C 기호 유지)

## 관련

국산 언어 랩 **이도 / 금척**(`geumcheok`)과는 별개입니다. 창한은 **창제 한글 번역 엔진**에 집중합니다.
