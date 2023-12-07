import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/100") == 1

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("x/y")


def test_guage():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(33) == "33%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"