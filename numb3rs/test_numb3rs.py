from numb3rs import validate

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("-1.-1.2.2") == False
    assert validate("256.255.255.255") == False
    assert validate("255.255.255.256") == False

def test_length():
    assert validate("0.0.0.2") == True
    assert validate("255.255.255") == False
    assert validate("255.255.255.255.255") == False
    assert validate("2.2") == False
    assert validate("255.") == False
    assert validate("cat") == False