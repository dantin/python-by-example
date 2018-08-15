
def make_album(artist, title, tracks=''):
    """Build a dictionary describing a music album."""
    album = {'artist_name': artist, 'album_title': title}
    if tracks:
        album['tracks'] = tracks

    return album


albums = [
    make_album('Adele', 'Hello'),
    make_album(title='Poker Face', artist='Lady Gaga'),
    make_album(artist='Marron 5', title='Moves Like Jagger', tracks=1),
]

for album in albums:
    print(album)
