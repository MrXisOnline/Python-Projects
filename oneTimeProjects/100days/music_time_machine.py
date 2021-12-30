from bs4 import BeautifulSoup as soup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

song_url = "https://www.billboard.com/charts/hot-100/"
date = input("date YYYY-MM-DD : ")
res = requests.get(url=song_url+date)
text = res.text
html = soup(text, "html.parser")
song_names = html.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names_text = [song.getText() for song in song_names]
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"],
                                                    client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
                                                    redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
                                                    scope="playlist-modify-public"))

playlist_name = "Hot 100 of " + date
# create playlist
playlist = spotify.user_playlist_create(user=os.environ["user_id"], name=playlist_name)
playlist_id = playlist["id"]
song_ids = []
for song in song_names_text:
    # song search
    track = spotify.search(q=song, limit=1)
    track_id = track['tracks']['items'][0]["id"]
    song_ids.append(track_id)

# add to playlist
ids = spotify.user_playlist_add_tracks(user=os.environ["user_id"],playlist_id=playlist_id,tracks=song_ids)




