# -- divmod(a, b) --

# Takes 2 non-complex numbers as arguments
# Returns a Tuple containing the quotient and the remainder
# Equivalent to doing (a // b, a % b) for integers


divmod(4, 2) # Returns: (2, 0)

divmod(7, 15) # Returns: (0, 7)

divmod(4.5, 2) # Returns: (2.0, 0.5)

divmod(5, 0) # Raises: ZeroDivisionError