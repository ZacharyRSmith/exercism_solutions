"""Palindrome Product"""


def validate_input(max_factor: int, min_factor: int) -> None:
    if max_factor < min_factor:
        raise ValueError("min must be <= max")


def is_palindrome(number):
    # ? check whether if a number is palindrome by comparing the number to its reversed version
    a = list(str(number))
    return a == a[::-1]


def create_result(factor_range, product_range):
    # ? loop through given range to find the 1st validated palindrome (as the given range is pre-sorted)
    for product in product_range:
        if is_palindrome(product):
            found_factors = [
                [x, int(product / x)]
                for x in factor_range
                if product % x == 0 and int(product / x) in factor_range
            ]

            if found_factors:
                # ? return result if found validated palindrome (i.e. found palindrome is not prime)
                return (product, found_factors)

    return (None, [])


def largest(max_factor, min_factor=0):
    validate_input(max_factor, min_factor)

    # ? create "reversed" ranges that go from highest to smallest => 1st validated palindrome is highest
    product_range = reversed(range(min_factor**2, max_factor**2 + 1))
    factor_range = range(max_factor, min_factor - 1, -1)

    # TODO why the below factor_range doesn't work?
    # factor_range = reversed(range(min_factor, max_factor + 1))

    return create_result(factor_range, product_range)


def smallest(max_factor, min_factor=0):
    validate_input(max_factor, min_factor)

    # ? create "normal" ranges that go from smallest to highest => 1st validated palindrome is smallest
    factor_range = range(min_factor, max_factor + 1)
    product_range = range(min_factor**2, max_factor**2 + 1)
    return create_result(factor_range, product_range)