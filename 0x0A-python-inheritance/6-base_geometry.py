#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    Base class for geometry.

    Attributes:
        None
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Indicates that the area() method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
