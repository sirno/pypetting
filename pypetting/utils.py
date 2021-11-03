"""Utils."""

import numpy as np


def bin_to_dec(array):
    """Convert binary vector to decimal."""
    return sum((array > 0) * 2 ** np.arange(len(array)))


def _format_number(num):
    return '"0"' if num == 0 else f'"{str(num)}"'


def volumes_to_string(volumes):
    """Convert volumes vector to string."""
    if len(volumes) < 12:
        volumes = np.append(volumes, np.zeros(12 - len(volumes)))
    return ",".join(map(_format_number, volumes))
