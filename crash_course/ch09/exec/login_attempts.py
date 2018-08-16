
class User():
    """A simple user class."""

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0

    def describe_user(self):
        """Print user description."""
        full_name = self.first_name + ' ' + self.last_name
        print(full_name.title() + ' has ' + str(self.login_attempts) +
              ' login attempts.')

    def greet_user(self):
        """Simulate greeting user."""
        print('Hi, ' + self.first_name.title() + '!')

    def increment_login_attempts(self):
        """Simulate login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


user = User('henry', 'han')
user.describe_user()

for _ in range(5):
    user.increment_login_attempts()
user.describe_user()

print('\nreset login attempts.')
user.reset_login_attempts()
user.describe_user()
