import re


def add(numbers):
    if '' == numbers:
        return 0
    else:
        integers = __parse__(numbers)
        __check_for_negatives__(integers)
        return sum([i for i in integers if i < 1001])


def __check_for_negatives__(integers):
    negatives = [n for n in integers if n < 0]
    if len(negatives) > 0:
        raise RuntimeError('negatives not allowed ' + str(negatives))


def __parse__(numbers):
    tokens = __tokenize__(numbers)
    return [int(x) for x in tokens]


def __tokenize__(numbers):
    delimiters, numbers = __split_into_delimiters_and_numbers__(numbers)
    return re.split(delimiters, numbers)


def __split_into_delimiters_and_numbers__(numbers):
    match = re.compile('//(.+)\n(.+)').match(numbers)
    if match:
        return (__generate_delimiters_regex__(match.group(1)), match.group(2))
    else:
        return (',|\n', numbers)


def __generate_delimiters_regex__(delimiters_definition):
    delimiters = re.findall('\[([^\[\]]+)\]', delimiters_definition)
    return '|'.join(re.escape(d) for d in delimiters)
