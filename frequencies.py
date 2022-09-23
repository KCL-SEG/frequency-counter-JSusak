"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Fill up the dictionary with initial values. If the value/string representation not in dict, add it and skip
    # subsequent values.
    for i in range(len(items)):
        if type(items[i]) != "str":
            items[i] = str(items[i])
    for val in items:
        if val not in frequencies or str(val) not in frequencies:
            frequencies[str(val)] = 0
    for(key) in frequencies:
        frequencies[key] += items.count(key)

    return frequencies
