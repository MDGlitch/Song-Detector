import time
from plyer import notification
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'YOUR ID HERE'
CLIENT_SECRET = 'YOUR SECRET HERE'
REDIRECT_URI = 'YOUR REDIRECT URL HERE'

def get_current_song(sp):
    try:
        current_track = sp.current_playback()
        if current_track is not None and current_track['is_playing']:
            track_name = current_track['item']['name']
            artist_name = ', '.join([artist['name'] for artist in current_track['item']['artists']])
            return track_name, artist_name
        return ("No song is currently playing", "")
    except Exception as e:
        print(f"Error getting current song: {str(e)}")
    return ("No song is currently playing", "")

previous_track_name = ""
previous_artist_name = ""

sp_oauth = spotipy.oauth2.SpotifyOAuth(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI,
    scope="user-read-currently-playing user-read-playback-state",
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

while True:
    current_track_name, current_artist_name = get_current_song(sp)
    
    if (
        current_track_name != previous_track_name
        or current_artist_name != previous_artist_name
    ):
        if current_track_name != "No song is currently playing":
            notification_text = f"Now Playing: {current_track_name}\nBy: {current_artist_name}"
        else:
            notification_text = "No song is currently playing"
        
        notification_title = "Song Detector"
        notification_message = notification_text
        notification_timeout = 10 
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=notification_timeout,
        )
    
    previous_track_name = current_track_name
    previous_artist_name = current_artist_name
    
    time.sleep(5)