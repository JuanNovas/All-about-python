# -- repr(OBJ) -> STR --

# Return a string containing a printable representation of an OBJ
# If the method __repr__() is defined, it is returned
# Otherwise the representation is the name of the type and the memory address


repr(20) # Returns: '20'

repr('hello') # Returns: 'hello'

repr(print) # Returns: '<built-in function print>'

from utils.repr import example_object
repr(example_object) # Returns: '<utils.repr.ExampleClass object at 0x0000000000000000>'

from utils.repr import example_object_with_repr
repr(example_object_with_repr) # Returns: 'custom message'