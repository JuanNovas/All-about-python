class EmptyObject:
    pass

class ObjectWithReprMethod:
    def __repr__(self):
        return "Example message"
    
class ObjectWithReprMethodNonAscii:
    def __repr__(self):
        return "Example message áéíóú"