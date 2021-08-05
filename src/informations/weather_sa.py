
import requests
import time
import os

from datetime import datetime

class WeatherSa:

  def get(self, sleep, lcd):
    try:  
      appid = os.getenv('API_KEY_OPENWEATHER')
      print(appid)
      response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Santo%20Andre&units=metric&appid=' + appid)
      data = response.json()
      temperature = data["main"]["temp"]
      feels_like = data["main"]["feels_like"]
    except Exception as e:
      temperature = "**"
      feels_like = "**"

    lcd.clear()
    lcd.write_string("Santo Andre - SP")
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"T-{round(temperature, 1)}C  F-{round(feels_like, 1)}C")
    print(f"T-{round(temperature, 1)}C F-{round(feels_like, 1)}")
    time.sleep(sleep)
