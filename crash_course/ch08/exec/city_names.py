
def city_country(city, country):
    """Return a formatted string of country and city."""
    return city.title() + ', ' + country.title()


print(city_country('shanghai', 'china'))
print(city_country(country='china', city='beijing'))
print(city_country(city='paris', country='france'))
