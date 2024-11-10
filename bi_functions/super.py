# -- super([type[, object-or-type]]) --

# Returns a proxy object that delegates method calls to a parent or sibling class

class FatherClass():
    def __init__(self):
        # Logic
        pass
    
    
class ChildClass():
    def __init__(self):
        super().__init__() # Calls father class logic
        # Extra logic