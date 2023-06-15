#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    Represents a student.

    Public instance attributes:
    - first_name: The first name of the student.
    - last_name: The last name of the student.
    - age: The age of the student.

    Methods:
    - to_json(self, attrs=None): Retrieves a dictionary
    representation of the Student instance.

    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
        - first_name: The first name of the student.
        - last_name: The last name of the student.
        - age: The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
        - attrs: A list of attribute names (optional).

        Returns:
        - A dictionary representation of the Student instance.
        """

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}
