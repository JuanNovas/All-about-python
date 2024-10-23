# Takes an INT between 0 and 1,114,111
# Returns the respective UNICODE character as a STR
# Raises ValueError if the INT is out of range
# The inverse of ord()

chr(1) # Returns '\x01'

chr(100) # Returns 'd'

chr(120) # Returns 'x'

chr(200) # Returns 'È'

chr(994) # Returns 'Ϣ'

chr(1200) # Returns 'Ұ'

chr(3000) # Returns 'ஸ'

chr(30000) # Returns '田'