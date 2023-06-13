#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_new_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("Can't add new attribute")
