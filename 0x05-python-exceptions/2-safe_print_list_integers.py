#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints first x integer elements of a list.

    Args:
        my_list (list): list elements are to be printed from.
        x (int): amount of elements of my_list to be printed.

    Returns:
        Total amount of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
