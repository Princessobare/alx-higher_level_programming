#!/usr/bin/python3
"""Defines a BaseGeometry class that raises exception."""


class BaseGeometry:
    """class of basegeometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
