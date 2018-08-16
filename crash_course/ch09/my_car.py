from car import Car


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Modifying an attribute's value directly.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attribute's value through a method.
my_new_car.update_odometer(23500)
my_new_car.read_odometer()

# Incrementing an attribute's value through a method.
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
