# -- mmemoryview(object) --

# Returns a memory view object created from the given argument


data = bytearray(b"Hello World")
view = memoryview(data)
view[0:5] = b"Goodb"
# data = b'Goodb World'