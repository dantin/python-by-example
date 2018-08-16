
import json


def get_store_username():
    """Get stored username if available."""
    filename = 'tmp/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input('What is your name? ')
    filename = 'tmp/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def verify_user(username):
    """Verify username to check whether it is the same user."""
    if not username:
        return False
    ans = input('Is ' + username + ' the correct username? (y/n) ')
    if ans in ('y', 'n') and ans == 'y':
        return True
    return False


def greet_user():
    """Greet the user by name."""
    username = get_store_username()

    if verify_user(username):
        print('Welcome back, ' + username + '!')
    else:
        username = get_new_username()
        print('We\'ll remember you when you come back, ' + username + '!')


greet_user()
