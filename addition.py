def add(numbers: str) -> int:
    """
    Add numbers in a string separated by commas
    """
    if numbers == "":
        return 0
    elif "," in numbers:
        return sum([int(number) for number in numbers.split(",")])
    else:
        return int(numbers)