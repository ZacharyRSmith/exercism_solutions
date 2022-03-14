from typing import Tuple


class MyIter:
    _SENTINEL = object()

    def __init__(self, iter_):
        self._iter = iter_

    def has_next(self):
        if self._next is self._SENTINEL:
            try:
                self._next = next(self._iter)
            except StopIteration:
                pass
        return self._next is not self._SENTINEL

    def next(self):
        next = self.peek()
        self._next = self._SENTINEL
        return next

    def peek(self):
        if self._next is self._SENTINEL:
            self._next = next(self._iter)
        return self._next


def _get_products(min_, max_):
    iter_a = MyIter(iter(max_, min_))
    iter_b = MyIter(iter(max_, min_))
    


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
    for product in _get_products(min_factor, max_factor):
        if not _is_palindrome(product):
            continue
        return product, _get_factors(product)
    return -1, []


    val = -1
    factors = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
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
