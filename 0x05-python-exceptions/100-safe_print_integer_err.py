#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Print integer with "{:d}".format().

    If ValueError message occurs, send a corresponding
    message to standard error.

    Args:
        value (int): integer to be printed.

    Returns:
        False - if TypeError or ValueError occurs.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
