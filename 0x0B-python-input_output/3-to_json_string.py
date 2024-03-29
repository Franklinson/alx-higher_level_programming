#!/usr/bin/python3
"""Defines a string-to-JSON function."""


import json


def to_json_string(my_obj):
    """
    Converts the given object to its JSON representation.

    Args:
        my_obj: The object to be converted.

    Returns:
        str: The JSON representation of the object.

    """
    return json.dumps(my_obj)
