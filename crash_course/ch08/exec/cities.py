
def describe_city(city, country='china'):
    """Print message that describe city."""
    print(city.title() + ' is in ' + country.title() + '.')


describe_city('shanghai')
describe_city(city='beijing')
describe_city(city='tokyo', country='japan')
