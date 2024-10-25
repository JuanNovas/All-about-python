# Creates a DICT obj
# Takes as a parameter a mapping object, an iterable that retrieves 2 items in each iteration or keyword arguments


data = {
    "first_key": "first_value",
    "second_key": "second_value"
}
new_dict = dict(data)


data = [("first_key", "first_value"), ("second_key", "second_value")]
new_dict = dict(data)


new_dict = dict(first_key="first_value", second_key="second_value")


# All return: {'first_key': 'first_value', 'second_key': 'second_value'}