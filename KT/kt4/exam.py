"""KT4."""

def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    string1 = str(nr)
    return [int(string1[0]), int(string1[1])]


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_elements_around_last_three([1, 3, 7]) -> 8
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_elements_around_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    index = None
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] == 3:
            index = i
            break
    if index is not None:
        if index > 0 and index < len(nums) - 1:
            return nums[index - 1] + nums[index + 1]
    return 0







def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    ax_block("abbCCCddBBBxx")m => 3
    max_block("") => 0
    """
    if len(s) == 0:
        return 0
    max_length = 0
    for i in range(len(s)):
        length = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            length += 1
            i += 1
        max_length = max(max_length, length)
    return max_length



def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    result = {}
    for pair in pairs:
        if ">" in pair:
            key, value = pair.split(">")
            if key not in result:
                result[key] = [value]
            else:
                if value not in result[key]:
                    result[key].append(value)
        if "<" in pair:
            key, value = pair.split("<")
            if value not in result:
                result[value] = [key]
            else:
                if key not in result[value]:
                    result[value].append(key)
    return result


print(create_dictionary_from_directed_string_pairs(["a>b", "a>c"]))
print(create_dictionary_from_directed_string_pairs(["a>b", "a<b"]))
print(create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]))