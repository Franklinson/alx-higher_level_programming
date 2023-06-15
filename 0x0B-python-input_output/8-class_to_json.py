#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Converts an instance of a class into a dictionary representation

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object.
    """
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj

    # If obj is an instance of a class, convert its attributes to a dictionary
    if hasattr(obj, '__dict__'):
        attributes = {}
        for attr_name, attr_value in obj.__dict__.items():
            attributes[attr_name] = class_to_json(attr_value)
        return attributes

    # If obj is not a recognized data structure, return None
    return None
