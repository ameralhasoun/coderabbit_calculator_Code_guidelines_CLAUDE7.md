def get_even_numbers(numbers):
    """
    Returns a list of even numbers from the given list.
    """
    return [n for n in numbers if n % 2 == 0]


print(get_even_numbers([1, 2, 3, 4, 5, 6]))