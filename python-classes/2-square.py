#!/usr/bin/python3
"""
This module defines a Square class with size validation
and a method to compute the area of the square.
"""


class Square:
    """
    A class that defines a square by its private size attribute.

    Attributes:
        __size (int): size of the square (private)

    Methods:
        area(): Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
