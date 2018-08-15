
def show_magicians(names):
    """Print the name of each magician in the list."""
    for name in names:
        print(name.title())


def make_great(names):
    """Modify magicans list by add the phrase 'the Great'."""
    for idx, name in enumerate(names):
        names[idx] = 'the Great ' + name


names = ['alice', 'bob', 'david']
make_great(names)
show_magicians(names)
