import random
import string


def random_number(low, high):
    if low > high:
        raise ValueError("Invalid range")
    return random.randint(low, high)


def random_list(count, low, high):
    if count < 0 or low > high:
        raise ValueError("Invalid values")

    return [
        random.randint(low, high)
        for _ in range(count)
    ]


def password(length):
    if length < 4:
        raise ValueError("Minimum length is 4")

    characters = string.ascii_letters + string.digits + "!@#$%"

    result = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%")
    ]

    result += [
        random.choice(characters)
        for _ in range(length - 4)
    ]

    random.shuffle(result)
    return "".join(result)


def otp(length):
    if not 4 <= length <= 10:
        raise ValueError("Length must be between 4 and 10")

    return "".join(
        random.choice(string.digits)
        for _ in range(length)
    )