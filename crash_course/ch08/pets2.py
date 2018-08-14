
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')


# positonal arguments
describe_pet('willie')
