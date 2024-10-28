# Creates a FLOAT obj from a NUMBER or a STR
# If no argument is given, returns 0.0

float('+1.23') # Returns: 1.23

float('   -12345\n') # Returns: -12345.0

float('1e-003') # Returns: 0.001

float('+1E6') # Returns: 1000000.0

float('-Infinity') # Returns: -inf