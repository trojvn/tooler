from string import digits, ascii_letters
from random import choice


def has_numbers(input_string: str) -> bool:
    return any(char.isdigit() for char in input_string)


def has_chars(input_string: str) -> bool:
    return any(char for char in input_string if char in "!@#")


def generate_random_string(length: int, punctuation: bool) -> str:
    """Генерирует строку из ascii_letters + digits + !@#"""
    characters = ascii_letters + digits + "!@#" if punctuation else ""
    while True:
        random_string = "".join(choice(characters) for _ in range(length))
        if has_numbers(random_string) and has_chars(random_string):
            return random_string
