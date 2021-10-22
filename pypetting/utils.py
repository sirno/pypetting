"""Utils."""

import numpy as np


def bin_to_dec(array):
    """Convert binary vector to decimal."""
    return sum(array * 2 ** np.arange(len(array))[::-1])


def _format_number(num):
    return '"0"' if num == 0 else f'"{str(num)}"'


def volumes_to_string(volumes):
    """Convert volumes vector to string."""
    if len(volumes) < 12:
        volumes = np.append(volumes, np.zeros(12 - len(volumes)))
    return ",".join(map(_format_number, volumes))


def _encode_well_select(volumes, offset, spacing):
    encoder = np.zeros(offset + len(volumes) * spacing, dtype=np.int8)
    for i, volume in enumerate(volumes):
        encoder[offset + spacing * i] = 1 if volume > 0 else 0
    splits = [encoder[(7 * i) : (7 * (i + 1))] for i in range((len(encoder) + 6) // 7)]
    return [2 ** np.arange(len(split)) * split for split in splits]


def well_select(volumes, row, col, nrows, ncols, spacing):
    """Generate well select string for volumes."""
    well = (col - 1) * nrows + row - 1
    encoders = _encode_well_select(volumes, well % 7, spacing)
    n_chars = (nrows * ncols + 6) // 7
    sequence = [
        f"{ncols:02x}",
        f"{nrows:02x}",
        "0" * int(well / 7),
        *[chr(sum(encoder) + 48) if sum(encoder) > 0 else "0" for encoder in encoders],
        "0" * (n_chars - len(encoders) - int(well / 7)),
    ]
    return "".join(sequence)


def mca_well_select(row, col, nrows, ncols, spacing):
    """Generate well select string for mca."""
    row = (row - 1) % 2
    col = (col - 1) % 2

    def _encode_mca_well_select(well, enc=7):
        def _use_well(_well):
            return (spacing == 1) or (
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
