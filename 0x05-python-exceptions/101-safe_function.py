#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """carries out safe execution of a function.

    Args:
        fct: function to be executed.
        args: fct arguments.

    Returns:
        None - If error occurs.
        Else - return result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
