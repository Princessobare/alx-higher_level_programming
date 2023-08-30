#!/usr/bin/python3
"""Defines a class MyList inherited from List."""


class MyList(list):
    """Implements printing for built-in list class in sorted order."""

    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
