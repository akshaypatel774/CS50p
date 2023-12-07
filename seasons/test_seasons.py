import pytest
from seasons import dateOfBirth, sing


def test_init():
    test_object = dateOfBirth("1999-01-01")
    assert str(test_object.birthdate) == "1999-01-01 00:00:00"

def test_sing():
    test_object2 = dateOfBirth("1999-01-01")
    assert (sing(test_object2.difference) == "Twelve million, nine hundred ninety thousand, two hundred forty minutes")

def test_invalid_date():
    with pytest.raises(SystemExit):
        dateOfBirth("1999-20-20")