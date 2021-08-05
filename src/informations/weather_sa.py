
import requests
import time

from datetime import datetime

class WeatherSa:

  def get(self, sleep, lcd):
    try:  
      response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Santo%20Andre&appid=7baccbe21fc603febb5f066422464010&units=metric')
      data = response.json()
      temperature = data["main"]["temp"]
      feels_like = data["main"]["feels_like"]
    except Exception as e:
      temperature = "**"
      feels_like = "**"

    lcd.clear()
    lcd.write_string("Santo Andre - SP")
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"T-{round(temperature, 1)}C F-{round(feels_like, 1)}")
    print(f"T-{round(temperature, 1)}C F-{round(feels_like, 1)}")
    time.sleep(sleep)
