"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    id_code = ""
    for i in text:
        if i.isdigit():
            id_code += i
    if len(id_code) > 11:
        return "Too many numbers!"
    elif len(id_code) < 11:
        return "Not enough numbers!"
    return id_code

    # Write your code here


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    id_code = ""
    for i in text:
        if i.isdigit():
            id_code += i
    if len(id_code) > 11:
        return "Incorrect ID code!"
    elif len(id_code) < 11:
        return "Incorrect ID code!"

    control_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    sum_numbers = 0
    new_id = id_code[:-1]
    a = 0

    for i in range(len(new_id)):
        some_num = int(new_id[i])
        sum_numbers += some_num * control_number[a]
        a += 1
    check_num = sum_numbers % 11
    if check_num >= 10:
        return "Needs the second algorithm!"
    if check_num != int(id_code[-1]):
        return "Incorrect ID code!"
    if check_num == int(id_code[-1]):
        return id_code

    # Write your code here


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("123456789123456789"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(the_first_control_number_algorithm("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm!"


"""EX03 ID code."""


def is_valid_gender_number(first_num: int) -> bool:
    """Check if ID first number is valid."""
    if 0 < first_num < 7:
        return True
    else:
        return False


def get_gender(gender: int) -> str:
    """Check if user is male or female."""
    if gender == 2 or gender == 4 or gender == 6:
        return "female"
    if gender == 1 or gender == 3 or gender == 5:
        return "male"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if (year_number >= 0) and (year_number < 100):
        return True
    else:
        return False

    # Write your code here


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    if month_number in range(1, 13):
        return True
    else:
        return False
    # Write your code here


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if birth_number in range(1, 1000):
        return True
    else:
        return False
    # Write your code here


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

"""EX03 ID code."""


def is_leap_year(year: int) -> bool:
    """Check if year is a leapyear."""
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    if (gender_number == 1) or (gender_number == 2):
        return 1800 + year_number
    if (gender_number == 3) or (gender_number == 4):
        return 1900 + year_number
    if (gender_number == 5) or (gender_number == 6):
        return 2000 + year_number
    # Write your code here


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if birth_number not in range(1, 1000):
        return "Wrong input!"
    if 1 <= birth_number <= 10:
        return "Kuressaare"
    if 11 <= birth_number <= 20:
        return "Tartu"
    if 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    if 271 <= birth_number <= 370:
        return "Tartu"
    if 371 <= birth_number <= 420:
        return "Narva"
    if 421 <= birth_number <= 470:
        return "Pärnu"
    if (471 <= birth_number <= 710) or (21 <= birth_number <= 220):
        return "Tallinn"
    if 711 <= birth_number <= 999:
        return "undefined"


if __name__ == '__main__':
    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

"""EX03 ID code."""


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    control_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    sum_numbers = 0
    new_id = id_code[:-1]
    a = 0

    for i in range(len(new_id)):
        some_num = int(new_id[i])
        sum_numbers += some_num * control_number[a]
        a += 1
    check_num = sum_numbers % 11
    if check_num >= 10:
        return False
    if check_num != int(id_code[-1]):
        return False
    if check_num == int(id_code[-1]):
        return True

    numbers2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum2 = 0
    new_id = id_code[:-1]
    b = 0

    for i in range(len(new_id)):
        some_num2 = int(new_id[i])
        sum2 += some_num2 * numbers2[b]
        b += 1
    check_num2 = sum2 % 11
    if check_num2 == int(id_code[-1]):
        return True
    if check_num2 != int(id_code[-1]):
        return False




def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    # Write your code here


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    # Write your code here


if __name__ == '__main__':
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
