import sys
import re
from contextlib import redirect_stdout
import io

# 预编译中文检测正则，避免每次调用重复编译
RE_CHINESE = re.compile(r'[\u4e00-\u9fff]')

SUPPORTED_LANGS = {
    "en": "英文",
    "zh": "中文",
    "ja": "日文",
    "ko": "韩文",
    "fr": "法文",
    "de": "德文",
    "es": "西班牙文",
}


class UnsupportedLanguageError(Exception):
    pass


def list_languages():
    """列出所有支持的目标语言"""
    print("支持的语言:")
    for code, name in SUPPORTED_LANGS.items():
        print(f"  {code} -> {name}")


def detect_language(text: str) -> str:
    """简单检测输入文本是否包含中文字符"""
    if RE_CHINESE.search(text):
        return "zh"
    return "en"


def translate(text: str, target_lang: str = "en") -> str:
    """将输入文本翻译为目标语言"""
    if target_lang not in SUPPORTED_LANGS:
        raise UnsupportedLanguageError(
            f"不支持的语言: {target_lang}\n支持的语言: {', '.join(SUPPORTED_LANGS.keys())}"
        )

    src_lang = detect_language(text)
    lang_name = SUPPORTED_LANGS[target_lang]  # 直接访问，无需 get
    print(f"[翻译] 检测源语言: {src_lang}")
    print(f"[翻译] 输入: {text[:80]}{'...' if len(text) > 80 else ''}")
    print(f"[翻译] 目标语言: {lang_name} ({target_lang})")
    return f"[{target_lang}] {text}"


# 测试套件，与主逻辑分离
def _run_tests():
    """运行内建测试"""
    passed, failed = 0, 0

    def check(name, actual, expected):
        nonlocal passed, failed
        if actual == expected:
            passed += 1
            print(f"  \u2713 {name}")
        else:
            failed += 1
            print(f"  \u2717 {name} \u2014 \u671f\u671b: {expected!r}, \u5b9e\u9645: {actual!r}")

    print("=" * 44)
    print("  Voice Translater \u2014 \u5185\u5efa\u6d4b\u8bd5\u5957\u4ef6")
    print("=" * 44)

    # 语言检测
    print("\n[\u8bed\u8a00\u68c0\u6d4b]")
    check("\u7eaf\u4e2d\u6587",  detect_language("\u4f60\u597d\u4e16\u754c"), "zh")
    check("\u7eaf\u82f1\u6587",  detect_language("Hello world"), "en")
    check("\u4e2d\u82f1\u6df7\u5408", detect_language("hello \u4f60\u597d"), "zh")
    check("\u7a7a\u5b57\u7b26\u4e32", detect_language(""), "en")
    check("\u4ec5\u6807\u70b9",  detect_language("!@#$%"), "en")

    # 翻译输出
    print("\n[\u7ffb\u8bd1\u8f93\u51fa]")
    for lang, name in SUPPORTED_LANGS.items():
        check(f"\u2192{name} ({lang})", translate("Hello", lang), f"[{lang}] Hello")

    # 边界情况
    print("\n[\u8fb9\u754c\u60c5\u51b5]")
    check("\u7a7a\u8f93\u5165 \u2192 en", translate("", "en"), "[en] ")
    check("\u8d8580\u5b57\u7b26",  translate("x" * 100, "en"), f"[en] {'x' * 100}")

    # 不支持的语言：应抛出异常
    try:
        with redirect_stdout(io.StringIO()):
            translate("hi", "xx")
        check("\u4e0d\u652f\u6301\u8bed\u8a00\u5e94\u629b\u51fa\u5f02\u5e38", "no_exception", "UnsupportedLanguageError")
    except UnsupportedLanguageError:
        check("\u4e0d\u652f\u6301\u8bed\u8a00\u5e94\u629b\u51fa\u5f02\u5e38", "UnsupportedLanguageError", "UnsupportedLanguageError")

    # 辅助功能
    print("\n[\u8f85\u52a9\u529f\u80fd]")
    check("\u8bed\u8a00\u5217\u8868\u6570\u91cf", len(SUPPORTED_LANGS) >= 7, True)

    # 报告
    total = passed + failed
    print(f"\n{'=' * 44}")
    print(f"  \u7ed3\u679c: {passed}/{total} \u901a\u8fc7, {failed}/{total} \u5931\u8d25")
    print("=" * 44)
    return failed == 0


def main():
    # 测试模式
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
    try:
        result = translate(text, target)
        print(f"结果: {result}")
    except UnsupportedLanguageError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()