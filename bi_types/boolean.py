# There are three boolean operations

# x or y: if x is true, then x, else y
# x and y: if x is false, then x, else y
# not x: if x is false, then True, else False


a = 1
b = 2
x = 0

a or b # Returns: 1 (A true value)
a or x # Returns: 1 (A true value)

a and b # Returns: 2 (A true value)
a and x # Returns: 0 (A false value)

not a # Returns: False
not x # Returns: True