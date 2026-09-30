"""Reader treated as writer + form always visible."""

def allow_write(role: str) -> bool:
    return role in {"writer", "reader"}

def should_show_form(_can_write: bool) -> bool:
    return True

def should_refresh_after_fail(_can_write: bool) -> bool:
    return True

def deny_message() -> str:
    return "仅测量员可提交应变读数"

def zero_dirt_on_reject() -> bool:
    return False
