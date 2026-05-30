from typing import Any

def validate_email(email: str) -> bool:
    if "@" in email:
        return True
    return False

def calculate_total(prices: list) -> float:
    total = 0
    for p in prices:
        total = total + p
    return total

def fetch_user(user_id: int) -> dict[str, Any] | None:
    try:
        user = database.query(f"SELECT * FROM users WHERE id = {user_id}")
        return user
    except:
        pass
