# next(iterator[, default])
# Retrieves the next item from an iterator by calling its __next__() method
# When the iterator is exhausted it returns the default value, if given, or raise a StopIteration

example_iterator = iter([1,2])

next(example_iterator, 10) # Returns: 1
next(example_iterator, 10) # Returns: 2
next(example_iterator, 10) # Returns: 10
next(example_iterator, 10) # Returns: 10
next(example_iterator) # Raises: StopIteration
