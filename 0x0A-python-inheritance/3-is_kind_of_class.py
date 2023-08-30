#!/usr/bin/python3
"""specifies instance of a class or a class that inherited
from a specified class.
"""

def is_kind_of_class(obj, a_class):
    """Check whether object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): specified class.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
