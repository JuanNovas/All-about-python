# -- int([x]) --
# -- int(x, base=10) --

# Creates an INT OBJ
# Takes a NUMBER, STR or OBJ with the methods: __int__, __index__ or __trunc__
# Also a custom parameter base that represents the base of the INT


int(6) # Returns: 6

int('10') # Returns: 10

int('ten') # Raise: ValueError