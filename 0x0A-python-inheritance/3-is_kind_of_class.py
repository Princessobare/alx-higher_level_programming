#!/usr/bin/python3
"""Defines a class and inherited class-checking function.

This specifies is_kind_of_class function that checks whether an object
is an instance or inherited instance of a_class.

The isinstance() function is used to determine this.
If obj is an instance or inherited instance of a_class, it returns True.
Else, it returns False.

"""


def is_kind_of_class(obj, a_class):
    """Checks object for instance or inherited instance of class.

    Args:
        obj (any): object to be checked.
        a_class (type): given class.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
