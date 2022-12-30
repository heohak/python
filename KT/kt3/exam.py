"""KT3."""

def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if s == "":
        return ""
    else:
        return s[-1] + s[0:-1]


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    result = []
    shitlist = []
    for i in numbers:
        if numbers.count(i) == 2:
            if i not in result:
                result.append(i)
        if numbers.count(i) > 2:
            shitlist.append(i)
    if len(result) == 1 and len(shitlist) == 0:
        return True
    else:
        return False







def pentabonacci(n: int) -> int:
    """
    Find the total number of odd values in the sequence up to the f(n) [included].

    The sequence is defined like this:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 4
    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)

    Keep in mind that 1 is the only value that is duplicated in the sequence
    and must be counted only once.

    pentabonacci(5) -> 1
    pentabonacci(10) -> 3
    pentabonacci(15) -> 5

    :param n: The last term to take into account.
    :return: Total number of odd values.
    """
    odd_values = []
    counted_1 = False
    # define the first two terms of the Fibonacci sequence
    a, b = 0, 1
    # loop until the current term is greater than or equal to n
    while b < n:
        # if the current term is odd and is not 1, or if it is 1 and has not been counted yet, append it to the list of odd values
        if (b % 2 == 1 and b != 1) or (b == 1 and not counted_1):
            odd_values.append(b)
            # if the current term is 1, set counted_1 to True
            if b == 1:
                counted_1 = True
        # update the current and previous terms
        a, b = b, a + b
    return len(odd_values)



def swap_dict_keys_and_value_lists(d: dict) -> dict:
    """
    Swap keys and values in dict.

    Values are lists.
    Every element in this list should be a key,
    and current key will be a value for the new key.
    Values in the result are lists.

    Every list in input dict has at least 1 element.
    The order of the values in the result dict is not important.

    swap_dict_keys_and_value_lists({"a": ["b", "c"]}) => {"b": ["a"], "c": ["a"]}
    swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) => {2: [1, 4], 3: [1], 5: [4]}
    swap_dict_keys_and_value_lists({}) => {}
    swap_dict_keys_and_value_lists({1: [2]}) => {2: [1]}
    """
    result = {}
    for key, value in d.items():
        for i in value:
            if i not in result:
                result[i] = [key]
            else:
                result[i].append(key)
    return result


if __name__ == '__main__':

    #print(only_one_pair([1, 2, 3])) #is False
    #print(only_one_pair([1])) #is False
    #print(only_one_pair([1, 2, 3, 1]))# is True
  #  print(only_one_pair([1, 2, 1, 3, 1])) #is False
  #  print(only_one_pair([1, 2, 1, 3, 1, 2])) #is False

    print(pentabonacci(5))
    print(pentabonacci(10)) #== 3
    print(pentabonacci(15))# == 5

    print(swap_dict_keys_and_value_lists({"a": ["b", "c"]}))# == {"b": ["a"], "c": ["a"]}
    print(swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}))# == {2: [1, 4], 3: [1], 5: [4]}  # or {2: [4, 1], 3: [1], 5: [4]}
    print(swap_dict_keys_and_value_lists({}))# == {}
    print(swap_dict_keys_and_value_lists({1: [2]}))# == {2: [1]}
