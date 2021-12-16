"""Teshake module tests."""

from pypetting.teshake import teshake_shake


def test_shake():
    """Test shake command."""
    assert teshake_shake() == (
        b'B;FACTS("Shaker","Shaker_Init","","0","",);\n'
        b'B;FACTS("Shaker","Shaker_SetFrequency","1000","0","",);\n'
        b'B;FACTS("Shaker","Shaker_Start","1","0","",);\n'
        b'B;StartTimer("40");\n'
        b'B;WaitTimer("40","10");\n'
        b'B;FACTS("Shaker","Shaker_Stop","","0","",);'
    )
