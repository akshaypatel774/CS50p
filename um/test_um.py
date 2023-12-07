from um import count

def test_count():
    assert count("tummy") == 0
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, hello, um") == 2