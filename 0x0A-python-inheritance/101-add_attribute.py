#!/usr/bin/python3
"""Specifies a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds new attribute to object where possible.

    Args:
        obj (any): object to be added an attribute.
        att (str): attribute name.
        value (any): attribute value.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

