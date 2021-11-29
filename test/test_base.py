"""Test base module."""

import pytest

from pypetting.base import GridStack, GridQueue
from pypetting.errors import GridSiteException


def test_grid_stack():
    """Test GridStack."""
    stack = GridStack(40, 2, "B")
    push1 = stack.push()
    push2 = stack.push()
    with pytest.raises(GridSiteException):
        stack.push()
    pop1 = stack.pop()
    pop2 = stack.pop()
    with pytest.raises(GridSiteException):
        stack.pop()
    assert push1 == pop2
    assert push2 == pop1


def test_grid_queue():
    """Test GridQueue"""
    queue = GridQueue(40, 2, "B")
    push1 = queue.push()
    push2 = queue.push()
    with pytest.raises(GridSiteException):
        queue.push()
    pop1 = queue.pop()
    pop2 = queue.pop()
    with pytest.raises(GridSiteException):
        queue.pop()
    assert push1 == pop1
    assert push2 == pop2
