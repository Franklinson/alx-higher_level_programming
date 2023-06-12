#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited instance of a class.
    Args:
        obj: The object to be checked.
        a_class: The class to be checked against.

    Returns:
    If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
        """
    return isinstance(obj, a_class)
