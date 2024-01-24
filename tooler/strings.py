import random
import string


def generate_random_string(length: int, punctuation: bool) -> str:
    """Генерирует строку из ascii_letters + digits + !@#"""
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for _ in range(length))
    rndm = "".join(random.choice("!@#") for _ in range(random.randint(1, 3)))
    random_string += rndm if punctuation else ""
    return random_string


if __name__ == "__main__":
    print(generate_random_string(12, True))
