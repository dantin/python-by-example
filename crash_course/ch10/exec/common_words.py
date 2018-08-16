
def count_common_words(filename, word):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exists.'
        print(msg)
    else:
        # Count approximate number of words in the file.
        num_words = contents.lower().count(word)
        print('The file ' + filename + ' has about ' + str(num_words) +
              ' ' + word +' words.')


filename = '../data/alice.txt'
count_common_words(filename, 'the')
