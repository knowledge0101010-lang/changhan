# KEYWORD_MAP — Han 한글 ↔ 창제

출처 UX: `zodiac-lab/han/docs/src/api/keywords.md`  
타깃: Cangjie SDK 1.0.5  
차이 상세: [CANGJIE_VS_RUST.md](CANGJIE_VS_RUST.md)

## 제어

| 한글 | 창제 | 비고 (≠ Rust/Han) |
|------|------|-------------------|
| `함수` | `func` | Rust `fn` 아님 |
| `반환` | `return` | 창제는 마지막 식 암시 return도 가능 |
| `변수` | `var` | Rust `let mut` 아님 |
| `상수` | `let` | 컴파일타임은 `const` (2차) |
| `만약` | `if` | 반드시 `(…)` |
| `이면` | _(삭제)_ | 창제에 then 키워드 없음 |
| `아니면` | `else` | |
| `그리고` | `&&` | |
| `또는` | `\|\|` | |
| `반복` | `for` | `for (x in …)` |
| `동안` | `while` | `while (…)` |
| `안에서` | `in` | |
| `멈춰` | `break` | 라벨 break 없음 |
| `계속` | `continue` | |

## 타입

| 한글 | 창제 |
|------|------|
| `정수` | `Int64` |
| `실수` | `Float64` |
| `문자열` | `String` |
| `불` | `Bool` |
| `없음` | `Unit` (반환) / `None` (Option) — 문맥 |

## 구조

| 한글 | 창제 | ≠ Rust |
|------|------|--------|
| `구조` | `struct` | 값 타입 |
| `클래스` | `class` | Han에 없는 창제 참조 타입 |
| `열거` | `enum` | `| Variant` 문법 |
| `맞춤` | `match` | `match (x) { case … => }` |
| `시도` | `try` | |
| `처리` | `catch` | |
| `포함` | `import` | Han 파일 include ≠ 창제 패키지 import |
| `패키지` | `package` | |
| `확장` | `extend` | Rust `impl` 대응에 가깝 |
| `인터페이스` | `interface` | |
| `상속`/`구현기호` | `<:` | |

## 리터럴·내장

| 한글 | 창제 |
|------|------|
| `참` | `true` |
| `거짓` | `false` |
| `출력` | `println` |
| `출력오류` | `eprintln` (또는 println stderr — 1차는 println 주석) |
| `길이` | `.size` / 헬퍼 (2차) |

## 창제 2차 맵 (Han에 없거나 다름)

| 한글(제안) | 창제 |
|------------|------|
| `생성` | `spawn` |
| `동기화` | `synchronized` |
| `속성` | `prop` |
| `공개`/`내부`/`비공개` | `public`/`internal`/`private` |
| `오버라이드` | `override` |
| `오픈` | `open` |
| `이즈`/`애즈` | `is`/`as` |

## 치환 순서 (엔진)

1. 문자열·주석 마스크  
2. 멀티토큰 구문 (`만약`…`이면`, `…동안`, `…안에서`)  
3. 키워드 longest-match  
4. 마스크 복원  
5. `main` 엔트리 정규화 (`함수 메인` / `함수 main` → `main`)
