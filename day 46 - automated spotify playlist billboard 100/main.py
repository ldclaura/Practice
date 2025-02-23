import requests
from bs4 import BeautifulSoup
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import sys
import json
import time



# scope = "user-library-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

#environment variables
#dir Env:
#prints Name and Value of environment variables
#$ENV:APP_ID="" sets environment variable (to do in terminal)   
#$ENV:SPOTIFY_CLIENT_ID=""
#$ENV:SPOTIFY_CLIENT_SECRET=""
#echo $ENV:SPOTIFY_CLIENT_SECRET
#echo $ENV:SPOTIFY_CLIENT_ID

#echo $ENV:APP_ID tells you if environment variable exists/is set do in terminal

#-----------------------------------------------------------------------------------

 
URL = "https://www.billboard.com/charts/billboard-global-200/#"
SPOTIFY_TOKEN = "uEjXwNKbf"

SPOTIPY_REDIRECT_URI = "http://example.com"
CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
print(CLIENT_ID)
print(CLIENT_SECRET)
# Write your code below this line 👇
response = requests.get(URL)
print(response)
top_songs_page = response.text
soup = BeautifulSoup(top_songs_page, 'html.parser')

songs = soup.find_all(name="h3", id="title-of-a-story")
list_of_songs = []
print(list_of_songs)
for song in songs:
    songtext = song.getText()
    songtext = songtext.replace("\n", "")
    songtext = songtext.replace("\t", "")
    list_of_songs.append(songtext)
list_of_songs.pop(0)
list_of_songs.pop(0)
if list_of_songs[0] == "Additional Awards":
    list_of_songs.pop(0)
for _ in range(13):
    list_of_songs.pop()
print(list_of_songs)

# with open("songs.json", "w") as f: #file dump so if error next time will have latest data
#     json.dump(list_of_songs, f)

#-------------------SPOTIFY--------------------
headers = {
    "Content-Type" : "application/x-www-form-urlencoded",
}

params = {
    "grant_type" : "client_credentials",
    "client_id" : f"{CLIENT_ID}",
    "client_secret" : f"{CLIENT_SECRET}",
}

spotipyresponse = requests.post(url="https://accounts.spotify.com/api/token", params=params, headers=headers)
 #headers=headers NOT header=header
spotifyresult = spotipyresponse.json()
print(spotifyresult)
#------------------------------------------------------------------------------------
def get_songs_id(token, songs):
    song_id_list = []
    for song in songs:
            
        param2 = {
            "q" : f"{song}",
            "type" : "track"
        }

        headers2 = {
            "Authorization" : f"{token['token_type']} {token['access_token']}"
        }

        get_song = requests.get(url="https://api.spotify.com/v1/search", params=param2, headers=headers2)
        gettingsong = get_song.json()
        # print(gettingsong)
        song_id = gettingsong["tracks"]["items"][0]["id"]
        song_id_list.append(f"spotify:track:{song_id}")
        print(song_id) #song id for APT.
        print(song_id_list)
        time.sleep(30)
        # with open("songs_id.json", "a") as f: #file dump so if error next time will have latest data
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded",
        }

        params = {
            "grant_type" : "client_credentials",
            "client_id" : f"{CLIENT_ID}",
            "client_secret" : f"{CLIENT_SECRET}",
        }

        spotipyresponse = requests.post(url="https://accounts.spotify.com/api/token", params=params, headers=headers)
        #headers=headers NOT header=header
        spotifyresult = spotipyresponse.json()
        print(spotifyresult)
        # json.dump(song_id_list, song_id)
        param3 = {
            "playlist_id" : "4HlFZSsAH7db7I9FrjF2gy",
            "uris" : f"{song_id}"
        }
        headers3 = {
            "Authorization" : f"{token['token_type']} {token['access_token']}",
            "Content-Type" : "application/json",
        }
        add_to_playlist = requests.post(url="https://api.spotify.com/v1/playlists/4HlFZSsAH7db7I9FrjF2gy/tracks",  params=param3, headers=headers3)
        added = add_to_playlist.json()
        print(added)


get_songs_id(spotifyresult, list_of_songs)
