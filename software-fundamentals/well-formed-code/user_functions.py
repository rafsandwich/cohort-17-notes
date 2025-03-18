def get_user_choice_from_options(words: list[str]) -> str:
    """Returns a user choice from a list."""

    choice = None

    while choice not in words:
        choice = input("Choose one option: ")
    
    return choice




if __name__ == "__main__":

    print(get_user_choice_from_options([
        "goat", "horse", "cow",
        "pig", "sheep", "chicken"
    ]))


# for v in container --> I only care about the values
# for i in range(len(container)) --> I mostly care about the positions
# for i, v in enumerate(container) --> I care about both equally

def has_spaced_pair(text: str) -> bool:
    """Returns True if a string has one character repeated with two steps in between."""
    pass

# has_spaced_pair("toot") -> True
# has_spaced_pair("toof") -> False

# Valid if 2 spaced pairs, but not three
# toottoot -> False -> t..t, t..t o..o
# foottoot -> True -> o..o, t..t

# break (stop a loop)
# continue (moves on to the next iteration of the loop)