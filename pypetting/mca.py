"""Tip handling."""

import numpy as np

from .labware import labwares


def mca_aspirate(volume, liquid_class, grid, site, row, col, labware):
    """Advanced aspirate command."""
    return (
        "B;MCAAspirate("
        f'"{liquid_class}",'
        f"{volume},"
        f"{grid},"
        f"{site},"
        f'"{_mca_well_select(row, col, **labwares[labware])}",'
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
        f'"{_mca_well_select(row, col, **labwares[labware])}",'
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
        f'"{_mca_well_select(row, col, **labwares[labware])}",'
        "0,0);"
    )


def mca_get_tips(grid, site, airgap=20):
    """Get tips for mca."""
    return f"B;MCAGetDitis({grid},{site},{airgap},96,0,0);"


def mca_drop_tips(grid, site, waste_site=0):
    """Drop tips for mca."""
    return f"B;MCADropDitis({grid},{site},1,{waste_site},0,0);"


def _mca_well_select(row, col, nrows, ncols, mca_spacing):
    """Generate well select string for mca."""
    row = (row - 1) % 2
    col = (col - 1) % 2

    def _encode_mca_well_select(well, enc=7):
        def _use_well(_well):
            return (mca_spacing == 1) or (
                (_well // nrows) % 2 == col and (_well % nrows) % 2 == row
            )

        encoder = 2 ** np.arange(enc) * np.array(
            list(map(_use_well, np.arange(enc) + well))
        )
        return chr(sum(encoder) + 48) if sum(encoder) > 0 else "0"

    nwells = nrows * ncols
    sequence = [
        f"{ncols:02x}{nrows:02x}",
        *map(_encode_mca_well_select, np.arange(0, nwells - 6, step=7)),
        _encode_mca_well_select(nwells - nwells % 7, enc=nwells % 7),
    ]
    return "".join(sequence)
