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

    return _liha_command(
        cmd="Aspirate",
        grid_site=grid_site,
        column=column,
        volumes=volumes,
        liquid_class=liquid_class,
        spacing=spacing,
        tip_mask=tip_mask,
        labware=labware,
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

    return _liha_command(
        cmd="Dispense",
        grid_site=grid_site,
        column=column,
        volumes=volumes,
        liquid_class=liquid_class,
        spacing=spacing,
        tip_mask=tip_mask,
        labware=labware,
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

    return _liha_command(
        cmd="Mix",
        grid_site=grid_site,
        column=column,
        volumes=volumes,
        liquid_class=liquid_class,
        spacing=spacing,
        tip_mask=tip_mask,
        labware=labware,
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
    ).encode()


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
    ).encode()


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
        f"{ncols:02x}".encode(),
        f"{nrows:02x}".encode(),
        b"0" * int(well / 7),
        *[
            int(sum(encoder) + 48).to_bytes(1, "big") if sum(encoder) > 0 else b"0"
            for encoder in encoders
        ],
        b"0" * (n_chars - len(encoders) - int(well / 7)),
    ]
    return b"".join(sequence)


def _liha_command(
    cmd: str,
    grid_site: GridSite,
    column: int,
    volumes: ArrayLike | int | float,
    liquid_class: str,
    spacing: int = 1,
    tip_mask: ArrayLike | int = 255,
    labware: Labware | str = "greiner96",
):

    if isinstance(volumes, int | float):
        volumes = np.array([volumes] * 8)

    pipette_volumes = volumes_to_string(
        volumes[volumes > 0] if spacing > 1 else volumes
    )

    if not isinstance(tip_mask, int | float):
        tip_mask = bin_to_dec(tip_mask)

    if isinstance(labware, str):
        labware = labwares[labware]

    command = (
        (
            f"B;{cmd}("
            f"{tip_mask},"
            f'"{liquid_class}",'
            f"{pipette_volumes},"
            f"{grid_site.grid},"
            f"{grid_site.site},"
            f"{spacing},"
        ).encode()
        + _well_select(volumes, column, labware.rows, labware.cols)
        + b",0,0);"
    )
    return command
