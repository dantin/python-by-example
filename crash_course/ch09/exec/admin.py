
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


admin = Admin('david', 'ding', 'can add post', 'can delete post', 'can ban user')
admin.show_privileges()
