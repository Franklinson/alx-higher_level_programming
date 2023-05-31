#!/usr/bin/python3

"""Define a class called magic class"""


import math


class MagicClass:

    """A class that calculates the area and circumference of a circle."""

    def __init__(self, radius):
        """
        Initializes a MagicClass instance with the given radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
