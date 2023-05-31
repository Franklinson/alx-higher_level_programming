#!/usr/bin/python3

"""Defines a class called square"""


class Square:

    """ A class that defines a square."""

    def __init__(self, size):
        """Initializes a new Square object with the given size."""
    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        return f"Square with size: {self.__size}"

    def get_size(self):
        """
        Returns the size of the square.
        """
        return self.__size

    def set_size(self, size):
        """
        Sets the size of the square to the given value.
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size * self.__size
