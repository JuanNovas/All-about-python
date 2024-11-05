# -- map(function, iterable, ...) --

# Returns an iterator that applies a function to every item of the iterable
# Takes a function and N amount of itetables (N >= 1)


map(lambda x : x * 2, [1,2,3,4]) # Returns an iterator that returns: 2, 4, 6, 8


map(lambda x, y: x * y, [10,20,30,40], [5,6,7,8]) # Returns an iterator that returns: 50, 120, 210, 320