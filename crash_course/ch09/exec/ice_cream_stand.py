
class Restaurant():
    """A simple Restaurant class."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print restaurant description."""
        print(self.restaurant_name.title() + ' is a ' + self.cuisine_type +
              ' restaurant.')

    def open_restaurant(self):
        """Simulate open restaurant."""
        print(self.restaurant_name.title() + ' is open.')


class IceCreamStand(Restaurant):
    """A specialize restaurant that make ice cream."""

    def __init__(self, name, cuisine_type, *flavors):
        """Initialize ice cream restaurant with flavors."""
        super().__init__(name, cuisine_type)
        self.flavors = [x for x in flavors]

    def display_flavors(self):
        """Print ice cream flavors."""
        self.describe_restaurant()
        print('It has the following flavors:')
        for flavor in self.flavors:
            print(' - ' + flavor)



restaurant = IceCreamStand('Ice Goods', 'ice cream', 'chocolate', 'vanilla', 'mint')
restaurant.display_flavors()
