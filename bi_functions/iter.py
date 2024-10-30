# Returns an Iterator OBJ 
# Takes an iterable or a Callable OBJ and a 'sentinel', when the iterator returns the same value as the 'sentinel' stops


iter([1,2,3,4]) # Returns an Iterator OBJ


import random
def generate_number():
    return random.randint(1,10)
iter(generate_number, 7) # Returns: an iterator that raises StopIteration after 7 is returned