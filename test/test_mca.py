"""MCA tests."""

from itertools import product

from pypetting import GridSite
from pypetting.mca import (
    mca_aspirate,
    mca_dispense,
)

grid_site = GridSite(40, 0, "MP 3Pos")


def test_mca_aspirate():
    """Test MCA aspirate."""
    for row, col in product([0, 1], repeat=2):
        assert mca_aspirate(grid_site, row, col, 10, "A", "greiner384")
