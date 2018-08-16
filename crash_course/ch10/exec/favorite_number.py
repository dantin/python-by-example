
import json


filename = 'tmp/favorite-number.json'

favorite = input('What is your favorite number? ')
with open(filename, 'w') as f_obj:
    json.dump(int(favorite), f_obj)
