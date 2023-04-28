def check_key_format(win_key: str) -> bool:
    """
    Checks that the key is in the correct format. Format should be three numbers, a hyphen, then 7 numbers
    :param win_key: Windows key as a string
    :return: bool
    """
    import re

    match = re.search("^[0-9]{3}-[0-9]{7}$", win_key)
    if match:
        return True
    return False


def check_key_part_one(key_part: str) -> bool:
    """
    Checks everything before the hyphen against the list of banned strings
    :param key_part: The three characters before the hyphen
    :return: bool
    """
    banned_key_parts = ("333", "444", "555", "666", "777", "888", "999")
    if key_part not in banned_key_parts:
        return True
    return False


def mod7(key_part: str):
    """
    Checks the final 7 numbers in the string.
    :param key_part: The final 7 characters of the win_key string
    :return: bool
    """
    total = sum([int(x) for x in key_part])
    if total % 7 == 0:
        return True
    return False


def validate_win95_key(win_key: str):
    """
    Validated a provided Windows 95 key.
    :param win_key:
    :return:
    """
    win_key = win_key.strip()
    win_key_split = win_key.split("-")

    # run through the checks for each part of the win_key
    if not check_key_format(win_key):
        print("Key is in an invalid format 🚫\n")
        return False
    if not check_key_part_one(win_key_split[0]):
        print("Key part one is invalid 🚫\n")
        return False
    if not mod7(win_key_split[1]):
        print("Key part two is invalid 🚫\n")
        return False

    # if we pass all the checks we can confirm the key is valid
    print(f"{win_key} is valid!\n")
    return True
