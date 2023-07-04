# Billboard to Spotify Playlist

This Python script allows you to create a Spotify playlist based on the Billboard Hot 100 chart for a specific date.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `spotipy` library

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command:

   ```shell
   pip install requests beautifulsoup4 spotipy
Set up a Spotify Developer account and create a new application to obtain the necessary credentials:

Go to the Spotify Developer Dashboard and log in.
Create a new application and note down the client ID and client secret.
Add a valid redirect URI (e.g., https://example.com/callback) in your Spotify application settings.
Create a config.py file in the same directory as the script and populate it with the following content:

python
Copy code
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_SECRET_ID = "YOUR_SPOTIFY_SECRET_ID"
REDIRECT_URI = "YOUR_REDIRECT_URI"
SCOPE = "playlist-modify-private"
USER_NAME = "YOUR_SPOTIFY_USERNAME"
Replace the placeholders with your actual Spotify client ID, client secret, redirect URI, Spotify username, and the desired scope.

Usage
Run the script:

shell
Copy code
python billboard_to_spotify.py
When prompted, enter the date for which you want to create the playlist in the format YYYY-MM-DD.

The script will scrape the Billboard Hot 100 chart for the given date, search for the corresponding tracks on Spotify, and create a new playlist or use an existing playlist with the name YYYY-MM-DD Billboard 100 in your Spotify account.

The songs found on Spotify will be added to the playlist.

Notes
Make sure you have an active internet connection for the script to fetch data from the web and communicate with the Spotify API.

The script uses the spotipy library, which utilizes the Spotify Web API. The authentication flow is handled using the OAuth 2.0 authorization code flow with the SpotifyOAuth class.

The script uses the requests library for making HTTP requests and the beautifulsoup4 library for parsing HTML content.

The Spotify access token is cached locally in the .cache file for subsequent runs. If you encounter authentication issues, you can delete the cache file and run the script again.
