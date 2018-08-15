from restaurant_lib import Restaurant


restaurant = Restaurant('Starbucks', 'cafe')
print(restaurant.restaurant_name + '\'s cuisine type is ' + restaurant.cuisine_type + '.')

restaurant.describe_restaurant()
restaurant.open_restaurant()
