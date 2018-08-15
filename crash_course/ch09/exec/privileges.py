
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


class Privileges():
    """Simple privileges class."""

    def __init__(self, *privileges):
        """Initialize with attributes."""
        self.privileges = [x for x in privileges]

    def show_privileges(self):
        """Print privileges of an admin user."""
        print('The following are the privileges:')
        for privilege in self.privileges:
            print(' - ' + privilege)


class Admin(User):
    """An Admin class."""

    def __init__(self, first, last, *privileges):
        """Initialize with attributes."""
        super().__init__(first, last)
        self.privileges = Privileges(*privileges)


admin = Admin('david', 'ding', 'can add post', 'can delete post', 'can ban user')
admin.privileges.show_privileges()
