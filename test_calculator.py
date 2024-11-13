import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add1(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
    
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-5, -2), 10)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(4, -2), -8)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(-3, -3), 1)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(8, -4), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(-8, 3), 1)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(-4, -3), -1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()