import unittest
from unittest.mock import patch #allows us to mock an object during a test. Can be used as a context manager or decorator
from test_employees import Employee
import requests

class TestEmployee(unittest.TestCase):

    ''' setUp method in python unittests runs code before every single test  '''
    def setUp(self):
        print('setUp')
        self.self.emp_1 = Employee('Tolu','A', 60000)
        self.self.emp_2 = Employee('Brandi', 'B', 70000)

    ''' tearDown method in python testing runs code after every single test'''
    def tearDown(self):
        print('tearDown')
        pass

    def test_email(self):
        print('test email')
        self.assertEqual(self.emp_1.email, 'Tolu.A@gmail.com')
        self.assertEqual(self.emp_2.email, 'Brandi.B@gmail.com')

        self.emp_1.first = 'Tom'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Tom.A@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.B@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.email, 'Tolu A')
        self.assertEqual(self.emp_2.email, 'Brandi B')

        self.emp_1.first = 'Tom'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Tom A')
        self.assertEqual(self.emp_2.email, 'Jane B')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    ''' Working with MockUps example for requests '''
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            ''' This basically says that when we use requests.get in our employee module, it is going to be mocked with the mocked_get'''
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            # Set our value.
            schedule = self.emp_1.monthly_schedule('April')
            # Perform our check to make sure the mocked_get went to the correct url
            mocked_get.assert_called_with('http://somehting.com/Tolu/April')
            ''' run our test '''
            self.assertEqual(schedule, 'Success')

            ''' Test failures examples '''
            mocked_get.return_value.ok = False

            # Set our value.
            schedule = self.emp_1.monthly_schedule('June')
            # Perform our check to make sure the mocked_get went to the correct url
            mocked_get.assert_called_with('http://somehting.com/Tolu/June')
            ''' run our test '''
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()