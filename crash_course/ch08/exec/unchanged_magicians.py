
def show_magicians(names):
    """Print the name of each magician in the list."""
    for name in names:
        print(name.title())


def make_great(names):
    """Modify magicans list by add the phrase 'the Great'."""
    return ['the Great ' + x for x in names]


names = ['alice', 'bob', 'david']
updated_names = make_great(names)
print('\nOld names:')
show_magicians(names)
print('\nUpdated names:')
show_magicians(updated_names)
