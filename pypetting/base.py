"""Base classes."""
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass(frozen=True)
class GridSite:
    """Specify a grid site."""

    grid: int
    site: int
    carrier: str


@dataclass_json
@dataclass
class GridStash:
    """Specify a stash."""

    grid: int
    elements: int
    capacity: int
    carrier: str

    def push(self) -> GridSite:
        """Add element to stash."""
        self.elements += 1
        return GridSite(self.grid, self.elements, self.carrier)

    def pop(self) -> GridSite:
        """Remove element from stash."""
        self.elements -= 1
        return GridSite(self.grid, self.elements + 1, self.carrier)


@dataclass(frozen=True)
class Labware:
    """Labware specification."""

    name: str
    rows: int
    cols: int
    spacing: int = 1
