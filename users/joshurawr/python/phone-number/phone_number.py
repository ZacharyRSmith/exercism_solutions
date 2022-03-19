import functools
import string


class _PhoneNumberValidator:

    VALID_PUNCTUATION = set("+-().")
    VALID_CHARACTERS = set(string.digits) | VALID_PUNCTUATION | set(string.whitespace)
    INVALID_LETTERS = set(string.ascii_letters)
    INVALID_PUNCTUATION = set(string.punctuation) - VALID_PUNCTUATION

    @classmethod
    def validate_number_characters(cls, number: str):
        number_character_set = set(number)
        if number_character_set & cls.INVALID_LETTERS:
            raise ValueError("letters not permitted")
        if number_character_set & cls.INVALID_PUNCTUATION:
            raise ValueError("punctuations not permitted")
        if not number_character_set <= cls.VALID_CHARACTERS:
            raise ValueError(f"only 0-9 or {''.join(cls.VALID_PUNCTUATION)}")
        return
        
    @classmethod
    def validate_digit_string(cls, validated_digit_string):
        @functools.wraps(validated_digit_string)
        def wrapper(number):
            cls.validate_number_characters(number)
            res = validated_digit_string(number)
            return res
        return wrapper


class PhoneNumber:

    def __init__(self, number: str):
        self._number = self.validated_digit_string(number)
        self.validate_area_code()
        self.validate_exchange_code()

    @staticmethod
    @_PhoneNumberValidator.validate_digit_string
    def validated_digit_string(number: str):
        digit_string = "".join(x for x in number if x.isdecimal())
        if len(digit_string) > 11:
            raise ValueError("more than 11 digits")
        if len(digit_string) < 10:
            raise ValueError("incorrect number of digits")
        if len(digit_string) == 11 and digit_string[0] != "1":
            raise ValueError("11 digits must start with 1")
        return digit_string[-10:]

    def validate_area_code(self):
        if self.area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if self.area_code[0] == "1":
            raise ValueError("area code cannot start with one")

    def validate_exchange_code(self):
        if self.exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

    @property
    def number(self):
        return self._number

    @property
    def area_code(self):
        return self._number[0:3]

    @property
    def exchange_code(self):
        return self._number[3:6]

    @property
    def station_code(self):
        return self._number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.station_code}"
