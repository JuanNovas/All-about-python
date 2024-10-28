# Returns the value of an atribute of an OBJ
# Takes the OBJ, the name of the atribute and an optional default value
# If no default value is given and the atribute does not exist AttributeError is raised


from utils.getattr import obj

getattr(obj, "test_attribute") # Returns: 'aaa'

getattr(obj, "invalid_attribute", "bbb") # Returns: 'bbb'

getattr(obj, "invalid_attribute") # Raises: AttributeError