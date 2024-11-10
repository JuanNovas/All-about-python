# -- __import__(name, globals=None, locals=None, fromlist=(), level=0) --

# Allows to import modules dinamically by its string name


math_module = __import__('math')
math_module.sqrt(16) # Returns: 4.0