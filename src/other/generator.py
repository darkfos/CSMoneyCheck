from random import randint
import string


async def generate_random_key():
    lower_case = string.ascii_lowercase
    upper_case = lower_case.upper()
    numbers = "123456789"
    symbols = "/.,]"

    all_elements: str = lower_case + upper_case + numbers + symbols  # noqa
    result_key: str = ""

    for _ in range(0, randint(5, randint(15, 40))):
        result_key += all_elements[randint(0, len(all_elements) - 1)]

    return result_key
