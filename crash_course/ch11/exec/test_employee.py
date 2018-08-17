
import unittest

from employee import Employee


class EmployeeTest(unittest.TestCase):
    """Test case for Employee class."""

    def setUp(self):
        """Make mock employee."""
        self.employee = Employee('David', 'Ding', 10000)

    def test_give_default_raise(self):
        """Test that default raise works properly."""
        self.employee.give_raise()
        self.assertEqual(15000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        """Test that customized raise works properly."""
        self.employee.give_raise(100)
        self.assertEqual(10100, self.employee.annual_salary)


unittest.main()
