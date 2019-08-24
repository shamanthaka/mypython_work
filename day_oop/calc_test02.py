import unittest
from day_oop.Calculator import *

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        cal = Calculator(5,-9)
        self.assertAlmostEqual(cal.add(),-4)

    def test_multi(self):
        cal = Calculator(6,7)
        self.assertAlmostEqual(cal.multiplication(),42)
