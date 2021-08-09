import requests
import base64
import time
import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)


# URLS
AUTH_URL = 'https://accounts.spotify.com/authorize'
CURRENT_URL = 'https://api.spotify.com/v1/me/player/currently-playing?market=ES'

token = 'BQBImqdzZi1YLf7uRGu_Xxr9_WZhfbHBL3fLCBNdj3K0HN70wRR_QFiM_lNIa8mzq72pnkpdKWGtQ7X6Ge3pgWH0l5ef5D_dIjfiGBWMlq8aUWGIeKmxP06qfDj9249c5KSjS_y-nx54bAbhUQ'
refresh_token = 'AQCdpO8-vXseK6PY97d3aHqFxT3BfTqlmSYzrvfHzTyvMzAmOcMFGKPUNgkIC1gUF4L2-skDujHIqc_pF0B7fyPsJoTmUWDVwgpfUSNmRYJeAd3ZuddVqUKEdMw2fsIFvT0'

def get_current_profile_token():
  basic = 'bc91c668b00841dca5706670c5a7d6dc' + ':' + '42d065ab43524f69911ba8dc0599ca0b'        
  basic = base64.b64encode(basic.encode('ascii'))

  response = requests.post(
      url = 'https://accounts.spotify.com/api/token',            
      data={
          'grant_type': 'authorization_code',
          'code': 'AQAZVaXEQtKwRng3FpPoVH6Eq2V_CTeSXGABDimTBDm_E7wYhym8tzlwv9OvGpaTrfdc3vQIN4-O_5l5OWCVyKl1WxaImHK_zavwM9p7qUkztkS090MmLvWHW0mWJoGvjWvS8B1VLirDTjH6yl01ShIaHHYmeATaZ9FQ2vvUN_64O8DQtnkrEL5cTNnjvDY_X76DqOraqsCw9nZG3vY9vMCMsZg',
          'redirect_uri': 'https://pedrofavari.com.br/callback'
      },
      headers={
          "Authorization": "Basic " + basic.decode('ascii'),
          "Content-Type": "application/x-www-form-urlencoded"
      },
      verify=True            
  )
  return response.json()['access_token'], response.json()['refresh_token']

def get_current_playing():
  url = "https://api.spotify.com/v1/me/player/currently-playing?market=ES"

  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  }

  response = requests.request("GET", url, headers=headers)

  print(response.text.encode('utf8'))
  
long_string = 'This string is too long to fit'
for i in range(len(long_string) - 16 + 1):
  lcd.write_string(long_string[i:i+16])

  time.sleep(0.2)