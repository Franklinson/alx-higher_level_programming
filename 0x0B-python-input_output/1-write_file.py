#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return f.write(text)
