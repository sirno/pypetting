"""Define wash routine."""
from pypetting import aspirate, dispense, wash, move_liha


def phage_wash():
    return [
        wash(1, 0.1, 32),
        aspirate(300, "sterileWash_N_bleach", 30, 0, labware="trough"),
        dispense(300, "sterileWash_N_bleach", 30, 0, labware="trough"),
        wash(1, 0.1, 31),
        aspirate(300, "sterileWash_N_bleach", 29, 0, labware="trough"),
        dispense(300, "sterileWash_N_bleach", 29, 0, labware="trough"),
        wash(2, 1, 31),
        aspirate(300, "sterileWash_N_H2O", 29, 1, labware="trough"),
        dispense(300, "sterileWash_N_H2O", 29, 1, labware="trough"),
        aspirate(300, "sterileWash_N_H2O", 29, 1, labware="trough"),
        dispense(300, "sterileWash_N_H2O", 29, 1, labware="trough"),
        aspirate(400, "sterileWash_N_EtOH", 30, 2, labware="trough"),
        dispense(400, "sterileWash_N_EtOH", 30, 2, labware="trough"),
        aspirate(450, "sterileWash_N_H2O", 30, 1, labware="trough"),
        dispense(450, "sterileWash_N_H2O", 30, 1, labware="trough"),
        move_liha(31, 1, local=True),
    ]
