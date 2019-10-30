import re

def add(numbers):
    if '' == numbers:
        return 0
    else:
        regex = ',|\n'
        if (numbers.startswith('//')):
            regex += '|' + numbers[2]
            numbers = numbers[4:]
        return sum([int(x) for x in re.split(regex, numbers)])
