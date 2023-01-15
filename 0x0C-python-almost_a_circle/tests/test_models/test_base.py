#!/usr/bin/python3
from models.base import Base
import unittest
""" modile to create unittests for Base class """


class TestBase(unittest.TestCase):
    """ TestBase Class: test all fearures of Base class """
    
    @classmethod
    def setUpClass(cls):
        print("Setup")
        
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_base_with_id(self):
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
        
    def test_base_with_None(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 3)
    
    def test_base_with_negative(self):
        b1 = Base(-2)
        self.assertEqual(b1.id, -2)
        
    def test_base_with_string(self):
        b1 = Base("4")
        self.assertEqual(b1.id, "4")

    @classmethod
    def tearDownClass(cls):
        print("TearDown")

if __name__ == "__main__":
    unittest.main()