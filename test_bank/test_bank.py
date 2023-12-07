from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Welcome sir") == 100
    assert value("Hey what's up") == 20