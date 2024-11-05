# -- max(iterable, *[, key, default]) --
# -- max(arg1, arg2, *args[, key]) --

# Returns the largest item
# If one argument is given it should be an Iterable
# If two or more parameters are given the largest is returned
# The optional parameter key tells how the values are going to be trait before ordering and define the max value, takes a function
# The optional default value only works when an only Iterable is given and returns itself when the iterator is empty

max([1,2,3,4]) # Returns: 4

max([1,2,3,4], default=5) # Returns: 4 

max([1,2,3,4], key=lambda x: (x + 2) / x) # Returns: 1

max([], default=2) # Returns: 2


max(1,2,3,4) # Returns: 4

max(1,2,3,4, default=5) # Raise: TypeError

max(1,2,3,4, key=lambda x: x - x * 2) # Returns:1