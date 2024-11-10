# -- zip(*iterable, strict=False) --

# Returns an iterator of tuples containing one element of each iterable in order
# If one iterable is shorten than the rest zip will stop at the end of it
# But if strict is set to True, zip will raise a ValueError

for item in zip([1,2,3], ['sugar', 'spice', 'everything nice']):
    print(item)
# Will print:
# (1, 'sugar')
# (2, 'spice')
# (3, 'everything nice')

for item in zip([1,2,3,4], ['sugar', 'spice', 'everything nice']): # Number added
    print(item)
# Will print the same as before:
# (1, 'sugar')
# (2, 'spice')
# (3, 'everything nice')


for item in zip([1,2,3,4], ['sugar', 'spice', 'everything nice'], strict=True):
    print(item)
# Will raise ValueError