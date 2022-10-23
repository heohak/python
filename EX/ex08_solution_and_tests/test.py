"""My testing file."""
import pytest


from solution import students_study


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
    assert students_study(2, False) is False

def test_students_study_day_coffee_needed():
    """During the day, coffee is needed for studies."""
    assert students_study(10, True) is True
    assert students_study(5, False) is False





