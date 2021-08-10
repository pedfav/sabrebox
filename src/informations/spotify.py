import os
import base64
import requests

REFRESH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
URL_CURRENT_PLAYING = 'https://api.spotify.com/v1/me/player/currently-playing?market=ES'

basic = os.getenv('SPOTIFY_CLIENT_ID') + ':' + os.getenv('SPOTIFY_CLIENT_SECRET')        
basic = base64.b64encode(basic.encode('ascii'))

class Spotify:

  def get(self):
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + os.getenv('TOKEN')
    }

    response = requests.request("GET", URL_CURRENT_PLAYING, headers=headers)

    if response.status_code == 401:
      self.refresh_token()
      return self.get()

    if response.status_code == 204:
      return None, None

    return ','.join(artist['name'] for artist in response.json()['item']['artists']), response.json()['item']['name']


  def refresh_token(self):
    response = requests.post(
      url = REFRESH_TOKEN_URL,            
      data={
          'grant_type': 'refresh_token',
          'refresh_token': os.getenv('REFRESH_TOKEN')
      },
      headers={
          "Authorization": "Basic " + basic.decode('ascii'),
          "Content-Type": "application/x-www-form-urlencoded"
      },
      verify=True            
    )

    token = response.json()['access_token']
    os.environ['TOKEN'] = token
