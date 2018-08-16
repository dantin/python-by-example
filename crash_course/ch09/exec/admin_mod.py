"""Admin module library."""
from user_mod import User


class Admin(User):
    """An Admin class."""

    def __init__(self, first, last, *privileges):
        """Initialize with attributes."""
        super().__init__(first, last)
        self.privileges = [p for p in privileges]

    def show_privileges(self):
        """Print privileges of an admin user."""
        self.describe_user()
        print('with privileges')
        for privilege in self.privileges:
            print(' - ' + privilege)
