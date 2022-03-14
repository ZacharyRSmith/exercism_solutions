"""A module implementing functionality for counting words."""
from collections import Counter
import string

NOT_CONNECTORS = string.punctuation.replace("'", "")

TRANSLATION_TABLE = str.maketrans(NOT_CONNECTORS, len(NOT_CONNECTORS) * " ")


def _get_words(sentence):
    for word in sentence.translate(TRANSLATION_TABLE).lower().split():
        yield word.strip("'")


def count_words(sentence: str) -> dict[str, int]:
    """Return the count for each individual word (combination) in sentence.

    :param sentence: str
        An arbitrary phrase.
    :return: dict
        A dict mapping an individual word (combination) to its number of
        occurrences in sentence.
    """
    word_to_count = Counter()
    for word in _get_words(sentence):
        word_to_count[word] += 1
    return dict(word_to_count)
