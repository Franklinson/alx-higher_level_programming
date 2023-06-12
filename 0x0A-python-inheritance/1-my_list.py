#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A subclass of list that provides a method to print the list in sorted order
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
