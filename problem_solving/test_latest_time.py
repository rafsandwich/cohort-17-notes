import pytest

from latest_time import (get_first_digit,
                         get_second_digit,
                         get_third_digit)

"""Test first digit POSITIVE"""


def test_get_first_digit_returns_zero():
    assert get_first_digit([0, 9, 3, 8]) == 0


def test_get_first_digit_returns_one():
    assert get_first_digit([1, 9, 8, 3]) == 1


def test_get_first_digit_returns_two():
    assert get_first_digit([9, 1, 2, 5]) == 2


"""Test second digit POSITIVE"""


def test_get_second_digit_returns_eight():
    assert get_second_digit([0, 8, 3, 1], 0) == 8


def test_get_second_digit_returns_three_when_first_is_two():
    assert get_second_digit([2, 3, 3, 1], 2) == 3


"""Test third digit POSITIVE"""


def test_get_third_digit_returns_five():
    assert get_third_digit([0, 8, 5, 1], 0, 8) == 5


# @pytest.mark.parametrize(["first", "second", "third", "fourth"],
#                          ())
