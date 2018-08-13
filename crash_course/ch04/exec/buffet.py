
print('original menu')
foods = ('egg', 'water', 'juice', 'meat', 'rice')
for food in foods:
    print(food)

# tuple can't change
# foods[0] = 'meat ball'
print('\nAfter menu change')
changed_foods = (foods[0], 'milk', foods[2], foods[3], 'fish')
for food in changed_foods:
    print(food)
