
import os
import requests

class WeatherSa:

  def get(self):
    try:  
      appid = os.getenv('API_KEY_OPENWEATHER')
      response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Santo%20Andre&units=metric&appid=' + appid)

      if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        min = data["main"]["temp_min"]
        max = data["main"]["temp_max"]
        
        print(f"T-{round(temperature, 1)}C F-{round(feels_like, 1)}")
        
      return ["Santo Andre - SP", f"Temperature-{round(temperature, 1)}C", f"Feels like-{round(feels_like, 1)}C", f"Min={round(min, 2)} Max={round(max, 2)}"]
    except Exception as e:
      print(f"Error on SA: {e}")
      return []
