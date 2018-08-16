
import json


filename = 'tmp/favorite-number.json'

try:
    with open(filename) as f_obj:
        favorite = json.load(f_obj)
except FileNotFoundError:
    favorite = input('What is your favorite number? ')
    with open(filename, 'w') as f_obj:
        json.dump(int(favorite), f_obj)
else:
    print('I know your favorite number! It\'s ' + str(favorite) + '.')
