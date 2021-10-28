"""Labware dimensions."""

from .base import Labware

labwares = {
    "trough100": Labware("Trough 100+25ml", 8, 1),
    "greiner96": Labware("96 Well Greiner SC", 8, 12),
    "greiner384": Labware("384 Well Plate Greiner", 16, 24, 2),
}
