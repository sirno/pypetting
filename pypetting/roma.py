"""Transfer labware."""

from .base import GridSite


def transfer_labware(
    src: GridSite,
    dest: GridSite,
    rack_type: str,
    lid: GridSite = None,
    cover: bool = False,
    back_home: bool = False,
):
    """Transfer labware with RoMa."""
    return (
        "B;Transfer_Rack("
        f'"{src.grid}",'
        f'"{dest.grid}",'
        f"{back_home:#d},"
        f"{bool(lid):#d},"
        "1,0,"
        f"{not cover:#d},"
        f'"{lid.grid}",'
        f'"{rack_type}",'
        '"Narrow",'
        '"","",'
        f'"{src.carrier}",'
        f'"{lid.carrier}",'
        f'"{dest.carrier}",'
        f'"{src.site + 1}",'
        f'"{lid.site + 1}",'
        f'"{dest.site + 1}");'
    )
