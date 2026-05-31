"""URL Shortener — 短链接生成器"""

import hashlib
import sys

URL_STORE: dict[str, str] = {}


def shorten(url: str) -> str:
    """将长链接转为短码"""
    code = hashlib.md5(url.encode()).hexdigest()[:6]
    URL_STORE[code] = url
    return code


def expand(code: str) -> str | None:
    """根据短码查找原始链接"""
    return URL_STORE.get(code)


def main():
    if len(sys.argv) < 2:
        print("URL Shortener 用法:")
        print("  python main.py shorten <url>  — 生成短码")
        print("  python main.py expand <code>   — 还原链接")
        print("  python main.py list            — 列出所有映射")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "shorten":
        if len(sys.argv) < 3:
            print("请提供 URL")
            sys.exit(1)
        url = sys.argv[2]
        code = shorten(url)
        print(f"短码: {code}  ->  {url}")

    elif cmd == "expand":
        if len(sys.argv) < 3:
            print("请提供短码")
            sys.exit(1)
        code = sys.argv[2]
        url = expand(code)
        if url:
            print(f"原始链接: {url}")
        else:
            print(f"未找到短码: {code}")

    elif cmd == "list":
        if not URL_STORE:
            print("暂无映射")
        else:
            for code, url in URL_STORE.items():
                print(f"  {code}  ->  {url}")

    else:
        print(f"未知命令: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
