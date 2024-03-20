import unittest

from OOPCalculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_sum(self):
        x = 10
        y = 20

        calculator = Calculator(x, y, Calculator.OPERATORS['SUM'])

        self.assertEqual(calculator.calculate(), x + y)
