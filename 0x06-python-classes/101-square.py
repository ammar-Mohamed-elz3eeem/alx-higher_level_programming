#!/usr/bin/python3
"""
Define Square Class with private attribute size
with some verfications that size attribute is correct
"""


class Square:
    """ Square Class is used to create
    squares with size == self.size """

    def __init__(self, s=0, position=(0, 0)):
        self.size = s
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """position: get the position of the square"""
        return self.__position

    @position.setter
    def position(self, new_pos):
        """position: set the position of the square"""
        if (not isinstance(new_pos, tuple) or
                len(new_pos) != 2 or
                not all(num >= 0 for num in new_pos) or
                not all(isinstance(num, int) for num in new_pos)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = new_pos

    def area(self):
        """Function to get area of Square object"""
        return (self.__size * self.__size)

    def my_print(self):
        """my_print: prints the square into console"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")

    def __str__(self):
        newstr = ""
        if self.__size == 0:
            return newstr

        for i in range(0, self.__position[1]):
            newstr += "\n"
        for j in range(0, self.__size):
            for k in range(0, self.__position[0]):
                newstr += " "
            for i in range(0, self.__size):
                newstr += "#"
            if j != self.__size - 1:
                newstr += "\n"
        return newstr
