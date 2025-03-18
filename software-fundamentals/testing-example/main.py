"""Example functions to test."""

import random


def get_fair_die_roll() -> int:
    """Returns a random number from a die."""
    return random.randint(1, 6)


def get_prefix(word: str) -> str:
    """Returns the prefix of a hyphenated word."""
    if "-" not in word:
        raise ValueError("Function expects a hyphenated word.")
    return word[:word.index("-")]


def get_length_of_user_input() -> int:
    """Returns the length of the user input."""

    return len(input())


def display_ascii_gift(gift: str) -> None:
    """Prints a string as a gift."""
    print(f"{gift} ノ( º _ ºノ)")


if __name__ == "__main__":

    PREFIXED_WORD = "trans-siberian"
    print(get_prefix(PREFIXED_WORD))
