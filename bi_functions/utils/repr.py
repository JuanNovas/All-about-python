class ExampleClass():
    pass

example_object = ExampleClass()

class ExampleClassWithRepr():
    def __repr__(self):
        return 'custom message'
    
    
example_object_with_repr = ExampleClassWithRepr()