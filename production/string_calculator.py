import re


def add(numbers):
    if '' == numbers:
        return 0
    else:
        integers = __parse__(numbers)
        __check_for_negatives__(integers)
        return sum([i for i in integers if i < 1001])


def __parse__(numbers):
    tokens = __tokenize__(numbers)
    return [int(x) for x in tokens]


def __tokenize__(numbers):
    pattern = re.compile('//\[(.+)\]\n(.+)')
    match = pattern.match(numbers)
    if match:
        return re.split(re.escape(match.group(1)), match.group(2))
    else:
        return re.split(',|\n', numbers)


def __check_for_negatives__(integers):
    negatives = [n for n in integers if n < 0]
    if len(negatives) > 0:
        raise RuntimeError('negatives not allowed ' + str(negatives))
