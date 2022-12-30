"""TK5."""

def make_ends(nums: list) -> list:
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array.

    The original array will be length 1 or more.

    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    return [nums[0], nums[-1]]


def near_ten(nr: int) -> bool:
    """
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10.

    near_ten(0) →  True
    near_ten(3) →  False
    near_ten(10) →  True
    near_ten(23) →  False
    near_ten(198) →  True

    :param nr: non-negative integer.
    :return: True if num is within 2 of a multiple of 10.
    """
    string1 = str(nr)
    if string1[-1] in "01289":
        return True
    else:
        return False


def combo_string(s1: str, s2: str) -> str:
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    if len(s1) < len(s2):
        return s1 + s2 + s1
    else:
        return s2 + s1 + s2


def min_diff(nums):
    """
    Find the smaller diff between the first and the last element.

    Diff is a distance (non-negative number) between a value of an element and a value of the element at position of original element value.
    Take diffs for both the first and the last element, return the smaller diff.

    If one index is out of range, then return the diff of other element.
    If both indices are out of range, return -1.

    min_diff([1, 2, 3, 4, 5, 3]) => 1
    min_diff([1, 3, 3, 4, 1, 4]) => 2
    min_diff([0, 1, 2, 0]) => 0
    min_diff([1, 100, 102, 2]) => 99

    min_diff([1, 2, 3]) => 1
    min_diff([79, 2, 0]) => 79
    min_diff([123, 0, 122]) => -1

    :param nums: List of integers.
    :return: Min diff
    """
    if nums[0] >= len(nums) and nums[-1] >= len(nums):
        return -1
    if nums[0] >= len(nums):
        return abs(nums[-1] - nums[nums[-1]])
    if nums[-1] >= len(nums):
        return abs(nums[0] - nums[nums[0]])
    else:
        vahe1 = abs(nums[0] - nums[nums[0]])
        vahe2 = abs(nums[-1] - nums[nums[-1]])
        if vahe1 < vahe2:
            return vahe1
        else:
            return vahe2


def word_numeration(words: list) -> list:
    """
    For a given list of string, add numeration for every string.

    The input list consists of strings. For every element in the input list,
    the output list adds a numeration after the string.
    The format is as follows: #N, where N starts from 1.
    String comparison should be case-insensitive.
    The case of symbols in string itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast#1", "no#1", "tere#3", "TERE#4"]

    :param words: A list of strings.
    :return: List of string with numeration.
    """
    numeration = {}
    result =[]
    # Iterate through the words and add the numeration to the dictionary
    for word in words:
        lower_word = word.lower()
        if lower_word in numeration:
            numeration[lower_word] += 1
            result.append(word + "#" + str(numeration[lower_word]))
        else:
            numeration[lower_word] = 1
            result.append(f"{word}#{numeration[lower_word]}")
    return result


print(word_numeration(["tere", "tere", "tulemast"]))
print(word_numeration(["Tere", "tere", "tulemast"]))
print(word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]))

