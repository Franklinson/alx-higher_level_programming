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

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
