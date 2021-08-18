
import time
import RPi.GPIO as gpio

from enum import Enum
from informations.weather_local import Weather
from informations.currency import Currency
from informations.ip import Ip
from informations.day_percentage import DayPercentage
from informations.weather_sa import WeatherSa
from informations.spotify import Spotify
from helpers.lcd import lcd_write


gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(22, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(12, gpio.OUT)
gpio.setup(11, gpio.OUT)


class Informations(Enum):
  SPOTIFY = Spotify()
  WEATHER = Weather()
  CURRENCY = Currency()
  DAY = DayPercentage()
  SA = WeatherSa()


def print_time(number_of_times):
  for x in range(number_of_times):
    if(gpio.input(22) == 1):
      gpio.output(12,gpio.HIGH)
      Ip().get(3)
      gpio.output(12,gpio.LOW)
    time.sleep(0.5)


while True:
  for info in Informations:
    lines= info.value.get()

    if len(lines) > 0:
      lcd_write(lines)
      print_time(6)
