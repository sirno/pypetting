"""Module for custom exceptions."""

__all__ = ["GridSiteException"]


class PypettingException(Exception):
    """Base class for pypetting exceptions."""


class GridSiteException(PypettingException):
    """Exceptions related to container elements on the grid."""

    def __init__(self, msg):
        self.msg = msg
        super().__init__()
