#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
""" modile to create unittests for Rectangle class """


class TestRectangle(unittest.TestCase):
    """ TestRectangle Class: test all fearures of Rectangle class """

    @classmethod
    def setUpClass(cls):
        cls.rect2 = Rectangle(25, 35, 15, 20, 1205)
        cls.rect3 = Rectangle(12, 12, 12, 12)

    def test_empty_rect(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle()

    def test_rect_area(self):
        rect1 = Rectangle(5, 5)
        self.assertEqual(rect1.area(), 25)
        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, 5)

    def test_rect_display(self):
        rect1 = Rectangle(1, 1)
        self.assertIsNone(rect1.display(), "Printed")

    def test_rect_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 1)

    def test_rect_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -1)

    def test_rect_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_rect_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_rect_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("0", 1)

    def test_rect_string_height(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "0")

    def test_rect_xy_pos(self):
        rect1 = Rectangle(5, 5)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

    def test_rect_negative_xpos(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(2, 5, -2, 5)

    def test_rect_negative_ypos(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(2, 5, 2, -5)

    def test_rect_string_xpos(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(2, 5, "3", 4)

    def test_rect_string_ypos(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(2, 5, 3, "4")

    def test_rect_width_setter(self):
        rect1 = Rectangle(5, 5)
        rect1.width = 20
        self.assertEqual(rect1.width, 20)

    def test_rect_height_setter(self):
        rect1 = Rectangle(5, 5)
        rect1.height = 25
        self.assertEqual(rect1.height, 25)

    def test_rect_zero_width_setter(self):
        rect1 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            rect1.width = 0

    def test_rect_zero_height_setter(self):
        rect1 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            rect1.height = 0

    def test_rect_string_width_setter(self):
        rect1 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            rect1.width = "20"

    def test_rect_string_height_setter(self):
        rect1 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            rect1.height = "20"

    def test_rect_negative_xpos_setter(self):
        rect1 = Rectangle(2, 5, 2, 5)
        with self.assertRaises(ValueError):
            rect1.x = -2

    def test_rect_negative_ypos_setter(self):
        rect1 = Rectangle(2, 5, 2, 5)
        with self.assertRaises(ValueError):
            rect1.y = -5

    def test_rect_string_xpos_setter(self):
        rect1 = Rectangle(2, 5, 3, 4)
        with self.assertRaises(TypeError):
            rect1.x = "3"

    def test_rect_string_ypos_setter(self):
        rect1 = Rectangle(2, 5, 3, 4)
        with self.assertRaises(TypeError):
            rect1.y = "4"

    def test_rect_width_getter(self):
        self.assertEqual(type(self).rect2.width, 25)

    def test_rect_height_getter(self):
        self.assertEqual(type(self).rect2.height, 35)

    def test_rect_xpos_getter(self):
        self.assertEqual(type(self).rect2.x, 15)

    def test_rect_ypos_getter(self):
        self.assertEqual(type(self).rect2.y, 20)

    def test_rect_id_getter(self):
        self.assertEqual(type(self).rect2.id, 1205)

    def test_rect_auto_id_getter(self):
        self.assertEqual(type(self).rect3.id, 4)

    def test_rect2_area(self):
        self.assertEqual(type(self).rect2.area(), 875)

    def test_rect2_magic_str(self):
        self.assertRegex(type(self).rect2.__str__(), r"\[[A-Za-z]+\]\s\([0-9]+\)(\s[0-9]+\/[0-9]+)+")

    def test_rect_kw_update(self):
        rect = Rectangle(4, 5)
        rect.update(x=22, y=11, width=11, id=5, height=10)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.width, 11)
        self.assertEqual(rect.x, 22)
        self.assertEqual(rect.y, 11)

    def test_rect_kw_update_width(self):
        rect = Rectangle(4, 5)
        rect.update(width=8)
        self.assertEqual(rect.width, 8)

    def test_rect_kw_update_negative_width(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(width=-5)

    def test_rect_kw_update_zero_width(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(width=0)

    def test_rect_kw_update_string_width(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(width="5")

    def test_rect_kw_update_height(self):
        rect = Rectangle(4, 5)
        rect.update(height=8)
        self.assertEqual(rect.height, 8)

    def test_rect_kw_update_negative_height(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(height=-5)

    def test_rect_kw_update_zero_height(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(height=0)

    def test_rect_kw_update_string_height(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(height="5")

    def test_rect_kw_update_x(self):
        rect = Rectangle(4, 5)
        rect.update(x=8)
        self.assertEqual(rect.x, 8)

    def test_rect_kw_update_negative_x(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(x=-5)

    def test_rect_kw_update_zero_x(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.x, 0)

    def test_rect_kw_update_string_x(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(x="5")

    def test_rect_kw_update_y(self):
        rect = Rectangle(4, 5)
        rect.update(y=8)
        self.assertEqual(rect.y, 8)

    def test_rect_kw_update_negative_y(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(y=-5)

    def test_rect_kw_update_zero_y(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.y, 0)

    def test_rect_kw_update_string_y(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(y="5")

    def test_rect_kw_update_id(self):
        rect = Rectangle(4, 5)
        rect.update(id=512)
        self.assertEqual(rect.id, 512)

    def test_rect_kw_update_negative_id(self):
        rect = Rectangle(4, 5)
        rect.update(id=-5)
        self.assertEqual(rect.id, -5)

    def test_rect_kw_update_zero_id(self):
        rect = Rectangle(4, 5)
        rect.update(id=0)
        self.assertEqual(rect.id, 0)

    def test_rect_kw_update_string_id(self):
        rect = Rectangle(4, 5)
        rect.update(id="-5")
        self.assertEqual(rect.id, "-5")

    def test_rect_no_kw_update(self):
        rect = Rectangle(4, 5)
        rect.update(22, 11, 11, 5, 10)
        self.assertEqual(rect.id, 22)
        self.assertEqual(rect.height, 11)
        self.assertEqual(rect.width, 11)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)

    def test_rect_no_kw_update_width(self):
        rect = Rectangle(4, 5)
        rect.update(0, 8)
        self.assertEqual(rect.width, 8)

    def test_rect_no_kw_update_negative_width(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(0, -5)

    def test_rect_no_kw_update_zero_width(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(0, 0)

    def test_rect_no_kw_update_string_width(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(0, "5")

    def test_rect_no_kw_update_height(self):
        rect = Rectangle(4, 5)
        rect.update(0, 1, 8)
        self.assertEqual(rect.height, 8)

    def test_rect_no_kw_update_negative_height(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(0, 1, -5)

    def test_rect_no_kw_update_zero_height(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(0, 1, 0)

    def test_rect_no_kw_update_string_height(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(0, 1, "5")

    def test_rect_no_kw_update_x(self):
        rect = Rectangle(4, 5)
        rect.update(0, 1, 8, 8)
        self.assertEqual(rect.x, 8)

    def test_rect_no_kw_update_negative_x(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(0, 1, 8, -5)

    def test_rect_no_kw_update_zero_x(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.x, 0)

    def test_rect_no_kw_update_string_x(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(0, 1, 8, "5")

    def test_rect_no_kw_update_y(self):
        rect = Rectangle(4, 5)
        rect.update(0, 1, 8, 8, 8)
        self.assertEqual(rect.y, 8)

    def test_rect_no_kw_update_negative_y(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.update(0, 1, 8, 8, -5)

    def test_rect_no_kw_update_zero_y(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.y, 0)

    def test_rect_no_kw_update_string_y(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.update(0, 1, 8, 8, "5")

    def test_rect_no_kw_update_id(self):
        rect = Rectangle(4, 5)
        rect.update(512)
        self.assertEqual(rect.id, 512)

    def test_rect_no_kw_update_negative_id(self):
        rect = Rectangle(4, 5)
        rect.update(-5)
        self.assertEqual(rect.id, -5)

    def test_rect_no_kw_update_zero_id(self):
        rect = Rectangle(4, 5)
        rect.update(0)
        self.assertEqual(rect.id, 0)

    def test_rect_no_kw_update_string_id(self):
        rect = Rectangle(4, 5)
        rect.update("-5")
        self.assertEqual(rect.id, "-5")

    def test_rect_nokw_and_kw_update(self):
        rect = Rectangle(4, 5)
        rect.update(22, 11, y=11, height=5, x=10)
        self.assertEqual(rect.id, 22)
        self.assertEqual(rect.width, 11)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    @classmethod
    def tearDownClass(cls):
        del cls.rect2
