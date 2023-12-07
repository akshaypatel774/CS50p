from plates import is_valid

def test_start():
    assert is_valid("3") == False
    assert is_valid("22") == False
    assert is_valid("ab1") == True
    assert is_valid("abc") == True


def test_length():
    assert is_valid("a") == False
    assert is_valid("abcdefg") == False
    assert is_valid("abcdef") == True


def test_numbers():
    assert is_valid("12abcd") == False
    assert is_valid("abc012") == False
    assert is_valid("ab12ab") == False
    assert is_valid("ab123a") == False
    assert is_valid("123456") == False
    assert is_valid("abc123") == True
    assert is_valid("abcd12") == True


def test_punctuations():
    assert is_valid("abc.-,") == False
    assert is_valid("@!%ab%") == False
    assert is_valid("*`~>") == False