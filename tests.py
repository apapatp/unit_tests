import calc
import unittest # import unit test module to run our tests

class Test(unittest.TestCase):
    ''' Tests have to start with test_'''
    def test_add(self):
        result = calc.add(10, 5)
        # Run the test as below
        self.assertEqual(result,15)
        self.assertEqual(calc.add(-1, 1), 3) # Should return "F" due to failure

    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, 1), 3) # Should return "F" due to failure

    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 1), 3) # Should return "F" due to failure

    def test_divide(self):
        ''' Since we have an assertion, we can do type of error tests'''
        self.assertRaises(ValueError, calc.divide, 3, 0) # One way
        self.assertEqual(calc.divide(-1, 1), 3) # Should return "F" due to failure

        ''' Testing using context manager for assertion exceptions '''
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

""" Run this module directly, run the code in this conditional. allowing us to run from same directory"""
if __name__ == '__main__':
    unittest.main()