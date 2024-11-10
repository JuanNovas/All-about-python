# Any object can be tested for truth value, for use in an if or while condition
# An object is considered True unless a __bool__() method is defined and returns False or a __len__() method that returns zero

# Built-in objects considered False:

## constants defined to be false: None and False.
## zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
## empty sequences and collections: '', (), [], {}, set(), range(0)