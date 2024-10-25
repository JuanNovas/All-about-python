# Delets an atribute from an object
# Takes the OBJ and the atribute name as a STR
# Equivalent: delattr(x, 'foobar') == del x.foobar
# The difference is that delattr() deletes the atribute with the name as a STR

from utils.delattr import TestClass
obj = TestClass()
obj.atribute # Returns 'aaa'
delattr(obj, 'atribute')
# obj.atribute -> Raises atribute error