import unittest

from day5.Circle_1 import circle_area
from day5.Circle_1 import *
from math import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):

        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_values(self):

        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):


     self.assertRaises(TypeError, circle_area, "radidi")



