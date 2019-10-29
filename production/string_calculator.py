def add(numbers):
    if '' == numbers:
        return 0
    elif len(numbers) == 1:
        return int(numbers[0])
    else:
        return int(numbers[0]) + int(numbers[2])