//! Changhan Rust host sketch — same keyword map, no full Han compiler.

fn translate_keyword(kr: &str) -> Option<&'static str> {
    match kr {
        "함수" => Some("func"),
        "변수" => Some("var"),
        "상수" => Some("let"),
        "만약" => Some("if"),
        "아니면" => Some("else"),
        "출력" => Some("println"),
        "참" => Some("true"),
        "거짓" => Some("false"),
        "정수" => Some("Int64"),
        _ => None,
    }
}

fn main() {
    println!("{}", translate_keyword("출력").unwrap());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn map_smoke() {
        assert_eq!(translate_keyword("함수"), Some("func"));
        assert_eq!(translate_keyword("변수"), Some("var"));
        assert_ne!(translate_keyword("함수"), Some("fn")); // ≠ Rust
    }
}
