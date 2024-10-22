# Takes an INT or an OBJ with __index__ method declared
# Returns a STR with a prefix "0b" and the number in binary

bin(10) # Returns '0b1010'

bin(-5) # Returns '-0b101'

bin(4.5) # Raises Type Error