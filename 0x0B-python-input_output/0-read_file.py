#!/usr/bin/python3
"""Defines a function for text file-reading."""


def read_file(filename=""):
    """Prints content of UTF8 text file to standard output."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
