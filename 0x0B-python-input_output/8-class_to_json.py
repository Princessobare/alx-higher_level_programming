#!/usr/bin/python3
"""Defines a Python class-to-JSON function which
returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    return obj.__dict__
