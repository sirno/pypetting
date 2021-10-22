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
        "B;TransferRack("
        f"{src_grid},"
        f"{dest_grid},"
        f"{back_home:#d},"
        "1,0,"
        f"{cover:#d},"
        f"{lid_grid},"
        f"{rack_type},"
        "Narrow,",
        '"","",'
        "MP 3Pos,"
        "MP 3Pos,"
        "MP 3Pos,"
        f"{src_site},"
        f"{lid_site},"
        f"{dest_site});",
    )
