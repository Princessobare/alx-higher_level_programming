#!/usr/bin/python3
"""Specifies a Square as a subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square from rectangle."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): new square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

