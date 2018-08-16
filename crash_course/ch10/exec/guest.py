
filename = 'tmp/guest.txt'

name = input('What is your name? ')

with open(filename, 'w') as file_object:
    file_object.write(name + '\n')
