# -- open(file, mode='r', buffering=- 1, encodgin=None, errors=None, newline=None, closefd=True, opener=None) --

# opens a file and returns a file object
# file is the path of the file
# mode specifies the mode in which the file is opened:
#   r: reading
#   w: write from the start
#   x: creation, fails if already exists
#   a: write from the end
#   b: binary mode
#   t: text mode
#   +: reading and writing
# buffering controls the amount of data that is storaged temporary
# encoding is the name of the encoding used to decode/encode the file
# errors especify how the encoding and decoding errors are handle
# newline determines how to parse newline characters from the stream
# closefd specifies if the file will be closed after the use of the object
# opener specifies a custom opener method


with open('utils/open.txt', 'r') as file:
    data = file.read()
    print(data)