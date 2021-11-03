"""Base classes."""
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

__all__ = [
    "GridSite",
    "GridStack",
    "GridQueue",
    "Labware",
]


class _DataClassCached(DataClassJsonMixin):
    """Wrapper class to add file writing to dataclass json serde."""

    def write_to_file(self, path):
        """Write dataclass to file."""
        with open(path, "w", encoding="utf8") as file_descriptor:
            file_descriptor.write(self.to_json())

    @classmethod
    def load_from_file(cls, path):
        """Load dataclass from file."""
        with open(path, "r", encoding="utf8") as file_descriptor:
            return cls.from_json(file_descriptor.read())


@dataclass(frozen=True)
class GridSite:
    """Specify a grid site."""

    grid: int
    site: int
    carrier: str


@dataclass
class GridStack(_DataClassCached):
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


@dataclass
class GridQueue(_DataClassCached):
    """Round robin queue."""

    grid: int
    capacity: int
    carrier: str
    first: int = 0
    last: int = 0

    def push(self) -> GridSite:
        """Add element to queue."""
        self.last = (self.last + 1) % self.capacity
        return GridSite(self.grid, self.last - 1, self.carrier)

    def pop(self) -> GridSite:
        """Get element from queue."""
        self.first = (self.first + 1) % self.capacity
        return GridSite(self.grid, self.first - 1, self.carrier)

    @property
    def size(self) -> int:
        """Number of elements in the queue."""
        size = self.last - self.first
        if size < 0:
            size = size + self.capacity
        return size


@dataclass(frozen=True)
class Labware:
    """Labware specification."""

    name: str
    rows: int
    cols: int
    spacing: int = 1
