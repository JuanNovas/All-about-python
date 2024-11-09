# -- reversed(seq) --

# Returns a reversed iterator
# Seq must be an object with a __reversed__() method
# Or support the sequence protocol (the __len__() and __getitem__() methods)


numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num) # Prints: 5\n 4\n 3\n 2\n 1\n