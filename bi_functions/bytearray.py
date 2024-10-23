# Takes an iterable of INTs between 0 and 255 or an INT that represents the lenght of the array
# Returns a mutable sequence of integers
# can take an 'encoding' parameter and an 'errors' parameter if 'encoding' is present.
# 'encoding':
#       'ascii', 'utf-8', 'utf-16', 'utf-32', 'latin-1', 'cp1252', 'shift_jis', 'euc_jp', 'euc_kr', 
#       'gb2312', 'big5', 'koi8-r', 'iso-8859-2', 'iso-8859-5', 'mac_roman', 'cp437', 'utf-7'
# 'errors':
#       'strict' (default value, do not allowed invalid values), 'ignore' (ignores the invalid values), 
#       'replace' (replace the invalid values for ?), 'backslashreplace' (replace the invalid values for a scape character)
#       'xmlcharrefreplace' (replace the invalid value by its reference in XML), 'namereplace' (replace the invalid value by its name in Unicode by \N{name})


bytearray([72, 101, 108, 108, 111]) # Returns bytearray(b'Hello')

bytearray(5) # Returns bytearray(b'\x00\x00\x00\x00\x00')

bytearray("Hello World", 'utf-8') # Returns bytearray(b'Hello World')

bytearray("Hello, smiley face: ☺", 'ascii', errors='replace') # Returns bytearray(b'Hello, smiley face: ?')