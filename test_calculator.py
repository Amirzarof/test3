from calculator import add, multiply


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_zero():
    assert multiply(5, 0) == 0
