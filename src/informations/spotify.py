import os
import base64
import requests


REFRESH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
URL_CURRENT_PLAYING = 'https://api.spotify.com/v1/me/player/currently-playing?market=ES'

basic = os.getenv('SPOTIFY_CLIENT_ID') + ':' + os.getenv('SPOTIFY_CLIENT_SECRET')        
basic = base64.b64encode(basic.encode('ascii'))


class Spotify:

  def get(self):
    try:
      response = requests.request("GET", URL_CURRENT_PLAYING, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv('TOKEN')
      })

      if response.status_code == 401:
        self.refresh_token()
        return self.get()

      if response.status_code == 204:
        return []

      artists = self.extract_artist(response)
      song = self.extract_song(response)

      print(f"Spotify playing artist={artists} and song={song}")
      return self.print_to_lcd(artists, song)
    except Exception:
      return []


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

    os.environ['TOKEN'] = response.json()['access_token']


  def extract_artist(self, response):
    return ','.join(artist['name'] for artist in response.json()['item']['artists'])
  

  def extract_song(self, response):
    return response.json()['item']['name']

  
  def print_to_lcd(artist, song):
    song_with_symbol = f"\x00 {song}"

    if len(song) > 20:
      song_line_one = song_with_symbol[:20]
      song_line_two = song_with_symbol[20:40]  
    
    return [" Playing on spotify ", artist, song_line_one, song_line_two]
  