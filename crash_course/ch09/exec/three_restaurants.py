
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


restaurants = [
    Restaurant('Starbucks', 'cafe'),
    Restaurant('KFC', 'fast food'),
    Restaurant('Lost Heaven', 'Chinese food'),
]

for restaurant in restaurants:
    restaurant.describe_restaurant()
