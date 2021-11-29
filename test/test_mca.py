"""MCA tests."""

from itertools import product

from pypetting import GridSite
from pypetting.mca import (
    mca_aspirate,
    mca_dispense,
    mca_mix,
    mca_get_tips,
    mca_drop_tips,
)

grid_site = GridSite(40, 0, "MP 3Pos")


def test_mca_aspirate():
    """Test MCA aspirate."""
    out = [
        b'B;MCAAspirate("A","10",40,0,"181000X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z",0,0);',
        b'B;MCAAspirate("A","10",40,0,"1810Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00",0,0);',
        b'B;MCAAspirate("A","10",40,0,"181000\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE",0,0);',
        b'B;MCAAspirate("A","10",40,0,"1810\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z500",0,0);',
    ]
    for idx, (row, col) in enumerate(product([0, 1], repeat=2)):
        assert mca_aspirate(grid_site, row, col, 10, "A", "greiner384") == out[idx]


def test_mca_dispense():
    """Test MCA dispense."""
    out = [
        b'B;MCADispense("A","10",40,0,"181000X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z",0,0);',
        b'B;MCADispense("A","10",40,0,"1810Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00",0,0);',
        b'B;MCADispense("A","10",40,0,"181000\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE",0,0);',
        b'B;MCADispense("A","10",40,0,"1810\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z500",0,0);',
    ]
    for idx, (row, col) in enumerate(product([0, 1], repeat=2)):
        assert mca_dispense(grid_site, row, col, 10, "A", "greiner384") == out[idx]


def test_mca_mix():
    """Test MCA mix."""
    out = [
        b'B;MCAMix("A","10",40,0,"181000X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z",0,0);',
        b'B;MCAMix("A","10",40,0,"1810Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00",0,0);',
        b'B;MCAMix("A","10",40,0,"181000\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE",0,0);',
        b'B;MCAMix("A","10",40,0,"1810\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z50pZ\x8500X\x85:00\x85Z10\x80ZE00Z\x8520P\x85Z00\x84Z500",0,0);',
    ]
    for idx, (row, col) in enumerate(product([0, 1], repeat=2)):
        assert mca_mix(grid_site, row, col, 10, "A", "greiner384") == out[idx]


def test_mca_get_tips():
    """Test MCA get tips."""
    assert mca_get_tips(grid_site) == b"B;MCAGetDitis(40,0,20,96,0,0);"


def test_mca_drop_tips():
    """Test MCA get tips."""
    assert mca_drop_tips(grid_site) == b"B;MCADropDitis(40,0,1,0,0,0);"
