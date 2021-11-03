"""Miscellaneous commands."""

__all__ = [
    "comment",
    "user_prompt",
    "set_variable",
    "start_timer",
    "wait_timer",
    "facts",
]


def comment(msg):
    """Write comment."""
    return f'B;Comment("{msg}");'.encode()


def user_prompt(msg, sound=0, timeout=-1):
    """Open user prompt."""
    return f'B;UserPrompt("{msg}",{sound},{timeout});'.encode()


def set_variable(name, value):
    """Set a variable."""
    return f'B;Variable({name},"{value}",0,"",0,1.000000,10.000000,0,2,0,0);'.encode()


def start_timer(index):
    """Start timer."""
    return f'B;StartTimer("{index}");'.encode()


def wait_timer(index, time):
    """Wait for timer."""
    return f'B;WaitTimer("{index}","{time}");'.encode()


def facts(device, command, parameter, needs_labware, allowed_labware):
    """General FACTS command"""
    return (
        "B;FACTS("
        f'"{device}",'
        f'"{command}",'
        f'"{parameter}",'
        f'"{needs_labware}",'
        f'"{allowed_labware}",'
        ");"
    ).encode()
