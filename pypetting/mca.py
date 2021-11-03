"""Tip handling."""

import numpy as np

from .base import GridSite, Labware
from .labware import labwares

__all__ = [
    "mca_aspirate",
    "mca_dispense",
    "mca_mix",
    "mca_get_tips",
    "mca_drop_tips",
]


def mca_aspirate(
    grid_site: GridSite,
    row: int,
    col: int,
    volume: int | float,
    liquid_class: str,
    labware: Labware | str = "greiner96",
):
    """Advanced aspirate command."""

    if isinstance(labware, str):
        labware = labwares[labware]

    command = (
        (
            "B;MCAAspirate("
            f'"{liquid_class}",'
            f"{volume},"
            f"{grid_site.grid},"
            f'{grid_site.site},"'
        ).encode()
        + _mca_well_select(row, col, labware)
        + b'",0,0);'
    )

    return command


def mca_dispense(
    grid_site: GridSite,
    row: int,
    col: int,
    volume: int | float,
    liquid_class: str,
    labware: Labware | str = "greiner96",
):
    """Advanced dispense command."""

    if isinstance(labware, str):
        labware = labwares[labware]

    command = (
        (
            "B;MCADispense("
            f'"{liquid_class}",'
            f"{volume},"
            f"{grid_site.grid},"
            f'{grid_site.site},"'
        ).encode()
        + _mca_well_select(row, col, labware)
        + b'",0,0);'
    )

    return command


def mca_mix(
    grid_site: GridSite,
    row: int,
    col: int,
    volume: int | float,
    liquid_class: str,
    labware: Labware | str = "greiner96",
):
    """Mix dispense command."""

    if isinstance(labware, str):
        labware = labwares[labware]

    command = (
        (
            "B;MCAMix("
            f'"{liquid_class}",'
            f"{volume},"
            f"{grid_site.grid},"
            f'{grid_site.site},"'
        ).encode()
        + _mca_well_select(row, col, labware)
        + b'",0,0);'
    )

    return command


def mca_get_tips(grid_site: GridSite, airgap: int = 20):
    """Get tips for mca."""
    return f"B;MCAGetDitis({grid_site.grid},{grid_site.site},{airgap},96,0,0);".encode()


def mca_drop_tips(grid_site: GridSite, waste_site=0):
    """Drop tips for mca."""
    return f"B;MCADropDitis({grid_site.grid},{grid_site.site},1,{waste_site},0,0);".encode()


def _mca_well_select(row: int, col: int, labware: Labware):
    """Generate well select string for mca."""
    row = (row - 1) % 2
    col = (col - 1) % 2

    def _encode_mca_well_select(well, enc=7):
        def _use_well(_well):
            return (labware.spacing == 1) or (
                (_well // labware.rows) % 2 == col and (_well % labware.rows) % 2 == row
            )

        encoder = 2 ** np.arange(enc) * np.array(
            list(map(_use_well, np.arange(enc) + well))
        )
        return int(sum(encoder) + 48).to_bytes(1, "big") if sum(encoder) > 0 else b"0"

    nwells = labware.rows * labware.cols
    sequence = [
        f"{labware.cols:02x}{labware.rows:02x}".encode(),
        *map(_encode_mca_well_select, np.arange(0, nwells - 6, step=7)),
        _encode_mca_well_select(nwells - nwells % 7, enc=nwells % 7),
    ]
    return b"".join(sequence)
