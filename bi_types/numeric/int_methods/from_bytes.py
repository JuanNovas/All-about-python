# -- int.from_bytes(bytes, byteorder, *, signed=False) --

# Returns the integer represented by the given array of bytes
# Byteorder defines the order. When 'big' the most significant byte is at the beginning, when 'little', the most significant byte is at the end


int.from_bytes(b'\x00\x10', byteorder='big') # Returns: 16

int.from_bytes(b'\x00\x10', byteorder='little') # Returns: 4096

int.from_bytes(b'\xfc\x00', byteorder='big', signed=True) # Returns: -1024

int.from_bytes(b'\xfc\x00', byteorder='big', signed=False) # Returns: 64512

int.from_bytes([255, 0, 0], byteorder='big') # Returns: 16711680