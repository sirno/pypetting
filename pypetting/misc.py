"""Miscellaneous commands."""


def comment(msg):
    """Write comment."""
    return f'B;Comment("{msg}");'


def user_prompt(msg, sound=0, timeout=-1):
    """Open user prompt."""
    return f'B;UserPrompt("{msg}",{sound},{timeout});'


def start_timer(index):
    """Start timer."""
    return f'B;StartTimer("{index}");'


def wait_timer(index, time):
    """Wait for timer."""
    return f'B;WaitTimer("{index}","{time}");'
