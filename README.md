# Pypetting

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Pypetting provides a simple set of wrappers to write complex worklists for the
Tecan EVOware pipetting software. Unfortunately it does not entirely avoid
interacting with the original software, but it reduces the necessary
interactions with it to a minimum.

## Installation

Install using pip with `pip install pypetting`.

Pypetting has only been tested with Python 3.9.6+.

## Examples

### Define a position on the grid

```python
from pypetting import GridSite

site = GridSite(grid=36, site=1, carrier="MP 3Pos")
```

### Define labwares

```python
from pypetting import Labware

greiner96 = Labware(name="96 Well Griner", rows=8, columns=12, spacing=1)
trough100 = Labware("Trough 100+25ml", 8, 12)
```

### Pipetting from one column to the next

```python
from pypetting import GridSite, Labware, aspirate, dispense, write_gwl

pipetting_site = GridSite(36, 1, "MP 3Pos")
labware = Labware("96 Well Greiner", 8, 12, spacing=1)

ALL = 8 * [True]

worklist = [
    aspirate(pipetting_site, 1, ALL, 50, "LB CD ZMAX", labware=labware),
    dispense(pipetting_site, 2, ALL, 50, "LB CD ZMAX", labware=labware),
]

write_gwl("worklist.gwl", worklist)
```

### Place plate in the incubator

```python
from pypetting import GridSite, Labware, transfer_labware, return_plate, write_gwl

src = GridSite(36, 0, "MP 3Pos")
dest = GridSite(68, 0, "StoreX 22Pos")
labware = Labware("96 Well Greiner", 8, 12, spacing=1)

worklist = [
    transfer_labware(src, dest, labware),
    return_plate(1, 1),
]

write_gwl("worklist.gwl", worklist)
```

## How to avoid touching EVOware

The author of Pypetting has strong opinions about the design of EVOware. In
order to implement more complex workflows modern techniques for modularization
and abstraction of logic are required. ANY general purpose programming language
provides these tools. Thus outsourcing as much logic as possible is desirable.

We suggest the following workflow for any form of iterative task:

- Call an application to generate the workflow, store the return value of the
  application in a variable e.g. called `return_value`
- Execute workflows
- Jump to the application when `return_value` is non-zero
