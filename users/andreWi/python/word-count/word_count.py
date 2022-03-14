"""A module implementing functionality for counting words."""
import string

NOT_CONNECTORS = string.punctuation.replace("'", "")

TRANSLATION_TABLE = str.maketrans(NOT_CONNECTORS, len(NOT_CONNECTORS) * " ")


def count_words(sentence: str) -> dict[str, int]:
    """Return the count for each individual word (combination) in sentence.

    :param sentence: str
        An arbitrary phrase.
    :return: dict
        A dict mapping an individual word (combination) to its number of
        occurrences in sentence.
    """
    words = sentence.translate(TRANSLATION_TABLE).lower().split()
    words = [word.strip("'") for word in words]

    return {word: words.count(word) for word in words}
