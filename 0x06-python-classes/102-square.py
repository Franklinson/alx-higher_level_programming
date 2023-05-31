#!/usr/bin/python3

"""Define a calss called square"""


class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int or float): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if the area of this square is equal
        to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the area of
        this square is not equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the area of this
        square is greater than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is
            greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of this
        square is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the area of this
        square is less than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of this square
        is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
