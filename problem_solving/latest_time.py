"""Returns the latest time given a list of integers"""

def get_first_digit(digits: list[int]) -> int:
    """Returns the first digit"""
    digits.sort(reverse=True)
    for digit in digits:
        if digit < 3:
            return digit
    raise ValueError("Incorrect input")


def get_second_digit(digits: list[int], first_digit: int) -> int:
    """Returns the second digit"""
    digits.sort(reverse=True)
    if first_digit < 2:
        return max(digits)
    for digit in digits:
        if digit < 4:
            return digit
    raise ValueError("Incorrect input")


def get_third_digit(digits: list[int]) -> int:
    """Returns the third digit"""
    for digit in digits:
        if digit < 6:
            return digit
    raise ValueError("Incorrect input")


def find_latest_time(digits: list[int]) -> str:
    """Returns the latest time"""
    digits.sort()
    first_digit = get_first_digit(digits)
    digits.remove(first_digit)

    second_digit = get_second_digit(digits, first_digit)
    digits.remove(second_digit)

    third_digit = get_third_digit(digits)
    digits.remove(third_digit)

    return f"{first_digit}{second_digit}:{third_digit}{digits[0]}"
