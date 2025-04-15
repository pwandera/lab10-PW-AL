import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0, 100), 0)
        self.assertEqual(mul(-1, -1), 1)
        self.assertAlmostEqual(mul(2.5, 2), 5)


    def test_divide(self): # 3 assertions
         with self.assertRaises(ValueError):
             div(0,1)

         self.assertEqual(div(10, -10), -100)
         self.assertAlmostEqual(div(2.5, 5), 2)


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion

        with self.assertRaises(ValueError):
            logarithm(0, -5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(-3,-4), 5)
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(0,5), 5)


    def test_sqrt(self): # 3 assertions

        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()