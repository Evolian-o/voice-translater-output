python
import sys

def translate(text: str, target_lang: str = "en") -> str:
    """将输入文本翻译为目标语言"""
    print(f"[翻译] 输入: {text[:80]}{'...' if len(text) > 80 else ''}")
    print(f"[翻译] 目标语言: {target_lang}")
    # TODO: 集成实际翻译API
    # 例如: from googletrans import Translator
    # translator = Translator()
    # return translator.translate(text, dest=target_lang).text
    return f"[{target_lang}] {text}"  # 占位实现


def main():
    if len(sys.argv) < 2:
        print("用法: python main.py <文本> [目标语言]", file=sys.stderr)
        print("示例: python main.py '你好世界' en", file=sys.stderr)
        sys.exit(1)

    text = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "en"
    result = translate(text, target)
    print(f"结果: {result}")