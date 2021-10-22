"""Transfer labware."""


def transfer_labware(
    src_grid,
    src_site,
    dest_grid,
    dest_site,
    rack_type,
    lid_grid=0,
    lid_site=0,
    cover=False,
    back_home=False,
):
    """Transfer labware with RoMa."""
    return (
        "B;Transfer_Rack("
        f'"{src_grid}",'
        f'"{dest_grid}",'
        f"{back_home:#d},"
        f"{bool(lid_grid):#d},"
        "1,0,"
        f"{not cover:#d},"
        f'"{lid_grid}",'
        f'"{rack_type}",'
        '"Narrow",'
        '"","",'
        '"MP 3Pos Fixed",'
        '"MP 3Pos Fixed",'
        '"MP 3Pos Fixed",'
        f'"{src_site + 1}",'
        f'"{lid_site + 1}",'
        f'"{dest_site + 1}");'
    )
