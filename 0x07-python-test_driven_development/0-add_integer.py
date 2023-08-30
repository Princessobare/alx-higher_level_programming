#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function for adding integer."""


def add_integer(a, b=98):
    """Returns the sum of a and b integer.

    Typecast float arguments to ints before addition.

    Raise:
        TypeError: If a or b is not an integer and a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
