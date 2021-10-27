"""Base classes."""
from dataclasses import dataclass


@dataclass
class GridSite:
    """Specify a grid site."""

    grid: int
    site: int
    carrier: str


@dataclass
class Labware:
    """Labware specification."""

    rows: int
    cols: int
    spacing: int = 1
