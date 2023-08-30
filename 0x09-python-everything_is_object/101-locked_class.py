#!/usr/bin/python3
"""Defines a locked class with no class or object attribute."""


class LockedClass:
    """
    Prevents user from dynamically creating new instance attributes,
    except the new instance attribute is called'first_name'.
    """

    __slots__ = ["first_name"]
