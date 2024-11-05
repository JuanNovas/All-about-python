# -- min(iterable, *[, key, default]) --
# -- min(arg1, arg2, *args[, key]) --

# Returns the smallest item
# If one argument is given it should be an Iterable
# If two or more parameters are given the smallest is returned
# The optional parameter key tells how the values are going to be trait before ordering and define the min value, takes a function
# The optional default value only works when an only Iterable is given and returns itself when the iterator is empty

min([1,2,3,4]) # Returns: 1

min([1,2,3,4], default=5) # Returns: 1

min([1,2,3,4], key=lambda x: (x + 2) / x) # Returns: 4

min([], default=2) # Returns: 2


min(1,2,3,4) # Returns: 1

min(1,2,3,4, default=5) # Raise: TypeError

min(1,2,3,4, key=lambda x: x - x * 2) # Returns: 4