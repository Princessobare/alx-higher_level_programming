#!/usr/bin/python3
# remove_c_and_C_from_string

def no_c(my_string):
    """Remove characters c and C from string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
