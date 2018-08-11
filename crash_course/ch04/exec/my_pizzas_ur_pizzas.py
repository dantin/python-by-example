
my_favorites = ['pepperoni', 'italino', 'meat']
friends_pizzas = my_favorites[:]

my_favorites.append('meat')
friends_pizzas.append('vegit')

print('My favorite pizzas are:')
for pizza in my_favorites:
    print(pizza)

print('\nMy friend\'s pizzas are:')
for pizza in friends_pizzas:
    print(pizza)
