# pylint: skip-file
import pytest

from latest_time import (get_first_digit,
                         get_second_digit,
                         get_third_digit,
                         find_latest_time)

"""Test first digit POSITIVE"""


def test_get_first_digit_returns_zero():
    assert get_first_digit([0, 9, 3, 8]) == 0


def test_get_first_digit_returns_one():
    assert get_first_digit([1, 9, 8, 3]) == 1


def test_get_first_digit_returns_two():
    assert get_first_digit([9, 1, 2, 5]) == 2


@pytest.mark.parametrize(["first", "second", "third", "fourth"],
                         ())
