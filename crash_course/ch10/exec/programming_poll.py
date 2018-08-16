
def save_reason(reason):
    """Save reason into file."""
    filename = 'tmp/reason.txt'

    with open(filename, 'a') as file_object:
        file_object.write(reason + '\n')


while True:
    print('Enter \'q\' to exit.')
    name = input('Why you like programming? ')
    if name == 'q':
        break
    save_reason(name)

