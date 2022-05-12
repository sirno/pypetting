"""FACTS commands, specifically for StoreX incubator"""

from .misc import facts
from .base import Labware

__all__ = [
    "read_all_barcodes",
    "read_plates_in_cartridge",
    "present_plate",
    "present_plate_by_bc",
    "return_plate",
    "return_plate_by_bc",
]


def read_all_barcodes():
    """Read all barcodes in StoreX"""
    return _facts_store_x("StoreX_ReadAllBarcodes", "", False, "")


def read_plates_in_cartridge(cartridge: int):
    """Read barcodes in cartridge"""
    return _facts_store_x("StoreX_ReadPlatesInCartridge", cartridge, False, "")


def present_plate(cartridge: int, position: int, labware: Labware):
    """Present plate"""
    return _facts_store_x(
        "StoreX_PresentPlate", f"{cartridge},{position}", True, labware.name
    )


def return_plate(cartridge: int, position: int):
    """Present plate"""
    return _facts_store_x("StoreX_ReturnPlate", f"{cartridge},{position}", False, "")


def present_plate_by_bc(bc_file_path: str, bc_file_line: int, labware: Labware):
    """Present plate by barcode from file"""
    return _facts_store_x(
        "StoreX_PresentPlateByBarcode",
        f"{bc_file_line},{bc_file_path}",
        1,
        labware.name,
    )


def return_plate_by_bc():
    """Return plate by barcode from file"""
    return _facts_store_x("StoreX_ReturnPlateByBarcode", "", False, "")


def _end_access():
    """End StoreX interactions"""
    return facts("StoreX", "StoreX_EndAccess", "", False, "")


def _facts_store_x(
    command: str, parameter: str, needs_labware: bool, allowed_labware: str
):
    """facts for storeX"""
    return (
        facts("StoreX", command, parameter, needs_labware, allowed_labware)
        + b"\n"
        + _end_access()
    )
