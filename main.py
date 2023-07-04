import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_ID, REDIRECT_URI, SCOPE, USER_NAME

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_SECRET_ID,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=".cache",
    show_dialog=True,
    username=USER_NAME
))

user_input = input("Enter the date (YYYY-MM-DD): ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{user_input}/"
response = requests.get(BILLBOARD_URL)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

user = sp.current_user()["id"]

playlist_name = f"{user_input} Billboard 100"
existing_playlists = sp.current_user_playlists()

playlist_id = None
for playlist in existing_playlists["items"]:
    if playlist["name"] == playlist_name:
        playlist_id = playlist["id"]
        break

if playlist_id:
    print(f"Using existing playlist: {playlist_name} (ID: {playlist_id})")
else:
    new_playlist = sp.user_playlist_create(user=user, name=playlist_name, public=False)
    playlist_id = new_playlist["id"]
    print(f"Created new playlist: {playlist_name} (ID: {playlist_id})")

song_uris = []

for name in song_names:
    uris = sp.search(q=name, type="track")
    if uris["tracks"]["items"]:
        uri = uris["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

add_to_playlist = sp.user_playlist_add_tracks(user=user, playlist_id=playlist_id, tracks=song_uris, position=None)
print("Songs added to the playlist.")
