#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A rebellious integer class that inherits from int.
    The == and != operators are inverted.

    Usage:
    a = MyInt(5)
    b = MyInt(10)

    print(a == b)  # Outputs: False
    print(a != b)  # Outputs: True
    """

    def __eq__(self, other):
        """
        Overrides the == operator.
        Returns the inverse of the parent class's __eq__() method.

        Parameters:
        - other: The object to compare with.

        Returns:
        - True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        Returns the inverse of the parent class's __ne__() method.

        Parameters:
        - other: The object to compare with.

        Returns:
        - True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
