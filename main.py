"""Voice Translater — 语音翻译工具"""

import sys


def translate(text: str, target_lang: str = "en") -> str:
    """将输入文本翻译为目标语言"""
    print(f"[翻译] 输入: {text[:80]}{'...' if len(text) > 80 else ''}")
    print(f"[翻译] 目标语言: {target_lang}")
    return f"[{target_lang}] {text}"


def main():
    if len(sys.argv) < 2:
        print("用法: python main.py <文本> [目标语言]")
        print("示例: python main.py '你好世界' en")
        sys.exit(1)

    text = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "en"
    result = translate(text, target)
    print(f"结果: {result}")


if __name__ == "__main__":
    main()
