
def make_album(artist, title):
    """Build a dictionary describing a music album."""
    return {'artist_name': artist, 'album_title': title}


while True:
    print('Enter an album\'s information:')
    print('(enter \'q\' to exit)')
    artist = input('Artist Name: ')
    if artist == 'q':
        break

    title = input('Album Title: ')
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
