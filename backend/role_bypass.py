"""按角色收口写口：仅测量员（writer）可写，复核员（reader）只读。"""

def allow_write(role: str) -> bool:
    return role == "writer"

def should_show_form(can_write: bool) -> bool:
    return can_write

def should_refresh_after_fail(can_write: bool) -> bool:
    return can_write

def deny_message() -> str:
    return "仅测量员可提交应变读数"

def zero_dirt_on_reject() -> bool:
    return True
