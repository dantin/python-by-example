
import json


filename = 'tmp/favorite-number.json'

with open(filename) as f_obj:
    favorite = json.load(f_obj)

print('I know your favorite number! It\'s ' + str(favorite) + '.')
