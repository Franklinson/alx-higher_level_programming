#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings available attributes and methods of the object.
    """
    attributes = []
    methods = []

    for attr in dir(obj):
        if not attr.startswith("__"):
            value = getattr(obj, attr)
            if callable(value):
                methods.append(attr)
            else:
                attributes.append(attr)

    return attributes + methods
