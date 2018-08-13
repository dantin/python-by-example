
eli = {
    'name': 'eli',
    'animal': 'dog',
    'owner': 'weimin',
}

bebe = {
    'name': 'bebe',
    'animal': 'dog',
    'owner': 'pingdi',
}

pets = [eli, bebe]

for pet in pets:
    print('\nName: ' + pet['name'].title())
    print('Animal: ' + pet['animal'])
    print('Owner: ' + pet['owner'].title())
