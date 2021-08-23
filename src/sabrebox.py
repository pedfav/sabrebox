
import time
import RPi.GPIO as gpio

from enum import Enum
from informations.weather_local import Weather
from informations.currency import Currency
from informations.ip import Ip
from informations.time import Time
from informations.weather_sa import WeatherSa
from informations.spotify import Spotify
from helpers.lcd import lcd_write
from spotify.spotify_manager import play_pause, next_song


gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(15, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(16, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(18, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(22, gpio.OUT)


class Informations(Enum):
  SPOTIFY = Spotify()
  WEATHER = Weather()
  CURRENCY = Currency()
  TIME = Time()
  SA = WeatherSa()


def print_time(number_of_times):
  for x in range(number_of_times):
    if(gpio.input(15) == 1):
      gpio.output(22,gpio.HIGH)
      Ip().get(3)
      gpio.output(22,gpio.LOW)

    if(gpio.input(16) == 1):
      next_song()
      return

    if(gpio.input(18) == 1):
      play_pause()
      return
      
    time.sleep(0.2)


while True:
  for info in Informations:
    lines= info.value.get()

    if len(lines) > 0:
      lcd_write(lines)
      print_time(15)
