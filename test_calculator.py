import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions #fill in code
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(5, 7), 12)

    def test_subtract(self): # 3 assertions #fill in code
        self.assertEqual(subtract(10,8), 2)
        self.assertEqual(subtract(3, 4), -1)
        self.assertEqual(subtract(10, 5), 5)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions #fill in code
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2)

    def test_log_invalid_base(self): # 1 assertion
         # use same technique from test_divide_by_zero #fill in code
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()