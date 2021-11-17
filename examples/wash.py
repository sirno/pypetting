"""Define wash routine."""
import numpy as np

from pypetting import aspirate, dispense, wash, move_liha, GridSite

ALL_TIPS = np.array([True] * 8)
COL96 = np.array([True] * 8)


def phage_wash():
    """Phage Wash routine."""
    bleach1 = GridSite(30, 0, "")
    bleach2 = GridSite(29, 0, "")
    h2o1 = GridSite(29, 1, "")
    h2o2 = GridSite(30, 1, "")
    ethanol = GridSite(30, 2, "")

    bleach = "sterileWash_N_bleach"
    water = "sterileWash_N_H2O"
    ethanol = "sterileWash_N_EtOH"

    return [
        wash(1, 0.1, 32),
        aspirate(bleach1, 1, COL96, 300 * ALL_TIPS, bleach, labware="trough100"),
        dispense(bleach1, 1, COL96, 300 * ALL_TIPS, bleach, labware="trough100"),
        wash(1, 0.1, 31),
        aspirate(bleach2, 1, COL96, 300 * ALL_TIPS, bleach, labware="trough100"),
        dispense(bleach2, 1, COL96, 300 * ALL_TIPS, bleach, labware="trough100"),
        wash(2, 1, 31),
        aspirate(h2o1, 1, COL96, 300 * ALL_TIPS, water, labware="trough100"),
        dispense(h2o1, 1, COL96, 300 * ALL_TIPS, water, labware="trough100"),
        aspirate(h2o1, 1, COL96, 300 * ALL_TIPS, water, labware="trough100"),
        dispense(h2o1, 1, COL96, 300 * ALL_TIPS, water, labware="trough100"),
        aspirate(ethanol, 1, COL96, 400 * ALL_TIPS, ethanol, labware="trough100"),
        dispense(ethanol, 1, COL96, 400 * ALL_TIPS, ethanol, labware="trough100"),
        aspirate(h2o2, 1, COL96, 450 * ALL_TIPS, water, labware="trough100"),
        dispense(h2o2, 1, COL96, 450 * ALL_TIPS, water, labware="trough100"),
        move_liha(GridSite(31, 1, ""), 0, local=True, labware="trough100"),
    ]
