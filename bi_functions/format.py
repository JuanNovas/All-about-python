# Converts a value to a formated representation
# Takes a value and a format specification
# Format specification is written in 'Format Specification Mini-Langugae'


format(123.456789, ".2f") # Returns: 123.46

format(0.75, ".1%") # Returns: 75.0%

format("text", ">10") # Returns: '      text'