"""Tip handling."""

from .utils import mca_well_select
from .labware import labwares


def mca_aspirate(volume, liquid_class, grid, site, row, col, labware):
    """Advanced aspirate command."""
    return (
        "B;MCAAspirate("
        f'"{liquid_class}",'
        f"{volume},"
        f"{grid},"
        f"{site},"
        f'"{mca_well_select(row, col, **labwares[labware])}",'
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
        f'"{mca_well_select(row, col, **labwares[labware])}",'
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
        f'"{mca_well_select(row, col, **labwares[labware])}",'
        "0,0);"
    )


def mca_get_tips(grid, site, airgap=20):
    """Get tips for mca."""
    return f"B;MCAGetDitis({grid},{site},{airgap},96,0,0);"


def mca_drop_tips(grid, site, waste_site=0):
    """Drop tips for mca."""
    return f"B;MCADropDitis({grid},{site},1,{waste_site},0,0);"
