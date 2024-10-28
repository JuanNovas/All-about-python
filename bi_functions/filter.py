# Creates an iterator from those elements of an iterable for which the function returns True
# Takes a function and an iterable
# The values of the iterable will be passed to the funtion


from utils.filter import numbers, is_even

even_numbers = list(filter(is_even, numbers)) # Returns: [0, 2, 4, 6, 8]