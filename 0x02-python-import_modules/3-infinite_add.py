#!/usr/bin/python3
# print-addition_of_arguments

if __name__ == "__main__":
    """Print addition of arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
