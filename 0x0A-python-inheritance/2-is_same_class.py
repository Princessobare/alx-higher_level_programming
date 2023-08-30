#!/usr/bin/python3
"""specifies a function checking class."""


def is_same_class(obj, a_class):
    """Checks whether object is same as given class.

    Args:
        obj (any): Object to be checked.
        a_class (type): Given  class.
    Returns:
        If obj is same as a_class - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
