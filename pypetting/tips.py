"""Tip handling."""


def mca_get_tips(grid, site, airgap=20):
    """Get tips for mca."""
    return f"B;MCAGetDitis({grid},{site},{airgap},96,0,0);"


def mca_drop_tips(grid, site, waste_site=0):
    """Drop tips for mca."""
    return f"B;MCADropDitis({grid},{site},1,{waste_site},0,0);"
