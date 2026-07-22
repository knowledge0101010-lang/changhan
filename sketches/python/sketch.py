"""Python host sketch — delegates to lab engine map."""

KEYWORD = {"함수": "func", "변수": "var", "출력": "println"}


def translate_token(tok: str) -> str:
    return KEYWORD.get(tok, tok)


if __name__ == "__main__":
    assert translate_token("함수") == "func"
    assert translate_token("함수") != "fn"  # ≠ Rust
    print("ok")
