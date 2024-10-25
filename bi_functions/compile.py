# Takes source code in STR, BYTE STR or AST obj and compiles it into a Code object that can be executed with exec() or eval()
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=1)
# filename: file to read from or '<string>' if source is a string
# mode: 'exec' if source code is a sequence of statements or if is a single expresion 'single' will print the output and 'eval' will return the output 
# flag: allows to specify advanced compile configurations
# dont_inherit: controls wheter the compiler inherit any flags and settings from the module where compile() is called
# optimize: sets the optimization level of the compiled code, where 0 is no optimization, 1 removes assert statements, and 2 removes both assert statements and docstrings.


result = None
code = "x = 5\ny = 10\nresult = x + y"
compile_code = compile(code, '<string>', 'exec')
exec(compile_code)
print(result) # Prints 15