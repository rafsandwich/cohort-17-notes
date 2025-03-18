"""Validates and formats UK phone numbers"""


def ask_user_for_phone_number() -> str:
    """Returns a string of + and numbers"""
    phone_number = input("What is the phone number to validate? ")
    valid_numbers = ""
    for letter in phone_number:
        if letter.isnumeric() or letter == "+":
            valid_numbers += letter
    return valid_numbers


# Not truthy: "", [], None


def format_uk_number():
    """Prints a formatted number"""
    phone_number = ask_user_for_phone_number()
    formatted_number = convert_phone_to_uk_format(phone_number)
    if formatted_number:
        print(" ".join(formatted_number))
    else:
        raise ValueError(f"{phone_number} is not a valid UK number. Please try again.")


def is_number_valid_length(phone_number: str) -> bool:
    """Checks is phone number is a valid length"""
    return len(phone_number) == 11


def is_uk_number(phone_no: str) -> bool:
    """Checks is phone number is a valid start"""
    return phone_no.startswith("07")


def has_country_code(phone_no: str) -> bool:
    """Checks if +44 in number"""
    return "+44" in phone_no


def convert_phone_to_uk_format(user_input: str) -> list:
    """Checks is phone number is a valid length"""

    if has_country_code(user_input):
        user_input = user_input.replace("+44", "07")

    if is_number_valid_length(user_input) and is_uk_number(user_input):
        return convert_string_to_phone_format(user_input)

    return None


def convert_string_to_phone_format(phone_str: str) -> list:
    """Checks is phone number is a valid length"""
    first_part = phone_str[:5]
    second_part = phone_str[5:]
    return [first_part, second_part]


if __name__ == "__main__":
    format_uk_number()
