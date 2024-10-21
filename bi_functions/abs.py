# Acepts a INT, FLOAT, COMPLEX NUMBER or an OBJ with __abs__() method
# Returns the absolute number of the parameter, for complex numbers it returns the magnitude

## INT
abs(10) # Returns 10
abs(-10) # Returns 10

## FLoat
abs(5.4) # Returns 5.4
abs(-5.4) # Returns 5.4

## COMPLEX NUMBER
z1 = 2 + 2j
abs(z1) # Returns 2.8284271247461903

## OBJ
from utils.bi_functions.abs import Point2d
obj_with_abs_property = Point2d(4,4) # Creates an object with the __abs__ property
abs(obj_with_abs_property) # Returns 5.656854249492381