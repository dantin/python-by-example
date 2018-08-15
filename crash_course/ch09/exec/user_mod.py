"""Admin library."""

class User():
    """A simple user class."""

    def __init__(self, first, last):
        """Initialize with attributes."""
        self.first_name = first
        self.last_name = last

    def describe_user(self):
        """Print user description."""
        full_name = self.first_name + ' ' + self.last_name
        print(full_name.title())

    def greet_user(self):
        """Simulate greeting user."""
        print('Hi, ' + self.first_name.title() + '!')
