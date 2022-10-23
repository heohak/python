"""My testing file."""
import pytest


from solution import students_study
from solution import lottery
from solution import fruit_order


def test_students_study_evening_coffee_not_needed():
    """During evening, coffee is not needed for studies."""
    assert students_study(18, True) is True
    assert students_study(18, False) is True
    assert students_study(24, False) is True
    assert students_study(24, True) is True
    assert students_study(21, False) is True
    assert students_study(21, True) is True


def test_students_study_night_no_study():
    """At night, students are sleeping."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, False) is False
    assert students_study(4, True) is False
    assert students_study(2, False) is False
    assert students_study(2, True) is False


def test_students_study_day_coffee_needed():
    """During the day, coffee is needed for studies."""
    assert students_study(5, True) is True
    assert students_study(5, False) is False
    assert students_study(17, False) is False
    assert students_study(17, True) is True
    assert students_study(10, False) is False
    assert students_study(10, True) is True


def test_lottery_all_fives():
    """All fives."""
    assert lottery(5, 5, 5) == 10


def test_lottery_all_same_positive():
    """All same positive numbers."""
    assert lottery(3, 3, 3) == 5


def test_lottery_all_same_negative():
    """All same negative numbers."""
    assert lottery(-7, -7, -7) == 5


def test_lottery_all_zeros():
    """All zeros."""
    assert lottery(0, 0, 0) == 5


def test_lottery_ab_same_c_diff():
    """A and B are same, c is different."""
    assert lottery(4, 4, 6) == 0


def test_lottery_ac_same_b_diff():
    """A and C are same, b is different."""
    assert lottery(6, 4, 6) == 0


def test_lottery_bc_same_a_diff():
    """B and C are same, a is different."""
    assert lottery(8, 5, 5) == 1


def test_lottery_all_diff():
    """All numbers different."""
    assert lottery(2, 6, 8) == 1


def test_fruit_order_all_zeros():
    """All zeros."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order_zero_amount_zero_small():
    """Amount zero and small baskets."""
    assert fruit_order(0, 4, 0) == 0


def test_fruit_order_zero_amount_zero_big():
    """Amount zero and big baskets zero."""
    assert fruit_order(6, 0, 0) == 0


def test_fruit_order_zero_amount_others_not():
    """Amount is zero, baskets not zero."""
    assert fruit_order(1, 4, 0) == 0
