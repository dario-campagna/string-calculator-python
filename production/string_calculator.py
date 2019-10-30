import re

def add(numbers):
    if '' == numbers:
        return 0
    else:
        return sum([int(x) for x in re.split(',|\n', numbers)])
