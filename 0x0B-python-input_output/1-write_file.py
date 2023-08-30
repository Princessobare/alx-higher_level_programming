#!/usr/bin/python3
"""Defines a function for file-writing."""


def write_file(filename="", text=""):
    """Writes string to UTF8 text file.

    Args:
        filename (str): name of file to be written on.
        text (str): text to be written to file.
    Returns:
        Total number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
