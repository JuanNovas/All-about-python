# -- all(iterable) --

# Takes an iterable as argument
# Returns True if all elements are True (or if the iterable is empty), otherwise, False
# Answers the question, "None of the elements on the iterable are false"


## LIST
iterable_1 = [1, 2, 3, 4]
all(iterable_1) # Returns True

iterable_2 = [1, 2, 0, 4] 
all(iterable_2) # Returns False

iterable_3 = []
all(iterable_3) # Returns True

## DICT
iterable_4 = {"aaa": 1, "bbb": 0, "ccc": ""}
all(iterable_4) # Returns True

iterable_5 = {"": 1}
all(iterable_5) # Returns False

iterable_6 = {}
all(iterable_6) # Returns True