
def read_file(filename):
    """Read file and print content by line."""
    try:
        with open(filename) as f_obj:
            for line in f_obj:
                print(line.rstrip())
    except FileNotFoundError:
        pass


filenames = ['data/catss.txt', 'data/dogs.txt']
for filename in filenames:
    read_file(filename)
