# Executes code given as a STR
# Also accepts 'globals' and 'locals' parameter to especify the scope the expression is capable to access
# Accepts multi line scripts

x = 1
code = """
for i in range(3):
    x += 1
print(x)
"""
exec(code) # Prints: 4
# Variable x is modified