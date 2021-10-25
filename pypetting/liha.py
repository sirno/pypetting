"""Pipetting functions."""

import numpy as np

from .utils import bin_to_dec, volumes_to_string
from .labware import labwares

__all__ = ["aspirate", "dispense", "mix", "wash", "move_liha"]


def aspirate(
    volumes, liquid_class, grid, site, spacing=1, row=1, col=1, labware="greiner96"
):
    """Advanced aspirate command."""
    if isinstance(volumes, int | float):
        volumes = np.array([volumes] * 8)
    tip_select = bin_to_dec(volumes > 0)
    return (
        "B;Aspirate("
        f"{tip_select},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid},"
        f"{site},"
        f"{spacing},"
        f'"{_well_select(volumes, row, col, spacing=spacing, **labwares[labware])}",'
        "0,0);"
    )


def dispense(
    volumes, liquid_class, grid, site, spacing=1, row=1, col=1, labware="greiner96"
):
    """Advanced dispense command."""
    if isinstance(volumes, int | float):
        volumes = np.array([volumes] * 8)
    tip_select = bin_to_dec(volumes > 0)
    return (
        "B;Dispense("
        f"{tip_select},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid},"
        f"{site},"
        f"{spacing},"
        f'"{_well_select(volumes, row, col, spacing=spacing, **labwares[labware])}",'
        "0,0);"
    )


def mix(
    volumes, liquid_class, grid, site, spacing=1, row=1, col=1, labware="greiner96"
):
    """Advanced mix command."""
    tip_select = bin_to_dec(volumes > 0)
    return (
        "B;Mix("
        f"{tip_select},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid},"
        f"{site},"
        f"{spacing},"
        f'"{_well_select(volumes, row, col, spacing=spacing, **labwares[labware])}",'
        "0,0);"
    )


def wash(waste_volume, cleaner_volume, station):
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
    grid,
    site,
    spacing=1,
    row=1,
    col=1,
    labware="greiner96",
    local=False,
    z_pos=0,
    speed=10,
):
    """Move LiHa to grid site."""
    return (
        "B;MoveLiha("
        "255,"
        f"{grid},"
        f"{site},"
        f"{spacing},"
        f'"{_well_select(np.array([1] * 8), row, col, *labwares[labware], spacing)}",'
        f"{local:#d},"
        f"{z_pos},"
        "0,"
        f"{speed},"
        "0,0);"
    )


def _encode_well_select(volumes, offset, spacing):
    encoder = np.zeros(offset + len(volumes) * spacing, dtype=np.int8)
    for i, volume in enumerate(volumes):
        encoder[offset + spacing * i] = 1 if volume > 0 else 0
    splits = [encoder[(7 * i) : (7 * (i + 1))] for i in range((len(encoder) + 6) // 7)]
    return [2 ** np.arange(len(split)) * split for split in splits]


def _well_select(volumes, row, col, nrows, ncols, spacing, **kwargs):
    """Generate well select string for volumes."""
    well = (col - 1) * nrows + row - 1
    encoders = _encode_well_select(volumes, well % 7, spacing)
    n_chars = (nrows * ncols + 6) // 7
    sequence = [
        f"{ncols:02x}",
        f"{nrows:02x}",
        "0" * int(well / 7),
        *[chr(sum(encoder) + 48) if sum(encoder) > 0 else "0" for encoder in encoders],
        "0" * (n_chars - len(encoders) - int(well / 7)),
    ]
    return "".join(sequence)
