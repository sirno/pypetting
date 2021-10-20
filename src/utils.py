import numpy as np

def bin_to_dec(array):
    """Convert binary vector to decimal."""
    return sum(array * 2 ** np.arange(array.length)[::-1])