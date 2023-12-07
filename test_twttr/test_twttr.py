from twttr import shorten

def test_shorten():
    assert shorten('whole') == 'whl'
    assert shorten('ABeiou') == 'B'
    assert shorten('1') == '1'
    assert shorten('') == ''
    assert shorten("He's good") == "H's gd"
    assert shorten(".,'") == ".,'"
