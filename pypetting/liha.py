"""Pipetting functions."""

import numpy as np

from .utils import bin_to_dec, volumes_to_string, well_select
from .labware import labwares

__all__ = ["aspirate", "dispense", "mix", "wash", "move_liha"]


def aspirate(
    volumes, liquid_class, grid, site, spacing=1, row=1, col=1, labware="greiner96"
):
    """Advanced aspirate command."""
    tip_select = bin_to_dec(volumes > 0)
    return (
        "B;Aspirate("
        f"{tip_select},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid},"
        f"{site},"
        f"{spacing},"
        f'"{well_select(volumes, row, col, *labwares[labware], spacing)}",'
        "0,0);"
    )


def dispense(
    volumes, liquid_class, grid, site, spacing=1, row=1, col=1, labware="greiner96"
):
    """Advanced dispense command."""
    tip_select = bin_to_dec(volumes > 0)
    return (
        "B;Dispense("
        f"{tip_select},"
        f'"{liquid_class}",'
        f"{volumes_to_string(volumes)},"
        f"{grid},"
        f"{site},"
        f"{spacing},"
        f'"{well_select(volumes, row, col, *labwares[labware], spacing)}",'
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
        f'"{well_select(volumes, row, col, *labwares[labware], spacing)}",'
        "0,0);"
    )


def wash(waste_volume, cleaner_volume, station):
    """Wash tips command."""
    return (
        "B;Wash("
        "255,"
        f"{station},1,{station},0,"
        f'"{str(waste_volume)}",'
        f"200,"
        f'"{str(cleaner_volume)}",'
        "10,70,30,0,0,1000,0);"
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
        f'"{well_select(np.array([1] * 8), row, col, *labwares[labware], spacing)}",'
        f"{local:#d},"
        f"{z_pos},"
        "0,"
        f"{speed},"
        "0,0);"
    )
