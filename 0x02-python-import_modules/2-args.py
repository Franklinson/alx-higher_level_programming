#!/usr/bin/python3

import sys


def print_arguments(argv):
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        plural = "s" if num_arguments > 1 else ""
        print(f"{num_arguments} argument{plural}:")

        for i, arg in enumerate(argv):
            print(f"{i+1}: {arg}")


if __name__ == "__main__":

    print_arguments(sys.argv[1:])
