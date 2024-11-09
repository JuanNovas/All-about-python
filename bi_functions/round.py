# -- round(number[, ndigits]) --

# Return number rounded to ndigits precision after the decimal point
# If ndigits is omitted or is None, it returns the nearest integer
# If two multiples are equally close, rounding is done toward the even one

round(1.5) # Returns: 2

round(2.5) # Returns: 2

round(3.7) # Returns: 4

round(9.789231, 4) # Returns: 9.7892

round(9.789271, 4) # Returns: 9.7893

round(9.789271, 0) # Returns: 10.0