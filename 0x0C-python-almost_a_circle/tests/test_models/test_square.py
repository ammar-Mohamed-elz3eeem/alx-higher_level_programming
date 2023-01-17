#!/usr/bin/python3
from models.square import Square
import unittest
""" modile to create unittests for Square class """


class TestSquare(unittest.TestCase):
    """ TestSquare Class: test all fearures of Square class """
    
    @classmethod
    def setUpClass(cls):
        cls.sq1 = Square(12)
        cls.sq2 = Square(12, 4)
        cls.sq3 = Square(12, 0, 4)
        cls.sq4 = Square(12, 0, 4, 2051)
        Square.save_to_file([cls.sq1, cls.sq2, cls.sq3, cls.sq4])

    def test_empty_rect(self):
        with self.assertRaises(TypeError):
            rect1 = Square()

    def test_squares_area(self):
        self.assertEqual(self.sq1.area(), 144)
        self.assertEqual(self.sq2.area(), 144)
        self.assertEqual(self.sq3.area(), 144)
        self.assertEqual(self.sq4.area(), 144)

    def test_square1_attrs(self):
        self.assertEqual(self.sq1.id, 79)
        self.assertEqual(self.sq1.width, 12)
        self.assertEqual(self.sq1.x, 0)
        self.assertEqual(self.sq1.y, 0)

    def test_square2_attrs(self):
        self.assertEqual(self.sq2.id, 80)
        self.assertEqual(self.sq2.width, 12)
        self.assertEqual(self.sq2.x, 4)
        self.assertEqual(self.sq2.y, 0)

    def test_square3_attrs(self):
        self.assertEqual(self.sq3.id, 81)
        self.assertEqual(self.sq3.width, 12)
        self.assertEqual(self.sq3.x, 0)
        self.assertEqual(self.sq3.y, 4)

    def test_square4_attrs(self):
        self.assertEqual(self.sq4.id, 2051)
        self.assertEqual(self.sq4.width, 12)
        self.assertEqual(self.sq4.x, 0)
        self.assertEqual(self.sq4.y, 4)

    def test_square_str(self):
        self.assertRegex(str(self.sq1), r"\[Square\]\s\(79\)\s0\/0\s-\s12")

    def test_square_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5)
    def test_square_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)





