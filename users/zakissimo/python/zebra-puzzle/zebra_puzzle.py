from itertools import product


class House:
    def __init__(self):
        self.id: int
        self.color: str | None = None
        self.nationality: str | None = None
        self.animal: None = None
        self.drink: str | None = None
        self.cigarette: str | None = None
        self.right: House
        self.left: House


KNOWN_VALUES = {
    "id": [1, 2, 3, 4, 5],
    "color": ["red", "blue", "yellow", "green", "ivory"],
    "nationality": ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
    "animal": ["snails", "zebra", "horse", "fox", "dog"],
    "cigarette": ["Old Gold", "Chesterfields", "Lucky Strike", "Kools", "Parliaments"],
    "drink": ["tea", "milk", "orange juice", "water", "coffee"],
}


def generate_neighborhood():
    neighborhood = [House() for _ in range(5)]

    for i, house in enumerate(neighborhood):
        house.id = i + 1
        if house.id > 1:
            house.left = neighborhood[i - 1]
        if house.id < 5:
            house.right = neighborhood[i + 1]

    return neighborhood


def test_uniq(n):
    n = [item for sublist in n for item in sublist]
    return len(n) == len(set(n))


def filter_houses(house):
    if (
        (
            all((x in house for x in [1, "Norwegian"]))
            or all((x in house for x in ["red", "Englishman"]))
            or all((x in house for x in ["dog", "Spaniard"]))
            or all((x in house for x in ["Ukrainian", "tea"]))
            or all((x in house for x in ["Japanese", "Parliaments"]))
        )
        and (
            all((x in house for x in ["coffee", "green"]))
            or all((x in house for x in ["milk", 3]))
            or all((x in house for x in ["Ukrainian", "tea"]))
            or all((x in house for x in ["Lucky Strike", "orange juice"]))
            or (
                "water" in house
                and not 3 in house
                and not "green" in house
                and not "Ukrainian" in house
                and not "Lucky Strike" in house
            )
        )
        and (
            all((x in house for x in ["blue", 2]))
            or all((x in house for x in ["red", "Englishman"]))
            or all((x in house for x in ["Kools", "yellow"]))
            or all((x in house for x in ["coffee", "green"]))
            or (
                "ivory" in house
                and not 2 in house
                and not "Englishman" in house
                and not "Kools" in house
                and not "coffee" in house
            )
        )
        and (
            all((x in house for x in ["Old Gold", "snails"]))
            or all((x in house for x in ["Lucky Strike", "orange juice"]))
            or all((x in house for x in ["Japanese", "Parliaments"]))
            or all((x in house for x in ["Kools", "yellow"]))
            or (
                "Chesterfields" in house
                and not "snails" in house
                and not "orange juice" in house
                and not "Japanese" in house
                and not "yellow" in house
            )
        )
        and (
            all((x in house for x in [1, "Norwegian"]))
            or all((x in house for x in ["blue", 2]))
            or all((x in house for x in ["milk", 3]))
            or (
                4 in house
                and not "Norwegian" in house
                and not "blue" in house
                and not "milk" in house
            )
            or (
                5 in house
                and not "Norwegian" in house
                and not "blue" in house
                and not "milk" in house
            )
        )
    ):
        return True
    return False


def generate_all_neighborhoods():

    houses = (
        (house)
        for house in product(
            KNOWN_VALUES["id"],
            KNOWN_VALUES["color"],
            KNOWN_VALUES["nationality"],
            KNOWN_VALUES["animal"],
            KNOWN_VALUES["cigarette"],
            KNOWN_VALUES["drink"],
        )
        if filter_houses(house)
    )

    one, two, three, four, five = [], [], [], [], []

    for house in houses:
        if 1 in house:
            one.append(house)
        elif 2 in house:
            two.append(house)
        elif 3 in house:
            three.append(house)
        elif 4 in house:
            four.append(house)
        elif 5 in house:
            five.append(house)

    neighborhoods = (
        (neighborhood)
        for neighborhood in product(one, two, three, four, five)
        if test_uniq(neighborhood)
    )

    return neighborhoods


def print_neighborhood(neighborhood):
    settings = [id, color, nationality, animal, cigarette, drink] = [
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    for house in neighborhood:
        id.append(house.id)
        color.append(house.color)
        nationality.append(house.nationality)
        animal.append(house.animal)
        cigarette.append(house.cigarette)
        drink.append(house.drink)

    for setting in settings:
        print("{!s:^13}|{!s:^13}|{!s:^13}|{!s:^13}|{!s:^13}".format(*setting))


def test_neighborhood(actual_n, generated_n):
    for house in actual_n:
        for gen in generated_n:
            if house.id == gen[0]:
                house.color = gen[1]
                house.nationality = gen[2]
                house.animal = gen[3]
                house.cigarette = gen[4]
                house.drink = gen[5]

    count = 0
    for house in actual_n:
        if house.color == "green" and house.id > 1 and house.left.color == "ivory":
            count += 1
        if house.cigarette == "Chesterfields" and (
            (house.id > 1 and house.left.animal == "fox")
            or (house.id < 5 and house.right.animal == "fox")
        ):
            count += 1
        if house.cigarette == "Kools" and (
            (house.id > 1 and house.left.animal == "horse")
            or (house.id < 5 and house.right.animal == "horse")
        ):
            count += 1

    if count == 3:
        return True
    return False


def drinks_water():
    neighborhoods = generate_all_neighborhoods()
    actual_n = generate_neighborhood()
    for generated_n in neighborhoods:
        if test_neighborhood(actual_n, generated_n):
            for house in actual_n:
                if house.drink == "water":
                    return house.nationality
    return 1


def owns_zebra():
    neighborhoods = generate_all_neighborhoods()
    actual_n = generate_neighborhood()
    for generated_n in neighborhoods:
        if test_neighborhood(actual_n, generated_n):
            for house in actual_n:
                if house.animal == "zebra":
                    return house.nationality
    return 1


if "__main__" == __name__:
    neighborhoods = generate_all_neighborhoods()
    actual_n = generate_neighborhood()
    for generated_n in neighborhoods:
        if test_neighborhood(actual_n, generated_n):
            print_neighborhood(actual_n)
