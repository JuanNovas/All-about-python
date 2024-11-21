# -- int.to_bytes(length, byteorder, *, signed=False) --

# Returns an array of bytes representing an integer

(1024).to_bytes(2, byteorder='big') # Returns: b'\x04\x00'

(1024).to_bytes(10, byteorder='big') # Returns: b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'