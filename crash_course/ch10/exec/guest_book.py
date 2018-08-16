
def save_guest(name):
    """Save name into file."""
    filename = 'tmp/guest_book.txt'

    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')


while True:
    print('Enter \'q\' to exit.')
    name = input('What is your name? ')
    if name == 'q':
        break
    print('Hello, ' + name + '!')
    save_guest(name)

