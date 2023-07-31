#!/usr/bin/python3


def safe_print_integer(value):
    """Prints integer with "{:d}".

    Args:
        value (int): integer to be printed.

    Returns:
        False - If there is a TypeError or ValueError.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
