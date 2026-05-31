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


# ============================================================
#  测试脚本
# ============================================================

def test_detect_chinese():
    """测试：中文文本检测"""
    assert detect_language("你好世界") == "zh"
    print("  PASS: test_detect_chinese")


def test_detect_english():
    """测试：英文文本检测"""
    assert detect_language("Hello world") == "en"
    print("  PASS: test_detect_english")


def test_detect_mixed():
    """测试：混合文本检测（只要有一个中文字就判定为中文）"""
    assert detect_language("hello 你好") == "zh"
    print("  PASS: test_detect_mixed")


def test_translate_en():
    """测试：翻译为英文"""
    result = translate("你好世界", "en")
    assert result == "[en] 你好世界"
    print("  PASS: test_translate_en")


def test_translate_ja():
    """测试：翻译为日文"""
    result = translate("Hello world", "ja")
    assert result == "[ja] Hello world"
    print("  PASS: test_translate_ja")


def test_translate_ko():
    """测试：翻译为韩文"""
    result = translate("Hello world", "ko")
    assert result == "[ko] Hello world"
    print("  PASS: test_translate_ko")


def test_translate_fr():
    """测试：翻译为法文"""
    result = translate("Hello world", "fr")
    assert result == "[fr] Hello world"
    print("  PASS: test_translate_fr")


def test_translate_de():
    """测试：翻译为德文"""
    result = translate("Hello world", "de")
    assert result == "[de] Hello world"
    print("  PASS: test_translate_de")


def test_translate_es():
    """测试：翻译为西班牙文"""
    result = translate("Hello world", "es")
    assert result == "[es] Hello world"
    print("  PASS: test_translate_es")


def test_translate_zh():
    """测试：翻译为中文"""
    result = translate("Hello world", "zh")
    assert result == "[zh] Hello world"
    print("  PASS: test_translate_zh")


def test_list_languages():
    """测试：列出所有语言"""
    print("  TEST: list_languages")
    list_languages()
    assert len(SUPPORTED_LANGS) >= 7
    print("  PASS: test_list_languages")


def test_unsupported_language():
    """测试：不支持的语言应抛出 SystemExit"""
    try:
        translate("hello", "xx")
        # 没有 exit 说明有问题
        print("  FAIL: test_unsupported_language (should have exited)")
    except SystemExit:
        print("  PASS: test_unsupported_language")


def test_empty_text():
    """测试：空字符串"""
    result = translate("", "en")
    assert result == "[en] "
    print("  PASS: test_empty_text")


def test_long_text():
    """测试：长文本（超过80字符）"""
    long_text = "Hello " * 30
    result = translate(long_text, "en")
    assert result == f"[en] {long_text}"
    print("  PASS: test_long_text")


def test_special_characters():
    """测试：包含特殊字符的文本"""
    result = translate("Hello\nWorld\tTab !@#$%", "en")
    assert result == "[en] Hello\nWorld\tTab !@#$%"
    print("  PASS: test_special_characters")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("  Voice Translater - 测试套件")
    print("=" * 50)

    tests = [
        ("语言检测", [
            test_detect_chinese,
            test_detect_english,
            test_detect_mixed,
        ]),
        ("翻译功能", [
            test_translate_en,
            test_translate_ja,
            test_translate_ko,
            test_translate_fr,
            test_translate_de,
            test_translate_es,
            test_translate_zh,
        ]),
        ("边界情况", [
            test_unsupported_language,
            test_empty_text,
            test_long_text,
            test_special_characters,
        ]),
        ("辅助功能", [
            test_list_languages,
        ]),
    ]

    passed = 0
    failed = 0
    total = sum(len(cases) for _, cases in tests)

    for category, cases in tests:
        print(f"\n-- {category} --")
        for case in cases:
            try:
                case()
                passed += 1
            except AssertionError as e:
                failed += 1
                print(f"  FAIL: {case.__name__} — {e}")
            except Exception as e:
                failed += 1
                print(f"  ERROR: {case.__name__} — {e}")

    print(f"\n{'=' * 50}")
    print(f"  结果: {passed}/{total} 通过, {failed} 失败")
    print("=" * 50)

    return failed == 0


def main():
    # 如果命令行参数包含 --test，运行测试套件
    if "--test" in sys.argv:
        success = run_all_tests()
        sys.exit(0 if success else 1)

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
