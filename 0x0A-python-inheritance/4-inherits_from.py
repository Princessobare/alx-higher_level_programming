#!/usr/bin/python3
"""Specifies function checking inherited class."""


def inherits_from(obj, a_class):
    """Checks whether object is an instance of inherited class.

    Args:
        obj (any): Object to be checked.
        a_class (type): Inherited class.
    Returns:
        If object is an instance of inherited class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
