# Returns True if the class is a subclass of he second parameter
# Returns a BOOL
# Takes an Class and a Class or Tuple of Classes

class FatherClass():
    pass

class ChildClass(FatherClass):
    pass

class GrandsonClass(ChildClass):
    pass

issubclass(ChildClass, FatherClass) # Returns: True

issubclass(FatherClass, ChildClass) # Returns: False

issubclass(GrandsonClass, FatherClass) # Returns: True

issubclass(FatherClass, FatherClass) # Returns: True