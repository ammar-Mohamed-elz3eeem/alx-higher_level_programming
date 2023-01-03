#!/usr/bin/python3
import unittest

class Test_Max_integer(unittest.TestCase):        
    @classmethod
    def setUpClass(cls):
        cls.max_int = __import__("6-max_integer").max_integer
    
    def test_max_integer(self):
        self.assertEqual(type(self).max_int([1,2,3,4,5,4,3]), 5)
        self.assertEqual(type(self).max_int([1,2,3,4,5]), 5)
        self.assertEqual(type(self).max_int([]), None)
        self.assertEqual(type(self).max_int(), None)
        self.assertEqual(type(self).max_int("aa"), "a")
        # self.assertEqual(self.max_int(745), None)
        with self.assertRaises(TypeError):
            type(self).max_int(745)
        with self.assertRaises(TypeError):
            type(self).max_int([5,"44",7])
        with self.assertRaises(TypeError):
            type(self).max_int(5,7,7)
        with self.assertRaises(TypeError):
            type(self).max_int([True, True, []])
