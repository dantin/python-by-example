
rivers = {
    'nile': 'egypt',
    'yangzi': 'china',
    'mississippi': 'usa',
}

for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.')
