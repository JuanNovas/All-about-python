# Waits for the user to type an input in the terminal and returns the value as a STR
# When EOF is read, EOFError is raised
# EOF in Windows is CTRL+Z, in Unix/Linux/MacOs is CTRL+D
# Takes an optional STR parameter that will be shown in the same line as the user will be writing the input


user_input = input() # Waits for the user and returns the user input


user_input = input('Write a value: ') # Waits for the user with the custom message before
# "It is normally used to leave a space at the end to separate the input from the custom message"

try:
    user_input = input("Waiting for a message, aware of the EOF: ")
except EOFError:
    print('Program exited')