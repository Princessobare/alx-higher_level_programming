#!/usr/bin/python3
"""It specifies the attribute of an object lookup function.

the lookup function takes an object argument and returns
a list of the object's attributes with the dir() function.

The dir() function returns a sorted list of strings
of all object's attributes names and methods.

"""


def lookup(obj):
    """Return a list of all object's attributes."""
    return (dir(obj))
