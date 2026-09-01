import pytest
from calculator import add, subtract, multiply, divide, is_even


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 1) == 4
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 6) == 24
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
