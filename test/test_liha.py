"""Pipetting unit tests."""

from itertools import product

import pytest
import numpy as np

from pypetting import (
    GridSite,
    aspirate,
    dispense,
    mix,
    wash,
    move_liha,
)

from pypetting.liha import _well_select

FIRST = np.array([True] + 7 * [False])
COL96 = np.array(8 * [True])
grid_site = GridSite(40, 0, "MP 3Pos")

LIHA_PIPETTING_ARGS = (
    b'(1,"A","1.0","0","0","0","0","0","0","0","0","0","0","0",40,0,1,"010810",0,0);'
)


def test_liha_aspirate():
    """Test LiHa aspirate."""
    assert (
        aspirate(grid_site, 1, FIRST, 1 * FIRST, "A", labware="trough100")
        == b"B;Aspirate" + LIHA_PIPETTING_ARGS
    )
    assert (
        aspirate(grid_site, 1, FIRST, 1, "A", labware="trough100")
        == b"B;Aspirate" + LIHA_PIPETTING_ARGS
    )
    with pytest.raises(IndexError):
        aspirate(grid_site, 0, FIRST, 1, "A", labware="trough100")
    with pytest.raises(IndexError):
        aspirate(grid_site, 2, FIRST, 1, "A", labware="trough100")


def test_liha_dispense():
    """Test Liha dispense."""
    assert (
        dispense(grid_site, 1, FIRST, 1 * FIRST, "A", labware="trough100")
        == b"B;Dispense" + LIHA_PIPETTING_ARGS
    )
    assert (
        dispense(grid_site, 1, FIRST, 1, "A", labware="trough100")
        == b"B;Dispense" + LIHA_PIPETTING_ARGS
    )
    with pytest.raises(IndexError):
        dispense(grid_site, 0, FIRST, 1, "A", labware="trough100")
    with pytest.raises(IndexError):
        dispense(grid_site, 2, FIRST, 1, "A", labware="trough100")


def test_liha_mix():
    """Test Liha mix."""
    assert (
        mix(grid_site, 1, FIRST, 1 * FIRST, "A", labware="trough100")
        == b"B;Mix" + LIHA_PIPETTING_ARGS
    )
    assert (
        mix(grid_site, 1, FIRST, 1, "A", labware="trough100")
        == b"B;Mix" + LIHA_PIPETTING_ARGS
    )
    with pytest.raises(IndexError):
        mix(grid_site, 0, FIRST, 1, "A", labware="trough100")
    with pytest.raises(IndexError):
        mix(grid_site, 2, FIRST, 1, "A", labware="trough100")


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


def test_well_select_minimal():
    """Test well select string with minimal length."""
    for mask in product([0, 1], repeat=7):
        value = 48
        for idx, val in enumerate(mask):
            value += val * 2 ** idx
        assert _well_select(mask, 1, 7, 1) == b"0107" + value.to_bytes(1, "big")
