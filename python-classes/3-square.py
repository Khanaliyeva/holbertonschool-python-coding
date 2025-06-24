#!/usr/bin/python3
"""
This module defines a Square class with a private size,
a public area method, and getter/setter for size with validation.
"""


class Square:
    """
    A class that defines a square by its private size attribute.

    Attributes:
        __size (int): size of the square (private)

    Methods:
        area(): Returns the current square area.
        size(): Getter for size.
        size(value): Setter for size with validation.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """
        Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
