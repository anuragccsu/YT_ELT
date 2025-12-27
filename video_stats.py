import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = 'MrBeast'  # Mr Beast


def get_playlist_id():
    try:
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

        response = requests.get(url)
        data = response.json()
        #print(response)
        data = response.json()
        #print(json.dumps(data, indent=4))

        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        #print(channel_playlist)  # Uploads playlist ID
        return channel_playlistId
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the playlist ID: {e}")
        return None

#call the function, python way
if __name__ == "__main__":
    playlist_id = get_playlist_id()
    if playlist_id:
        print(f"Playlist ID: {playlist_id}")
