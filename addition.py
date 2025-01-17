def add(numbers: str) -> int:
    """
    Add numbers in a string separated by commas or newlines
    function also supports custom separators
    custom separators are defined by a string starting with "//" and ending with "\n"
    """
    if numbers == "":
        return 0
    else:
        return _add(numbers)
    
def _add(numbers: str) -> int:
    """
    Add numbers in a string separated by commas or newlines or custom separators
    """
    _validate_numbers(numbers)
    seperator, numbers = _get_separator(numbers)
    return _get_sum(numbers, seperator)

def _validate_numbers(numbers: str) -> None:
    """
    Validate the numbers in the string
    if the string contains negative numbers, raise a ValueError
    """
    if "-" in numbers:
        negatives = [number for number in numbers.split(",") if "-" in number]
        raise ValueError(f"Negatives not allowed: {', '.join(negatives)}")
    
def _get_separator(numbers: str) -> tuple:
    """
    Get the separator from the string
    """
    if "//" in numbers:
        separator, numbers = numbers.split("\n")
        return separator[2:], numbers
    elif "," in numbers or "\n" in numbers:
        numbers = numbers.replace("\n", ",")
        return ",", numbers
    else:
        return ",", numbers
    
def _get_sum(numbers: str, separator: str) -> int:
    """
    Get the sum of numbers in the string
    """
    if separator in numbers:
        return sum([int(number) for number in numbers.split(separator)])
    else:
        return int(numbers)
