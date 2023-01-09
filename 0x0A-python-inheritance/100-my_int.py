#!/usr/bin/python3
""" module that contains MyInt class """


class MyInt(int):
    """ 
    MyInt: inherits from int class and 
    invert the operations of equality and enequlaity operators 
    """
    
    def __eq__(self, other):
        return not super().__eq__(other)
    
    def __ne__(self, other):
        return not super().__ne__(other)