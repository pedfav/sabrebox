import os
import requests
from informations.spotify import Spotify

URL_PLAY = 'https://api.spotify.com/v1/me/player/play'
URL_PAUSE = 'https://api.spotify.com/v1/me/player/pause'
URL_NEXT_SONG = 'https://api.spotify.com/v1/me/player/next'


def play_pause():
  try:
    print('play/pause')
    response = requests.request("PUT", URL_PLAY, 
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + os.getenv('TOKEN')
    }, data={})

    if response.status_code == 403:
      response = requests.request("PUT", URL_PAUSE, headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + os.getenv('TOKEN')
    }, data={})

    if response.status_code == 401:
      Spotify.refresh_token()
      return play_pause()
  
  except Exception:
    print('Cannot play/pause')

def next_song():
  try:
    print('next song')
    response = requests.request("POST", URL_NEXT_SONG, headers= {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + os.getenv('TOKEN')
    }, data={})

    if response.status_code == 401:
      Spotify.refresh_token()
      return play_pause()

  except Exception:
    print('Cannot go to next song')
