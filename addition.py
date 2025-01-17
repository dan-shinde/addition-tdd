def add(numbers: str) -> int:
    """
    Add numbers in a string separated by commas or newlines
    function also supports custom separators
    custom separators are defined by a string starting with "//" and ending with "\n"
    """
    if numbers == "":
        return 0
    elif "-" in numbers:
        raise ValueError("Negatives not allowed")
    elif "//" in numbers:
        separator, numbers = numbers.split("\n")
        separator = separator[2:]
        return sum([int(number) for number in numbers.split(separator)])
    elif "," in numbers or "\n" in numbers:
        numbers = numbers.replace("\n", ",")
        return sum([int(number) for number in numbers.split(",")])
    else:
        return int(numbers)