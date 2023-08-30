#!/usr/bin/python3
"""Specifies a square as subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square from Class rectangle."""

    def __init__(self, size):
        """creates new square.

        Args:
            size (int): new square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

