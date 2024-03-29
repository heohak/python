"""Exercise 8."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time in range(18, 25):
        return True
    elif time in range(5, 18) and coffee_needed:
        return True
    elif time in range(5, 18) and not coffee_needed:
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c and a != 5:
        return 5
    elif b != a and c != a:
        return 1
    elif b == a or c == a:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    big_basket_kilos = big_baskets * 5
    calc1 = big_basket_kilos + small_baskets

    if calc1 == ordered_amount:
        return small_baskets
    elif small_baskets > ordered_amount:
        return ordered_amount
    elif big_basket_kilos == ordered_amount:
        return 0
    elif big_basket_kilos > ordered_amount:
        while big_basket_kilos > ordered_amount:
            big_basket_kilos = big_basket_kilos - 5
        b = ordered_amount - big_basket_kilos
        if b <= small_baskets:
            return b
        else:
            return -1
    elif big_basket_kilos < ordered_amount:
        x = ordered_amount - big_basket_kilos
        if x <= small_baskets:
            return x
        else:
            return -1
    else:
        return -1
