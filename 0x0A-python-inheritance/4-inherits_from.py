#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
        Checks if an object is an inherited instance of a class.
    Args:
        obj: An object to be checked.
        a_class: A class to compare inheritance against.

    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False
        """

    inherited_classes = set(type(obj).__bases__)

    if a_class in inherited_classes:
        return True

    for inherited_class in inherited_classes:
        if inherits_from(inherited_class, a_class):
            return True

    return False
