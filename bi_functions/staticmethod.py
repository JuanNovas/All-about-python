# -- @staticmethod --

# Transform a method into a static method
# An static method does not receive an implicit first argument

class ExampleClass():
    @staticmethod
    def method_with_no_implicit_argument():
        pass