"""Infinite Reader Commands."""

from .misc import facts


def open_infinite_reader():
    """Open infinite reader."""
    return facts("ReaderNETwork", "ReaderNETwork_Open", "", 0, "")


def close_infinite_reader():
    """Close infinite reader."""
    return facts("ReaderNETwork", "ReaderNETwork_Close", "", 0, "")


def measure_infinite_reader(path, settings):
    """Measure infinite reader."""
    return facts("ReaderNETwork", "ReaderNETwork_Measure", f"{path}|{settings}", 0, "")
