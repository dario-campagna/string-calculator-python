import re


def add(numbers):
    if '' == numbers:
        return 0
    else:
        return sum([int(x) for x in __tokenize__(numbers)])


def __tokenize__(numbers):
    delimiter_regex, numbers = __split_into_delimiter_and_numbers__(numbers)
    return re.split(delimiter_regex, numbers)


def __split_into_delimiter_and_numbers__(numbers):
    pattern = re.compile(r"//(.)\n(.+)")
    match = pattern.match(numbers)
    if match:
        return (match.group(1), match.group(2))
    else:
        return (',|\n', numbers)
