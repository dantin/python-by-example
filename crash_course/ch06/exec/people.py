
person_0 = {
    'first_name': 'henry',
    'last_name': 'han',
    'age': 36,
    'city': 'shanghai',
}
person_1 = {
    'first_name': 'henius',
    'last_name': 'dong',
    'age': 36,
    'city': 'shanghai',
}
person_2 = {
    'first_name': 'alex',
    'last_name': 'ruan',
    'age': 40,
    'city': 'paris',
}

people = [person_0, person_1, person_2]


for person in people:
    full_name = person['first_name'] + ' ' + person['last_name']
    print('\nFull Name: ' + full_name.title())
    print('Age:        ' + str(person['age']))
    print('City:       ' + person['city'].title())
