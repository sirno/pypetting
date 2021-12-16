"""Te-Shaker commands."""
from .misc import facts
from .misc import start_timer, wait_timer

__all__ = [
    "teshake_shake",
    "teshake_init",
    "teshake_start",
    "teshake_stop",
    "teshake_set_frequency",
]


def teshake_shake(frequency=1000, time=10, timer_id=40):
    """Shake with teshake."""
    return b"\n".join(
        [
            teshake_init(),
            teshake_set_frequency(frequency),
            teshake_start(),
            start_timer(timer_id),
            wait_timer(timer_id, time),
            teshake_stop(),
        ]
    )


def teshake_init():
    """Init teshake."""
    return facts("Shaker", "Shaker_Init", "", False, "")


def teshake_start(clockwise: bool = True):
    """Start teshake."""
    return facts("Shaker", "Shaker_Start", f"{1 + (not clockwise)}", False, "")


def teshake_stop():
    """Stop teshake."""
    return facts("Shaker", "Shaker_Stop", "", False, "")


def teshake_set_frequency(frequency=1000):
    """Start teshake."""
    return facts("Shaker", "Shaker_SetFrequency", f"{frequency}", False, "")
