"""Examples of Exception Handling."""


def divide(a: int, b: int) -> int:
    """Returns the division of two numbers."""

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Function requires two integers.")
    
    if not b:
        raise ValueError("Dividing by zero is forbidden.")

    return a // b


def feed_iguana(food: str) -> None:
    """Feed an iguana."""

    if food == "bomb":
        raise Exception("BOOOOM!")

    if food == "leaf":
        print("CHOMP!")
    else:
        raise ValueError("Iguanas are gentle creatures who no longer consume flesh.")


def feed_iguanas(iguanas: list[str], foods: list[str]) -> None:

    for i in range(len(iguanas)):
        try:
            feed_iguana(foods[i])
        except ValueError:
            print(f"{iguanas[i]} refused the food.")


if __name__ == "__main__":
    
    feed_iguanas(["Dorothy", "Matteo", "Blitz"],
                  ["leaf", "bomb", "leaf"])
