
class Restaurant():
    """A simple Restaurant class."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print restaurant description."""
        print(self.restaurant_name.title() + ' is a ' + self.cuisine_type +
              ' restaurant. It has served ' + str(self.number_served) +
              ' people.')

    def open_restaurant(self):
        """Simulate open restaurant."""
        print(self.restaurant_name.title() + ' is open.')

    def set_number_served(self, served_number):
        """Simulate set restaurant served number."""
        self.number_served = served_number

    def increment_number_served(self, increment_number):
        """Increment restaurant served number."""
        self.number_served += increment_number


restaurant = Restaurant('Starbucks', 'cafe')
print(restaurant.restaurant_name + '\'s cuisine type is ' + restaurant.cuisine_type + '.')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(1000)
restaurant.describe_restaurant()

restaurant.increment_number_served(100)
restaurant.describe_restaurant()
