
vocations = {}

active = True

while active:
    name = input('\nWhat is your name? ')
    location = input('If you could visit one place in the world, where would you go? ')

    vocations[name] = location

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        active = False

print('\n--- Poll Results ---')
for name, location in vocations.items():
    print(name + ' would like to go ' + location + '.')
