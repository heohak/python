"""TK1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = minutes // 60
    ext = minutes % 60
    if hours == 0:
        return f"{ext}min"
    elif ext == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {ext}min"


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if not is_birthday:
        if speed <= 60:
            return 0
        if 61 <= speed <= 80:
            return 1
        if speed > 80:
            return 2
    else:
        if speed <= 65:
            return 0
        if 66 <= speed <= 85:
            return 1
        if speed > 85:
            return 2


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    x = len(text)
    string1 = slice(0, x // 2)
    return text[string1]


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    firstnum = nums[0]
    lastnum = nums[-1]
    if firstnum < lastnum:
        i = firstnum
    else:
        i = lastnum
    if i > len(nums) - 1:
        return i
    else:
        return nums[i]


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    if not to_remove or to_remove not in text:
        return text

        # Find the index of the first and last occurrences of to_remove
    first_idx = text.index(to_remove)
    last_idx = text.rindex(to_remove)

    # Split the text into three parts: the part before the first occurrence,
    # the part between the first and last occurrences, and the part after the last occurrence
    prefix = text[:first_idx]
    middle = text[first_idx:last_idx + len(to_remove)]
    suffix = text[last_idx + len(to_remove):]

    # Remove all occurrences of to_remove in the middle part
    middle = middle.replace(to_remove, "")

    # Concatenate the three parts and return the result
    return prefix + middle + suffix
"""
print(remove_in_middle("abc", "def"))
print(remove_in_middle("abcabcabc", "abc"))
print(remove_in_middle("abcdabceabcabc", "abc"))
print(remove_in_middle("abcd", "abc"))
print(remove_in_middle("abcdabc", "abc"))
print(remove_in_middle("ABCAaaaAA", "a"))
"""