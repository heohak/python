"""My testing file."""
import pytest


from solution import students_study
from solution import lottery


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

