# -- type(object) --
# -- type(name, bases, dict, **kwds) --

# With one argumet, return the type of the object
# With three arguments, return a new type object
# name is the name of the class name
# bases is a tuple containing the base clases
# dict contains attribute and method definitions


type('hello world') # Returns: str

type(43) # Returns: int


type('ClassName', (), dict(example_attribute='hello world')) # Returns a new object


example_object = type('ClassName', (), dict(example_attribute='hello world'))
type(example_object) # Returns: type