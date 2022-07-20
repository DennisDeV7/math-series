import pytest
from series import fibonacci, lucas, sum_series


# ***** fibonacci ******
def test_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


# ***** lucas *****
def test_four():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_five():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_six():
    actual = lucas(4)
    expected = 7
    assert actual == expected


# ***** sum series *****
# @pytest.mark.skip("pending")
def test_seven():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


# @pytest.mark.skip("pending")
def test_eight():
    actual = sum_series(4, 2, 1)
    expected = 7
    assert actual == expected


# @pytest.mark.skip("pending")
def test_nine():
    actual = sum_series(4, 3, 2)
    expected = 12
    assert actual == expected

