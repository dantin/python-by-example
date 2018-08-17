
class Employee():
    """Employee class."""

    def __init__(self, first, last, annual_salary):
        """Initialize using attributes."""
        self.first_name = first
        self.last_name = last
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Raise annual salary, default amount is $5000."""
        self.annual_salary += amount
