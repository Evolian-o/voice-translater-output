"""Random Utilities — 随机工具集合"""

import random
import string
import sys


def generate_password(length: int = 16) -> str:
    """生成随机密码"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))


def roll_dice(sides: int = 6, count: int = 1) -> list[int]:
    """掷骰子"""
    return [random.randint(1, sides) for _ in range(count)]


def pick_one(items: list[str]) -> str:
    """从列表中随机选一个"""
    return random.choice(items)


def shuffle_list(items: list[str]) -> list[str]:
    """随机打乱列表"""
    random.shuffle(items)
    return items


def main():
    if len(sys.argv) < 2:
        print("Random Utilities 用法:")
        print("  python main.py password [长度]  — 生成随机密码")
        print("  python main.py dice [面数] [次数] — 掷骰子")
        print("  python main.py pick a b c ...  — 随机选一个")
        print("  python main.py shuffle a b c ... — 随机打乱")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "password":
        length = int(sys.argv[2]) if len(sys.argv) > 2 else 16
        print(f"密码: {generate_password(length)}")

    elif cmd == "dice":
        sides = int(sys.argv[2]) if len(sys.argv) > 2 else 6
        count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        results = roll_dice(sides, count)
        print(f"掷 {count} 个 {sides} 面骰子: {results} (总和: {sum(results)})")

    elif cmd == "pick":
        items = sys.argv[2:]
        if not items:
            print("请提供选项列表")
            sys.exit(1)
        print(f"随机选择: {pick_one(items)}")

    elif cmd == "shuffle":
        items = sys.argv[2:]
        if not items:
            print("请提供选项列表")
            sys.exit(1)
        print(f"随机打乱: {shuffle_list(items)}")

    else:
        print(f"未知命令: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
