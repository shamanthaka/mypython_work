import unittest

from day05.Circle import *
from math import pi

class TestCircle(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_radius_negative(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, "radidi")

