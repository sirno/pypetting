"""Pipetting functions."""

from .utils import bin_to_dec, volumes_to_string, well_select, mca_well_select

__all__ = ["aspirate", "dispense", "mix", "wash", "mca_aspirate", "mca_dispense"]

labwares = {
    "greiner96": (8, 12),
    "greiner384": (16, 24),
}


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


def mca_aspirate(volume, liquid_class, grid, site, row, col, labware):
    """Advanced aspirate command."""
    return (
        "B;MCAAspirate("
        f'"{liquid_class}",'
        f"{volume},"
        f"{grid},"
        f"{site},"
        f'"{mca_well_select(row, col, *labwares[labware])}",'
        "0,0);"
    )


def mca_dispense(volume, liquid_class, grid, site, row, col, labware):
    """Advanced dispense command."""
    return (
        "B;MCADispense("
        f'"{liquid_class}",'
        f"{volume},"
        f"{grid},"
        f"{site},"
        f'"{mca_well_select(row, col, *labwares[labware])}",'
        "0,0);"
    )


def mca_mix(volume, liquid_class, grid, site, row, col, labware):
    """Mix dispense command."""
    return (
        "B;MCAMix("
        f'"{liquid_class}",'
        f"{volume},"
        f"{grid},"
        f"{site},"
        f'"{mca_well_select(row, col, *labwares[labware])}",'
        "0,0);"
    )
