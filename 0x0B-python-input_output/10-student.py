#!/usr/bin/python3
"""Defines a class Student by first name, last name etc."""


class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Defines dictionary representation of the Student.

        If attribute is a list of strings, represents attributes
        exclusively in the list.

        Args:
            attrs (list): (Optional) represented attributes.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
