import functools
import re


def validate_set_number_parts(set_number_parts):
    def length_check(number: str) -> None:
        if 10 > len(number):
            raise ValueError("incorrect number of digits")
        if 11 == len(number) or (12 == len(number) and number.startswith("+1")):
            if number.startswith("1") or number.startswith("+1"):
                return re.sub("\+", "", number)[1:]
            raise ValueError("11 digits must start with 1")
        if 11 < len(number):
            raise ValueError("more than 11 digits")
        return None

    def letter_punctuation_check(n: str) -> None:
        if regex := re.findall("[^\d]", n):
            raise ValueError(
                f'{"letters" if re.match("[a-z]", regex[0]) else "punctuations"} not permitted'
            )

    def num_code_checks(n: str, code: str) -> None:
        print(n)
        if n[0] == "0":
            raise ValueError(f"{code} code cannot start with zero")
        elif n[0] == "1":
            raise ValueError(f"{code} code cannot start with one")

    @functools.wraps(set_number_parts)
    def wrapper(self, number, *args, **kwargs):
        length_check(number)
        letter_punctuation_check(number)
        set_number_parts(self, number, *args, **kwargs)
        num_code_checks(self.area_code, "area")
        num_code_checks(self.exchange_code, "exchange")

    return wrapper

class PhoneNumber:
    def __init__(self, number: str):
        cleaned_number = self.clean_number(number)
        self.set_number_parts(cleaned_number)
        self.number = cleaned_number[1:] if cleaned_number[0] == "1" else cleaned_number

    def clean_number(self, number: str) -> int:
        return re.sub("[)(\-. +]", "", number).lower()

    @validate_set_number_parts
    def set_number_parts(self, number: str) -> None:
        number_minus_cc = (
            number[1:] if len(number) == 11 and number[0] == "1" else number
        )
        self.area_code, self.exchange_code, self.subscriber_number = (
            number_minus_cc[:3],
            number_minus_cc[3:6],
            number_minus_cc[6:],
        )

    def pretty(self) -> str:
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
