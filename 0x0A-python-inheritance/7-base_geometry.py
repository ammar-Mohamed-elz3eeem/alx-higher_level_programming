#!/usr/bin/python3
"""
BaseGeometry module: class BaseGeometry implementation
"""


class BaseGeometry:
    """
    BaseGeometry Class: class with non implemented function area,
    function integer_validator that validate if value is not int
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is integer

		Args:
			name (str): the name of the parameter
			value (int): the value of the parameter

		Raises:
			TypeError: if value is not integer
			ValueError: if value <= 0
		"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
