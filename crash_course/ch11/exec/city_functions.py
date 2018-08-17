
def city_country(city, country, population=''):
    """Generate a neatly formatted city/country name."""
    full_name = city + ', ' + country
    if population:
        return full_name.title() + ' - population ' + str(population)
    else:
        return full_name.title()
