def raise_error():
    return 5/0

def user_raises_error():
    """LOL RSING ERS"""
    raise EnvironmentError("There are no windows!!!")

def user_raises_error_but_different_message():
    raise EnvironmentError("There are no windows I can't see the sun!!!")


def first_function(s: str) -> str:
    return s.upper()

def second_function(s: str) -> str:
    return s.lower()

def does_it_all(s:str) -> str:
    return second_function(first_function(s))

def main():
    # This does everything
    pass


if __name__ == "__main__":
    string = "Hey"
    string = first_function(string)
    string = second_function(string)
    print(string)
    print(does_it_all(string))
    print(__name__)
