# Returns an ascii printable representation of an object
# Takes an object as a parameter
# Calls the __repr__ method and scapes the non ascii caracters

string_value = "áéíóú"
ascii(string_value) # Returns '\\xe1\\xe9\\xed\\xf3\\xfa'

list_value = ["¿", "?", "¡", "!"]
ascii(list_value) # Returns  "['\\xbf', '?', '\\xa1', '!']"

## Obj
from utils.ascii import EmptyObject, ObjectWithReprMethod, ObjectWithReprMethodNonAscii

empty_obj_value = EmptyObject()
ascii(empty_obj_value) # Returns "<utils.ascii.EmptyObject object at 0x0000000000000000>"

with_repr_obj_value = ObjectWithReprMethod()
ascii(with_repr_obj_value) # Returns "Example message"

with_repr_and_no_ascii_obj_value = ObjectWithReprMethodNonAscii()
ascii(with_repr_and_no_ascii_obj_value) # Returns "Example message \xe1\xe9\xed\xf3\xfa"