#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints a list's x elememts.

    Args:
        my_list (list): This is the list the elements would be printed from.
        x (int): The amount of elements of my_list to be printed.

    Returns:
        Total amount of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
