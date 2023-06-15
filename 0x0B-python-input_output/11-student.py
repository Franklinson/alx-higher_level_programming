#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    A class that represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attributes to retrieve.
                If None, retrieves all attributes.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based
        on the provided dictionary.

        Args:
            json (dict): Dictionary representing the attributes of the
            Student instance.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
