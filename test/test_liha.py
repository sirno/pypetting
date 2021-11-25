"""Pipetting unit tests."""

import numpy as np

from pypetting import (
    GridSite,
    aspirate,
    dispense,
    mix,
    wash,
    move_liha,
)

FIRST = np.array([True] + 7 * [False])
COL96 = np.array(8 * [True])
grid_site = GridSite(40, 0, "MP 3Pos")


def test_liha_aspirate():
    """Test LiHa aspirate."""
    assert (
        aspirate(grid_site, 1, FIRST, 1 * FIRST, "A", labware="trough100")
        == b'B;Aspirate(1,"A","1.0","0","0","0","0","0","0","0","0","0","0","0",40,0,1,"010810",0,0);'
    )


def test_liha_dispense():
    """Test Liha dispense."""
    assert (
        dispense(grid_site, 1, FIRST, 1 * FIRST, "A", labware="trough100")
        == b'B;Dispense(1,"A","1.0","0","0","0","0","0","0","0","0","0","0","0",40,0,1,"010810",0,0);'
    )


def test_liha_mix():
    """Test Liha mix."""
    assert (
        mix(grid_site, 1, FIRST, 1 * FIRST, "A", labware="trough100")
        == b'B;Mix(1,"A","1.0","0","0","0","0","0","0","0","0","0","0","0",40,0,1,"010810",0,0);'
    )


def test_wash():
    """Test LiHa wash."""
    assert (
        wash(waste_volume=1, cleaner_volume=0.1, station=10)
        == b'B;Wash(255,10,1,10,0,"1",500,"0.1",0,10,70,30,0,0,1000,0);'
    )


def test_move_liha():
    """Test LiHa move."""
    assert (
        move_liha(grid_site, 1, labware="trough100")
        == b'B;MoveLiha(255,40,0,1,"0108\xaf1",0,0,0,10,0,0);'
    )
