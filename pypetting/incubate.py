"""FACTS commands, specifically for StoreX incubator"""


def facts(device, command, parameter, needs_labware, allowed_labware):
    """General FACTS command"""
    return (
        "B;FACTS("
        f'"{device}",'
        f'"{command}",'
        f'"{parameter}",'
        f'"{needs_labware}",'
        f'"{allowed_labware}",'
        ");"
    )

def _end_access():
    """End StoreX interactions"""
    return facts("StoreX", "StoreX_EndAccess", "", "0", "")


def _facts_storeX(command, parameter, needs_labware, allowed_labware):
    """facts for storeX"""
    return (
        facts("StoreX", command, parameter, needs_labware, allowed_labware)
        + "\n"
        + _end_access()
    )


def read_all_barcodes():
    """Read all barcodes in StoreX"""
    return _facts_storeX("StoreX_ReadAllBarcodes", "", "0", "")


def read_plates_in_cartridge(cartridge):
    """Read barcodes in cartridge"""
    return _facts_storeX("StoreX_ReadPlatesInCartridge", cartridge, "0", "")


def present_plate(cartridge, position, labware):
    """Present plate"""
    return _facts_storeX(
        "StoreX_PresentPlate", f'{cartridge},{position}', "1", labware
    )


def return_plate(cartridge, position):
    """Present plate"""
    return _facts_storeX("StoreX_ReturnPlate", f'{cartridge},{position}', "1", "")


def present_plate_by_bc(bc_file_path, bc_file_line, labware):
    """Present plate by barcode from file"""
    return _facts_storeX(
        "StoreX_PresentPlateByBarcode", f'{bc_file_line},{bc_file_path}', "1", labware
    )


def return_plate_by_bc():
    """Return plate by barcode from file"""
    return _facts_storeX("StoreX_ReturnPlateByBarcode", "", "0", "")
