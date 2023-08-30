#!/usr/bin/python3
# 4-print_square.py
"""Defines a function that prints square with # character."""


def print_square(size):
    """Prints square with # character.

    Args:
        size (int): The width and height of square.
    Raise:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
