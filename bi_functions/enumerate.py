# -- enumerate(iterable, start=0) --

# Returns an enumeate object
# Takes an iterable and an optional start number
# Enumerate obj __next__ method returns a tuple containing the count and the value

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

list(enumerate(seasons)) # Returns: [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(enumerate(seasons, start=1)) # Returns: [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# Normal use:

for i, season in enumerate(seasons):
    print(f'{season} is index {i}')
    
## Prints: 
    """
    Spring is index 0
    Summer is index 1
    Fall is index 2
    Winter is index 3
    """