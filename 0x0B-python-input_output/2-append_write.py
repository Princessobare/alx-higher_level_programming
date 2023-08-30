#!/usr/bin/python3
"""Defines a function for appending a file."""


def append_write(filename="", text=""):
    """Appends string to UTF8 text file end.

    Args:
        filename (str): name of file to be appended to.
        text (str): string to be appended.
    Returns:
        Total number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
