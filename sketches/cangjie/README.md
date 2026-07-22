# 창한 번역 스케치 (창제 호스트)

맵은 `spec/KEYWORD_MAP.md`와 동일. 파일 IO + 단순 치환은 `std.fs` / String API로 승격 가능.

```cangjie
package changhan_sketch

// SCORE 채택 시 engine/ 로직을 .cj 로 이식하는 자리
main() {
    println("changhan sketch host=cangjie")
}
```

VERIFY: `cjpm build` in this folder after copying to a cjpm package (see smoke_proj pattern).
