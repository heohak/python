"""My testing file."""

from solution import fruit_order
from solution import lottery
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


def test_fruit_order_only_big_match():
    """Only big baskets and exact match."""
    assert fruit_order(0, 1, 5) == 0


def test_fruit_order_only_big_not_enough_multi_big():
    """Only big baskets but not enough(multiple of 5)."""
    assert fruit_order(0, 5, 30) == -1


def test_fruit_order_only_big_more_than_required_match_and_not():
    """Only big baskets, more than required match and not match."""
    assert fruit_order(0, 5, 20) == 0
    assert fruit_order(0, 5, 19) == -1


def test_fruit_order_only_small_more_than_5_match_and_not():
    """Only small baskets, more than 5, match and no match."""
    assert fruit_order(8, 0, 5) == 5
    assert fruit_order(7, 0, 13) == -1


def test_fruit_order_only_small_exact_match():
    """Only small baskets and exact match."""
    assert fruit_order(4, 0, 4) == 4


def test_fruit_order_match_with_more_than_5_small():
    """More than 5 small baskets, match."""
    assert fruit_order(8, 2, 17) == 7


def test_fruit_order_all_positive_exact_match():
    """Exact match."""
    assert fruit_order(4, 3, 19) == 4


def test_fruit_order_all_smalls_some_bigs():
    """Use all small baskets and some big baskets."""
    assert fruit_order(1, 2, 6) == 1


def test_fruit_order_use_some_big_and_some_small():
    """Read function name."""
    assert fruit_order(3, 2, 6) == 1


def test_fruit_order_not_enough():
    """Not enough everything."""
    assert fruit_order(4, 5, 45) == -1
    assert fruit_order(6, 1, 30) == -1


def test_enough_big_not_enough_smalls():
    """Not enough small baskets."""
    assert fruit_order(1, 8, 24) == -1
    assert fruit_order(2, 1800, 1603) == -1


def test_match_large_numbers():
    """Match with large numbers."""
    assert fruit_order(4000, 1000, 8000) == 3000
