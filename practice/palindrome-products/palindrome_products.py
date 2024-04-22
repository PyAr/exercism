def palindrome(s):
    """
    Check if a number or string is a palindrome.

    Args:
        s (int or str): The number or string to check.

    Returns:
        bool: True if the input is a palindrome, False otherwise.
    """
    s = str(s)
    return s[::-1] == s


def largest(min_factor, max_factor):
    """
    Find the largest palindrome product of numbers within the specified range.

    Args:
        min_factor (int): The minimum factor.
        max_factor (int): The maximum factor.

    Returns:
        tuple: A tuple containing the largest palindrome product and its factors.
    """
    factors_list = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for x in range(max_factor ** 2, min_factor ** 2 - 1, -1):
        if palindrome(x):
            for y in range(min_factor, max_factor + 1):
                if x % y == 0 and min_factor <= x / y <= max_factor:
                    factors_list.append([y, int(x / y)])
            if factors_list:
                return x, factors_list
    return None, factors_list


def smallest(min_factor, max_factor):
    """
    Find the smallest palindrome product of numbers within the specified range.

    Args:
        min_factor (int): The minimum factor.
        max_factor (int): The maximum factor.

    Returns:
        tuple: A tuple containing the smallest palindrome product and its factors.
    """
    factors_list = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for x in range(min_factor ** 2, (max_factor + 1) ** 2):
        if palindrome(x):
            for y in range(min_factor, max_factor + 1):
                if x % y == 0 and min_factor <= x / y <= max_factor:
                    factors_list.append([y, int(x / y)])
            if factors_list:
                return x, factors_list
    return None, factors_list
