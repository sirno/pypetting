"""Labware dimensions."""

from .base import Labware

labwares = {
    "trough100": Labware(8, 1),
    "greiner96": Labware(8, 12),
    "greiner384": Labware(16, 24, 2),
}
