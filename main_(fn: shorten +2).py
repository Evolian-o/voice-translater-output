python
import sys
import hashlib
import random
from typing import Dict
from urllib.parse import urlparse

URL_STORE: Dict[str, str] = {}


def shorten(url: str) -> str:
    """将长链接转为短码"""
    suffix = 0
    while True:
        raw = f"{url}{random.randint(1000, 9999)}{suffix}"
        code = hashlib.sha256(raw.encode()).hexdigest()[:8]
        if code not in URL_STORE or URL_STORE[code] == url:
            break
        suffix += 1
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
        parsed_url = urlparse(url)
        allowed_schemes = {"http", "https"}
        if parsed_url.scheme not in allowed_schemes or not parsed_url.netloc:
            print("错误：仅支持HTTP/HTTPS协议的合法URL")
            sys.exit(1)
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