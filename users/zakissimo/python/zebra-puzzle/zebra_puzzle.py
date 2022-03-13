from enum import Enum, auto
from multiprocessing.sharedctypes import Value


class Color(Enum):
    RED = auto()
    GREEN = auto()
    IVORY = auto()
    YELLOW = auto()
    BLUE = auto()


class Nationality(Enum):
    ENGLISHMAN = auto()
    SPANIARD = auto()
    UKRAINIAN = auto()
    JAPANESE = auto()
    NORWEGIAN = auto()


class Pet(Enum):
    DOG = auto()
    SNAILS = auto()
    FOX = auto()
    HORSE = auto()
    ZEBRA = auto()


class Beverage(Enum):
    COFFEE = auto()
    TEA = auto()
    MILK = auto()
    ORANGE_JUICE = auto()
    WATER = auto()


class CigaretteBrand(Enum):
    OLD_GOLD = auto()
    KOOLS = auto()
    CHESTERFIELDS = auto()
    LUCKY_STRIKE = auto()
    PARLIAMENTS = auto()


relations = [
    (Nationality.ENGLISHMAN, Color.RED),
    (Nationality.SPANIARD, Pet.DOG),
    (Beverage.COFFEE, Color.GREEN),
    (Nationality.UKRAINIAN, Beverage.TEA),
    (CigaretteBrand.OLD_GOLD, Pet.SNAILS),
    (CigaretteBrand.KOOLS, Color.YELLOW),
    (CigaretteBrand.LUCKY_STRIKE, Beverage.ORANGE_JUICE),
    (Nationality.JAPANESE, CigaretteBrand.PARLIAMENTS),
]


class Household:
    _val_to_household = {}

    @classmethod
    def get_household(cls, val):
        if val not in cls._val_to_household:
            raise ValueError(f"val {val} not found")
        return cls._val_to_household[val]

    def __init__(self):
        self._vals = set()
        self.invalid_vals = set()


key_to_household = {}
for relation in relations:
    for key_1, key_2 in relation:
        # TOOD: UnionFind?
        pass

Household.get_household(CigaretteBrand.CHESTERFIELDS).invalid_vals.add(Pet.FOX)  # FOX is all the way to the left or right?
Household.get_household(CigaretteBrand.KOOLS).invalid_vals.add(Pet.HORSE)  # HORSE is all the way to the left or right?

houses = [
    Household.get_household(Nationality.NORWEGIAN),
    Household.get_household(Color.BLUE),
    Household.get_household(Beverage.MILK),
]
# Household.get_household(Color.GREEN).left = Household.get_household(Color.IVORY)


def drinks_water():
    pass


def owns_zebra():
    pass
