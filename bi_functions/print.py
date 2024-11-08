# -- print(*objects, sep=' ', end='\n', file=none, flush=False) --

# Prints objects to the text stream file, separated by sep and followed by end
# File must be an object with a write(string) method
# If flush is True forces the output to appear immediatly on the screen

print('Hello world') # Prints: Hello world

print(1,2,3,4,5) # Prints: 1 2 3 4 5

print(1,2,3,4,5, sep=', ') # Prints: 1, 2, 3, 4, 5