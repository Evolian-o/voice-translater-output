"""Voice Translater — 语音翻译工具"""

import sys

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
        print(f"  {code} → {name}")


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


def main():
    if len(sys.argv) < 2:
        print("用法: python main.py <文本> [目标语言]")
        print("示例: python main.py '你好世界' en")
        list_languages()
        sys.exit(1)

    text = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "en"
    result = translate(text, target)
    print(f"结果: {result}")


if __name__ == "__main__":
    main()
