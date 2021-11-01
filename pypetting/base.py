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
class GridStack:
    """Specify a stash."""

    grid: int
    capacity: int
    carrier: str
    size: int = 0

    def push(self) -> GridSite:
        """Add element to stash."""
        self.size += 1
        return GridSite(self.grid, self.size - 1, self.carrier)

    def pop(self) -> GridSite:
        """Remove element from stash."""
        self.size -= 1
        return GridSite(self.grid, self.size, self.carrier)


@dataclass_json
@dataclass
class GridQueue:
    """Specify a stash."""

    grid: int
    capacity: int
    carrier: str
    first: int = 0
    last: int = 0

    def push(self) -> GridSite:
        """Add element to queue."""
        self.last += 1
        return GridSite(self.grid, self.last - 1, self.carrier)

    def pop(self) -> GridSite:
        """Get element from queue."""
        self.first += 1
        return GridSite(self.grid, self.first - 1, self.carrier)

    @property
    def size(self) -> int:
        """Number of elements in the queue."""
        return self.last - self.first


@dataclass(frozen=True)
class Labware:
    """Labware specification."""

    name: str
    rows: int
    cols: int
    spacing: int = 1
