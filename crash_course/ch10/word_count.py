
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exists.'
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) +
              ' words.')


filenames = [
    'data/alice.txt',
    'data/sssssiddhartha.txt',
    'data/moby_dick.txt',
    'data/little_women.txt',
]

for filename in filenames:
    count_words(filename)
