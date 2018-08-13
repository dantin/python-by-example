
cities = {
    'beijing': {
        'country': 'china',
        'population': 35000000,
        'fact': 'capital',
    },
    'shanghai': {
        'country': 'china',
        'population': 33000000,
        'fact': 'great city',
    },
    'paris': {
        'country': 'france',
        'population': 13000000,
        'fact': 'captital',
    }
}

for city, city_info in cities.items():
    print('\n' + city + ' is in ' + city_info['country'] + '.')
    print('\tIt has ' + str(city_info['population']) + ' people, and it is a ' + city_info['fact'])
