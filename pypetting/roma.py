"""Transfer labware."""

from .base import GridSite, Labware

from .labware import labwares

__all__ = ["transfer_labware"]


def transfer_labware(
    src: GridSite,
    dest: GridSite,
    labware: Labware | str,
    lid: GridSite = None,
    cover: bool = False,
    back_home: bool = False,
):
    """Transfer labware with RoMa."""
    if isinstance(labware, str):
        labware = labwares[labware]

    return (
        "B;Transfer_Rack("
        f'"{src.grid}",'
        f'"{dest.grid}",'
        f"{back_home:#d},"
        f"{bool(lid):#d},"
        "1,0,"
        f"{not cover:#d},"
        f'"{lid.grid if lid is not None else ""}",'
        f'"{labware.name}",'
        '"Narrow",'
        '"","",'
        f'"{src.carrier}",'
        f'"{lid.carrier if lid is not None else ""}",'
        f'"{dest.carrier}",'
        f'"{src.site + 1}",'
        f'"{lid.site + 1 if lid is not None else ""}",'
        f'"{dest.site + 1}");'
    ).encode()
