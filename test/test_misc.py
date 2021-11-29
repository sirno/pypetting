"""Misc module tests."""

from pypetting.misc import (
    comment,
    user_prompt,
    set_variable,
    start_timer,
    wait_timer,
    facts,
)


def test_comment():
    """Test comment."""
    assert comment("hello") == b'B;Comment("hello");'


def test_user_prompt():
    """Test user prompt."""
    assert user_prompt("hello") == b'B;UserPrompt("hello",0,-1);'


def test_set_variable():
    """Test set variable."""
    assert (
        set_variable("var_name", 100)
        == b'B;Variable(var_name,"100",0,"",0,1.000000,10.000000,0,2,0,0);'
    )


def test_start_timer():
    """Test start timer."""
    assert start_timer(1) == b'B;StartTimer("1");'


def test_wait_timer():
    """Test wait timer."""
    assert wait_timer(1, 100) == b'B;WaitTimer("1","100");'


def test_facts():
    """Test facts."""
    assert facts("D", "C", "0,0", False, "") == b'B;FACTS("D","C","0,0","0","",);'
