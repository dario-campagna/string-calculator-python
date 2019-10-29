def add(numbers):
    if '' == numbers:
        return 0
    else:
        return sum([int(x) for x in numbers.replace('\n', ',').split(',')])
