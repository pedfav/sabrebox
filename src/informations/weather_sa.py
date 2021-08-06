
import requests
import time
import os

from helpers.lcd import lcd_write

class WeatherSa:

  def get(self, sleep):
    try:  
      appid = os.getenv('API_KEY_OPENWEATHER')
      response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Santo%20Andre&units=metric&appid=' + appid)

      if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        lcd_write("Santo Andre - SP", f"T-{round(temperature, 1)}C  F-{round(feels_like, 1)}C")
        print(f"T-{round(temperature, 1)}C F-{round(feels_like, 1)}")
        
      time.sleep(sleep)
    except Exception as e:
      print(f"Error on SA: {e}")
