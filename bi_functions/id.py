# Returns the 'identity' of an object as an INT
# This id is garantee to be unique during its lifetime
# Two objects with non-overlapping lifetime may have the same id() value
# The int returned is the memory address of the OBJ

x = "aaa"
id(x) # Returns the memory address

x = 45
id(x) # Returns the memory address

from utils.id import example_object
id(example_object) # Returns the memory address