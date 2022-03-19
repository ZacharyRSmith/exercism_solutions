from typing import Tuple, Union


class Palindrome:
    """
    Class for processing palindrome products.
    """

    def __init__(self, min_factor: int, max_factor: int, find_value: str):
        self.min_factor = min_factor
        self.max_factor = max_factor
        self.find_value = find_value
        self.factors = []
        self.val = 0

        self.validate_input(find_value)

    def validate_input(self, find_value: str):
        """
        Checks min_factor is smaller than or equal to max_factor, and that
        find_value is either 'smallest' or 'largest'
        """
        if self.min_factor > self.max_factor:
            raise ValueError("min must be <= max")
        if find_value not in ["smallest", "largest"]:
            raise ValueError("Function only finds 'smallest' / 'largest'.")

    def find_palindromes(self):
        """
        Launches correct palindrome search based on 'small' or 'large'
        input value
        """
        if self.find_value == "smallest":
            self.val = self.max_factor**2 + 1
            self.find_smallest()
        if self.find_value == "largest":
            self.val = -1
            self.find_largest()

    def check_for_palindrome(self, new_val: int, pair: list[int]):
        """
        Checks the newly found smallest/largest value is not in factors list,
        and updates self.factors / self.val accordingly
        """
        if str(new_val) == str(new_val)[::-1]:
            if new_val != self.val:
                self.factors = []
            self.val = new_val
            if pair not in self.factors:
                self.factors.append(pair)

    def return_palindrome(self) -> Tuple[Union[int, None], list]:
        """
        Returns calculated palindrome values and list of factors.
        """
        if (self.find_value == "largest" and self.val == -1) or (
            self.find_value == "smallest" and self.val == self.max_factor**2 + 1
        ):
            return None, []
        return self.val, self.factors

    def find_largest(self):
        """
        Performs search across max_factor -> min_factor range and calculates
        largest possible value in range, populating the value and list of
        factors of that value.
        """
        for i in range(self.max_factor, self.min_factor - 1, -1):
            for j in range(self.max_factor, self.min_factor - 1, -1):
                if (new_val := i * j) < self.val:
                    break
                self.check_for_palindrome(new_val=new_val, pair=[i, j])

    def find_smallest(self):
        """
        Performs search across max_factor -> min_factor range and calculates
        smallest possible value in range, populating the value and list of
        factors of that value.
        """
        for i in range(self.min_factor, self.max_factor + 1):
            for j in range(self.min_factor, self.max_factor + 1):
                if (new_val := i * j) >= self.val:
                    break
                self.check_for_palindrome(new_val=new_val, pair=[i, j])


def largest(min_factor: int, max_factor: int) -> Tuple[Union[int, None], list]:
    """
    Given a range of numbers, find the largest palindromes which
    are products of two numbers within that range.
    """
    palindrome = Palindrome(
        min_factor=min_factor, max_factor=max_factor, find_value="largest"
    )
    palindrome.find_palindromes()
    return palindrome.return_palindrome()


def smallest(min_factor: int, max_factor: int) -> Tuple[Union[int, None], list]:
    """
    Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.
    """
    palindrome = Palindrome(
        min_factor=min_factor, max_factor=max_factor, find_value="smallest"
    )
    palindrome.find_palindromes()
    return palindrome.return_palindrome()
