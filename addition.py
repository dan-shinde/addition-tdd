def validate_and_add_numbers_string(func):
    """
    Decorator to validate the numbers string and add the numbers
    """
    def wrapper(args, **kwargs):
        numbers = func(args, **kwargs)
        if numbers == 0:
            return numbers
        _validate_numbers(numbers)
        seperator, numbers = _get_separator(numbers)
        numbers_list = _get_list_of_numbers_from_string_and_seperator(numbers, seperator)
        return sum([int(number) for number in numbers_list])
    return wrapper

@validate_and_add_numbers_string
def add(numbers: str) -> int:
    """
    Add numbers in a string separated by commas or newlines
    function also supports custom separators
    custom separators are defined by a string starting with "//" and ending with "\n"
    """
    if numbers == "":
        return 0
    else:
        return numbers

def _get_list_of_numbers_from_string_and_seperator(numbers: str, seperator: str) -> list:
    """
    Function to get a list of numbers from string
    where the numbers in the string are seperated by seperator
    """
    return numbers.split(seperator)

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
