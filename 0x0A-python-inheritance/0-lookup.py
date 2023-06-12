#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings available attributes and methods of the object.
    """
    retun(dir(obj))
