
def make_car(manufacturer, model, **extra_info):
    """Make a car dictionary using input information."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in extra_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
