# Returns a BOOL representing if the OBJ has the atribute
# Takes an OBJ and the name of an atribute as a STR

from utils.hasattr import obj

hasattr(obj, "test_attribute") # Returns: True

hasattr(obj, "invalid_attribute") # Returns: False