"""Miscellaneous commands."""

__all__ = [
    "comment",
    "user_prompt",
    "set_variable",
    "start_timer",
    "wait_timer",
    "facts",
]


def comment(msg: str):
    """Write comment."""
    return f'B;Comment("{msg}");'.encode()


def user_prompt(msg: str, sound: bool = False, timeout: int = -1):
    """Open user prompt."""
    return f'B;UserPrompt("{msg}",{sound:d},{timeout});'.encode()


def set_variable(name: str, value: int):
    """Set a variable."""
    return f'B;Variable({name},"{value}",0,"",0,1.000000,10.000000,0,2,0,0);'.encode()


def start_timer(index: int):
    """Start timer."""
    return f'B;StartTimer("{index}");'.encode()


def wait_timer(index: int, time: int):
    """Wait for timer."""
    return f'B;WaitTimer("{index}","{time}");'.encode()


def facts(
    device: str,
    command: str,
    parameter: str,
    needs_labware: bool,
    allowed_labware: str,
):
    """General FACTS command"""
    return (
        "B;FACTS("
        f'"{device}",'
        f'"{command}",'
        f'"{parameter}",'
        f'"{needs_labware:d}",'
        f'"{allowed_labware}",'
        ");"
    ).encode()
