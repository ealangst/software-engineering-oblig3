from leap_year import *


def test_years_divisible_by_4_but_not_100_are_leap_years():
    assert is_leap_year(4)
    assert is_leap_year(12)
    assert not is_leap_year(100)
    assert not is_leap_year(2100)


def test_years_divisible_by_400_are_leap_years():
    assert is_leap_year(400)
    assert is_leap_year(2000)


def test_years_not_divisible_by_4_are_not_leap_years():
    assert not is_leap_year(5)
    assert not is_leap_year(101)
    assert not is_leap_year(1)
    assert not is_leap_year(19)
