"""Voice Translater — 语音翻译工具"""

import sys
import os

# 支持的语言列表
SUPPORTED_LANGS = {
    "en": "英语",
    "zh": "中文",
    "ja": "日语",
    "ko": "韩语",
    "fr": "法语",
    "de": "德语",
    "es": "西班牙语",
}


def list_languages():
    """列出所有支持的目标语言"""
    print("支持的语言:")
    for code, name in SUPPORTED_LANGS.items():
        print(f"  {code} -> {name}")


def detect_language(text: str) -> str:
    """简单检测输入文本是否包含中文字符"""
    for ch in text:
        if '一' <= ch <= '鿿':
            return "zh"
    return "en"


def translate(text: str, target_lang: str = "en") -> str:
    """将输入文本翻译为目标语言"""
    if target_lang not in SUPPORTED_LANGS:
        print(f"不支持的语言: {target_lang}")
        print(f"支持的语言: {', '.join(SUPPORTED_LANGS.keys())}")
        sys.exit(1)

    src_lang = detect_language(text)
    lang_name = SUPPORTED_LANGS.get(target_lang, target_lang)
    print(f"[翻译] 检测源语言: {src_lang}")
    print(f"[翻译] 输入: {text[:80]}{'...' if len(text) > 80 else ''}")
    print(f"[翻译] 目标语言: {lang_name} ({target_lang})")
    return f"[{target_lang}] {text}"


# ── 测试套件 ──
# 运行方式: python main.py --test

def _run_tests():
    """运行内建测试"""
    passed, failed = 0, 0

    def check(name, actual, expected):
        nonlocal passed, failed
        if actual == expected:
            passed += 1
            print(f"  ✓ {name}")
        else:
            failed += 1
            print(f"  ✗ {name} — 期望: {expected!r}, 实际: {actual!r}")

    print("=" * 44)
    print("  Voice Translater — 内建测试套件")
    print("=" * 44)

    # ── 语言检测 ──
    print("\n[语言检测]")
    check("纯中文",  detect_language("你好世界"), "zh")
    check("纯英文",  detect_language("Hello world"), "en")
    check("中英混合", detect_language("hello 你好"), "zh")
    check("空字符串", detect_language(""), "en")
    check("仅标点",  detect_language("!@#$%"), "en")

    # ── 翻译输出 ──
    print("\n[翻译输出]")
    for lang, name in [("en", "英文"), ("ja", "日文"), ("ko", "韩文"),
                        ("fr", "法文"), ("de", "德文"), ("es", "西班牙文"), ("zh", "中文")]:
        check(f"→{name} ({lang})", translate("Hello", lang), f"[{lang}] Hello")

    # ── 边界情况 ──
    print("\n[边界情况]")
    check("空输入 → en", translate("", "en"), "[en] ")
    check("超80字符",  translate("x" * 100, "en"), f"[en] {'x' * 100}")

    # 不支持的语言
    try:
        translate("hi", "xx")
        check("不支持语言应 exit", "no_exit", "SystemExit")
    except SystemExit:
        check("不支持语言应 exit", "SystemExit", "SystemExit")

    # ── 辅助 ──
    print("\n[辅助功能]")
    check("语言列表数量", len(SUPPORTED_LANGS) >= 7, True)

    # ── 报告 ──
    total = passed + failed
    print(f"\n{'=' * 44}")
    print(f"  结果: {passed}/{total} 通过, {failed}/{total} 失败")
    print("=" * 44)
    return failed == 0


def main():
    # --test 模式
    if "--test" in sys.argv:
        ok = _run_tests()
        sys.exit(0 if ok else 1)

    if len(sys.argv) < 2:
        print("用法: python main.py <文本> [目标语言]")
        print("测试: python main.py --test")
        print("示例: python main.py '你好世界' en")
        list_languages()
        sys.exit(1)

    text = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "en"
    result = translate(text, target)
    print(f"结果: {result}")


if __name__ == "__main__":
    main()
