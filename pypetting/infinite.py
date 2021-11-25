"""Infinite Reader Commands."""

from .misc import facts

__all__ = [
    "open_infinite_reader",
    "close_infinite_reader",
    "measure_infinite_reader",
]


def open_infinite_reader():
    """Open infinite reader."""
    return facts("ReaderNETwork", "ReaderNETwork_Open", "", 0, "")


def close_infinite_reader():
    """Close infinite reader."""
    return facts("ReaderNETwork", "ReaderNETwork_Close", "", 0, "")


def measure_infinite_reader(path: str, settings_path: str):
    """Measure infinite reader."""
    with open(settings_path, encoding="utf8") as settings_file:
        settings = settings_file.read()

    settings_string = (
        settings.replace('"', "&quote;")
        .replace("=", "&equal;")
        .replace("  ", "")
        .replace("\n", " ")
        .replace("> <", "><")
        .replace(" />", "/>")
    )

    return facts(
        "ReaderNETwork",
        "ReaderNETwork_Measure",
        f"{path}|{settings_string}",
        0,
        "",
    )
