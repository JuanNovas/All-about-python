# Returns a list of names in the specific scope
# With no arguments return the names of the current local scope
# With an argument attempt to return a list of valid attributes for that object
# If the object has the method __dir__() it will call it
# Otherwise the function tries to gather information from the __dict__ parameter and the resulting list may not be necessarily completed
# The resulting list is sorted alphabetically

import struct
dir() # Returns: ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'struct']

dir(struct) # Returns: ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_clearcache', 'calcsize', 'error', 'iter_unpack', 'pack', 'pack_into', 'unpack', 'unpack_from']

class Example():
    def __dir__(self):
        return ["parameter_one", "parameter_two", "parameter_three"]
    
x = Example()
dir(x) # Returns: ["parameter_one", "parameter_two", "parameter_three"]