
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(3, 5), -2)
        self.assertEqual(sub(0, 0), 0)
    ##########################

    ######## Partner 1
    # def test_multiply(self):
    #     fill in code

    # def test_divide(self):
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 81), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    ##########################

    ######## Partner 1
    # def test_log_invalid_argument(self):
    #     fill in code

    # def test_hypotenuse(self):
    #     fill in code

    # def test_sqrt(self):
    #     fill in code
    ##########################

if __name__ == "__main__":
    unittest.main()
