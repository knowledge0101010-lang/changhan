"""창한 번역 엔진 — .cjh(한글 표면) → .cj(공식 창제).

화웨이 공식 제품이 아니며 창제 SDK의 원본 소유자가 아닙니다. NOTICE.md 참고.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Longest-first keyword map (Han UX → Cangjie). See spec/KEYWORD_MAP.md
KEYWORD_MAP: list[tuple[str, str]] = [
    ("출력오류", "println"),  # 1차: stdout로 대체
    ("아니면", "else"),
    ("함수", "func"),
    ("반환", "return"),
    ("변수", "var"),
    ("상수", "let"),
    ("만약", "if"),
    ("그리고", "&&"),
    ("또는", "||"),
    ("반복", "for"),
    ("동안", "while"),
    ("안에서", "in"),
    ("멈춰", "break"),
    ("계속", "continue"),
    ("구조", "struct"),
    ("클래스", "class"),
    ("열거", "enum"),
    ("맞춤", "match"),
    ("시도", "try"),
    ("처리", "catch"),
    ("포함", "import"),
    ("패키지", "package"),
    ("확장", "extend"),
    ("인터페이스", "interface"),
    ("정수", "Int64"),
    ("실수", "Float64"),
    ("문자열", "String"),
    ("불", "Bool"),
    ("없음", "Unit"),
    ("참", "true"),
    ("거짓", "false"),
    ("출력", "println"),
    ("생성", "spawn"),
    ("속성", "prop"),
    ("공개", "public"),
    ("내부", "internal"),
    ("비공개", "private"),
    ("오버라이드", "override"),
    ("오픈", "open"),
]

_STRING_RE = re.compile(
    r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\')'
)
_LINE_COMMENT_RE = re.compile(r"//[^\n]*")
_BLOCK_COMMENT_RE = re.compile(r"/\*[\s\S]*?\*/")


def _mask(src: str) -> tuple[str, list[str]]:
    slots: list[str] = []

    def keep(m: re.Match[str]) -> str:
        slots.append(m.group(0))
        return f"\x00S{len(slots) - 1}\x00"

    out = _STRING_RE.sub(keep, src)
    out = _BLOCK_COMMENT_RE.sub(keep, out)
    out = _LINE_COMMENT_RE.sub(keep, out)
    return out, slots


def _unmask(src: str, slots: list[str]) -> str:
    for i, s in enumerate(slots):
        src = src.replace(f"\x00S{i}\x00", s)
    return src


def _word_replace(src: str, kr: str, en: str) -> str:
    # Hangul keywords: replace when not mid-identifier (no hangul/alnum/_ adjacent)
    pattern = re.compile(
        rf"(?<![0-9A-Za-z_\uac00-\ud7a3]){re.escape(kr)}(?![0-9A-Za-z_\uac00-\ud7a3])"
    )
    return pattern.sub(en, src)


def _fix_if_imyun(src: str) -> str:
    # 만약 COND 이면 {  →  if (COND) {
    return re.sub(
        r"\bif\s+(.+?)\s+이면\s*\{",
        lambda m: f"if ({m.group(1).strip()}) {{",
        src,
    )


def _fix_while_soz(src: str) -> str:
    # COND 동안 { → while (COND) {
    src = re.sub(
        r"(?<![0-9A-Za-z_])(.+?)\s+while\s*\{",
        lambda m: f"while ({m.group(1).strip()}) {{",
        src,
    )
    # while COND { → while (COND) {
    src = re.sub(
        r"\bwhile\s+([^{\n]+)\s*\{",
        lambda m: f"while ({m.group(1).strip()}) {{",
        src,
    )
    return src


def _fix_for_in(src: str) -> str:
    # for x in xs { → for (x in xs) {
    return re.sub(
        r"\bfor\s+(\w+)\s+in\s+([^{\n]+)\s*\{",
        lambda m: f"for ({m.group(1)} in {m.group(2).strip()}) {{",
        src,
    )


def _fix_match(src: str) -> str:
    # match EXPR { → match (EXPR) {  if not already parenthesized
    def repl(m: re.Match[str]) -> str:
        expr = m.group(1).strip()
        if expr.startswith("("):
            return m.group(0)
        return f"match ({expr}) {{"

    return re.sub(r"\bmatch\s+([^{\n]+)\s*\{", repl, src)


def _fix_func_arrow(src: str) -> str:
    # func name(...)-> T {  or  func name(...) -> T {
    src = re.sub(
        r"\bfunc\s+(\w+)\s*(\([^)]*\))\s*->\s*(\w+)",
        r"func \1\2: \3",
        src,
    )
    # func main(...) → main()  (cangjie package entry; keep trailing space)
    src = re.sub(r"\bfunc\s+main\s*\([^)]*\)\s*(:\s*\w+)?", "main()", src)
    src = re.sub(r"\bfunc\s+메인\s*\([^)]*\)\s*(:\s*\w+)?", "main()", src)
    src = re.sub(r"main\(\)\{", "main() {", src)
    src = re.sub(r"\)\{", ") {", src)
    # bare: main already after 메인 keyword map? 메인 not in map — handle hangul main name
    return src


def _fix_bare_if(src: str) -> str:
    # if COND { without parens (when 이면 already stripped)
    def repl(m: re.Match[str]) -> str:
        cond = m.group(1).strip()
        if cond.startswith("("):
            return m.group(0)
        return f"if ({cond}) {{"

    return re.sub(r"\bif\s+([^{\n]+)\s*\{", repl, src)


def translate(source: str) -> str:
    masked, slots = _mask(source)
    out = masked
    for kr, en in sorted(KEYWORD_MAP, key=lambda kv: -len(kv[0])):
        out = _word_replace(out, kr, en)
    # leftover 이면 (if pattern missed)
    out = _word_replace(out, "이면", "")
    out = _fix_if_imyun(out)
    out = _fix_bare_if(out)
    out = _fix_while_soz(out)
    out = _fix_for_in(out)
    out = _fix_match(out)
    out = _fix_func_arrow(out)
    # collapse double spaces from 이면 removal
    out = re.sub(r"[ \t]{2,}", " ", out)
    return _unmask(out, slots)


def translate_file(path: Path) -> str:
    return translate(path.read_text(encoding="utf-8"))


def _ensure_package_wrapper(cj: str, package: str = "changhan_smoke") -> str:
    if re.search(r"^\s*package\s+", cj, re.M):
        return cj
    return f"package {package}\n\n{cj}"


def run_with_cjpm(cjh: Path, *, envsetup: Path | None = None) -> int:
    cj = _ensure_package_wrapper(translate_file(cjh))
    proj = ROOT / "smoke_proj"
    src = proj / "src" / "main.cj"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(cj, encoding="utf-8")
    toml = proj / "cjpm.toml"
    if not toml.exists():
        toml.write_text(
            '[package]\n  name = "changhan_smoke"\n  version = "0.1.0"\n'
            '  cjc-version = "1.0.0"\n  output-type = "executable"\n',
            encoding="utf-8",
        )

    bash = "set -euo pipefail\n"
    if envsetup and envsetup.exists():
        bash += f"source '{envsetup}'\n"
    else:
        default = ROOT.parents[1] / "system" / "untitled-bridge" / "envsetup-mac105.sh"
        if default.exists():
            bash += f"source '{default}'\n"
    bash += f"cd '{proj}' && cjpm build && cjpm run\n"
    return subprocess.call(["bash", "-lc", bash])


def _self_test() -> None:
    cases = [
        (
            '함수 main() {\n    출력("안녕하세요")\n}\n',
            'main()',
            'println("안녕하세요")',
        ),
        (
            "만약 x > 0 이면 {\n    반환 x\n} 아니면 {\n    반환 0\n}\n",
            "if (x > 0)",
            "else",
        ),
        (
            "변수 a: 정수 = 1\n상수 b = 참\n",
            "var a: Int64 = 1",
            "let b = true",
        ),
        (
            '출력("함수는 문자열")\n',
            'println("함수는 문자열")',
            "",
        ),
    ]
    failed = 0
    for src, *needles in cases:
        out = translate(src)
        for n in needles:
            if n and n not in out:
                print(f"FAIL need {n!r} in:\n{out}", file=sys.stderr)
                failed += 1
        # string must keep hangul keyword inside quotes
        if "함수는" in src and "println(\"함수는" not in out.replace("'", '"'):
            if 'println("함수는 문자열")' not in out:
                print(f"FAIL string mask:\n{out}", file=sys.stderr)
                failed += 1
    # golden files
    examples = ROOT / "examples"
    golden = ROOT / "golden"
    if examples.exists():
        for cjh in sorted(examples.glob("*.cjh")):
            g = golden / (cjh.stem + ".cj")
            got = translate_file(cjh)
            if g.exists():
                exp = g.read_text(encoding="utf-8")
                if got.strip() != exp.strip():
                    print(f"FAIL golden {cjh.name}\n--- got ---\n{got}\n--- exp ---\n{exp}", file=sys.stderr)
                    failed += 1
            else:
                print(f"WARN no golden for {cjh.name}", file=sys.stderr)
    if failed:
        raise SystemExit(failed)
    print("ok")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="cjh", description="창한: 한글 → 창제 번역 엔진")
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("translate", help="번역만 수행")
    t.add_argument("input", type=Path)
    t.add_argument("-o", "--output", type=Path)

    r = sub.add_parser("run", help="번역 후 cjpm으로 실행")
    r.add_argument("input", type=Path)

    sub.add_parser("test", help="자체·골든 테스트")

    args = p.parse_args(argv)
    if args.cmd == "translate":
        out = translate_file(args.input)
        if args.output:
            args.output.write_text(out, encoding="utf-8")
        else:
            sys.stdout.write(out)
    elif args.cmd == "run":
        raise SystemExit(run_with_cjpm(args.input))
    elif args.cmd == "test":
        _self_test()


if __name__ == "__main__":
    main()
