#!/usr/bin/python3
"""Defines a function for reading a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
