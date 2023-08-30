#!/usr/bin/python3
"""Defines a function for inserting a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filename (str): the file name.
        search_string (str): The string to be searched for.
        new_string (str): The string to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
