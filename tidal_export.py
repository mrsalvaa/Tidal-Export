import csv
import tidalapi

session = tidalapi.Session()
session.login_oauth_simple()  #URL for authorization

user_playlists = session.user.playlists()

with open('mis_playlists.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['playlist', 'track', 'artist', 'album'])
    for pl in user_playlists:
        for track in pl.tracks():
            writer.writerow([pl.name, track.name, track.artist.name, track.album.name])

print("Listo: mis_playlists.csv")
