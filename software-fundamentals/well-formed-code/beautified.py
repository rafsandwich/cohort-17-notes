"""A simple word-guessing game."""

import random


def get_random_word(words: list[str]) -> str:
    """Returns a randomly-selected word from the list."""
    return random.choice(words)


def get_five_letter_word() -> str:
    """Returns a five-letter word entered by the user."""

    word = ""

    while len(word) != 5 or not word.isalpha():
        word = input("Please enter a five-letter word: ")

    return word


def get_masked_result(guess: str, secret: str) -> str:
    """Returns a masked version of the secret, with unknown letters replaced with '?'."""
    return "".join(c if guess[i] == c else "?" for i, c in enumerate(secret))
    # masked_word = ""
    # for index, letter in enumerate(secret):
    #     if letter == guess[index]:
    #         masked_word += letter
    #     else:
    #         masked_word += "?"

def play_game(secret_word:str, max_guesses:int=5) -> None:
    """Plays a round of a word-guessing game."""

    turns_remaining = max_guesses

    while turns_remaining > 0:
        turns_remaining -= 1

        guess = get_five_letter_word()

        print(get_masked_result(guess, secret_word), f"{turns_remaining}/{max_guesses}")

        if guess == secret_word:
            print("You win!")
            return

    print(f"Sorry, you didn't guess the word. The word was {secret_word}.")


if __name__ == "__main__":

    word_list = ["apple", "place", "grape", "chair", "spear", "green",
                 "plant", "house", "water", "money", "tiger", "panda"]

    chosen_word = get_random_word(word_list)

    play_game(chosen_word)
