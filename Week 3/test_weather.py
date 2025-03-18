from weather import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(70) == approx(21.11111)

#Call the main function that is part of pytest so that the 
#computer will execute the test function in this file

pytest.main(["-v", "--tb=line", "-rN", "__file__"])
