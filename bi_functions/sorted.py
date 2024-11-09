# -- sorted(iterable, /, *, key=None, reverse=False) --

# Return a new sorted list from the items in iterable
# key specifies a function of one argument that is used to compare each element
# reverse especifies if the result iterable will be reversed or not


example_iterable = ['A', 'b', '#', 'z', 'Q', '*', 'k', '!', 'Z', 'r']

sorted(example_iterable) # Returns: ['!', '#', '*', 'A', 'Q', 'Z', 'b', 'k', 'r', 'z']

sorted(example_iterable, key=str.lower) # Returns: ['!', '#', '*', 'A', 'b', 'k', 'Q', 'r', 'z', 'Z']

sorted(example_iterable, reverse=True) # Returns: ['z', 'r', 'k', 'b', 'Z', 'Q', 'A', '*', '#', '!']

sorted(example_iterable, key=str.upper, reverse=True) # Returns: ['z', 'Z', 'r', 'Q', 'k', 'b', 'A', '*', '#', '!']