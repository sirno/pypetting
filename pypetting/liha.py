"""Pipetting functions."""

import numpy as np

from numpy.typing import ArrayLike

from .base import GridSite, Labware
from .labware import labwares
from .utils import bin_to_dec, volumes_to_string

__all__ = ["aspirate", "dispense", "mix", "wash", "move_liha"]


def aspirate(
    grid_site: GridSite,
    column: int,
    volumes: ArrayLike | int | float,
    liquid_class: str,
    spacing: int = 1,
    tip_mask: ArrayLike | int = 255,
    labware: Labware | str = "greiner96",
):
    """Advanced aspirate command."""

    if isinstance(volumes, int | float):
        volumes = np.array([volumes] * 8)

    if isinstance(tip_mask, ArrayLike):
        tip_mask = bin_to_dec(tip_mask)

    if isinstance(labware, str):
        labware = labwares[labware]

    return (
        "B;Aspirate("
        f"{tip_mask},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid_site.grid},"
        f"{grid_site.site},"
        f"{spacing},"
        f'"{_well_select(volumes, column, labware.rows, labware.cols)}",'
        "0,0);"
    )


def dispense(
    grid_site: GridSite,
    column: int,
    volumes: ArrayLike | int | float,
    liquid_class: str,
    spacing: int = 1,
    tip_mask: ArrayLike | int = 255,
    labware: Labware | str = "greiner96",
):
    """Advanced dispense command."""

    if isinstance(volumes, int | float):
        volumes = np.array([volumes] * 8)

    if isinstance(tip_mask, ArrayLike):
        tip_mask = bin_to_dec(tip_mask)

    if isinstance(labware, str):
        labware = labwares[labware]

    return (
        "B;Dispense("
        f"{tip_mask},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid_site.grid},"
        f"{grid_site.site},"
        f"{spacing},"
        f'"{_well_select(volumes, column, labware.rows, labware.cols)}",'
        "0,0);"
    )


def mix(
    grid_site: GridSite,
    column: int,
    volumes: ArrayLike | int | float,
    liquid_class: str,
    spacing: int = 1,
    tip_mask: ArrayLike | int = 255,
    labware: Labware | str = "greiner96",
):
    """Advanced mix command."""

    if isinstance(volumes, int | float):
        volumes = np.array([volumes] * 8)

    if isinstance(tip_mask, ArrayLike):
        tip_mask = bin_to_dec(tip_mask)

    if isinstance(labware, str):
        labware = labwares[labware]

    return (
        "B;Mix("
        f"{tip_mask},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid_site.grid},"
        f"{grid_site.site},"
        f"{spacing},"
        f'"{_well_select(volumes, column, labware.rows, labware.cols)}",'
        "0,0);"
    )


def wash(waste_volume: int | float, cleaner_volume: int | float, station: int):
    """Wash tips command."""
    return (
        "B;Wash("
        "255,"
        f"{station},1,{station},0,"
        f'"{waste_volume}",'
        f"500,"
        f'"{cleaner_volume}",'
        "0,10,70,30,0,0,1000,0);"
    )


def move_liha(
    grid_site: GridSite,
    column: int,
    positions: ArrayLike = None,
    spacing: int = 1,
    labware: Labware | str = "greiner96",
    local: bool = False,
    z_pos: int = 0,
    speed: int = 10,
):
    """Move LiHa to grid site."""

    if isinstance(labware, str):
        labware = labwares[labware]

    if positions is None:
        positions = np.array([1] * 8)

    return (
        "B;MoveLiha("
        "255,"
        f"{grid_site.grid},"
        f"{grid_site.site},"
        f"{spacing},"
        f'"{_well_select(positions, column, labware.rows, labware.cols)}",'
        f"{local:#d},"
        f"{z_pos},"
        "0,"
        f"{speed},"
        "0,0);"
    )


def _encode_well_select(volumes, offset):
    encoder = np.zeros(offset + len(volumes), dtype=np.int8)
    for i, volume in enumerate(volumes):
        encoder[offset + i] = 1 if volume > 0 else 0
    splits = [encoder[(7 * i) : (7 * (i + 1))] for i in range((len(encoder) + 6) // 7)]
    return [2 ** np.arange(len(split)) * split for split in splits]


def _well_select(volumes, column, nrows, ncols, **kwargs):
    """Generate well select string for volumes."""
    well = (column - 1) * nrows
    encoders = _encode_well_select(volumes, well % 7)
    n_chars = (nrows * ncols + 6) // 7
    sequence = [
        f"{ncols:02x}",
        f"{nrows:02x}",
        "0" * int(well / 7),
        *[chr(sum(encoder) + 48) if sum(encoder) > 0 else "0" for encoder in encoders],
        "0" * (n_chars - len(encoders) - int(well / 7)),
    ]
    return "".join(sequence)
