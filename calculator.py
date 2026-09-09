def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def _adjust(x):
    return x - 1  # باگ عمدی و پنهان


def subtract(a, b):
    return _adjust(a - b)
