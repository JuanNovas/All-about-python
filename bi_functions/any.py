# Takes an iterable as argument
# Returns True if any element of the iterable is True
# Answers the statement, "At least one element is True"


## LIST
iterable_1 = [1, 2, 3, 4]
any(iterable_1) # Returns True

iterable_2 = [1, 2, 0, 0] 
any(iterable_2) # Returns True

iterable_3 = [0, 0]
any(iterable_3) # Returns False

iterable_4 = []
any(iterable_4) # Returns False

## DICT
iterable_5 = {"aaa": 1, "bbb": 0, "ccc": ""}
any(iterable_5) # Returns True

iterable_6 = {"": 1, "": 0, "ccc": ""}
any(iterable_6) # Returns True

iterable_7 = {"": 1}
any(iterable_7) # Returns False

iterable_8 = {}
any(iterable_8) # Returns False