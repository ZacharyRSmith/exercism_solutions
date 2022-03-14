from typing import Tuple

def largest(min_factor: int, max_factor: int) -> Tuple[int, list]:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    val = -1
    factors = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, min_factor - 1, -1):
            if (new_val := i * j) < val:
                break
            if str(new_val) == str(new_val)[::-1]:
                if new_val != val:
                     factors = []
                val = new_val
                factors.append([i, j])
    if val == -1:
        return None, []
    return val, factors


def smallest(min_factor: int, max_factor: int) -> Tuple[int, list]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    val = max_factor**2 + 1
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            if (new_val := i * j) >= val:
                break
            if str(new_val) == str(new_val)[::-1]:
                if new_val != val:
                     factors = []
                val = new_val
                factors.append([i, j])
    if val == max_factor**2 + 1:
        return None, []
    return val, factors
