# Takes and objects as an argument.
# Returns True if the object is callable.
# Instances of classes are callable if their have a __call__() method.

from utils.callable import example_function
callable(example_function) # Returns True


from utils.callable import example_class
callable(example_class) # Returns True

example_object = example_class()
callable(example_object) # Returns False

from utils.callable import example_class_with_call
callable(example_class_with_call) # Returns True

example_object_with_call = example_class_with_call
callable(example_object_with_call) # Returns True