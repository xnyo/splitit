import random
import string


def random_string(length: int = 8) -> str:
    """
    Returns a random string (just letters) of a specified length

    :param length: the length
    :return: the random string
    """
    return "".join(random.choice(string.ascii_letters) for _ in range(length))
