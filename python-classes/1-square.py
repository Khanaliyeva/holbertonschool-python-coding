#!/usr/bin/python3
"""
This module defines a Square class with private size attribute,
including validation on initialization.
"""


class Square:
    """
    A class that defines a square by its private size attribute.

    Attributes:
        __size (int): size of the square (private)

    Instantiation with optional size (default 0).
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
