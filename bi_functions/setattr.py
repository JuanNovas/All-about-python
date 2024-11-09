# -- setattr(OBJ, name, value) --

# Creates or modifies an attribute from the OBJ
# name is the name of the attribute
# value is the new value for the attribute


class Example():
    def __init__(self):
        self.x = 'init value'
example_object = Example()

example_object.x # Returns: 'init value'

setattr(example_object, 'x', 'setattr value')
setattr(example_object, 'b', 'new value')

example_object.x # Returns: 'setattr value'
example_object.b # Returns: 'new value'