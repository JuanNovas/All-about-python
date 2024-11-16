# -- isinstance(object, classinfo) --

# Returns True if the obj is an instance of the second argument
# Returns a BOOL
# Takes an OBJ and a Type or Tuple of types


isinstance(4, int) # Returns: True

isinstance('aaa', (int, float)) # Returns: False


# Example when rewriting the equal comparison in a custom object
    def __eq__(self, other: NameOfTheClass):
        if not isinstance(other, NameOfTheClass):
            raise TypeError
