#!/usr/bin/python3
"""Defines function string-to-JSON."""
import json


def to_json_string(my_obj):
    """Returns a string object's JSON representation."""
    return json.dumps(my_obj)
