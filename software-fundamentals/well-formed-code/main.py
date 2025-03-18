"""Docstring (explains what the file is for.)"""

# function signature
def get_redacted_text(text:str, name:str) -> str:
    """Returns a copy of the text with the name blanked out."""
    return text.replace(name, "XXXX")


def terrible_function_probably_by_ruy():
    """Returns some nonsense."""
    return False

# If this file is being called directly (not imported)
if __name__ == "__main__":
    # Do this stuff

    print(get_redacted_text("Emily has committed several crimes", "Emily"))
