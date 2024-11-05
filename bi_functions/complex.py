# -- complex([real[, imag]]) --

# Converts a single string to a complex number or creates a complex number from real and imaginary parts

complex('+1.23') # Returns (1.23+0j)

complex('-4.5j') # Returns -4.5j

complex('-1.23+4.5j') # Returns (-1.23+4.5j)

complex('\t( -1.23+4.5J )\n') # Returns (-1.23+4.5j)

complex('-Infinity+NaNj') # Returns (-inf+nanj)

complex(1.23) # Returns (1.23+0j)

complex(imag=-4.5) # Returns -4.5j

complex(-1.23, 4.5) # Returns (-1.23+4.5j)