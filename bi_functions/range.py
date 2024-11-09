# -- range(stop) --
# -- range(start, stop[, step]) --

# Returns a range object
# Is an immutable secuence type


## for i in range examples:
for i in range(5):
    print(i) # Prints: 0\n 1\n 2\n 3\n 4\n
    
    
for i in range(1, 5):
    print(i) # Prints: 1\n 2\n 3\n 4\n
    
    
for i in range(1, 5, 2):
    print(i) # Prints: 1\n 3\n
 
    
for i in range(1, 5, -1):
    print(i) # Prints nothing
    
    
for i in range(1, -5, -1):
    print(i) # Prints: 1\n 0\n -1\n -2\n -3\n -4\n
    
    
## list creation examples:
example_list = list(range(1,11)) # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]