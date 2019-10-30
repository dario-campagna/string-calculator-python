import re

def add(numbers):
    if '' == numbers:
        return 0
    else:
        return sum([int(x) for x in __tokenize__(numbers)])

def __tokenize__(numbers):
    regex = ',|\n'
    if (numbers.startswith('//')):
        regex = numbers[2]
        numbers = numbers[4:]
    return re.split(regex, numbers)
